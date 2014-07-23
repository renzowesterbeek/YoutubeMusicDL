import pafy

def getDownloadList():
	# Gets all the urls from the musicfile
	musicFile = open("musicFile.txt", "r")
	downloadList = []
	for url in musicFile:
		downloadList.append(url.strip())
	musicFile.close()
	return downloadList

downloadList = getDownloadList()

# Downloads music
for url in downloadList:
	audio = pafy.new(url)
	audiostreams = audio.audiostreams
	audiofiles = []
	for a in audiostreams:
		audiofiles.append(a.extension)
	print(audiofiles)

	audiofile = audio.getbestaudio(preftype="m4a")
	myfilename = audiofile.title + "." + audiofile.extension

	audiofile.download(filepath=myfilename)