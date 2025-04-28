import docx2txt #Biblioteca conversão DOCX/DOC.
import fitz  #Bibloteca conversão PDF.

class DocParser:
    def convert_file2content(self, file_path):

        #Converte ficheiros .DOCX .DOC E .PDF para texto.
        if file_path.lower().endswith(('.docx', '.doc')):
            return self._read_doc(file_path)
        
        elif file_path.lower().endswith('.pdf'):
            return self._read_pdf(file_path)
        
        else: #Se não for nenhuma das extensões aceites.
            raise ValueError("Tipo de ficheiro não suportado.")

    def _read_doc(self, file_path):
        #Extrai o texto do ficheiro .DOCX ou .DOC.
        return docx2txt.process(file_path)

    def _read_pdf(self, file_path):
        #Extrai o texto do ficheiro .PDF.
        texto_extraido = ""
        documento = fitz.open(file_path)
        for pagina in documento:
            texto_extraido += pagina.get_text()
        documento.close()
        return texto_extraido
