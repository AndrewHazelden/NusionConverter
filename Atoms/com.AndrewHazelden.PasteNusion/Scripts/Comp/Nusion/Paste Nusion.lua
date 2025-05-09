--[[--
Paste Nusion.lua - 2025-05-09 03.17 PM
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
    local platform = GetPlatform()
    if platform == "Windows" then
        os.execute([[start "" /wait ]] .. commandString)
        -- bmd.wait(2)
        return ""
    else
        local handler = io.popen(commandString);
        local response = tostring(handler:read('*a'))
        handler:close()

        -- Trim off the last character which is a newline
        return response:sub(1,-2)
    end
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

    if type(json_tbl) == "table" then
        for k, v in pairs(json_tbl) do
            if k == key then
                value = v
                found = true
                break
            end
        end
    else
        print(string.format("The json data is invalid. No table present."))
    end 
    if not found then
        print(string.format("no key '%s' found in json table", key))
    end

    return value
end

function curlOutputFilename()
    local dir = comp:MapPath('Temp:/Nusion/')
    bmd.createdir(dir)
    local path = dir .. 'cURL_Output.json'
    local pathNormalizeSlashes_str = string.gsub(path, "\\", "/")
    
    return pathNormalizeSlashes_str
end

function JSONToFile(node_str, width, height)
    local json = require("dkjson")

    local dir = comp:MapPath('Temp:/Nusion/')
    bmd.createdir(dir)
    local path = dir .. 'Nodes.json'
    local pathNormalizeSlashes_str = string.gsub(path, "\\", "/")

    -- Create a Lua table
    local tbl = {}
    tbl.data = node_str
    tbl.width = width
    tbl.height = height
    tbl.fromSoftware = "nuke"

--    print("[JSON Encoded Table]")
--    dump(tbl)

    outJson_str = json.encode(tbl, {indent = 1})

    local fp = io.open(pathNormalizeSlashes_str, "w")
    if fp == nil then
        error(string.format("file could not be created: %s", path))
    else
        fp:write(outJson_str)
        fp:write("\n")
        fp:close()
    end

    return pathNormalizeSlashes_str, outJson_str
end

function CopyFromClipboard()
    local out = ""

    if jit.os ~= "OSX" then
        -- Windows or Linux
        out = bmd.getclipboard()
    else
        -- macOS
        -- A workaround is used since bmd.getclipboard() deletes the last character in a string in Fusion v16-17 on macOS
        local dir = comp:MapPath('Temp:\\Nusion\\')
        bmd.createdir(dir)
        local path = dir .. 'ClipboardText.txt'

        command = 'pbpaste > "' .. path .. '"'
        print('[Copy Text to Clipboard Command] ' , command)
        os.execute(command)

        local fp = io.open(path, "r")
        if fp == nil then
            error(string.format("file does not exist: %s", path))
        else
            out = fp:read("*all")
            fp:close()
            os.remove(path)
        end
    end

    return out
end


function Main()
    print("[Paste Nusion]")
    -- Nusion Web app IP address
    -- Default port is "5000"
    -- The current system's localhost IP address is "http://127.0.0.1"
    local nusionServerIP = "http://127.0.0.1:5000"

    -- Show debugging info in the Console window
    local show_dump = 1

    -- Comp Resolution
    local formatPrefs = comp:GetPrefs("Comp.FrameFormat")
    local width = tostring(formatPrefs.Width or 1920)
    local height = tostring(formatPrefs.Height or 1080)

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

    -- Write the JSON file to disk
    local jsonFile, jsonStr = JSONToFile(nukeScript_str, width, height)

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

    local curlOutput = curlOutputFilename()

    local launchCommand = [["]] .. tostring(curlFile) .. [[" "]] .. nusionServerIP .. [[/convert" -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "Referer: ]] .. nusionServerIP .. [[/" -H "Content-Type: application/json" -H "Origin: ]] .. nusionServerIP .. [[" -H "Connection: keep-alive" --data-ascii "@]] .. jsonFile .. [[" --output "]] .. curlOutput .. [["]]
    local result = System(launchCommand)

    if show_dump == 1 then
        print("\n----------------------")
        print("\n[Nuke Script]")
        print(nukeScript_str)
  
        print("\n[JSON Output]")
        print(jsonStr)

        print("\n[CLI Parameters]")
        print(launchCommand)

        print("\n[CLI Output] ")
        print(result)
    end

    local json_str = "{}"
    local fp = io.open(curlOutput, "r")
    if fp == nil then
        print(string.format("cURL output JSON file does not exist: %s", curlOutput))
    else
        json_str = fp:read("*all")
        fp:close()
    end

    -- Remove the JSON files
    os.remove(jsonFile)
    os.remove(curlOutput)

    local fusionComp_str = GetJSONKey(json_str, "result") or ""

    if show_dump == 1 then
        print("\n[cURL JSON Output] ")
        print(json_str)
    end
    
    -- Check if the clipboard contents is a table
    local clipboard_tbl = {}
    if fusionComp_str then
        clipboard_tbl = bmd.readstring(fusionComp_str) or {}
        -- Add the macro snippet to your foreground comp
        comp:Paste(clipboard_tbl)
        bmd.setclipboard(nukeScript_str)
    end

    if show_dump == 1 then
        print("\n[Fusion Comp Output] ")
        dump(fusionComp_str)
        print("\n[Clipboard Contents]")
        dump(clipboard_tbl)
    end
end

-- Main is where the magic happens!
Main()
print("[Done]")
