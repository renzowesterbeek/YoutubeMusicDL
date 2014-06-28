import pafy

# Gets all the urls from the musicfile
musicFile = open("musicFile.txt", "r")
downloadList = []
for url in musicFile:
    downloadList.append(url.strip())
musicFile.close()

# Downloads music
for url in downloadList:
	audio = pafy.new(url)
	audiofile = audio.getbestaudio()
	myfilename = "audiofiles/" + audiofile.title + "." + audiofile.extension

	audiofile.download(filepath=myfilename)