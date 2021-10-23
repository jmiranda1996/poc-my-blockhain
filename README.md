# my-blockhain
Prueba de concepto para crear una blockhain aplicando conceptos básicos

### Como iniciar la aplicacion

1. Instalar las dependecias con 
<code>
pip install -r requirements.txt
</code>

2. Crear un archivo ".env" y dentro de él, colocar
<code>
FLASK_APP=app.py
</code>

2. Correr el comando
<code>
flask run --host=127.0.0.1 --port=6670
</code>

### Uso de la aplicacion

La aplicación expone las siguientes rutas http:

- mine_block (GET)
- get_chain (GET)
- valid (GET)