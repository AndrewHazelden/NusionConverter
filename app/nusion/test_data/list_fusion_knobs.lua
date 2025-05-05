--
-- Run in fusion script editor to list all knobs on selected node.
--

-- List all attributes:
-- attrs = comp.ActiveTool
-- for key, value in pairs(attrs) do
--     inputAttrs = value:GetAttrs()
--     for k, v in pairs(inputAttrs) do
--       print()
--       print(k)
--       print(v)
--     end
--   end

--List only "effect knobs" -- more useful:
attrs = comp.ActiveTool:GetInputList()
for key, value in pairs(attrs) do
  inputAttrs = value:GetAttrs("INPS_Name")
  print(inputAttrs)
end
