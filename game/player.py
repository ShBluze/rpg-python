import json

class Player:
    
    def __init__(self, nombre, nivel, experiencia, estado, racha):
        self.nombre = nombre
        self.nivel = int(nivel)
        self.experiencia = int(experiencia)
        self.estado = estado
        self.racha = racha
        
        
    #barra de experiencia    
    def xp_bar(self, xp, xp_max, size=20):
        filled = int((xp / xp_max) * size)
        empty = size - filled
        bar = "█" * filled + "░" * empty
        percent = int((xp / xp_max) * 100)
        return f"[{bar}] {percent}%"
    
    def mostrarDatos(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Nivel: {self.nivel}\n"
            f"Experiencia: {self.experiencia}\n{self.xp_bar(self.experiencia, 100)}\n"
            f"Estado: {self.estado}\n"
       f"Racha: {self.racha}"
        )
        
    #guardar datos jugador en json
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "nivel": self.nivel,
            "experiencia": self.experiencia,
            "estado": self.estado,
            "racha": self.racha
        }
        
    def guardar(self, archivo="player.json"):
        with open(archivo, "w") as f:
            json.dump(self.to_dict(), f, indent=4)
            
    @classmethod
    def cargar(cls, archivo="player.json"):
        with open(archivo, "r") as f:
            data = json.load(f)
            
        return cls(
            data["nombre"],
            data["nivel"],
            data["experiencia"],
            data["estado"],
            data["racha"]
    )
    
        

jugador = Player("Jorge", 2, 10, "normal", 0)
# jugador = Player.cargar()

#guardar los datos
jugador.guardar()

print(jugador.estado)
    
    
    
    
