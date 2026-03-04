<!DOCTYPE html>
<html lang="pt-br">
<body>

  <h1>🎙️ Voice Agent: LangGraph + LangChain</h1>

  <p>
    Assistente virtual que integra reconhecimento de voz e orquestração de agentes para execução de tarefas via comandos de áudio.
  </p>

  <div style="background-color: #e3f2fd; border-left: 5px solid #2196f3; padding: 15px; margin: 20px 0;">
    <strong>🛠️ Estágio Experimental (Versão Inicial)</strong><br>
    O projeto está em seus primeiros passos de desenvolvimento. Atualmente, o sistema opera com <b>apenas um modelo de linguagem (LLM)</b> configurado.
  </div>

  <hr>

  <h2>🔍 Características Atuais</h2>
  <ul>
    <li><b>Interface:</b> SpeechRecognition para entrada de comandos por voz.</li>
    <li><b>Lógica:</b> Fluxos estruturados via LangGraph e LangChain.</li>
    <li><b>Custo:</b> Projeto 100% gratuito.</li>
  </ul>

  <hr>

  <h2>⚠️ Observações de Desempenho</h2>
  
  <ul>
    <li>
      <b>Tempo de Resposta:</b> Devido ao processamento do modelo único e à natureza gratuita da infraestrutura, as respostas <b>não são instantâneas</b> e podem levar alguns segundos.
    </li>
    <li>
      <b>Requisito de API:</b> A execução das tarefas pelos agentes requer a configuração prévia de chaves de API.
    </li>
  </ul>

  <hr>

  <h2>🚀 Roadmap Curto Prazo</h2>
  <ol>
    <li>Otimização do tempo de latência na transcrição.</li>
    <li>Implementação de suporte a múltiplos modelos simultâneos.</li>
    <li>Refinamento da memória de curto prazo do agente.</li>
  </ol>

</body>
</html>
