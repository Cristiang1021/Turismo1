# app/models.py

from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    correo = db.Column(db.String(255), unique=True)
    contraseña_hash = db.Column(db.String(256))
    es_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def password(self):
        return self.contraseña_hash

    @password.setter
    def password(self, contraseña):
        self.contraseña_hash = generate_password_hash(contraseña)

    def check_password(self, contraseña):
        return check_password_hash(self.contraseña_hash, contraseña)


class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    descripcion = db.Column(db.String(100), unique=False, nullable=False)
    image_url = db.Column(db.String(255))
    actividades = db.relationship('ActividadTuristica', backref='categoria', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    # ... otros campos según necesidad

class ActividadTuristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion_equipamiento = db.Column(db.Text, nullable=False)
    nivel_dificultad = db.Column(db.String(50), nullable=False)
    nivel_fisico_requerido = db.Column(db.String(50), nullable=False)
    tiempo_promedio_duracion = db.Column(db.String(100), nullable=False)
    sitio = db.Column(db.String(100), nullable=False)
    cota_maxima = db.Column(db.Integer)
    cota_minima = db.Column(db.Integer)
    desnivel_subida = db.Column(db.Integer)
    desnivel_bajada = db.Column(db.Integer)
    lugar_partida = db.Column(db.String(100), nullable=False)
    lugar_llegada = db.Column(db.String(100), nullable=False)
    epoca_recomendada = db.Column(db.String(100), nullable=False)
    tipo_superficie = db.Column(db.String(100), nullable=False)
    temperatura_minima = db.Column(db.Integer)
    temperatura_maxima = db.Column(db.Integer)
    precipitacion_media_anual = db.Column(db.Integer)
    requerimiento_guia = db.Column(db.Text, nullable=False)
    localizacion_geografica = db.Column(db.String(100), nullable=False)
    acceso = db.Column(db.Text, nullable=False)
    precio_referencial = db.Column(db.String(100), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    imagenes = db.relationship('ImagenActividad', backref='actividad', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    # ... otros campos según necesidad

class ImagenActividad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    actividad_id = db.Column(db.Integer, db.ForeignKey('actividad_turistica.id'))
    es_portada = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    # ... otros campos como descripción, si es portada, etc.



class PreferenciaUsuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    nivel_dificultad = db.Column(db.String(50), nullable=False)
    tipo_superficie = db.Column(db.String(50), nullable=False)
    temperatura_minima = db.Column(db.Integer, nullable=False)
    temperatura_maxima = db.Column(db.Integer, nullable=False)
    usuario = db.relationship('Usuario', backref='preferencias')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class ActividadVista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    actividad_id = db.Column(db.Integer, db.ForeignKey('actividad_turistica.id'), nullable=False)
    vistas = db.Column(db.Integer, default=0, nullable=False)
    fecha_vista = db.Column(db.DateTime, default=datetime.now, nullable=False)
    usuario = db.relationship('Usuario', backref='vistas_actividades')
    actividad = db.relationship('ActividadTuristica', backref='vistas_por_usuarios')
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)



