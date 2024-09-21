#        Instituto Mauá de Tecnologia
#
#        Engenharia de Computação:      Angelo Zanini / Nuncio Perrella
#        Ciência da Computação:         Ana Paula Serra / Angelo Zanini / Nuncio Perrella / Mateus Capaldo
#        Design:                        Tiago Perrella

import os
import serial.tools.list_ports
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as mpimg
#dotenv
from dotenv import load_dotenv
from urllib.request import urlopen
from io import BytesIO

def listar_portas_seriais():
    portas = serial.tools.list_ports.comports()
    return portas[0].name

ser = serial.Serial(          
    port=listar_portas_seriais(),
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
#get url with dotenv
load_dotenv()
url= os.getenv('URL_IMAGEM')

image = mpimg.imread(BytesIO(urlopen(url).read()), format=os.getenv('TIPO_IMAGEM'))

fig, ax = plt.subplots()
fig.canvas.manager.set_window_title('Sensor de Altura - Mauá')
fig.patch.set_facecolor("#02278F")
logo_ax = fig.add_axes([0.84, 0.87999, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(image)
logo_ax.axis('off')


xs = []
ys = []

def animate(i, xs, ys):
    # Ler uma linha da porta serial
    line = ser.readline().decode('utf-8').strip()
    
    try:
        xs.append(len(xs))
        if line == "Couldn't get distance: 0":
            raise Exception
        ys.append(float(line))
        
    except ValueError as err:
        print(f"Inicializando conexão: {err}")
        ys.append(0)
    except Exception as err:
        print(f"Valor inválido encontrado: {err}")
        ys.append(sum(ys[len(ys) - 11: len(ys) - 1])/len(ys[len(ys) - 11: len(ys) - 1]))
    print(line)
    # Limitar o tamanho das listas para manter o gráfico atualizado
    xs = xs[-45:]
    ys = ys[-45:]

    # Limpar e atualizar o gráfico
    ax.clear()
    ax.plot(xs, ys, color='white')


    fig_width, fig_height = fig.get_size_inches()
    base_fontsize = fig_width * 1.1 
    labelpad = fig_height * 1.7      
    title_fontsize = fig_height * 3

    ax.set_xlabel('Tempo [ms]', color='white', fontweight='bold', fontsize=base_fontsize, labelpad=labelpad)
    ax.set_ylabel('Medida [mm]', color='white', fontweight='bold', fontsize=base_fontsize, labelpad=labelpad)
    ax.set_title('Sensor de Altura - Mauá', color='white', fontweight='bold', fontsize=title_fontsize, pad=labelpad)


    ax.spines['bottom'].set_color('white')  
    ax.spines['left'].set_color('white')  
    ax.spines['right'].set_color('white')  
    ax.spines['top'].set_color('white') 

    ax.tick_params(axis='x', colors='white') 
    ax.tick_params(axis='y', colors='white')
   
    ax.set_facecolor("#02278F")
   
# Configuração da animação
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=100)

# Mostrar o gráfico
plt.show()
