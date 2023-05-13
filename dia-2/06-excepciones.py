try : 
    print(5/1)
except ZeroDivisionError:
    print("error al hacer la division")
except TypeError:
    print("Error por cuestiones de tipos de datos")
except Exception:
    print("ya no se cual es el error!")
else:
    #en el caso que nunca ingrese a ningun except
    print("todo bien")
finally:
    #ingresa ya sea si estuvo bien o si entro a algun except
    print("Yo ingreso SI o SI")
    
print("yo soy el final del archivo")