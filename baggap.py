from rubixgram import (Client); #from time import (sleep);from random import (choice)

bot = Client("exkrbbkbkeuzsodmifoqninbtrhewfmz")

links = "https://rubika.ir/joing/DDDCECFD0DRYWUKMZJEXKQYTSSQFZWBA"

#text = "تولد سالمون"

while True :
	try:
		join=bot.joinGroup(links)
		guid = join['data']['group']['group_guid']
		#bot.sendMessage(guid,text)
		bot.sendVoice(guid,"/storage/emulated/0/VoiceChanger/باگ گپ.mp3",time="66388383444")
		print("Send gap voice ")
	
	except:break