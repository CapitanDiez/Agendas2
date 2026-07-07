import web
import sqlite3

render = web.template.render('views', base='layout')

class VerContacto:

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
            print(f"ERROR verContacto 100: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR 101: {error.args}")
            return {}
        finally:
            conn.close()

    def GET(self, id_contacto):
        print(f"ID_CONTACTO: {id_contacto}")
        contacto = self.buscarContacto(id_contacto)
        print(contacto)
        return render.ver_contacto(contacto)