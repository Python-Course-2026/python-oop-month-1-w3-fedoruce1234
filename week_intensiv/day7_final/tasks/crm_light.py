class Client:
    def __init__(self, client_id, name, email):
        self.client_id = client_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Client(id={self.client_id}, name='{self.name}')"

class CRM:
    """
    ЗАДАЧА: Управление клиентами.
    1. add_client(client): добавляет объект Client в список self.clients.
    2. get_client(client_id): возвращает объект клиента по ID или None.
    3. delete_client(client_id): удаляет клиента из списка.
    4. update_client(client_id, **kwargs): находит клиента и обновляет его
       атрибуты (name, email), переданные в kwargs.
    """
    def __init__(self):
        self.clients = []

    def add_client(self, client: Client):
        self.clients.append(client)

    def get_client(self, client_id):
        # ТВОЙ КОД ЗДЕСЬ
        # Проходим по всем клиентам
        for client in self.clients:
            # Если нашли клиента с нужным ID
            if client.client_id == client_id:
                return client
        # Если не нашли, возвращаем None
        return None

    def delete_client(self, client_id):
        # ТВОЙ КОД ЗДЕСЬ
        # Проходим по всем клиентам
        for client in self.clients:
            # Если нашли клиента с нужным ID
            if client.client_id == client_id:
                # Удаляем его из списка
                self.clients.remove(client)
                return

    def update_client(self, client_id, **kwargs):
        """
        Пример: update_client(1, name="New Name") должен изменить только имя.
        Используйте setattr(obj, key, value) для динамического обновления.
        """
        # ТВОЙ КОД ЗДЕСЬ
        # Найдем  клиента
        client = self.get_client(client_id)

        # Если клиент не найден, просто выходим
        if client is None:
            return

        # Обновляем атрибуты
        for key, value in kwargs.items():
            setattr(client, key, value)