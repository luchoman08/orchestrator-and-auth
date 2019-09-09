from gestionAplicaciones.models import AppPermission

def init_permissions():
    p1 = AppPermission(name="group_assign")
    p2 = AppPermission(name="pair_assign")
    p3 = AppPermission(name="attribute_assign")
    p4 = AppPermission(name="unique_punctuation_assign")

    try:
        p1.save()
        p2.save()
        p3.save()
        p4.save()
    except:
        print("Error en la creación de permisos")
        return False
    
    return True