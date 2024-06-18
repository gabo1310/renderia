import os
import warnings

# Ignorar todas las advertencias de LangChain deprecado
warnings.filterwarnings("ignore", category=DeprecationWarning, module='langchain_core._api.deprecation')

class ClaudeEmbeddings:
    def __init__(self, model_name="claude-3-opus-20240229", api_key=None):
        self.model_name = model_name
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("Anthropic API key must be set in environment variables or passed as an argument.")

    def embed(self, text):
        # Implementa el método para obtener embeddings desde Claude
        # Esto es una simulación, ya que Claude podría no tener un endpoint específico para embeddings.
        # En un caso real, aquí se llamaría al API de Anthropic para obtener embeddings.
        return [0.0] * 768  # Devuelve un vector de ejemplo

# Crear una instancia de ClaudeEmbeddings
embeddings = ClaudeEmbeddings()