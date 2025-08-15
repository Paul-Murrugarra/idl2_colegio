from flask import Flask
from controller.alumnos_controller import bp as alumnos_bp
# Importar después los otros controladores
from controller.profesores_controller import bp as profesores_bp
from controller.cursos_controller import bp as cursos_bp
from controller.matriculas_controller import bp as matriculas_bp

app = Flask(__name__)

# Registrar blueprints
app.register_blueprint(alumnos_bp)
app.register_blueprint(profesores_bp)
app.register_blueprint(cursos_bp)
app.register_blueprint(matriculas_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
