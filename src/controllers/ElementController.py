from flask import Blueprint, request, jsonify

from src.models.ElementEntity import Element
from src.schemas.ElementSchema import element_schema
from src.services.ElementService import ElementServices

element = Blueprint('space_element', __name__)
element_services = ElementServices()

#trae a un solo elemento por medio de su id
@element.route('/<int:id_element>', methods=['GET'])
def get_one_elements(id_element):
    entity_element = element_services.get_element(id_element);
    if entity_element is None:
        return jsonify({'message': f"no se ha encontrado el elemento con id: {id_element}"}), 404
    return jsonify(element_schema.dump(entity_element)), 200

#crea un elemento
@element.route('/create', methods=['POST'])
def create_element():
    data = element_schema.load(request.get_json())
    # controlar errores de intercepción
    element_entity = Element(
        data['id'],
        data['name'],
        data['other_thing']
    )
    event_provess = element_services.create_element(element_entity)
    if event_provess is False or None:
        return jsonify({'message': "error al momento de registrar la cuenta", f'status': "{event_provess}"}), 400

    return jsonify(element_schema.dump(element_entity)), 200

@element.route('/all', methods=['GET'])
def get_all_elemenst():
    list_element = element_services.collage_all_elements()
    lenght_list = len(list_element)
    print(lenght_list)
    if lenght_list < 1:
        return jsonify({"message": "no se han registrado mas elementos"}), 200
    return jsonify({"message": f"se han registrado {lenght_list} elementos", "data": list_element}), 200

#trae solo los datos escenciales de los elementos
@element.route('/name/<name_element>', methods=['GET'])
def get_simple_elements(name_element):
    pass

#elimina los elementos en la BD por medio de la id
@element.route('/<int:id_element>', methods=['DELETE'])
def delete_elements(id_element):
    pass
