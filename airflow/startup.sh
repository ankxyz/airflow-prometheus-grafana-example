#!/usr/bin/env bash

airflow initdb

airflow scheduler & airflow webserver

# sleep 365d