# ScapICMP
 Primer Lab de cripto, esta vez, bien hecho

## Descripción de lab

Usted empieza a trabajar en una empresa tecnológica que se jacta de poseer sistemas
que permiten identificar filtraciones de información a través de Deep Packet Inspection
(DPI). A usted le han encomendado auditar si efectivamente estos sistemas son capaces
de detectar las filtraciones a través de tráfico de red. Debido a que el programa ping es
ampliamente utilizado desde dentro y hacia fuera de la empresa, su tarea será crear un
software que permita replicar tráfico generado por el programa ping con su configuración
por defecto, pero con fragmentos de información confidencial. Recuerde que al comparar
tráfico real con el generado no debe gatillar alarmas. De todas formas, deberá hacer
una prueba de concepto, en la cual se demuestre que al conocer el algoritmo, será
fácil determinar el mensaje en claro. 

## Herramientas a utilizar.

Para este laboratorio se utilizaron las siguiente herramientas:

- Anaconda -> Conda -> Python3 (Python)

De las Librerías de Python se utilizaron las siguientes:

- [Scapy](https://scapy.net/)
- [Termcolor](https://pypi.org/project/termcolor/)
- [pyspellchecker](https://pypi.org/project/pyspellchecker/)

Otras herramientas utilizadas fueron:

- ChatGPT: Inteligencia Artificial para contrucción de codigo.
- Copilot: Inteligencia Artificial para corrección de código, analisis de depuración, etc.

## Procedimiento

1. Si no se tiene instalado [Python](https://www.python.org/) o [Anaconda](https://www.anaconda.com/) instalar, junto con todas las librerías mencionadas. Para esto ultimo, siga as intrucciones de cada librería.  
1. Serciorase de que no haya más procesos utilizando la instancia loopback.
2. Inicializar captura de paquetes en el puerto loopback (ln0).
3. Ejecutar ICMPSendCesar.py mediante el siguiente comando ```python ICMPSendCesar.py``` y realizar instrucciones. Si no funciona, alternativamente intentar ```python3 ICMPSendCesar.py```. Si con este ultimo llegara a funcionar, remplaze todos los comandos python -> python3.
4. Guarde el archivo capturado en el directorio donde se aloja este github como `captura.pcap` remplazando el actual (Usar este nombre es mandatorio).
5. Ejecute ```python pcapInterpeter.py```, si su mensaje tiene palabras que estan en ingles o español bien escritas, su mensaje se resaltara en verde.

