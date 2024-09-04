#        Instituto Mauá de Tecnologia
#
#        Engenharia de Computação:      Angelo Zanini / Nuncio Perrella
#        Ciência da Computação:         Ana Paula Serra / Angelo Zanini / Nuncio Perrella / Mateus Capaldo
#        Design:                        Tiago Perrella
import serial.tools.list_ports
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def listar_portas_seriais():
    portas = serial.tools.list_ports.comports()
    for porta in portas:
        print(porta)

if __name__ == "__main__":
    listar_portas_seriais()



# Configuração da porta serial
#ser = serial.Serial('COM11', 115200)  # Substitua 'COM3' pela porta serial correta
ser = serial.Serial(          
    port='COM3',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)



# Configuração do gráfico
fig, ax = plt.subplots()
xs = []
ys = []

def animate(i, xs, ys):
    # Ler uma linha da porta serial
    line = ser.readline().decode('utf-8').strip()
    # Adicionar os dados lidos nas listas
    xs.append(len(xs))
    ys.append(float(line))

    # Limitar o tamanho das listas para manter o gráfico atualizado
    xs = xs[-100:]
    ys = ys[-100:]

    # Limpar e atualizar o gráfico
    ax.clear()
    ax.plot(xs, ys)

    # Configurar os eixos
    ax.set_xlabel('Tempo [ms]')
    ax.set_ylabel('Medida [mm]')
    ax.set_title('Sensor de Altura  - Mauá')
   
   
# Configuração da animação
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=100)



# Mostrar o gráfico
plt.show()