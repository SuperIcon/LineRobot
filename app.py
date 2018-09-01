from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('HDzqQa/1o/h+0d+HMBYqVew12oTMxYoFQsSBoo5gWh2i7/SCtBy2Fta8Fs6QTeFMbSDDOYqH5dCd/SqI63imaZyCXwhV3eBqbdkE5L2wQXVgMEGTJ2dLzstnlqPOmoPGhwLGHvA3eHi3fH8BLmZhowdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b5ab18e8b1691b1f1f81f7b1b00128ed')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()