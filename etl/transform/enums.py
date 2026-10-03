from enum import Enum


class EstadoUsuario(str, Enum):
    ACTIVO = "Activo"
    INACTIVO = "Inactivo"
    SUSPENDIDO = "Suspendido"
    DESCONOCIDO = "Desconocido"


class EstadoProducto(str, Enum):
    DISPONIBLE = "Disponible"
    AGOTADO = "Agotado"
    DESCONTINUADO = "Descontinuado"
    DESCONOCIDO = "Desconocido"


class NivelCliente(str, Enum):
    BRONCE = "Bronce"
    PLATA = "Plata"
    ORO = "Oro"
    PLATINO = "Platino"
    DESCONOCIDO = "Desconocido"


class EstadoPedido(str, Enum):
    PENDIENTE = "Pendiente"
    PAGADO = "Pagado"
    ENVIADO = "Enviado"
    ENTREGADO = "Entregado"
    CANCELADO = "Cancelado"


class MetodoPago(str, Enum):
    TARJETA_CREDITO = "Tarjeta Crédito"
    TARJETA_DEBITO = "Tarjeta Débito"
    PSE = "PSE"
    TRANSFERENCIA = "Transferencia"
    EFECTIVO = "Efectivo"
    DESCONOCIDO = "Desconocido"


class EstadoPago(str, Enum):
    PENDIENTE = "Pendiente"
    APROBADO = "Aprobado"
    RECHAZADO = "Rechazado"
    DESCONOCIDO = "Desconocido"


class EstadoEnvio(str, Enum):
    PREPARANDO = "Preparando"
    EN_TRANSITO = "En tránsito"
    ENTREGADO = "Entregado"
    PENDIENTE = "Pendiente"
    DESCONOCIDO = "Desconocido"


class EstadoDevolucion(str, Enum):
    PENDIENTE = "Pendiente"
    APROBADA = "Aprobada"
    RECHAZADA = "Rechazada"
    FINALIZADA = "Finalizada"
    DESCONOCIDO = "Desconocido"


class MotivoDevolucion(str, Enum):
    PRODUCTO_DEFECTUOSO = "Producto defectuoso"
    PRODUCTO_EQUIVOCADO = "Producto equivocado"
    NO_CUMPLIO_EXPECTATIVAS = "No cumplió expectativas"
    EMPAQUE_DANADO = "Empaque dañado"
    LLEGO_INCOMPLETO = "Llegó incompleto"
    CAMBIO_DE_OPINION = "Cambio de opinión"
    DESCONOCIDO = "Desconocido"


class TipoDireccion(str, Enum):
    CASA = "Casa"
    TRABAJO = "Trabajo"
    FACTURACION = "Facturación"
    DESCONOCIDO = "Desconocido"
