# DROP TABLES

client_table_drop = "DROP TABLE IF EXISTS client"
reservation_table_drop = "DROP TABLE IF EXISTS reservation"
driver_table_drop = "DROP TABLE IF EXISTS driver"
trip_table_drop = "DROP TABLE IF EXISTS trip"


# CREATE TABLES

client_table_create = ("""
CREATE TABLE IF NOT EXISTS client (
    client_id integer NOT NULL,
	created_at timestamptz NULL,
	first_name varchar(50) NULL,
	last_name varchar(50) NULL,
	birthdate date NULL,
	gender varchar(6) NULL,
	CONSTRAINT client_id PRIMARY KEY (client_id)
);
""")

reservation_table_create = ("""
CREATE TABLE IF NOT EXISTS reservation (
    reservation_id integer NOT NULL,
	trip_id integer NULL,
	client_id integer NULL,
	created_at timestamptz NULL,
	seats integer NULL,
	total_price integer NULL,
	CONSTRAINT reservation_id PRIMARY KEY (reservation_id)
);
""")

driver_table_create = ("""
CREATE TABLE IF NOT EXISTS driver (
    driver_id integer NOT NULL,
	created_at timestamptz NULL,
	first_name varchar(50) NULL,
	last_name varchar(50) NULL,
	birthdate date NULL,
	gender varchar(6) NULL,
	CONSTRAINT driver_id PRIMARY KEY (driver_id)
);
""")

trip_table_create = ("""
CREATE TABLE IF NOT EXISTS trip (
    trip_id integer NOT NULL ,
	driver_id integer NULL,
	on_sale_at timestamptz NULL,
	departure_at timestamptz NULL,
	arrival_at timestamptz NULL,
	vehicle_capacity integer NULL,
	seat_price _float4 NULL,
	route_name text NULL,
	line_name text NULL,
	route_type text NULL,
	CONSTRAINT trip_id PRIMARY KEY (trip_id)
);
""")


# QUERY LISTS

create_table_queries = [client_table_create, reservation_table_create, driver_table_create, trip_table_create]
drop_table_queries = [client_table_drop, reservation_table_drop, driver_table_drop, trip_table_drop]
