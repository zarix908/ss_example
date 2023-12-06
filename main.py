import httpx 
from httpx_socks import SyncProxyTransport

def main():
    transport = SyncProxyTransport.from_url('socks5://127.0.0.1:1080')
    with httpx.Client(transport=transport) as client:
        res = client.get("https://twitter.com")
        print(res.text)

if __name__ == '__main__':
    main()
