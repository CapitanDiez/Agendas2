import web
import sqlite3

render = web.template.render('views', base='layout')

class BorrarContacto:

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
            print(f"ERROR borrarContacto 100: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR 101: {error.args}")
            return {}
        finally:
            conn.close()

    def eliminarContacto(self, id_contacto):
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            query = "DELETE FROM contactos WHERE id_contacto=?"
            cursor.execute(query, (id_contacto,))
            conn.commit()
            return True
            conn.close()
        except sqlite3.Error as error:
            print(f"ERROR borrarContacto 102: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR 103: {error.args}")
            return False
        finally:
            conn.close()

    def GET(self, id_contacto):
        contacto = self.buscarContacto(id_contacto)
        return render.borrar_contacto(contacto)

    def POST(self, id_contacto):
        resultado = self.eliminarContacto(id_contacto)
        return resultado

        