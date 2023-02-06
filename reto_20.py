# * Crea una función que sume 2 números y retorne su resultado pasados
# * unos segundos.
# * - Recibirá por parámetros los 2 números a sumar y los segundos que
# *   debe tardar en finalizar su ejecución.
# * - Si el lenguaje lo soporta, deberá retornar el resultado de forma
# *   asíncrona, es decir, sin detener la ejecución del programa principal.
# *   Se podría ejecutar varias veces al mismo tiempo.
import time
import asyncio

async def sum_with_delay(num1,num2,delay): #al ser async permite la ejecución en simultaneo.
    await asyncio.sleep(delay)
    return num1+num2

print(asyncio.run(sum_with_delay(3,3,10)))

def sum_with_delay2(num1,num2,delay):
    time.sleep(delay)
    return num1+num2

print(sum_with_delay2(2,2,2))