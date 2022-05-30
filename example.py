import json

print('Opcion 2: Jugar nueva partida')
n = str(input())
print('Partida Guardada!!')
print()

p_saved_games = {}
saved_games_sin_p = {}
new_dict = {}
with open('temporal.json') as f:
    data = [json.loads(line) for line in f]

i = 0
for line in data:
    for key in line.items():
        if key[0] == n:
            
            dict = line[key[0]]
            name = key[0]

            p_saved_games[i] = line

            grid = dict['partida']
            grid_o = dict['grid_original']
            tiempo = dict['tiempo']
            errores = dict['errores']
            puntaje = tiempo - errores
            if n == name:
                i+=1
        else:
            name = key[0]
            saved_games_sin_p[name] = line[key[0]]
        new_dict[key[0]] = {'puntaje':0,'partidas':0}


print('Opcion 3: Jugar una partida guardada:')
for x in p_saved_games:
    print('Juego numero:',x)
    print(p_saved_games[x])
y = int(input('Que partida quiere eliminar?'))
del(p_saved_games[y])

for line in data:
    for key in line.items():
        name = key[0]
        tiempo = line[name]['tiempo']
        errores = line[name]['errores']
        puntaje = tiempo - errores
        new_dict[name]['partidas'] += 1
        new_dict[name]['puntaje'] += puntaje

print()
print('Opcion 4: Mostrar partidas por jugador')
sorted_dict = sorted(new_dict.items(),key=lambda kv: kv[1]['puntaje'], reverse=True) 
print(sorted_dict)

for i in p_saved_games:
    saved_games_sin_p[n] = p_saved_games[i][n]

f = open('temporal.json','w')
for line in saved_games_sin_p:
    dict={line:saved_games_sin_p[line]}
    data = json.dumps(dict)
    f.write(data)
    f.write('\n')
f.close


'''
data = json.dumps(saved_games_sin_p)
f = open('temporal.json','w')
f.write(data)
f.close'''