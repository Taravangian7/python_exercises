#/*
# * Crea una función que evalúe si un/a atleta ha superado correctamente una
# * carrera de obstáculos.
# * - La función recibirá dos parámetros:
# *      - Un array que sólo puede contener String con las palabras
# *        "run" o "jump"
# *      - Un String que represente la pista y sólo puede contener "_" (suelo)
# *        o "|" (valla)
# * - La función imprimirá cómo ha finalizado la carrera:
# *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
# *        será correcto y no variará el símbolo de esa parte de la pista.
# *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
# *      - Si hace "run" en "|" (valla), se variará la pista por "/".
# * - La función retornará un Boolean que indique si ha superado la carrera.
# * Para ello tiene que realizar la opción correcta en cada tramo de la pista.

def race_completed(actions,trial):
    race={'run':'_','jump':'|'}
    trial_check=''
    for x,y in zip(actions,trial):
        if race[x]==y:
            trial_check+=y
        else:
            if x=='jump' and y=='_':
                trial_check+='x'
            elif x=='run' and y=='|':
                trial_check+='/'
    print(trial_check)
    if trial==trial_check:
        return True
    return False

runner_1=['run','run','jump','run','jump']
trial_a='__|_|'

print(race_completed(runner_1,trial_a))
