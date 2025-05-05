--[[--
Paste Nusion.lua - 2025-05-05 06.25 PM
Ported by Andrew Hazelden <andrew@andrewhazelden.com>

The "Edit > Paste Nusion" menu item lets you paste a Foundry Nuke node from your clipboard and have it instantly translated into the corresponding Fusion Studio node.

This Paste Nusion comp script/menu item uses the NodeJS/Python based "Nusion" flask appication that is able to run locally on your system, or on a server that is accessible to workstations on your local LAN. Check out the NusionConverter GitHub repo for more details on the local webapp installation process.

## NusionConverter GitHub Repo:

https://github.com/AndrewHazelden/NusionConverter

## Example Nuke .nk Comp Snippet:

Blur {
 inputs 1+1
 size 4
 name car_Dust_Blur
 xpos 950
 ypos 1330
}

--]]--

function System(commandString)
    local handler = io.popen(commandString);
    local response = tostring(handler:read('*a'))
    handler:close()

    -- Trim off the last character which is a newline
    return response:sub(1,-2)
end

-- Find out the current directory from a file path
-- Example: print(Dirname('/Users/Shared/image.0000.exr'))
function Dirname(mediaDirName)
    if mediaDirName then
        return mediaDirName:match("(.*[/\\])")
    else
        return nil
    end
end

function GetPlatform()
    -- Find out the current Fusion host platform (Windows/Mac/Linux)
    local platform = ""
    if jit.os == "Windows" then
        platform = "Windows"
    elseif jit.os == "Linux" then
        platform = "Linux"
    elseif jit.os == "OSX" then
        platform = "Mac"
    else
        platform = "Linux"
    end

    return platform
end

function GetJSONKey(json_str, key)
    local json = require("dkjson")
    local json_tbl = json.decode(json_str)

    local value = nil
    local found = false

    for k, v in pairs(json_tbl) do
        if k == key then
            value = v
            found = true
            break
        end
    end

    if not found then
        print(string.format("no key '%s' found in json table", key))
    end

    return value
end


function CopyFromClipboard()
    local out = ""

    if jit.os ~= "OSX" then
        -- Windows or Linux
        out = bmd.getclipboard()
    else
        -- macOS
        -- A workaround is used since bmd.getclipboard() deletes the last character in a string in Fusion v16-17 on macOS
        local dir = comp:MapPath('Temp:\\Vonk\\')
        bmd.createdir(dir)
        local path = dir .. 'ClipboardText.txt'

        command = 'pbpaste > "' .. path .. '"'
        print('[Copy Text to Clipboard Command]' , command)
        os.execute(command)

        local fp = io.open(path, "r")
        if fp == nil then
            error(string.format("file does not exist: %s", path))
        else
            out = fp:read("*all")
            fp:close()
        end
    end

    return out
end


function Main()
    print("[Paste Nusion]")

    -- Show debugging info in the Console window
    local show_dump = 1

    -- Comp Resolution
    local width = tostring(1920)
    local height = tostring(1080)

    -- Nusion Web app IP address
    -- Default port is "5000"
    -- The current system's localhost IP address is "http://127.0.0.1"
    local nusionServerIP = "http://127.0.0.1:5000"

    -- Sample Nuke .nk Script Code Chunk
    local nukeScript_str = CopyFromClipboard()

--    local nukeScript_str = [=[
--Blur {
--inputs 1+1
--size 4
--name car_Dust_Blur
--xpos 950
--ypos 1330
--}
--
--]=]

    local nukeScriptNoNewlines_str = string.gsub(nukeScript_str, "\n", "\\n")
    -- print(nukeScriptNoNewlines_str)

    local platform = GetPlatform()
    local curlFile = ""
    if platform == "Windows" then
        -- Running on Windows
        curlFile = "C:/Windows/System32/curl.exe"
    elseif platform == "Mac" then
        -- Running on Mac
        curlFile = "/usr/bin/curl"
    elseif platform == "Linux" then
        -- Running on Linux
        curlFile = "/usr/bin/curl"
    else
        error("[Curl Filepath] There is an invalid Fusion platform detected")
    end

    local launchCommand = [["]] .. tostring(curlFile) .. [[" "]] .. nusionServerIP .. [[/convert" -X POST -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Referer: ]] .. nusionServerIP .. [[/' -H 'Content-Type: application/json' -H 'Origin: ]] .. nusionServerIP .. [[' -H 'Connection: keep-alive' --data-raw '{"data":"]] .. nukeScriptNoNewlines_str .. [[" ,"width":"]] .. 1920 .. [[","height":"]] .. 1080 .. [[","fromSoftware":"nuke"}''']]

    local json_str = System(launchCommand)
    local fusionComp_str = GetJSONKey(json_str, "result") or ""

    if show_dump == 1 then
        print("\n----------------------")
        print("\n[CLI Parameters]")
        print(launchCommand)

        print("\n[CLI Output] ")
        print(json_str)
    end

    -- Check if the clipboard contents is a table
    local clipboard_tbl = {}
    if fusionComp_str then
        clipboard_tbl = bmd.readstring(fusionComp_str) or {}
        -- Add the macro snippet to your foreground comp
        comp:Paste(clipboard_tbl)
    end

    if show_dump == 1 then
        print("\n[Fusion Comp Output] ")
        dump(fusionComp_str)
        print('[Clipboard Contents]\n')
        dump(clipboard_tbl)
    end
end

-- Main is where the magic happens!
Main()
print("[Done]")
