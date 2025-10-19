import customtkinter

from windows_application import WindowsApplication


# Устанавливаем режим внешнего вида
customtkinter.set_appearance_mode("")  # "System", "Dark", "Light"
customtkinter.set_appearance_mode("Dark")  # "System", "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # "blue", "dark-blue", "green"


def main():
    application = WindowsApplication()
    application.mainloop()


if __name__ == '__main__':
    main()
