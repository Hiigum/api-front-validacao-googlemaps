document.getElementById("apiForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let chaveApi = document.getElementById("chave_api").value;
    let resultadoDiv = document.getElementById("resultado");
    
    fetch("/verificar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ chave_api: chaveApi })
    })
    .then(response => response.json())
    .then(data => {
        if (data.valido) {
            resultadoDiv.textContent = "✅ " + data.mensagem;
        } else {
            resultadoDiv.textContent = "❌ " + data.mensagem;
        }
        resultadoDiv.classList.remove("hidden");
    })
    .catch(error => {
        resultadoDiv.textContent = "Erro: " + error;
        resultadoDiv.classList.remove("hidden");
    });
});
