# Imports
import subprocess
import webbrowser
import platform
import ctypes
import socket
import typing
import sys
import os

# Auto pip install the package
for package in [['requests'], ['rgbprint'], ['colorama'], ['pwinput']]:
    try:
        __import__(package[-1])
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package[0]])

from rgbprint import gradient_print
import requests
import pwinput

# Title 
ctypes.windll.kernel32.SetConsoleTitleW(f"Logged in as: {os.getlogin()}")

current_folder = str(os.path.dirname(os.path.abspath(sys.argv[0]))).replace('\\', "/") + "/"

sys_os = platform.system()
def clear():
    os.system("cls") if sys_os == "Windows" else os.system('clear')
   
def press_enter_to_continue():
	pwinput.pwinput(
		prompt=f"\nPress enter to continue...",
		mask=''
	)
        
def get_private_ip():
	hostname = socket.gethostname()
	ip_address = socket.gethostbyname(hostname)
	if ip_address.startswith('::ffff:'):
		ip_address = ip_address[7:]
	return ip_address


def get_self_ip() -> str | None:
	response = requests.get(
		'https://useful-apis.user0092.ml/get_ip.php',
		headers={
			'User-Agent': 'useful_hBsbzc5N68ACCx3fWti2HWjd55mW53prELLjLxqZE6KUjz4guiyQv45bcF2Dt9vVxhKzayYFGGCL7jbG7FXG6K_apis'
		}
	)

	if response.status_code != 200:
		return None

	return response.json()['ip']

def better_print(*text, end='\n'):
	for line in text:
		for char in line:
			print(char, end='')
	print('', end=end)

def get_text_length(text: str):
	for i in TextColor.__dict__.items():
		if isinstance(i[1], str):
			text = text.replace(i[1], '')

	return len(text)
        
class Color:
	def __init__(self, r: int | str, g: typing.Optional[int] = None, b: typing.Optional[int] = None) -> None:
		if isinstance(r, str) and g is None and b is None:
			if not r.startswith('#'):
				r = '#' + r

			r += "0" * (6 - len(r))
			r, g, b = tuple(int(r[i:i + 2], 16) for i in (1, 3, 5))

		else:
			if g is None or not isinstance(g, int):
				g = 0

			if b is None or not isinstance(b, int):
				b = 0

		self.__r, self.__g, self.__b = r, g, b
		self.__fore: str = f"\x1b[38;2;{self.__r};{self.__g};{self.__b}m"
		self.__back: str = f"\x1b[48;2;{self.__r};{self.__g};{self.__b}m""]"
		self.__printable: str = f'{r}, {g}, {b}'
		self.__rgb: tuple = (self.__r, self.__g, self.__b)

	class InvalidType(Exception):
		pass

	@property
	def fore(self):
		return self.__fore

	@property
	def back(self):
		return self.__back

	@property
	def printable(self):
		return self.__printable

	@property
	def rgb(self):
		return self.__rgb

	@property
	def r(self):
		return self.__r

	@property
	def g(self):
		return self.__g

	@property
	def b(self):
		return self.__b


class TextColor:
	yellow = Color(255, 255, 0).fore
	red = Color(255, 0, 0).fore
	green = Color(0, 128, 0).fore
	lime = Color(0, 255, 0).fore
	blue = Color(0, 0, 255).fore
	royal_blue = Color(65, 105, 225).fore
	electric_purple = Color(184, 0, 255).fore
	cyan = Color(0, 246, 255).fore
	white = Color(255, 255, 255).fore
	grey = Color(128, 128, 128).fore
	black = Color(0, 0, 0).fore
	light_black = Color(90, 90, 90).fore
	light_blue = Color(173, 216, 230).fore
	reset = white

while True:
    clear()
    Tool_main = f"""
                                                                _____              
                                        ╭─╮  ╭─╮               │_   _│             
                                        │ │  │ │___  ___ _ __    │ │  _ __   ___   
                                        │ │  │ / __│/ _ \ '__│   │ │ │ '_ \ / __│  
                                        │ │__│ \__ \  __/ │     _│ │_│ │ │ │ (__ _ 
                                         \____/│___/\___│_│    │_____│_│ │_│\___(_)     
                            ╭─────────────────────────────────────────────────────────────╮
                            │                          User Inc.                          │
                            ├────┬─────────────────────────┬────┬─────────────────────────┤
                            │ 1  │ Pinger                  │ 8  │ Task Manager            │
                            │ 2  │ TCP Ping                │ 9  │ Check Host              │
                            │ 3  │ Port Scan               │ -- │                         │
                            │ 4  │ Lookup                  │ -- │                         │
                            │ 5  │ Lookup my IP            │ -- │                         │
                            │ 6  │ What's my IP            │ -- │                         │
                            │ 7  │ Weather Info            │ -- │                         │
                            ╰────┴─────────────────────────┴────┴─────────────────────────╯
                                                    Made By User0420
    """

    gradient_print(Tool_main, start_color=0x00F6FF, end_color=0xB700FF)

    choice = input(f"{TextColor.light_black}┏━({TextColor.green}root-{os.getlogin()}{TextColor.light_black})\n┗━━╸▶{TextColor.reset} ")

    while type(choice) != int:
        try:
            choice = int(choice)
            break
        except:
            choice = input(f"{TextColor.light_black}┏━({TextColor.green}root-{os.getlogin()}{TextColor.light_black})\n┗━━╸▶{TextColor.reset} ")

    if int(choice) < 1 or int(choice) > 9:
            choice = input(f"{TextColor.light_black}┏━({TextColor.green}root-{os.getlogin()}{TextColor.light_black})\n┗━━╸▶{TextColor.reset} ")
    
    elif choice == 1:
        host = input("Enter the IP address: ")
        num = input("Number of requests: ")
        os.system(f"ping {host} -n {num}")
        press_enter_to_continue()

    elif choice == 2:
        host = input("Enter the IP address: ")
        port = input("Enter the Port: ")
        num = input("Number of requests: ")

        command = f'{current_folder}paping.exe {host} -p {port} -c {num}'
        subprocess.run(command, shell=True)
        
        press_enter_to_continue()

    elif choice == 3:
        host = input("Enter the IP: ")
        start_port = input("Enter the starting port: ")
        end_port = input("Enter the ending port: ")
        
        print(f'{TextColor.electric_purple}Please wait...{TextColor.reset}', end='\r', flush=True)

        for port in range(int(start_port), int(end_port) + 1):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.1)  # set timeout to 0.2 seconds
                    result = s.connect_ex((host, port))
                    if result == 0:
                        print(f'Port {port} is open')
                    # else:
                    #     print(f'Port {port} is closed')
            except socket.error as e:
                    print(f'Error occurred while scanning port {port}: {str(e)}')
        press_enter_to_continue()
          
    elif choice == 4:
        def get_ip_info() -> dict:
            try:
                response = requests.get(
                    f'http://demo.ip-api.com/json/{host}?fields=66842623&lang=en',
                    headers={'User-Agent': '5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5666.197 Safari/537.36'}
                )
                if response.status_code == 200:
                    return {
                        'status': True,
                        'data': response.json()
                    }
                else:
                    return {
                        'status': False,
                        'message': f'Invalid response ({response.status_code})'
                    }
            except Exception as e:
                return {
                    'status': False,
                    'message': f'Unexpected error: {e}'
                }
            
        host = input("Enter the host: ")
        ip_info = get_ip_info()
        data = ip_info['data']
        info: list = [
            f'{TextColor.royal_blue}IP:{TextColor.reset} {data["query"]}',
            f'{TextColor.royal_blue}Longitude:{TextColor.reset} {data["lon"]}',
            f'{TextColor.royal_blue}Latitude:{TextColor.reset} {data["lat"]}',
            f'{TextColor.royal_blue}Zip Code:{TextColor.reset} {data["zip"]}',
            f'{TextColor.royal_blue}Region:{TextColor.reset} {data["region"]}',
            f'{TextColor.royal_blue}City:{TextColor.reset} {data["city"]}',
            f'{TextColor.royal_blue}Proxy:{TextColor.reset} {data["proxy"]}',
            f'{TextColor.royal_blue}Timezone:{TextColor.reset} {data["timezone"]}',
            f'{TextColor.royal_blue}Organization:{TextColor.reset} {data["org"]}',
            f'{TextColor.royal_blue}Internet service provider:{TextColor.reset} {data["isp"]}'
        ]

        for item in info:
            print(item)

        press_enter_to_continue()

    elif choice == 5:
        def get_self_info() -> dict:
            try:
                response = requests.get(
                    f'http://demo.ip-api.com/json/?fields=66842623&lang=en',
                    headers={'User-Agent': '5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5666.197 Safari/537.36'}
                )
                if response.status_code == 200:
                    return {
                        'status': True,
                        'data': response.json()
                    }
                else:
                    return {
                        'status': False,
                        'message': f'Invalid response ({response.status_code})'
                    }
            except Exception as e:
                return {
                    'status': False,
                    'message': f'Unexpected error: {e}'
                }

        ip_info = get_self_info()
        data = ip_info['data']

        info: list = [
            f'{TextColor.royal_blue}IP:{TextColor.reset} {data["query"]}',
            f'{TextColor.royal_blue}Longitude:{TextColor.reset} {data["lon"]}',
            f'{TextColor.royal_blue}Latitude:{TextColor.reset} {data["lat"]}',
            f'{TextColor.royal_blue}Zip Code:{TextColor.reset} {data["zip"]}',
            f'{TextColor.royal_blue}Region:{TextColor.reset} {data["region"]}',
            f'{TextColor.royal_blue}City:{TextColor.reset} {data["city"]}',
            f'{TextColor.royal_blue}Proxy:{TextColor.reset} {data["proxy"]}',
            f'{TextColor.royal_blue}Timezone:{TextColor.reset} {data["timezone"]}',
            f'{TextColor.royal_blue}Organization:{TextColor.reset} {data["org"]}',
            f'{TextColor.royal_blue}Internet service provider:{TextColor.reset} {data["isp"]}'
        ]

        for item in info:
            print(item)
        press_enter_to_continue()

    elif choice == 6:
        self_ip = get_self_ip() or 'Failed to Retrieve'
        private_ip = get_private_ip() or 'Failed to Retrieve'

        info: list = [
            f'{TextColor.royal_blue}Public IP: {TextColor.lime if self_ip != "Failed to Retrieve" else TextColor.red}{self_ip}{TextColor.reset}',
            f'{TextColor.royal_blue}Private IP: {TextColor.lime if private_ip != "Failed to Retrieve" else TextColor.red}{private_ip}{TextColor.reset}'
        ]
        for item in info:
            print(item)
                    
        press_enter_to_continue()

    elif choice == 7:
        def get_weather_info(code: str) -> dict:
            try:
                response = requests.get(
                    f'http://api.weatherapi.com/v1/current.json?key=638e350524ab4650a4303224220807&q={code}&aqi=no',
                    headers={'User-Agent': '5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5666.197 Safari/537.36'}
                )
                if response.status_code == 200:
                    return {
                        'status': True,
                        'data': response.json()
                    }
                else:
                    return {
                        'status': False,
                        'message': f'Invalid response ({response.status_code})'
                    }
            except Exception as e:
                return {
                    'status': False,
                    'message': f'Unexpected error: {e}'
                }


        zip_code = input("Enter the Zip Code: ")
        weather_info = get_weather_info(zip_code)
        data = weather_info['data']
        
        info: list = [
            f'{TextColor.royal_blue}Time:{TextColor.reset} {data["location"].get("localtime")}',
            f'{TextColor.royal_blue}City:{TextColor.reset} {data["location"].get("name")}',
            f'{TextColor.royal_blue}State:{TextColor.reset} {data["location"].get("region")}',
            f'{TextColor.royal_blue}Country:{TextColor.reset} {data["location"].get("country")}',
            f'{TextColor.royal_blue}Timezone:{TextColor.reset} {data["location"].get("tz_id")}',

            f'{TextColor.royal_blue}Clouds:{TextColor.reset} {data["current"]["cloud"]}',
            f'{TextColor.royal_blue}Humidity:{TextColor.reset} {data["current"]["humidity"]}%',
            f'{TextColor.royal_blue}UV Index:{TextColor.reset} {data["current"]["uv"]}',
            f'{TextColor.royal_blue}Pressure:{TextColor.reset} {data["current"]["pressure_in"]} in, {data["current"]["pressure_mb"]} mb.',

            f'{TextColor.royal_blue}Condition:{TextColor.reset} {data["current"]["condition"]["text"]}',
            f'{TextColor.royal_blue}Day/Night:{TextColor.reset} {"Day" if data["current"]["is_day"] == 1 else "Night"}',
            f'{TextColor.royal_blue}Wind Speed:{TextColor.reset} {data["current"]["wind_mph"]} mph, {data["current"]["wind_kph"]} kph.',

            f'{TextColor.royal_blue}Visibility:{TextColor.reset} {data["current"]["vis_miles"]} miles, {data["current"]["vis_km"]} km.',

            f'{TextColor.royal_blue}Temperature:{TextColor.reset} {data["current"]["temp_f"]}°F, {data["current"]["temp_c"]}°C',
            f'{TextColor.royal_blue}Precipitation:{TextColor.reset} {data["current"]["precip_in"]} in, {data["current"]["precip_mm"]} mm.',
        ]
        for item in info:
            print(item)
        press_enter_to_continue()

    elif choice == 8:
        host = input("Enter the host: ")
        url = f"http://check-host.net/ip-info?host={host}"
        webbrowser.open(url)

    elif choice == 9:
        def task_manager() -> dict:
            os.startfile(r"C:\WINDOWS\system32\Taskmgr.exe")
            return {
                'status': True,
                'pre_choice': None
            }