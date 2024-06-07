from flask import Flask, jsonify, render_template
import platform
import psutil
import threading
import time

print("Başlangıç")

app = Flask(__name__, template_folder='templates')



print("Flask oluşturuldu")

system_info = {}

def get_used_ram():
    print("get_used_ram fonksiyonu çalıştı")
    ram = psutil.virtual_memory()
    used_ram = ram.used / (1024 ** 3)
    total_ram = ram.total / (1024 ** 3)
    available_ram = ram.available / (1024 ** 3)
    return used_ram, total_ram, available_ram

def get_system_info():
    print("get_system_info fonksiyonu çalıştı")
    global system_info
    system_info['İsletimSistemi'] = platform.system()
    system_info['OS_Version'] = platform.version()
    system_info['OS_Release'] = platform.release()
    system_info['İslemci'] = platform.processor()
    system_info['İslemciHizi'] = f"{psutil.cpu_freq().current:.2f} MHz"
    system_info['ÇekirdekSayisi'] = psutil.cpu_count(logical=False)
    system_info['MantıksalÇekirdekSayisi'] = psutil.cpu_count(logical=True)
    disk_usage = psutil.disk_usage('/')
    system_info['DiskKapasitesi'] = f"{disk_usage.total / (1024 ** 3):.2f} GB"
    system_info['DiskKullanılan'] = f"{disk_usage.used / (1024 ** 3):.2f} GB"
    system_info['DiskBoş'] = f"{disk_usage.free / (1024 ** 3):.2f} GB"

    used_ram, total_ram, available_ram = get_used_ram()
    system_info['Kullanılan RAM'] = f"{used_ram:.2f} GB"
    system_info['Toplam RAM'] = f"{total_ram:.2f} GB"
    system_info['Kullanılabilir RAM'] = f"{available_ram:.2f} GB"

def update_system_info():
    print("update_system_info fonksiyonu çalıştı")
    while True:
        get_system_info()
        time.sleep(5)

@app.route('/api', methods=['GET'])
def api_function():
    print("api_function çalıştı")
    return jsonify(system_info)

@app.route('/')
def index():
    print("index fonksiyonu çalıştı")
    return render_template('index.html')

if __name__ == '__main__':
    print("Uygulama başlatılıyor")
    threading.Thread(target=update_system_info, daemon=True).start()
    app.run(debug=True)
    print("Uygulama çalışıyor")
