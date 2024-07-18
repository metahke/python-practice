--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: customers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customers (
    id integer NOT NULL,
    name text NOT NULL,
    surname text NOT NULL,
    gender text NOT NULL,
    date_joined date NOT NULL,
    training_id integer NOT NULL,
    mentor_id integer NOT NULL
);


ALTER TABLE public.customers OWNER TO postgres;

--
-- Name: departments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.departments (
    city character varying(255) NOT NULL
);


ALTER TABLE public.departments OWNER TO postgres;

--
-- Name: invoices; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.invoices (
    id integer NOT NULL,
    customer_id integer NOT NULL
);


ALTER TABLE public.invoices OWNER TO postgres;

--
-- Name: mentors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mentors (
    id integer NOT NULL,
    name text NOT NULL,
    department_city character varying(255) NOT NULL
);


ALTER TABLE public.mentors OWNER TO postgres;

--
-- Name: notes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.notes (
    id integer NOT NULL,
    content text NOT NULL,
    mentor_id integer NOT NULL,
    customer_id integer NOT NULL
);


ALTER TABLE public.notes OWNER TO postgres;

--
-- Name: payments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.payments (
    id integer NOT NULL,
    date date NOT NULL,
    amount integer NOT NULL,
    customer_id integer NOT NULL
);


ALTER TABLE public.payments OWNER TO postgres;

--
-- Name: payroll; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.payroll (
    id integer NOT NULL,
    amount integer NOT NULL,
    mentor_id integer NOT NULL
);


ALTER TABLE public.payroll OWNER TO postgres;

--
-- Name: trainings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.trainings (
    id integer NOT NULL,
    name text NOT NULL,
    price integer NOT NULL,
    duration text NOT NULL
);


ALTER TABLE public.trainings OWNER TO postgres;

--
-- Name: trainingshistory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.trainingshistory (
    id integer NOT NULL,
    date date NOT NULL,
    training_id integer NOT NULL
);


ALTER TABLE public.trainingshistory OWNER TO postgres;

--
-- Name: trainingsmaterials; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.trainingsmaterials (
    id integer NOT NULL,
    content text NOT NULL,
    training_id integer NOT NULL
);


ALTER TABLE public.trainingsmaterials OWNER TO postgres;

--
-- Data for Name: customers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customers (id, name, surname, gender, date_joined, training_id, mentor_id) FROM stdin;
1	Tomasz	Bąk	male	2021-03-12	4	4
2	Ewa	Kowalczyk	female	2021-01-18	3	3
3	Marek	Wojciechowski	male	2023-06-22	2	2
4	Katarzyna	Kaczmarek	female	2024-01-09	1	1
\.


--
-- Data for Name: departments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.departments (city) FROM stdin;
Warszawa
Kraków
Wrocław
Gdańsk
\.


--
-- Data for Name: invoices; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.invoices (id, customer_id) FROM stdin;
1	1
2	2
3	3
4	4
\.


--
-- Data for Name: mentors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mentors (id, name, department_city) FROM stdin;
1	Jan Kowalski	Warszawa
2	Anna Nowak	Kraków
3	Piotr Wiśniewski	Wrocław
4	Magdalena Zielińska	Gdańsk
\.


--
-- Data for Name: notes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.notes (id, content, mentor_id, customer_id) FROM stdin;
1	Notatki do kursu Java	1	1
2	Notatki do kursu Python	2	2
3	Notatki do kursu SQL	3	3
4	Notatki do kursu Web Development	4	4
\.


--
-- Data for Name: payments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.payments (id, date, amount, customer_id) FROM stdin;
1	2024-01-15	1500	1
2	2024-02-20	1200	2
3	2024-03-25	1000	3
4	2024-04-30	1800	4
5	2024-05-27	1100	3
\.


--
-- Data for Name: payroll; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.payroll (id, amount, mentor_id) FROM stdin;
1	3000	1
2	2500	2
3	2000	3
4	3500	4
\.


--
-- Data for Name: trainings; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.trainings (id, name, price, duration) FROM stdin;
1	Kurs Java	1500	30 godzin
2	Kurs Python	1200	25 godzin
3	Kurs SQL	1000	20 godzin
4	Kurs Web Development	1800	40 godzin
\.


--
-- Data for Name: trainingshistory; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.trainingshistory (id, date, training_id) FROM stdin;
1	2021-01-10	1
2	2022-02-15	2
3	2023-03-20	3
4	2024-04-25	4
\.


--
-- Data for Name: trainingsmaterials; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.trainingsmaterials (id, content, training_id) FROM stdin;
1	Materiały do kursu Java	1
2	Materiały do kursu Python	2
3	Materiały do kursu SQL	3
4	Materiały do kursu Web Development	4
\.


--
-- Name: customers customers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (id);


--
-- Name: departments departments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.departments
    ADD CONSTRAINT departments_pkey PRIMARY KEY (city);


--
-- Name: invoices invoices_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.invoices
    ADD CONSTRAINT invoices_pkey PRIMARY KEY (id);


--
-- Name: mentors mentors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mentors
    ADD CONSTRAINT mentors_pkey PRIMARY KEY (id);


--
-- Name: notes notes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notes
    ADD CONSTRAINT notes_pkey PRIMARY KEY (id);


--
-- Name: payments payments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payments
    ADD CONSTRAINT payments_pkey PRIMARY KEY (id);


--
-- Name: payroll payroll_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payroll
    ADD CONSTRAINT payroll_pkey PRIMARY KEY (id);


--
-- Name: trainings trainings_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trainings
    ADD CONSTRAINT trainings_pkey PRIMARY KEY (id);


--
-- Name: trainingshistory trainingshistory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trainingshistory
    ADD CONSTRAINT trainingshistory_pkey PRIMARY KEY (id);


--
-- Name: trainingsmaterials trainingsmaterials_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trainingsmaterials
    ADD CONSTRAINT trainingsmaterials_pkey PRIMARY KEY (id);


--
-- Name: customers customers_mentor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_mentor_id_fkey FOREIGN KEY (mentor_id) REFERENCES public.mentors(id);


--
-- Name: customers customers_training_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_training_id_fkey FOREIGN KEY (training_id) REFERENCES public.trainings(id);


--
-- Name: invoices invoices_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.invoices
    ADD CONSTRAINT invoices_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(id);


--
-- Name: mentors mentors_department_city_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mentors
    ADD CONSTRAINT mentors_department_city_fkey FOREIGN KEY (department_city) REFERENCES public.departments(city);


--
-- Name: notes notes_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notes
    ADD CONSTRAINT notes_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(id);


--
-- Name: notes notes_mentor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notes
    ADD CONSTRAINT notes_mentor_id_fkey FOREIGN KEY (mentor_id) REFERENCES public.mentors(id);


--
-- Name: payments payments_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payments
    ADD CONSTRAINT payments_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(id);


--
-- Name: payroll payroll_mentor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payroll
    ADD CONSTRAINT payroll_mentor_id_fkey FOREIGN KEY (mentor_id) REFERENCES public.mentors(id);


--
-- Name: trainingshistory trainingshistory_training_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trainingshistory
    ADD CONSTRAINT trainingshistory_training_id_fkey FOREIGN KEY (training_id) REFERENCES public.trainings(id);


--
-- Name: trainingsmaterials trainingsmaterials_training_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trainingsmaterials
    ADD CONSTRAINT trainingsmaterials_training_id_fkey FOREIGN KEY (training_id) REFERENCES public.trainings(id);


--
-- PostgreSQL database dump complete
--

