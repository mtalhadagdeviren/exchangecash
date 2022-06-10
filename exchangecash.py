import requests
import json


bozulan_doviz=input('Bozdurmak İstediğiniz Döviz: ')
alınan_doviz=input('Hangi Para Biriminden Bozulacak: ')   
miktar=input('Bozdurulmak İstenilen Miktar: ')

url = f"https://api.apilayer.com/fixer/convert?to={alınan_doviz}&from={bozulan_doviz}&amount={miktar}"
payload = {}
headers= {
  "apikey": "7gzjHnSL9ZNC8C2Gpn6rtabLyvdzRDpc"
}

response = requests.request("GET", url, headers=headers, data = payload)
result=json.loads(response.text)

print("1 {0} = {1}".format(bozulan_doviz,result["info"]["rate"])+' '+alınan_doviz)
print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,result["result"],alınan_doviz))
