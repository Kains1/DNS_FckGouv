import os
import sys
import ctypes
import tkinter as tk
from tkinter import messagebox

def is_admin():
    """Vérifie si le script est exécuté avec des droits administrateurs"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def elevate_privileges():
    """Relance le script avec des droits administrateurs"""
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join([f'"{arg}"' for arg in sys.argv]), None, 1
    )

def get_wifi_interface():
    """Retourne le nom de l'interface Wi-Fi connectée (SSID)"""
    try:
        output = os.popen("netsh wlan show interfaces").read()
        interface_name = None
        ssid = None

        for line in output.splitlines():
            # Détecter le nom de l'interface
            if "Nom                   :" in line:
                interface_name = line.split(":")[-1].strip()
            # Détecter le SSID
            if "SSID                  :" in line and not "BSSID" in line:
                ssid = line.split(":")[-1].strip()

        if not interface_name or not ssid:
            raise ValueError("Impossible de détecter l'interface Wi-Fi ou le SSID.")

        return interface_name, ssid
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la détection de l'interface Wi-Fi : {e}")
        return None, None

def set_dns():
    """Configurer le DNS sur 8.8.8.8 et 8.8.4.4 pour l'interface Wi-Fi"""
    interface, ssid = get_wifi_interface()
    if interface:
        try:
            os.system(f'netsh interface ip set dns name="{interface}" static 8.8.8.8')
            os.system(f'netsh interface ip add dns name="{interface}" addr=8.8.4.4 index=2')
            messagebox.showinfo("Succès", f"DNS configuré sur {interface} (SSID : {ssid}) : 8.8.8.8 et 8.8.4.4.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
    else:
        messagebox.showerror("Erreur", "Aucune interface Wi-Fi détectée.")

def reset_dns():
    """Réinitialise le DNS en mode automatique pour l'interface Wi-Fi"""
    interface, ssid = get_wifi_interface()
    if interface:
        try:
            os.system(f'netsh interface ip set dns name="{interface}" source=dhcp')
            messagebox.showinfo("Succès", f"DNS réinitialisé en mode automatique sur {interface} (SSID : {ssid}).")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
    else:
        messagebox.showerror("Erreur", "Aucune interface Wi-Fi détectée.")

def verify_dns():
    """Vérifie les paramètres DNS actuels de l'interface Wi-Fi"""
    interface, ssid = get_wifi_interface()
    if interface:
        try:
            output = os.popen(f'netsh interface ip show dns name="{interface}"').read()
            messagebox.showinfo("Paramètres DNS", f"Interface : {interface}\nSSID : {ssid}\n{output}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la vérification DNS : {e}")
    else:
        messagebox.showerror("Erreur", "Aucune interface Wi-Fi détectée pour vérification.")

def create_gui():
    """Créer l'interface graphique"""
    window = tk.Tk()
    window.title("Gestionnaire de DNS")
    window.geometry("400x250")
    
    label = tk.Label(window, text="Choisissez une action :", font=("Arial", 12))
    label.pack(pady=10)
    
    btn_set_dns = tk.Button(window, text="Configurer DNS (8.8.8.8 et 8.8.4.4)", command=set_dns, width=50)
    btn_set_dns.pack(pady=5)
    
    btn_reset_dns = tk.Button(window, text="Réinitialiser DNS (mode automatique)", command=reset_dns, width=50)
    btn_reset_dns.pack(pady=5)
    
    btn_verify_dns = tk.Button(window, text="Vérifier les paramètres DNS", command=verify_dns, width=50)
    btn_verify_dns.pack(pady=5)
    
    btn_quit = tk.Button(window, text="Quitter", command=window.quit, width=50)
    btn_quit.pack(pady=10)
    
    window.mainloop()

if __name__ == "__main__":
    if is_admin():
        create_gui()
    else:
        elevate_privileges()
