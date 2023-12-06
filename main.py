import httpx 
from httpx_socks import SyncProxyTransport
from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_twitter():
    transport = SyncProxyTransport.from_url('socks5://shadowsocks:1080')
    text = None
    with httpx.Client(transport=transport) as client:
        text = client.get("https://twitter.com").text
    
    return text

def main():
    app.run('0.0.0.0', 9090)

if __name__ == '__main__':
    main()
