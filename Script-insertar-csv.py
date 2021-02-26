import psycopg2
from sql_queries_urbvan import create_table_queries, drop_table_queries

def create_database():
    #Conectamos a la bd
        conn = psycopg2.connect("host=database-2.c295zanvccq2.us-east-1.rds.amazonaws.com dbname=student user=student password=root2021")
        conn.set_session(autocommit=True)
        cur = conn.cursor()
        
        #Creamos la base de datos con UTF 8 encoding
        cur.execute("DROP DATABASE IF EXISTS urbvan2")
        cur.execute("CREATE DATABASE urbvan WITH ENCODING 'utf8' TEMPLATE template0")
        
        #Cerramos la conexión con la actual base de datos
        conn.close()
        
        #Conectamos con la base de datos de sparkify
        conn = psycopg2.connect("host=database-2.c295zanvccq2.us-east-1.rds.amazonaws.com dbname=urbvan user=student password=root2021")
        cur = conn.cursor()
        
        #Agregamos las llaves foraneas
        cur.execute("ALTER TABLE public.reservation ADD CONSTRAINT reservation_fk FOREIGN KEY (client_id) REFERENCES public.client(client_id);)
        cur.execute("ALTER TABLE public.reservation ADD CONSTRAINT reservation_fk_1 FOREIGN KEY (trip_id) REFERENCES public.trip(trip_id);")
        cur.execute("ALTER TABLE public.trip ADD CONSTRAINT trip_fk FOREIGN KEY (driver_id) REFERENCES public.driver(driver_id);")
        
        return cur, conn
    
def drop_tables(cur,conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()
        
            
def create_tables(cur,conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def procesando_datos(cur,conn,table_name,filepath):
    with open(filepath,'r',encoding='utf8') as f:
        next(f)
        cur.copy_from(f,table_name,sep=',')
        conn.commit()

 


 # En esta funcion procesamos nuestros datos, abrimos nuestro archivo y procedmos a insertar los datos por tabla
 # Esta función para insertar datos se encuentra optimizada para insertar archivos muy muy grandes, hasta 30 millones de records
 # Unicamente es en cada metodo de insertar_datos_nombre_de_la_tabla, se especifica la ruta del archivo   
        
            
    
def crear_base_de_datos():
    cur, conn = create_database()
    drop_tables(cur,conn)
    create_tables(cur,conn)
    conn.close()
    

def insertar_datos_cliente():
    conn = psycopg2.connect("host=database-2.c295zanvccq2.us-east-1.rds.amazonaws.com dbname=urbvan user=student password=root2021")
    cur = conn.cursor()
    procesando_datos(cur,conn,"client", filepath='client_table.csv')
    conn.close()

    
def insertar_datos_driver():
    conn = psycopg2.connect("host=database-2.c295zanvccq2.us-east-1.rds.amazonaws.com dbname=urbvan user=student password=root2021")
    cur = conn.cursor()
    procesando_datos(cur,conn,"driver", filepath='driver_table.csv')
    conn.close()
    
    
def insertar_datos_trip():
    conn = psycopg2.connect("host=database-2.c295zanvccq2.us-east-1.rds.amazonaws.com dbname=urbvan user=student password=root2021")
    cur = conn.cursor()
    procesando_datos(cur,conn,"trip", filepath='trip_table.csv')
    conn.close()

    
def insertar_datos_reservation():
    conn = psycopg2.connect("host=database-2.c295zanvccq2.us-east-1.rds.amazonaws.com dbname=urbvan user=student password=root2021")
    cur = conn.cursor()
    procesando_datos(cur,conn,"reservation", filepath='reservation_table.csv')
    conn.close()

                    
                    
#Método para crear la base de datos
crear_base_de_datos() 
                    
                    
#Método para insertar datos en la tabla cliente
insertar_datos_cliente()  
                    
#Método para insertar datos en la tabla driver
insertar_datos_driver()  
                    
#Método para insertar datos en la tabla trip
insertar_datos_trip()     
                    
                    
#Método para insertar datos en la table reservation
insertar_datos_reservation()                    
                    

        
