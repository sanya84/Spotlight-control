import serial
import time


class PCArduinoRS485(serial.Serial):
    def __init__(self, port=None, baud_rate=9600, timeout=3):
        super(PCArduinoRS485, self).__init__(port=port, baudrate=baud_rate, timeout=timeout)

    def send_data(self, data: str):
        # Отправляем данные
        # Пример: "Hello Arduino-RS485!\n"
        self.write(data.encode('utf-8'))

    def read_data(self):
        # Проверяем наличие данных
        if self.in_waiting > 0:
            try:
                # Читаем ответ
                response = self.readline().decode('utf-8').strip()
            except UnicodeDecodeError as exception:
                response = None
            return response
            # response = serial_rs485.readline()
            # print(f"Получено: '{response}'")

    def close_serial_port(self):
        # Закрываем порт
        if self.is_open:
            self.close()
            while self.is_open:
                # print("Закрытие порта...")
                time.sleep(0.1)
            print("Порт RS485-USB закрыт.")


# import serial
# import time
#
# # Укажите COM-порт, к которому подключен ваш Arduino
# # Для Windows это может быть 'COM3', 'COM4' и т.д.
# # Для Linux - '/dev/ttyACM0'
# # Укажите COM-порт, к которому подключен ваш RS485-USB
# #
# # serial_port_arduino = 'COM3'
# # serial_port_rs485 = 'COM4'
#
# # Настройки для COM-порта
# baud_rate = 9600
# timeout = 3
#
# try:
#     # Открываем COM-порт для Arduino
#     # ser_arduino = serial.Serial(serial_port_arduino, baud_rate, timeout=timeout_)
#     # Открываем COM-порт для RS485-USB
#     serial_rs485 = serial.Serial('COM8', baud_rate, timeout=timeout)
#     print(f"Подключено к RS485-USB на {serial_rs485.port}")
#     # print(f"Подключено к Arduino на {ser_arduino.port}")
#     # Отправляем данные
#     serial_rs485.write("Hello Arduino-RS485!\n".encode('utf-8'))
#
#     message = "Hello Arduino-RS485!\n"
#     serial_rs485.write(message.encode('utf-8'))
#     message = message.strip('\n')
#     print(f"Отправлено: '{message}'")
#     time.sleep(1.5)  # Даём время на обработку
#
#     # Читаем ответ
#     response = serial_rs485.readline().decode('utf-8').strip()
#     # response = serial_rs485.readline()
#     print(f"Получено: '{response}'")
#
# except serial.SerialException as e:
#     print(f"Ошибка: {e}")
#
# finally:
#     # Закрываем порт
#     if 'serial_rs485' in locals() and serial_rs485.is_open:
#         serial_rs485.close()
#         while serial_rs485.is_open:
#             print("Закрытие порта...")
#             time.sleep(0.1)
#         # print(serial_rs485.is_open)
#         print("Порт RS485-USB закрыт.")
#     # if 'ser_arduino' in locals() and serial_rs485.is_open:
#     #     serial_rs485.close()
#     #     print("Порт Arduino закрыт.")
#
# # import serial
# # import time
# #
# # try:
# #     ser_rs485 = serial.Serial('COM8', 9600, timeout=1)
# #     print(f"Подключено к RS485-USB на {ser_rs485.port}")
# #     message = "Hello Arduino!"
# #     ser_rs485.write(message.encode('utf-8'))
# #     print(f"Отправлено: '{message}'")
# #     time.sleep(3)  # Задержка для получения полного ответа
# #
# #     response = ser_rs485.readline()  # Чтение байтов без декодирования
# #     print(f"Получено: '{response}'")
# #
# # except serial.SerialException as e:
# #     print(f"Ошибка: {e}")
# #
# # finally:
# #     if 'ser_rs485' in locals() and ser_rs485.is_open:
# #         ser_rs485.close()
# #         print("Порт RS485-USB закрыт.")
