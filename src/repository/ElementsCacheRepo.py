from src.interfaces.Crud import SimpleCRUD
from src import cache, Cache
from src.models.ElementEntity import Element

class ElemCacheRepo(SimpleCRUD):
    _NAME = "element"

    def __init__(self):
        self.handler_cache:Cache = cache

    #retorna valores booleanos para confirmar su ejecución
    def create_object(self, object: Element):
        return self.handler_cache.set(f"{self._NAME}:{object.id}", object)
    
    def get_object(self, id_object: int):
        return self.handler_cache.get(f"{self._NAME}:{id_object}")
    
    def get_all_objects(self):
        list_element = self.handler_cache.get(f"{self._NAME}:index") or [] 
        elements = []
        for key in list_element:
            element = self.handler_cache.get(f"{self._NAME}:{key}")
            if element is not None:
                elements.append(element)
        return elements

    def update_object(self, id_object: int):
        pass
    
    def delete_object(self, id_object: int):
        return self.handler_cache.delete(f"{self._NAME}:{id_object}")