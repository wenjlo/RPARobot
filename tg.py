from telegram import Bot
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import telegram
bot = Bot(token='7709895587:AAG1d1S4t1PlL73FA0adcWUhVb1ETEuGcv4')
# -1002427408332 群組
# -1002420365302 頻道
#asyncio.run(bot.sendMessage(chat_id='-1002427408332', text='發送給群組'))
asyncio.run(bot.send_video(chat_id='-1002427408332', video=open(r'C:\Users\User\Downloads\白虎性感OL - 1of2.mp4', 'rb'), supports_streaming=True))
