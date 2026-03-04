<!DOCTYPE html>
<html lang="pt-br">
<body>

  <h1>🎙️ Voice Agent: LangGraph + LangChain</h1>

  <p>
    Assistente virtual que integra reconhecimento de voz e orquestração de agentes para execução de tarefas via comandos de áudio.
  </p>

  <div style="background-color: #f8f9fa; border-left: 5px solid #6c757d; padding: 15px; margin: 20px 0;">
    <strong>🛠️ Versão Inicial (MVP)</strong><br>
    Projeto em estágio embrionário de desenvolvimento, focado na validação da arquitetura de agentes de voz.
  </div>

  <hr>

  <h2>🧠 Inteligência e Processamento</h2>
  <ul>
    <li><b>Modelo Único:</b> Atualmente operando com o <b>Gemma 3 (4b)</b>.</li>
    <li><b>Local Engine:</b> Processamento realizado via <b>Ollama</b>.</li>
    <li><b>Orquestração:</b> Fluxos cíclicos gerenciados por <b>LangGraph</b> e <b>LangChain</b>.</li>
  </ul>

  <hr>

  <h2>⚠️ Considerações Técnicas</h2>
  
  <ul>
    <li>
      <b>Velocidade:</b> Por utilizar um modelo local e agentes de decisão, o tempo de resposta é moderado (não é instantâneo). A latência reflete o processamento do grafo de pensamento.
    </li>
    <li>
      <b>Requisitos:</b> O sistema exige a configuração de <b>APIs externas</b> para determinadas funções dos agentes e o Ollama rodando localmente.
    </li>
    <li>
      <b>Interface:</b> Entrada de dados via <b>SpeechRecognition</b> para uma experiência Hands-Free.
    </li>
  </ul>

</body>
</html>
