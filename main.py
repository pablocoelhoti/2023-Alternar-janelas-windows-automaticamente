import tkinter as tk
import threading
import pyautogui
import time

class AltTabSimulator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simulador Alteracao Janelas")

        self.running = False

        self.label = tk.Label(self.root, text="Parar a Alteracao?")
        self.label.pack(pady=10)

        self.button = tk.Button(self.root, text="Parar", command=self.stop_simulation)
        self.button.pack()

        self.thread = None

    def simulate_alt_tab(self):
        while self.running:
            
            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=1)
            pyautogui.keyUp('alt')
            time.sleep(25)

            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=2)
            pyautogui.keyUp('alt')
            time.sleep(25)

            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=3)
            pyautogui.keyUp('alt')
            time.sleep(25)

            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=4)
            pyautogui.keyUp('alt')
            time.sleep(25)
            
            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=5)
            pyautogui.keyUp('alt')
            time.sleep(25)
            
            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=6)
            pyautogui.keyUp('alt')
            time.sleep(25)

    def start_simulation(self):
        self.running = True
        self.thread = threading.Thread(target=self.simulate_alt_tab)
        self.thread.start()

    def stop_simulation(self):
        self.running = False
        if self.thread:
            self.thread.join()
        self.root.destroy()

    def run(self):
        self.start_simulation()
        self.root.mainloop()

if __name__ == "__main__":
    simulator = AltTabSimulator()
    simulator.run()


import tkinter as tk
import threading
import pyautogui
import time
import ctypes

class AltTabSimulator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simulador Alteracao Janelas")

        self.running = False

        self.label = tk.Label(self.root, text="Parar a Alteracao?")
        self.label.pack(pady=10)

        self.button = tk.Button(self.root, text="Parar", command=self.stop_simulation)
        self.button.pack()

        self.thread = None

        # Variáveis para monitorar o movimento do mouse e teclas
        self.mouse_moved = False
        self.keys_pressed = False

        # Configuração do hook de mouse e teclado
        self.user32 = ctypes.windll.user32
        self.mouse_hook = self.user32.SetWindowsHookExW(0x14, self.mouse_hook_proc, None, 0)
        self.keyboard_hook = self.user32.SetWindowsHookExW(0x2, self.keyboard_hook_proc, None, 0)

    def mouse_hook_proc(self, nCode, wParam, lParam):
        if nCode >= 0:
            self.mouse_moved = True
        return self.user32.CallNextHookEx(None, nCode, wParam, lParam)

    def keyboard_hook_proc(self, nCode, wParam, lParam):
        if nCode >= 0:
            self.keys_pressed = True
        return self.user32.CallNextHookEx(None, nCode, wParam, lParam)

    def simulate_alt_tab(self):
        while self.running:
            if self.mouse_moved or self.keys_pressed:
                self.stop_simulation()
                break

            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=1)
            pyautogui.keyUp('alt')
            time.sleep(25)

            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=2)
            pyautogui.keyUp('alt')
            time.sleep(25)

            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=3)
            pyautogui.keyUp('alt')
            time.sleep(25)

            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=4)
            pyautogui.keyUp('alt')
            time.sleep(25)

            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=5)
            pyautogui.keyUp('alt')
            time.sleep(25)

            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=6)
            pyautogui.keyUp('alt')
            time.sleep(25)

    def start_simulation(self):
        self.running = True
        self.thread = threading.Thread(target=self.simulate_alt_tab)
        self.thread.start()

    def stop_simulation(self):
        self.running = False
        if self.thread:
            self.thread.join()
        self.user32.UnhookWindowsHookEx(self.mouse_hook)
        self.user32.UnhookWindowsHookEx(self.keyboard_hook)
        self.root.destroy()

    def run(self):
        self.start_simulation()
        self.root.mainloop()

if __name__ == "__main__":
    simulator = AltTabSimulator()
    simulator.run()

import tkinter as tk
import threading
import pyautogui
import time
import ctypes
import sys

class AltTabSimulator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simulador Alteracao Janelas")

        self.running = False

        self.label = tk.Label(self.root, text="Parar a Alteracao?")
        self.label.pack(pady=10)

        self.button = tk.Button(self.root, text="Parar", command=self.stop_simulation)
        self.button.pack()

        self.thread = None

        # Variáveis para monitorar o movimento do mouse e teclas
        self.mouse_moved = False
        self.keys_pressed = False

        # Configuração do hook de mouse e teclado
        self.user32 = ctypes.windll.user32
        self.mouse_hook = None
        self.keyboard_hook = None

    def mouse_hook_proc(self, nCode, wParam, lParam):
        if nCode >= 0:
            self.mouse_moved = True
        return self.user32.CallNextHookEx(None, nCode, wParam, lParam)

    def keyboard_hook_proc(self, nCode, wParam, lParam):
        if nCode >= 0:
            self.keys_pressed = True
        return self.user32.CallNextHookEx(None, nCode, wParam, lParam)

    def simulate_alt_tab(self):
        self.mouse_hook = self.user32.SetWindowsHookExW(0x14, self.mouse_hook_proc, ctypes.windll.kernel32.GetModuleHandleW(None), 0)
        self.keyboard_hook = self.user32.SetWindowsHookExW(0x2, self.keyboard_hook_proc, ctypes.windll.kernel32.GetModuleHandleW(None), 0)

        while self.running:
            if self.mouse_moved or self.keys_pressed:
                self.stop_simulation()
                break

            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=1)
            pyautogui.keyUp('alt')
            time.sleep(25)

            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=2)
            pyautogui.keyUp('alt')
            time.sleep(25)

            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=3)
            pyautogui.keyUp('alt')
            time.sleep(25)

            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=4)
            pyautogui.keyUp('alt')
            time.sleep(25)

            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=5)
            pyautogui.keyUp('alt')
            time.sleep(25)

            pyautogui.keyDown('alt')
            pyautogui.press('tab', presses=6)
            pyautogui.keyUp('alt')
            time.sleep(25)

        if self.mouse_hook:
            self.user32.UnhookWindowsHookEx(self.mouse_hook)
        if self.keyboard_hook:
            self.user32.UnhookWindowsHookEx(self.keyboard_hook)

    def start_simulation(self):
        self.running = True
        self.thread = threading.Thread(target=self.simulate_alt_tab)
        self.thread.start()

    def stop_simulation(self):
        self.running = False
        if self.thread:
            self.thread.join()
        self.root.destroy()

    def run(self):
        self.start_simulation()
        self.root.mainloop()

if __name__ == "__main__":
    simulator = AltTabSimulator()
    simulator.run()

    