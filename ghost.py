##### `ghost.py`
##### Ghostwriter
##### Open-Source, hosted on https://github.com/DrBenjamin/Ghostwriter
##### Please reach out to ben@benbox.org for any questions
#### Loading needed Python libraries
import streamlit as st
import pandas as pd
import mysql.connector
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy.sql import text
import openai
import deepl

st.header("Ghostwriter")
