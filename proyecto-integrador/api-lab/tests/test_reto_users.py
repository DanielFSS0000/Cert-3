"""Reto de la Sesion 04: CRUD de usuarios con Python y Pytest."""

import time

import pytest

from conftest import load_json


CONTRATO_USER = {
    "id": int,
    "name": str,
    "username": str,
    "email": str,
}

CASOS_USER = load_json("users_payloads.json")


def cumple_contrato(recurso: dict, contrato: dict) -> bool:
    """Comprueba que cada campo exista y tenga el tipo esperado."""
    return all(
        campo in recurso and isinstance(recurso[campo], tipo)
        for campo, tipo in contrato.items()
    )


def test_listar_users(api):
    respuesta = api.get("/users")

    assert respuesta.status_code == 200
    assert len(respuesta.json()) == 10


def test_detalle_cumple_contrato(api):
    respuesta = api.get("/users/1")

    assert respuesta.status_code == 200
    assert cumple_contrato(respuesta.json(), CONTRATO_USER)


@pytest.mark.parametrize(
    "caso",
    CASOS_USER,
    ids=[caso["caso"] for caso in CASOS_USER],
)
def test_crear_user(api, caso):
    payload = caso["payload"].copy()
    payload["name"] = f'{payload["name"]} {time.time_ns()}'

    respuesta = api.post("/users", json=payload)

    assert respuesta.status_code == 201
    creado = respuesta.json()
    assert isinstance(creado["id"], int)
    assert creado["name"] == payload["name"]


def test_actualizar_user(api):
    payload = {
        "id": 1,
        "name": "Leanne Graham Actualizada",
        "username": "Bret",
        "email": "leanne.actualizada@cert3.test",
    }

    respuesta = api.put("/users/1", json=payload)

    assert respuesta.status_code == 200
    assert respuesta.json()["name"] == payload["name"]


def test_eliminar_user(api):
    respuesta = api.delete("/users/1")

    assert respuesta.status_code == 200
    assert respuesta.json() == {}
