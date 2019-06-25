print('Resumir texto')
def resumir (texto):
    texto= texto[0:140] + "..."
    return texto
print(resumir("Numa terra fantástica e única, chamada Terra-Média, um hobbit recebe de presente de seu tio o Um Anel, um anel mágico e maligno que precisa ser destruído antes que caia nas mãos do mal. Para isso o hobbit Frodo (Elijah Woods) terá um caminho árduo pela frente, onde encontrará perigo, medo e personagens bizarros. Ao seu lado para o cumprimento desta jornada aos poucos ele poderá contar com outros hobbits, um elfo, um anão, dois humanos e um mago, totalizando 9 pessoas que formarão a Sociedade do Anel."))
print('')
print('Dicíonário')
dic = {
    2019:{'Avengers: Endgame':2750667499},
    2018:{'Black Panther':1346913161, 'Avengers: Infinity War': 2048359754,'Jurassic World: Fallen Kingdom':130948446},
    2017:{'Beauty and the Beast':126352112,'Star Wars: The Last Jedi':133253988},
    2015:{'Jurassic World': 1671713208,' Star Wars: The Force Awakens':206822362, 'Furious 7':1516045911, 'Avengers: Age of Ultron': 1405403694},
    2013:{'Frozen': 1276480335,},
    2012:{"Marvel's The Avengers":1518812988},
    2011:{'Harry Potter and the Deathly Hallows – Part 2': 1341693157},
    2009:{'Avatar':1516045911},
    1997:{'Titanic':2187463944}
    }
print(dic)
print('')
print('Valor Arrecadado')
s1=0
s2=0
s3=0
s4=0
s5=0
s6=0
s7=0
s8=0
s9=0
y=open('filme.txt', 'r')
for s in y.readlines():
    s = s.split(',')
    if s[0]=='1997':
       s1=s1 + int(s[2]) 
    if s[0]=='2009':
        s2=s2 + int(s[2])
    if s[0]=='2011':
        s3=s3 + int(s[2])
    if s[0]=='2012':
        s4=s4 + int(s[2])
    if s[0]=='2013':
        s5=s5 +int(s[2])
    if s[0]=='2015':
        s6=s6 + int(s[2])
    if s[0]=='2017':
        s7=s7 +int(s[2])
    if s[0]=='2018':
        s8=s8 + int(s[2])
    if s[0]=='2019':
        s9=s9 + int(s[2])

print('Valor arrecadado em 1997:US$',s1/1000000000, 'Bilhões')
print('Valor arrecadado em 2009:US$',s2/1000000000, 'Bilhões')
print('Valor arrecadado em 2011:US$',s3/1000000000, 'Bilhões')
print('Valor arrecadado em 2012:US$',s4/1000000000, 'Bilhões')
print('Valor arrecadado em 2013:US$',s5/1000000000, 'Bilhões')
print('Valor arrecadado em 2015:US$',s6/1000000000, 'Bilhões')
print('Valor arrecadado em 2017:US$',s7/1000000000, 'Bilhões')
print('Valor arrecadado em 2018:US$',s8/1000000000, 'Bilhões')
print('Valor arrecadado em 2019:US$',s9/1000000000, 'Bilhões')

