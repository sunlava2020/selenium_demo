import pytube
import time
import pafy
import os
import shutil
FILEPATH = 'H:\\srtDown\\'
FILEPATHTEST = 'H:\\srtDown\\test\\'

class VideoDownloader():
    def __init__(self):
        self.urls = {}
    def runDownload(self,download_url,save_path):
        #开始下载
        video = pafy.new(download_url)
        v_best =video.getbest() #下载最清晰画质
        mystr = v_best.download(save_path)
        print(mystr)
    #修改文件名
    def changFileName(self,olddirpath,newdirpath,newfilename):
        os.chdir(olddirpath)
        files = filter(os.path.isfile, os.listdir(olddirpath))
        files = [os.path.join(olddirpath, f) for f in files]  # add path to each file
        files.sort(key=lambda x: os.path.getmtime(x))
        newest_file = files[-1]
        os.rename(newest_file, newfilename)
        shutil.copy(os.path.join(olddirpath, newfilename), newdirpath)
        os.remove(os.path.join(olddirpath, newfilename))
if __name__ == '__main__':

    '''调用方法示例'''
    youtube = VideoDownloader() #先实例化该类，设置需要下载的url
    youtube.runDownload('https://www.youtube.com/watch?v=UDgKavi2aYM',FILEPATHTEST) #设置保存路径，并执行下载
    youtube.changFileName(FILEPATHTEST,FILEPATH,"1__.mp4")
    
