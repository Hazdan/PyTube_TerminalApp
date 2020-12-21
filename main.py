from pytube import YouTube

def main():
    url = input('Enter a url of a video:\n')
    video = YouTube(url)
    stream = video.streams.get_by_itag('22')
    stream.download(r'Downloads')


if __name__ == '__main__':
    main()