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
            #有字幕的视频要,没有字幕的视频不要
            if len(yt.captions.all()) > 0:
                #视频下载
                fileNameAll0 = FILEPATH + str(id)
                video = yt.streams.filter(file_extension='mp4', res='1080p').first()
                video1 = yt.streams.filter(file_extension='mp4', res='720p').first()
                video = video if video!=None else video1
                print("即将下载的视频是:",video)
                video.download(FILEPATH, str(id)+"", '')
                print("下载完毕!.......")

if __name__ == '__main__':
    downloader = VideoDownloader()
    downloader.urls[0] = "https://www.youtube.com/watch?v=wJ4hXGq0TV0"
    downloader.getVideo()
