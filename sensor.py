#        Instituto Mauá de Tecnologia
#
#        Engenharia de Computação:      Angelo Zanini / Nuncio Perrella
#        Ciência da Computação:         Ana Paula Serra / Angelo Zanini / Nuncio Perrella / Mateus Capaldo
#        Design:                        Tiago Perrella

import serial.tools.list_ports
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as mpimg

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

# url = 'https://maua.br/images/logo-IMT.png'
# image = mpimg.imread('https://maua.br/images/logo-IMT.png')

# Configuração do gráfico
fig, ax = plt.subplots()
fig.patch.set_facecolor("#004785")
# fig.figimage(image, 50, 400, zorder=1) 
xs = []
ys = []

def animate(i, xs, ys):
    # Ler uma linha da porta serial
    line = ser.readline().decode('utf-8').strip()
    # Adicionar os dados lidos nas listas

    try:
        xs.append(len(xs))
        if line == "Couldn't get distance: 0":
            raise Exception
        ys.append(float(line))
        print(line)
    except ValueError as err:
        print(f"Inicializando conexão: {err}")
        ys.append(0)
    except Exception as err:
        print(f"Valor inválido encontrado: {err}")
        ys.append(sum(ys[len(ys) - 11: len(ys) - 1])/len(ys[len(ys) - 11: len(ys) - 1]))

    # Limitar o tamanho das listas para manter o gráfico atualizado
    xs = xs[-100:]
    ys = ys[-100:]

    # Limpar e atualizar o gráfico
    ax.clear()
    ax.plot(xs, ys, color='white')

    # Configurar os eixos
    ax.set_xlabel('Tempo [ms]', color='white')
    ax.set_ylabel('Medida [mm]', color='white')
    ax.set_title('Sensor de Altura  - Mauá', color='white')

    ax.spines['bottom'].set_color('white')  
    ax.spines['left'].set_color('white')  
    ax.spines['right'].set_color('white')  
    ax.spines['top'].set_color('white') 

    ax.tick_params(axis='x', colors='white') 
    ax.tick_params(axis='y', colors='white')
   
    ax.set_facecolor("#004785")
   
# Configuração da animação
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=100)



# Mostrar o gráfico
plt.show()