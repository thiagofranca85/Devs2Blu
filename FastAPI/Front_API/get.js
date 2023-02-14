console.log("Rodando arquivo JS")

    function get_alunos(){
        fetch(
            'http://127.0.0.1:8000/api/v1/alunos/',
            {
                Headers:
                {
                    'Accept': 'aplication/json'
                }
            }
        )
        .then(Response => Response.text())
        .then(
            text => {
                console.log(text)
                let dados = JSON.parse(text)
                console.log(dados)
    
                let tbody = document.getElementById("tbody-alunos")
                dados.forEach(aluno => {
                    tbody.innerHTML += `
                    <tr>
                        <td>${aluno.id}</td>
                        <td>${aluno.nome}</td>
                        <td>${aluno.idade}</td>
                        <td>${aluno.email}</td>
                    </tr>
                    `                
                });
            }
        )
    }

    function get_aluno(){
        let id = document.getElementById('id_busca').value
            fetch(
                `http://127.0.0.1:8000/api/v1/alunos/${id}`,
                {
                    Headers:
                    {
                        'Accept': 'aplication/json'
                    }
                })
                .then(Response => Response.text())
                .then(
                    text => {
                        console.log(text)
                        let dados = JSON.parse(text)                    
                        console.log(dados)
            
                        let tbody = document.getElementById("tbody-alunos")
                            tbody.innerHTML = "";
                            tbody.innerHTML += `
                            <tr>
                                <td>${dados.id}</td>
                                <td>${dados.nome}</td>
                                <td>${dados.idade}</td>
                                <td>${dados.email}</td>
                            </tr>
                            `     
                        }
                )                
    }

    get_alunos()