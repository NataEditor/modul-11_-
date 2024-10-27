import inspect




def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    dop=inspect.ismodule(obj) 
    dop2=inspect.isclass(obj)

    info = {'Тип объекта': obj_type, 'Атрибуты объекта': attributes, 'Методы объекта': methods, 'Модуль, к которому объект принадлежит': module, 'Является ли объект модулем': dop, 'Является ли объект классом': dop2}
    
    return info


number_info = introspection_info(42)
print(number_info)