import os
import sys
import stat
import hashlib
import mimetypes
import requests
import datetime
import tempfile
import chardet
import time
try:
    from PIL import Image
    from PIL.ExifTags import TAGS, GPSTAGS
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

from colorama import Fore, Style, init

init(autoreset=True)

def print_logo():
    print(r"""
███╗   ███╗███████╗████████╗ █████╗ ██████╗  █████╗ ████████╗ █████╗     ███████╗██╗  ██╗██████╗  ██████╗ ███████╗███████╗██████╗ 
████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗    ██╔════╝╚██╗██╔╝██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔══██╗
██╔████╔██║█████╗     ██║   ███████║██║  ██║███████║   ██║   ███████║    █████╗   ╚███╔╝ ██████╔╝██║   ██║███████╗█████╗  ██║  ██║
██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║  ██║██╔══██║   ██║   ██╔══██║    ██╔══╝   ██╔██╗ ██╔═══╝ ██║   ██║╚════██║██╔══╝  ██║  ██║
██║ ╚═╝ ██║███████╗   ██║   ██║  ██║██████╔╝██║  ██║   ██║   ██║  ██║    ███████╗██╔╝ ██╗██║     ╚██████╔╝███████║███████╗██████╔╝
╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚══════╝╚══════╝╚═════╝ 
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ 
                                                                                                                                  
███╗   ███╗ █████╗ ██████╗ ███████╗    ██████╗ ██╗   ██╗    ██╗   ██╗ ██╗██╗    ████████╗██████╗ ██████╗                         
████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██╔══██╗╚██╗ ██╔╝    ██║   ██║███║██║    ╚══██╔══╝██╔══██╗██╔══██╗                        
██╔████╔██║███████║██║  ██║█████╗      ██████╔╝ ╚████╔╝     ██║   ██║╚██║██║       ██║   ██████╔╝██████╔╝                        
██║╚██╔╝██║██╔══██║██║  ██║██╔══╝      ██╔══██╗  ╚██╔╝      ╚██╗ ██╔╝ ██║██║       ██║   ██╔══██╗██╔══██╗                        
██║ ╚═╝ ██║██║  ██║██████╔╝███████╗    ██████╔╝   ██║        ╚████╔╝  ██║███████   ██║   ██║  ██║██║  ██║                        
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝    ╚═════╝    ╚═╝         ╚═══╝   ╚═╝╚══════╝  ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝                           
""")

def loading_bar(duration=3):
    length = 30
    for i in range(duration * 10):
        progress = int((i / (duration * 10)) * length)
        bar = "■" * progress + "-" * (length - progress)
        percent = int((i / (duration * 10)) * 100)
        sys.stdout.write(f"\r[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(f"\r[{'■'*length}] 100%\n")

def format_size(size):
    for unit in ['B','KB','MB','GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

def calc_hashes(filepath):
    hashes = {'md5': None, 'sha1': None, 'sha256': None}
    try:
        with open(filepath, "rb") as f:
            data = f.read()
            hashes['md5'] = hashlib.md5(data).hexdigest()
            hashes['sha1'] = hashlib.sha1(data).hexdigest()
            hashes['sha256'] = hashlib.sha256(data).hexdigest()
    except Exception as e:
        print(Fore.RED + f"[!] Hash error: {e}")
    return hashes

def get_permissions(filepath):
    try:
        st = os.stat(filepath)
        return stat.filemode(st.st_mode)
    except Exception:
        return "N/A"

def get_file_encoding(filepath):
    try:
        with open(filepath, 'rb') as f:
            raw = f.read(4096)
            result = chardet.detect(raw)
            return result['encoding']
    except Exception:
        return "Unknown"

def get_strings(filepath, min_length=4):
    try:
        with open(filepath, 'rb') as f:
            result = []
            buffer = ""
            for byte in f.read():
                if 32 <= byte <= 126:
                    buffer += chr(byte)
                    continue
                if len(buffer) >= min_length:
                    result.append(buffer)
                buffer = ""
            if len(buffer) >= min_length:
                result.append(buffer)
            return result[:20]  # max 20 strings
    except Exception:
        return []

def get_exif_data(filepath):
    if not PIL_AVAILABLE:
        return None
    try:
        image = Image.open(filepath)
        info = image._getexif()
        if not info:
            return None
        exif = {}
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            exif[decoded] = value

        gps_data = {}
        if 'GPSInfo' in exif:
            for t in exif['GPSInfo']:
                sub_decoded = GPSTAGS.get(t, t)
                gps_data[sub_decoded] = exif['GPSInfo'][t]

            lat = _convert_to_degrees(gps_data.get('GPSLatitude'), gps_data.get('GPSLatitudeRef'))
            lon = _convert_to_degrees(gps_data.get('GPSLongitude'), gps_data.get('GPSLongitudeRef'))
            return {'EXIF': exif, 'GPS': {'Latitude': lat, 'Longitude': lon}}
        return {'EXIF': exif}
    except Exception:
        return None

def _convert_to_degrees(value, ref):
    if not value or not ref:
        return None
    d, m, s = value
    degrees = d[0]/d[1] + (m[0]/m[1])/60 + (s[0]/s[1])/3600
    if ref in ['S', 'W']:
        degrees = -degrees
    return degrees

def print_table(data):
    print(Style.BRIGHT + "+" + "-"*27 + "+" + "-"*59 + "+")
    print("| {:<25} | {:<57} |".format("Champ", "Valeur"))
    print("+" + "-"*27 + "+" + "-"*59 + "+")
    for key, value in data.items():
        printable = str(value) if value is not None else "N/A"
        print("| {:<25} | {:<57} |".format(key, printable[:57]))
    print("+" + "-"*27 + "+" + "-"*59 + "+\n")

def analyze_file(filepath, mode="extended"):
    print(Style.BRIGHT + f"\n[+] Analyse de : {filepath}")
    loading_bar(duration=2) 
    try:
        full_path = os.path.abspath(filepath)
        stat_info = os.stat(full_path)
        mimetype, _ = mimetypes.guess_type(full_path)
        hashes = calc_hashes(full_path)
        encoding = get_file_encoding(full_path)
        strings = get_strings(full_path)
        exif = get_exif_data(full_path)

        infos = {
            "Nom du fichier": os.path.basename(full_path),
            "Chemin absolu": full_path,
            "Taille": format_size(stat_info.st_size),
            "Permissions": get_permissions(full_path),
            "MIME Type": mimetype or "Inconnu",
            "Encodage": encoding,
            "Création": datetime.datetime.fromtimestamp(stat_info.st_ctime),
            "Dernière modification": datetime.datetime.fromtimestamp(stat_info.st_mtime),
            "Dernier accès": datetime.datetime.fromtimestamp(stat_info.st_atime),
            "MD5": hashes['md5'],
            "SHA1": hashes['sha1'],
            "SHA256": hashes['sha256'],
        }

        if exif:
            infos["EXIF (présent)"] = "Oui"
            if 'GPS' in exif and exif['GPS']['Latitude'] and exif['GPS']['Longitude']:
                infos["Latitude"] = exif['GPS']['Latitude']
                infos["Longitude"] = exif['GPS']['Longitude']
        else:
            infos["EXIF (présent)"] = "Non"

        print_table(infos)

        if mode == "extended":
            print(Style.BRIGHT + "[*] Readable strings in the file :")
            for s in strings:
                print("  •", s)
            print()

    except Exception as e:
        print(Fore.RED + f"[!] Error while parsing : {e}")

def analyze_url(url, mode="extended"):
    print(Style.BRIGHT + f"\n[+] Download from : {url}")
    loading_bar(duration=2)
    try:
        r = requests.get(url, stream=True, timeout=10)
        r.raise_for_status()

        suffix = os.path.splitext(url)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
            for chunk in r.iter_content(chunk_size=8192):
                tmp_file.write(chunk)
            tmp_path = tmp_file.name

        print(Style.BRIGHT + f"[+] Temporary file saved : {tmp_path}")
        analyze_file(tmp_path, mode)

        os.remove(tmp_path)

    except Exception as e:
        print(Fore.RED + f"[!] Error while downloading or analyzing : {e}")

def menu_select_mode():
    print("\nDisplay mode :")
    print("1 - Extended (details + readable strings)")
    print("2 - Reduced (essential information only)")
    while True:
        choice = input(">>> ").strip()
        if choice == "1":
            return "extended"
        elif choice == "2":
            return "reduced"
        else:
            print("Invalid choice.")

def menu_select_source():
    print("\nSelecting the type of analysis :")
    print("1 - Local file")
    print("2 - Remote file (URL)")
    print("3 - Leave")
    while True:
        choice = input(">>> ").strip()
        if choice == "1":
            return "local"
        elif choice == "2":
            return "url"
        elif choice == "3":
            sys.exit(0)
        else:
            print("Invalid choice.")

def get_local_files():
    print("\n[?] Enter one or more file paths separated by a comma :")
    paths = input(">>> ").split(",")
    return [p.strip() for p in paths if p.strip()]

def get_url_list():
    print("\n[?] Enter one or more URLs separated by a comma :")
    urls = input(">>> ").split(",")
    return [u.strip() for u in urls if u.strip()]

if __name__ == "__main__":
    print_logo()

    while True:
        source = menu_select_source()
        mode = menu_select_mode()

        if source == "local":
            files = get_local_files()
            for file in files:
                if os.path.isfile(file):
                    analyze_file(file, mode)
                else:
                    print(Fore.RED + f"[!] File not found : {file}")

        elif source == "url":
            urls = get_url_list()
            for url in urls:
                if url.startswith("http://") or url.startswith("https://"):
                    analyze_url(url, mode)
                else:
                    print(Fore.RED + f"[!] Invalid URL : {url}")
