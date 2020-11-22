er={"city": "Москва", "temperature": "20"}
print(er.get("city"))
a=int(er.get("temperature"))-5
er["temperature"]=a
print(er)
ab=str(er.keys()) in 'country'
print(ab)
er['country']='Россия'
print(er)
er['date']='27.05.2019'

print(len(er))
