from abc import ABC, abstractmethod
from src.models.ElementEntity import Element

#hacer esta wea generica
class SimpleCRUD(ABC):
    @abstractmethod
    def create_object(self, object: Element):
        pass

    @abstractmethod
    def get_object(self, id_object: int):
        pass

    @abstractmethod
    def get_all_objects(self):
        pass

    @abstractmethod
    def update_object(self, id_object: int):
        pass

    @abstractmethod
    def delete_object(self, id_object: int):
        pass