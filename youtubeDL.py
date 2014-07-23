import pafy

def getDownloadList(musicfile):
	# Gets all the urls from musicfile
	musicFile = open(musicfile, "r")
	downloadList = []
	for url in musicFile:
		downloadList.append(url.strip())
	musicFile.close()
	return downloadList

def downloadAudio(files):
	for url in files:
		audio = pafy.new(url)

		audiofile = audio.getbestaudio(preftype="m4a")
		myfilename = audiofile.title + "." + audiofile.extension

		audiofile.download(filepath=myfilename)
		
def downloadVideo(files):
	for url in files:
		video = pafy.new(url)

		videofile = video.getbest(preftype="mp4")
		myfilename = videofile.title + "." + videofile.extension

		videofile.download(filepath=myfilename)

videoOptions = ["video", "Video", "v", "V"]
audioOptions = ["audio", "Audio", "a", "A"]

print("Want to download Video or Audio?")
typeInput = ""
while typeInput not in videoOptions and typeInput not in audioOptions:
	typeInput = raw_input("V/A? ")
if typeInput in videoOptions:
	type = "Video"
else:
	type = "Audio"

print("Put in Youtube url(s) or a textfile with url(s), 1 per line.")
print("Put in empty line to start download.")	

urlInput = "."
urlList = []
while urlInput != "":
	urlInput = raw_input("")
	if '.txt' in urlInput:
		urlList = getDownloadList(urlInput)
	else:
		urlList.append(urlInput)

urlList.pop() # Remove last enter (nil) from list
print("Download starting...")

if type == "Video":
	downloadVideo(urlList)
else:
	downloadAudio(urlList)
	
print("")