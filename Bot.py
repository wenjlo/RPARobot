import telebot
from config import tg_token,channel_id,group_id
import asyncio

class telegram:
    def __init__(self,token):
        self.token = token
        self.bot = telebot.TeleBot(self.token)
    def send_video(self,video_path,chat_id,caption):
        self.bot.send_video(chat_id=chat_id, video=open(video_path, 'rb'), caption=caption,
                       supports_streaming=True)
# -1002427408332 群組
# -1002420365302 頻道
video_path = r'C:\Users\User\Downloads\Telegram Desktop\PRED-704 - 2of6.mp4'
image_path = r'C:\Users\User\Downloads\1-1.jpg'
file_path = r'C:\Users\User\Downloads\1-3.txt'
with open(file_path, 'r',encoding="utf-8") as file:
    file_content = file.read()
file_content = 'PRED-704 - 2of6'

bot = telebot.TeleBot(tg_token)
#
# def send_progress(bytes_sent, total_bytes, file_name):
#     percent = int(bytes_sent * 100 / total_bytes)
#     print(f"Uploading {file_name}: {percent}%")

async def send_video(GROUP_ID):
    await bot.send_video(chat_id=GROUP_ID,video=open('C:/Users/User/Downloads/Telegram Desktop/PRED-704 - 1of6.mp4', 'rb'),supports_streaming=True,width=1280,height=720,timeout=1000000
    )
asyncio.run(send_video(group_id))
# for i in range(1,2):
#     file_content = f'PRED-704 - {i}of6'
#     video_path = f'C:/Users/User/Downloads/Telegram Desktop/PRED-704 - {i}of6.mp4'
#     # with open(image_path, 'rb') as thumb:
#     #     bot.send_video(chat_id=group_id, video=open(video_path, 'rb'), caption=file_content,thumb=thumb, supports_streaming=True,width=1280,height=720,timeout=100000)
#     bot.send_message(chat_id=group_id,text=file_content)
# bot = telegram(token=tg_token)
# bot.send_video(r'C:\Users\User\Downloads\白虎性感OL - 1of2.mp4',group_id,'白虎性感OL Part1')
# Replace 'YOUR_BOT_TOKEN' with your actual bot token
# bot = telebot.TeleBot('7709895587:AAG1d1S4t1PlL73FA0adcWUhVb1ETEuGcv4')
#
# # Replace 'PATH_TO_YOUR_VIDEO' with the path to your video file
# video_path = r'C:\Users\User\Downloads\白虎性感OL - 1of2.mp4'
#
# # Send the video to a specific chat ID (replace 'CHAT_ID' with the actual chat ID)
# #bot.send_message(chat_id='-1002427408332',text='白虎性感OL')
# bot.send_video(chat_id='-1002427408332', video=open(video_path, 'rb'),caption='白虎性感OL',supports_streaming=True)
