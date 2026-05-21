
# PRODUTO ABSTRATO
class Documento:
    def exibir_formato(self):
     pass

# PRODUTOS CONCRETOS
class DocumentoPDF(Documento):
    def exibir_formato(self):
        return "Formato: PDF"
    
class DocumentoHTML(Documento):
    def exibir_formato(self):
        return "Formato: HTML"
    
# CRIADOR ABSTRATO (DECLARA O Factory Method)
class CriadorDocumento:
    def fabricar_documento(self):
        raise NotImplementedError
    def renderizar(self):
        doc = self.fabricar_documento()
        return f"Documento renderizado. {doc.exibir_formato()}"
    

    # CRIADOR CONCRETO
class CriadorPDF(CriadorDocumento):
    def fabricar_documento(self):
     return DocumentoPDF()
# CLIENTE

cliente = CriadorPDF()
print(cliente.renderizar())
# Saída: Documento renderizado. Formato: PDF

    # CRIADOR CONCRETO
class CriadorHTML(CriadorDocumento):
    def fabricar_documento(self):
     return DocumentoHTML()
# CLIENTE

cliente = CriadorHTML()
print(cliente.renderizar())
# Saída: Documento renderizado. Formato: PDF