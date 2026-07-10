import web

urls = (
    '/', 'controllers.index.Index',
    '/lista_contactos','controllers.lista_contactos.ListaContactos',
    '/insertar_contacto', 'controllers.insertar_contacto.InsertarContacto',
    '/ver_contacto/(\\d+)', 'controllers.ver_contacto.VerContacto',
    '/editar_contacto/(\\d+)', 'controllers.editar_contacto.EditarContacto',
    '/borrar_contacto/(\\d+)', 'controllers.borrar_contacto.BorrarContacto',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()