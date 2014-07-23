import pafy

def getDownloadList():
	# Gets all the urls from musicfile
	musicFile = open("musicFile.txt", "r")
	downloadList = []
	for url in musicFile:
		downloadList.append(url.strip())
	musicFile.close()
	return downloadList

def downloadMusic(files):
	for url in files:
		audio = pafy.new(url)
		audiofiles = []

		audiofile = audio.getbestaudio(preftype="m4a")
		myfilename = audiofile.title + "." + audiofile.extension

		audiofile.download(filepath=myfilename)

downloadMusic(getDownloadList())
	
print("")