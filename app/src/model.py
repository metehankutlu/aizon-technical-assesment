from marshmallow import Schema, fields, post_load

class InputSchema(Schema):
    Material_A_Charged_Amount = fields.Float(required=True)
    Material_B_Charged_Amount = fields.Float(required=True)
    Reactor_Volume = fields.Float(required=True)
    Material_A_Final_Concentration_Previous_Batch = fields.Float(required=True)

    @post_load
    def make_input(self, data, *args, **kwargs):
        return {k: [[v]] for k, v in data.items()}