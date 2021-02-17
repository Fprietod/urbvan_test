CREATE DATABASE postgres;
CREATE SCHEMA public;

CREATE TABLE public.client (
	client_id integer NOT NULL,
	created_at timestamptz NULL,
	first_name varchar(50) NULL,
	last_name varchar(50) NULL,
	birthdate date NULL,
	gender varchar(6) NULL,
	CONSTRAINT client_id PRIMARY KEY (client_id)
);

CREATE TABLE public.reservation (
	reservation_id integer NOT NULL,
	trip_id integer NULL,
	client_id integer NULL,
	created_at timestamptz NULL,
	seats integer NULL,
	total_price integer NULL,
	CONSTRAINT reservation_id PRIMARY KEY (reservation_id),
	CONSTRAINT reservation_fk FOREIGN KEY (client_id) REFERENCES client(client_id),
	CONSTRAINT trip_id FOREIGN KEY (trip_id) REFERENCES trip(trip_id)
);
CREATE TABLE public.driver (
	driver_id integer NOT NULL,
	created_at timestamptz NULL,
	first_name varchar(50) NULL,
	last_name varchar(50) NULL,
	birthdate date NULL,
	gender varchar(6) NULL,
	CONSTRAINT driver_id PRIMARY KEY (driver_id)
);
CREATE TABLE public.trip (
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
	CONSTRAINT trip_id PRIMARY KEY (trip_id),
	CONSTRAINT driver_id FOREIGN KEY (driver_id) REFERENCES public.driver(driver_id)
);


-- Comando para modificar una tabla y en este caso agregar una llave foranea
-- Este comando lo usuamos después que creamos nuestras tablas con su respectiva
-- llave primaria para después hacer la relación
ALTER TABLE public.trip ADD CONSTRAINT trip_fk FOREIGN KEY (driver_id) REFERENCES public.driver(driver_id);
ALTER TABLE public.reservation ADD CONSTRAINT trip_id FOREIGN KEY (trip_id) REFERENCES public.trip(trip_id);