"""Aula 1 — PBL: mochila com slots fixos."""


class MochilaRPG:
    def __init__(self, slots):
        self.slots = slots
        self.itens_guardados = 0
        self.inventario = [None] * slots

    def coletar_item(self, item):
        print(f"Tentando coletar: {item}...")
        if self.itens_guardados < self.slots:
            self.inventario[self.itens_guardados] = item
            self.itens_guardados += 1
            print(f"[Sucesso] {item} no slot {self.itens_guardados - 1}.")
        else:
            print(f"[Falha] Mochila cheia! Descarte algo para pegar {item}.")

    def abrir_mochila(self):
        print("--- Conteúdo da Mochila ---")
        for i in range(self.slots):
            status = self.inventario[i] or "[Vazio]"
            print(f"Slot {i}: {status}")


if __name__ == "__main__":
    mochila = MochilaRPG(4)
    for item in ("Poção de Cura", "Espada de Ferro", "Mapa Antigo", "Tocha"):
        mochila.coletar_item(item)
    mochila.abrir_mochila()
    mochila.coletar_item("Amuleto Mágico")
