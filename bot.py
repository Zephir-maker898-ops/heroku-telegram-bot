# -*- coding: utf-8 -*-
import redis
import os
import telebot
import asyncio
import aiohttp
from aiohttp import web
import json

# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
r = redis.from_url(os.environ.get("REDIS_URL"))

TOKEN = '1885600223:AAG9Be2lb9uX3-FzkB2xuVBoyEh178FJ4HM'
API_URL = 'https://api.telegram.org/bot%s/sendMessage' % TOKEN

bot = telebot.TeleBot("1885600223:AAG9Be2lb9uX3-FzkB2xuVBoyEh178FJ4HM")

async def handler(request):
    data = await request.json()
    headers = {
        'Content-Type': 'application/json'
    }
    message = {
        'chat_id': data['message']['chat']['id'],
        'text': data['message']['text']
    }
    async with aiohttp.ClientSession(loop=loop) as session:
        async with session.post(API_URL,
                                data=json.dumps(message),
                                headers=headers) as resp:
            try:
                assert resp.status == 200
            except:
                return web.Response(status=500)
    return web.Response(status=200)

async def init_app(loop):
    app = web.Application(loop=loop, middlewares=[])
    app.router.add_post('/api/v1', handler)
    return app

if __name__ == 'echo_bot':
    loop = asyncio.get_event_loop()
    try:
        app = loop.run_until_complete(init_app(loop))
        web.run_app(app, host='0.0.0.0', port=23456)
    except Exception as e:
        print('Error create server: %r' % e)
    finally:
        pass
    loop.close()

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text + ", а еще я отень люблю Лизу)💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘 и много кутаю))")



bot.infinity_polling()
