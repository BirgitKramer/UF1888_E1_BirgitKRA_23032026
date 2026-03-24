# Analisis de modelos de datos
#### Como funciona Odoo
1. Tablas > donde se guarda la informacion
2. Campos > datos dentro de las tablas
3. Relaciones > como se conectan enre si
Ej. Clientes, Productos, Ventas

#### Entrar en PostgreSQL
```
sudo -u postgres psql
```
![alt text](imagen01.png)
ver base de datos 
```
\l
```
![alt text](imagen02.png)
```
\c odoo19
```
![alt text](imagen03.png)

```
\dt
```
![alt text](imagen04.png)

![alt text](imagen05.png)

----------
| Tipo de dato | Tabla | Observaciones|
| -----------
| Clientes | res_partner | guarda clientes, contactos y empresas |
| Productos | product_template | guarda informaciones general de los productos y empresas |
| Ventas |sale_ordner | guarda los pedidos |
----------

#### analizar estructura de tablas
- Toca ver que campos tiene cada tabla y localizador las claves.
```
\d res-partner
\d sale-ordner
\d product_template
```


