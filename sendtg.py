import telebot
from config import tg_token,group_id
from telebot import types

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot(tg_token)

@bot.message_handler(commands=['send_videos'])
def send_videos(message):
    # List of video file paths
    video_paths = [
        r'C:\Users\User\Downloads\Telegram Desktop\PRED-704 - 1of6.mp4',
        r'C:\Users\User\Downloads\Telegram Desktop\PRED-704 - 2of6.mp4',
        # ... more video paths
    ]

    for video_path in video_paths:
        with open(video_path, 'rb') as video:
            bot.send_video(chat_id=group_id, video=video, caption="Video caption",supports_streaming=True)

bot.polling()