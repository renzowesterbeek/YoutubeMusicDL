# Console Version of the Python Youtube downloader 
# App by Renzo Westerbeek - 2014

import pafy
import os
import errno
execfile("general.py") # Includes generalfunctions file

# Gets all the urls from urlfile
def get_download_list(urlfile):
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
		myfilename = "Downloads/Audio/" + audiofile.title + "." + audiofile.extension

		audiofile.download(filepath=myfilename)
		
def download_video(files):
	for url in files:
		video = pafy.new(url)

		videofile = video.getbest(preftype="mp4")
		myfilename = "Downloads/Video/" + videofile.title + "." + videofile.extension

		videofile.download(filepath=myfilename)

def download_files(files, dltype):
	for url in files:
		thefile = pafy.new(url)
		if(dltype == "Video"):
			file = thefile.getbest(preftype="mp4")
		else:
			file = thefile.getbestaudio(preftype="m4a")
		
		myfilename = "Downloads/"+dltype+"/" + file.title + "." + file.extension

		file.download(filepath=myfilename)

videoOptions = ["video", "Video", "v", "V"]
audioOptions = ["audio", "Audio", "a", "A"]

make_sure_path_exists("Downloads")

print("Want to download video or audio?")
typeInput = ""

# Choose video or audio mode
while typeInput not in videoOptions and typeInput not in audioOptions:
	typeInput = raw_input("video or audio? (v/a) ")
if typeInput in videoOptions:
	dltype = "Video"
else:
	dltype = "Audio"

# Adding urls to list
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

# Start download
print("Download starting...")
make_sure_path_exists("Downloads/" + dltype)
download_files(urlList, dltype)
	
print("")