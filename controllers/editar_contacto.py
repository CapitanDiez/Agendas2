import web
import sqlite3

render = web.template.render('views', base='layout')

class EditarContacto:

    def buscarContacto(self, id_contacto:int):
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            query = "SELECT * FROM contactos WHERE id_contacto=?"
            cursor.execute(query, (id_contacto,))
            row = cursor.fetchone()
            contacto = {
                'id_contacto': row[0],
                'nombre': row[1],
                'primer_apellido': row[2],
                'segundo_apellido': row[3],
                'email': row[4],
                'telefono': row[5]
            }
            conn.close()
            return contacto
        except sqlite3.Error as error:
            print(f"ERROR editarContacto 100: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR 101: {error.args}")
            return {}
        finally:
            conn.close()

    def actualizarContacto(self, contacto:dict):
        try:
            # Conecta a la base de datos
            conn = sqlite3.connect("sql/agenda.db")
            cursor = conn.cursor()
            # Consulta los registros de la tabla contactos
            query = """
                UPDATE contactos
                SET 
                    nombre = ?,
                    primer_apellido = ?,
                    segundo_apellido = ?,
                    email = ?,
                    telefono = ?
                WHERE id_contacto = ?;
            """
            datos = (
                contacto['nombre'],
                contacto['primer_apellido'],
                contacto['segundo_apellido'],
                contacto['email'],
                contacto['telefono'],
                contacto['id_contacto'],
            )
            cursor.execute(query,datos)
            conn.commit()
            return True
        except sqlite3.Error as error:
            print(f"ERROR verContactos 102: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR verContactos 103: {error.args}")
            return False
        finally:
            conn.close()

    def GET(self, id_contacto):
        contacto = self.buscarContacto(id_contacto)
        return render.editar_contacto(contacto)

    def POST(self, id_contacto):
        formulario=web.input()
        contacto={
            "id_contacto":formulario['id_contacto'],
            "nombre":formulario['nombre'],
            "primer_apellido":formulario['primer_apellido'],
            "segundo_apellido":formulario['segundo_apellido'],
            "email":formulario['email'],
            "telefono":formulario['telefono'],
        }
        resultado = self.actualizarContacto(contacto)
        return resultado

