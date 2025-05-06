# Nusion for cURL

The Nusion Web app can use cURL from the terminal to process JSON encoded Nuke scripts.

The Nuke node data is stored in a "data" JSON key that is submitted by cURL via an HTTP post request.

```bash
curl 'http://127.0.0.1:5000/convert' -X POST -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Referer: http://127.0.0.1:5000/' -H 'Content-Type: application/json' -H 'Origin: http://127.0.0.1:5000' -H 'Connection: keep-alive' --data-raw '{"data":"Blur {\n inputs 1+1\n size 4\n name car_Dust_Blur\n xpos 950\n ypos 1330\n}","width":"1920","height":"1080","fromSoftware":"nuke"}'
```

cURL Terminal Result:

The Fusion formatted node data can be accessed using the "result" JSON key.

```json
{"result":"{\nTools = ordered() {\ncar_Dust_Blur = Blur {\nInputs = {\nXBlurSize = Input { Value = 1.43561, },\n},\nViewInfo = OperatorInfo {\nPos = { 950, 1330 },\n},\n}\n}\n}"}
```

![Nusion CLI](images/11_curl_cli.png)
