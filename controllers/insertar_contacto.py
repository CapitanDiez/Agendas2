import web
import sqlite3

render = web.template.render('views', base='layout')

class InsertarContacto:
    def insertarContacto(self, contacto: dict):
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            query = """
                INSERT INTO contactos (nombre, primer_apellido, segundo_apellido, email, telefono)
                VALUES (?, ?, ?, ?, ?);
            """
            datos = (
                contacto['nombre'],
                contacto['primer_apellido'],
                contacto['segundo_apellido'],
                contacto['email'],
                contacto['telefono']
            )
            cursor.execute(query, datos)
            conn.commit()
            return True
        except sqlite3.Error as error:
            print(f"ERROR insertarContacto 200: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR 201: {error.args}")
            return False
        finally:
            conn.close()

    def GET(self):
        # Carga el HTML limpio de insertar_contacto
        return render.insertar_contacto()

    def POST(self):
        formulario = web.input()
        contacto = {
            "nombre": formulario['nombre'],
            "primer_apellido": formulario['primer_apellido'],
            "segundo_apellido": formulario['segundo_apellido'],
            "email": formulario['email'],
            "telefono": formulario['telefono']
        }
        resultado = self.insertarContacto(contacto)
        # Regresa True en la pantalla si se guardó con éxito
        return str(resultado)