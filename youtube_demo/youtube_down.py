import pytube
import time
FILEPATH = 'H:\\srtDown\\'

class VideoDownloader():
    def __init__(self):
        self.urls = {}
        
    def getVideo(self):
        for id in list(self.urls.keys()):
            yt = pytube.YouTube(self.urls[id])
            print("id: "+str(id)+" url=="+self.urls[id])
            print(yt.captions.all())
            #Video with subtitles, no video without subtitles
            if len(yt.captions.all()) > 0:
                #Video download
                fileNameAll0 = FILEPATH + str(id)
                video = yt.streams.filter(file_extension='mp4', res='1080p').first()
                video1 = yt.streams.filter(file_extension='mp4', res='720p').first()
                video = video if video!=None else video1
                print("The upcoming video is:",video)
                video.download(FILEPATH, str(id)+"", '')
                print("The download!.......")

if __name__ == '__main__':
    downloader = VideoDownloader()
    downloader.urls[0] = "https://www.youtube.com/watch?v=wJ4hXGq0TV0"
    downloader.getVideo()
