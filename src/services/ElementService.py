from src.repository.ElementsCacheRepo import ElemCacheRepo 

class ElementServices():
    def __init__(self):
        self.repository_caching = ElemCacheRepo()

    def create_element(self, data):
        return self.repository_caching.create_object(data)

    def get_element(self, id_element):
        return self.repository_caching.get_object(id_element)

    def collage_all_elements(self):
        return self.repository_caching.get_all_objects()

    def delete_elemeny(self, id_element):
        try:
            pass
        except NameError:
            pass