--
-- PostgreSQL database dump
--

-- Dumped from database version 15.5
-- Dumped by pg_dump version 15.5

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
-- Name: user; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public."user" (
    user_id bigint NOT NULL,
    registration_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    admine_status boolean DEFAULT false NOT NULL,
    subscription boolean DEFAULT false NOT NULL,
    status_registr_web boolean DEFAULT false NOT NULL,
    web_account_id integer,
    user_language character varying(255)
);


ALTER TABLE public."user" OWNER TO admin;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public."user" (user_id, registration_date, admine_status, subscription, status_registr_web, web_account_id, user_language) FROM stdin;
6831193510	2024-01-31 17:12:16.092689	f	f	f	\N	ru
6988704175	2024-01-31 18:30:14.454546	f	f	f	\N	ru
\.


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_id);


--
-- PostgreSQL database dump complete
--

