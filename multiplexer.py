class multiplexer:
    def __init__(self):
        # Список активных неисправностей
        self.errors = set()
        self.log("[INIT] Мультиплексор создан")
    
    def log(self, message): 
        # Логирование
        print(message)

    def add_error(self, error):
        # Добавить неисправность.
        self.errors.add(error)
        self.log(f"[ERROR] Добавлена неисправность: {error}")

    def remove_error(self, error):
        # Удалить неисправность.
        self.errors.discard(error)
        self.log(f"[ERROR] Удалена неисправность: {error}")

    def clear_errors(self):
        # Удалить все неисправности.
        self.errors.clear()
        self.log("[ERROR] Все неисправности удалены")

    def process(self, D, A3, A2, A1, A0):
        # Работа мультиплексора

        # D - список из 10 
        # D0-D9 - информационных входов  
        # A3-A0 - адресные входы
        
        if len(D) != 10:
            # Проверка количества входов
            raise ValueError("Должно быть ровно 10 входов D0-D9")

        self.log("[MUX] Начало обработки") 
        self.log(f"[INPUT] D = {D}") 
        self.log(f"[INPUT] A = {A3}{A2}{A1}{A0}")

        # Неисправности адресных входов

        if "A0_INVERT" in self.errors: 
            A0 = 1 - A0 
            self.log("[ERROR] A0 инвертирован")

        if "A1_INVERT" in self.errors:
            A1 = 1 - A1
            self.log("[ERROR] A1 инвертирован")

        if "A2_INVERT" in self.errors: 
            A2 = 1 - A2 
            self.log("[ERROR] A2 инвертирован")

        if "A3_INVERT" in self.errors: 
            A3 = 1 - A3 
            self.log("[ERROR] A3 инвертирован")

        # Формирование адреса
        address = A3 * 8 + A2 * 4 + A1 * 2 + A0
        self.log( f"[MUX] Адрес: " f"{A3}*8 + {A2}*4 + {A1}*2 + {A0} = {address}" )

        # Неисправности информационных входов

        # делаем копию
        D = D.copy()

        if "D2_D3_SWAP" in self.errors:
            D[2], D[3] = D[3], D[2]
            self.log("[ERROR] D2 и D3 поменяны местами")

        if "D5_STUCK_AT_0" in self.errors:
            D[5] = 0
            self.log("[ERROR] D5 зафиксирован в 0")

        if "D5_STUCK_AT_1" in self.errors: 
            D[5] = 1 
            self.log("[ERROR] D5 зафиксирован в 1")

        # Выбор информационного входа

        if address < 10:
            out = D[address]
            self.log(f"[MUX] Выбран вход D{address}")
            self.log(f"[MUX] Значение D{address} = {out}")
        else:
            # Адреса 10-15 не используются
            out = 0

            self.log("[MUX] Неиспользуемый адрес")
            self.log("[MUX] OUT = 0")

        # Неисправности выхода

        if "OUT_STUCK_AT_0" in self.errors:
            out = 0
            self.log("[ERROR] OUT зафиксирован в 0")

        if "OUT_STUCK_AT_1" in self.errors:
            out = 1
            self.log("[ERROR] OUT зафиксирован в 1")

        if "OUT_INVERT" in self.errors:
            out = 1 - out
            self.log("[ERROR] OUT инвертирован")

        if "OUT_INVERT" in self.errors:
            out = 1 - out

        # Результат

        self.log(f"[RESULT] OUT = {out}")

        return out