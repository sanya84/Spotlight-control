import os
import time

import customtkinter
from PIL import Image

from serial_port import PCArduinoRS485


class WindowsApplication(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("650x480")
        self.title("Управление светодиодным прожектором")
        self.resizable(0, 0)  # Don't allow resizing in the x or y direction

        # Настройка сетки (grid)
        # Устанавливаем вес для колонок и строк, чтобы виджеты растягивались
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=4)  # Строка для изображения, делаем ее больше
        self.grid_rowconfigure(1, weight=1)  # Строка для кнопок

        # Логотип программы
        icon = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Images\\icon.ico")
        self.iconbitmap(icon)

        # Создание CTkLabel с изображением
        self.image_label = customtkinter.CTkLabel(
            self,
            text="",
            image=self.load_image("led-lamp-off.png")  # Передаем созданный CTkImage
        )

        # Размещение в сетке: строка 0, колонка 0. sticky="nsew" растянет по всей ячейке.
        self.image_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # 4. Создание Frame для кнопок, чтобы держать их вместе в одной строке
        self.button_frame = customtkinter.CTkFrame(self)
        self.button_frame.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew")

        # Настройка сетки внутри Frame для кнопок
        self.button_frame.grid_columnconfigure((0, 1), weight=1)

        # Создание кнопок
        self.button_on = customtkinter.CTkButton(
            self.button_frame,
            text="включить",
            command=self.button_handler_turn_on_device
        )
        # Размещение в сетке: строка 0 (внутри Frame), колонка 0.
        self.button_on.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="ew")

        self.button_off = customtkinter.CTkButton(
            self.button_frame,
            text="выключить",
            command=self.button_handler_turn_off_device
        )

        # Размещение в сетке: строка 0 (внутри Frame), колонка 1.
        self.button_off.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="ew")

        # Открываем COM-порт для Arduino
        # serial = serial.Serial(serial_port_arduino, baud_rate, timeout=timeout_)
        # Открываем COM-порт для RS485-USB
        self.serial_port = PCArduinoRS485('COM8')

        self.after(0, self.state_handler)

        # 1. Назначаем функцию-обработчик для протокола WM_DELETE_WINDOW
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    # turn on the device button handler
    def button_handler_turn_on_device(self):
        self.button_on.configure(state="disabled")
        self.serial_port.send_data("1")
        time.sleep(0.05)

    # turn off the device button handler
    def button_handler_turn_off_device(self):
        self.button_off.configure(state="disabled")
        self.serial_port.send_data("0")
        time.sleep(0.5)

    def state_handler(self):
        state = self.serial_port.read_data()
        if state is not None:
            print(f"Статус светодиодного прожектора: {state}")
            if state == "1":
                self.button_on.configure(state="disabled")
                self.button_off.configure(state='normal')
                # Обновляем, используя метод .configure()
                self.image_label.configure(
                    image=self.load_image("led-lamp-on.png"),
                )
            elif state == "0":
                self.button_off.configure(state='disabled')
                self.button_on.configure(state="normal")
                # Обновляем, используя метод .configure()
                self.image_label.configure(
                    image=self.load_image("led-lamp-off.png"),
                )

        self.after(50, self.state_handler)

    def on_closing(self):
        self.serial_port.close()
        self.destroy()

    @classmethod
    def load_image(cls, path):
        try:
            # 2. Загрузка изображения
            # Получаем путь к текущему скрипту для относительных путей,
            # если ваше изображение лежит рядом. Замените "test_image.png" на ваше имя файла.
            # path = os.path.dirname(os.path.realpath(__file__))
            # image_path = os.path.join(path, "test_image.png")

            # Предполагается, что изображение находится в папке 'images' относительно скрипта
            current_directory = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(current_directory, "Images", path)

            # Загрузка изображения с помощью PIL (Pillow)
            image = Image.open(image_path)

            # Создание CTkImage, который используется в CustomTkinter
            # Вы можете установить нужный размер
            spotlight_image = customtkinter.CTkImage(light_image=image,
                                                     dark_image=image,
                                                     size=(400, 380))  # Примерный размер
            return spotlight_image
        except FileNotFoundError:
            # Если изображение не найдено, используем пустой лейбл
            print("Изображение не найдено. Убедитесь, что путь к файлу с изображением существует существует.")
            spotlight_image = None
