# controller/profesores_controller.py
from flask import Blueprint, request, jsonify
from service.profesores_service import ProfesoresService

bp = Blueprint("profesores", __name__)
service = ProfesoresService()

@bp.route("/api/profesores", methods=["GET"])
def listar():
    return jsonify(service.listar())

@bp.route("/api/profesores/<int:id>", methods=["GET"])
def obtener(id):
    resp = service.obtener(id)
    if isinstance(resp, tuple): return jsonify(resp[0]), resp[1]
    return jsonify(resp)

@bp.route("/api/profesores", methods=["POST"])
def crear():
    data = request.json or {}
    resp = service.crear(data)
    if isinstance(resp, tuple): return jsonify(resp[0]), resp[1]
    return jsonify(resp)

@bp.route("/api/profesores/<int:id>", methods=["PUT"])
def actualizar(id):
    data = request.json or {}
    resp = service.actualizar(id, data)
    if isinstance(resp, tuple): return jsonify(resp[0]), resp[1]
    return jsonify(resp)

@bp.route("/api/profesores/<int:id>", methods=["DELETE"])
def eliminar(id):
    resp = service.eliminar(id)
    if isinstance(resp, tuple): return jsonify(resp[0]), resp[1]
    return jsonify(resp)
