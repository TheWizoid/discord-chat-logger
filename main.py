import discord
import os

class Bot(discord.Client):

    def on_message(self, message):
        self.log(message)

    def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)

    def log(self, message):
        try:
            chatlog = open("{}/chatlog.txt".format(message.server.id), "a", encoding="utf-8")
        except:
            try:
                os.mkdir("{}".format(message.server.id))
            except:
                pass
            chatlog = open("{0}/chatlog.txt".format(message.server.id),"w",encoding="utf-8")
            chatlog.close()
            chatlog = open("{0}/chatlog.txt".format(message.server.id),"a",encoding="utf-8")
        """Uploaded files"""
        try:
            message.content += (" " + str(message.attachments[0]["url"]))
        except:
            pass
        """Time is in UTC+0000"""
        chatlog.write("[{}][{}]{}:{}\n".format(str(message.timestamp),message.channel,message.author.name,message.content))
        chatlog.close()


a = Bot()
a.run("MjIxMDQ5MTQ4NTU4ODAyOTQ0.CqpLwA.MGMOmRJR7TQNXYzaxXIfW60WNUU")