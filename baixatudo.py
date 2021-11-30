from pytube import YouTube
from time import sleep

while True:
    try:
        link = str(input('Insira o link do vídeo: '))
        video = YouTube(link)
        print(f'Efetuando o download de: {video.title}')
        print('Carregando...')
        sleep(3)

        stream = video.streams.get_highest_resolution()
        stream.download()
        print('Download realizado com sucesso!')

        break
    except:
        print('Por favor insira um link válido.')
