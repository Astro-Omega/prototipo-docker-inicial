from marshmallow import fields, Schema

class ElementSchema(Schema):
    # id = fields.Integer(dump_only= True)
    id = fields.Integer(required= True)
    name = fields.Str(required= True)
    other_thing = fields.Str(required= True)

element_schema = ElementSchema()