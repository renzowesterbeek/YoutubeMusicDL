# Console Version of the Python Youtube downloader 
# App by Renzo Westerbeek - 2014

import pafy
import os
import errno

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def get_download_list(urlfile):
	# Gets all the urls from urlfile
	urlfile = open(urlfile, "r")
	downloadList = []
	for url in urlfile:
		downloadList.append(url.strip())
	urlfile.close()
	return downloadList

def download_audio(files):
	for url in files:
		audio = pafy.new(url)

		audiofile = audio.getbestaudio(preftype="m4a")
		myfilename = "YTDownloads/Audio/" + audiofile.title + "." + audiofile.extension

		audiofile.download(filepath=myfilename)
		
def download_video(files):
	for url in files:
		video = pafy.new(url)

		videofile = video.getbest(preftype="mp4")
		myfilename = "YTDownloads/Video/" + videofile.title + "." + videofile.extension

		videofile.download(filepath=myfilename)

videoOptions = ["video", "Video", "v", "V"]
audioOptions = ["audio", "Audio", "a", "A"]

make_sure_path_exists("YTDownloads")

print("Want to download Video or Audio?")
typeInput = ""
while typeInput not in videoOptions and typeInput not in audioOptions:
	typeInput = raw_input("V/A? ")
if typeInput in videoOptions:
	type = "Video"
else:
	type = "Audio"

print("Enter Youtube url(s) or a textfile with url(s), 1 per line.")
print("Put in empty line to start download.")	

urlInput = "."
urlList = []
while urlInput != "":
	urlInput = raw_input("")
	if '.txt' in urlInput:
		urlList = get_download_list(urlInput)
	else:
		urlList.append(urlInput)

urlList.pop(-1) # Remove last enter (nil) from list
print("Download starting...")

if type == "Video":
	make_sure_path_exists("YTDownloads/Video")
	download_video(urlList)
else:
	make_sure_path_exists("YTDownloads/Audio")
	download_audio(urlList)
	
print("")