# controller/matriculas_controller.py
from flask import Blueprint, request, jsonify
from service.matriculas_service import MatriculasService

bp = Blueprint("matriculas", __name__)
service = MatriculasService()

@bp.route("/api/matriculas", methods=["GET"])
def listar():
    return jsonify(service.listar())

@bp.route("/api/matriculas/<int:id>", methods=["GET"])
def obtener(id):
    resp = service.obtener(id)
    if isinstance(resp, tuple): return jsonify(resp[0]), resp[1]
    return jsonify(resp)

@bp.route("/api/matriculas", methods=["POST"])
def crear():
    data = request.json or {}
    resp = service.crear(data)
    if isinstance(resp, tuple): return jsonify(resp[0]), resp[1]
    return jsonify(resp)

@bp.route("/api/matriculas/<int:id>", methods=["PUT"])
def actualizar(id):
    data = request.json or {}
    resp = service.actualizar(id, data)
    if isinstance(resp, tuple): return jsonify(resp[0]), resp[1]
    return jsonify(resp)

@bp.route("/api/matriculas/<int:id>", methods=["DELETE"])
def eliminar(id):
    resp = service.eliminar(id)
    if isinstance(resp, tuple): return jsonify(resp[0]), resp[1]
    return jsonify(resp)
