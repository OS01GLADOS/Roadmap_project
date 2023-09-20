--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3 (Debian 13.3-1.pgdg100+1)
-- Dumped by pg_dump version 13.3 (Debian 13.3-1.pgdg100+1)

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

--
-- Name: custom_scheme; Type: SCHEMA; Schema: -; Owner: root
--

CREATE SCHEMA custom_scheme;


ALTER SCHEMA custom_scheme OWNER TO root;

--
-- Name: SCHEMA custom_scheme; Type: ACL; Schema: -; Owner: root
--

GRANT ALL ON SCHEMA custom_scheme TO djangosite;


--
-- PostgreSQL database dump complete
--

