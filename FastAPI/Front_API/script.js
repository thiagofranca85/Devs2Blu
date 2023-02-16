var api_url_alunos = 'http://localhost:8000/api/v1/alunos';
var api_url_usuarios = 'http://localhost:8000/api/v1/usuarios';
var api_url_professores = 'http://localhost:8000/api/v1/professores';

// Função pela lista de Alunos
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

            let dados = JSON.parse(text)
            let tbody = document.getElementById("tbody-lista")
            tbody.innerHTML = "";
            dados.forEach(aluno => {
                tbody.innerHTML += `
                <tr>
                    <td>${aluno.id}</td>
                    <td>${aluno.nome}</td>
                    <td>${aluno.idade}</td>
                    <td>${aluno.email}</td>
                    <td>
                    <a href="save.html?id=${aluno.id}">editar</a> |
                    <button onclick='remove(${aluno.id})'>deletar</button>
                    </td>
                </tr>
                `                
            });
        }
    )
}
    
// Função pela lista de Usuarios
function get_usuarios(){
    fetch(
        'http://127.0.0.1:8000/api/v1/usuarios/',
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

            let dados = JSON.parse(text)
            let tbody = document.getElementById("tbody-lista")
            tbody.innerHTML = "";
            dados.forEach(usuario => {
                tbody.innerHTML += `
                <tr>
                    <td>${usuario.id}</td>
                    <td>${usuario.nome}</td>
                    <td>${usuario.idade}</td>
                    <td>${usuario.email}</td>
                    <td>
                    <a href="save.html?id=${usuario.id}">editar</a> |
                    <button onclick='remove(${usuario.id})'>deletar</button>
                    </td>
                </tr>
                `                
            });
        }
    )
}

// // Função pela lista de Professores
function get_professores(){
    fetch(
        'http://127.0.0.1:8000/api/v1/professores/',
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

            let dados = JSON.parse(text)
            let tbody = document.getElementById("tbody-lista")
            tbody.innerHTML = "";
            dados.forEach(professor => {
                tbody.innerHTML += `
                <tr>
                    <td>${professor.id}</td>
                    <td>${professor.nome}</td>
                    <td>${professor.idade}</td>
                    <td>${professor.email}</td>
                    <td>
                    <a href="save.html?id=${professor.id}">editar</a> |
                    <button onclick='remove(${professor.id})'>deletar</button>
                    </td>
                </tr>
                `                
            });
        }
    )
}

// Pegar ID de uma lista
function get_by_id(){
    let list = document.getElementById('lista_busca').value
    let id = document.getElementById('id_busca').value    

    fetch(`http://127.0.0.1:8000/api/v1/${list}/${id}`)
        .then(Response => Response.text())
        .then(
            text => {
                console.log(text)
                let dados = JSON.parse(text)                    
                console.log(dados)
    
                let tbody = document.getElementById("tbody-lista")
                    tbody.innerHTML = "";
                    tbody.innerHTML += `
                    <tr>
                        <td>${dados.id}</td>
                        <td>${dados.nome}</td>
                        <td>${dados.idade}</td>
                        <td>${dados.email}</td>
                        <td>
                        <a href="save.html?id=${dados.id}">editar</a> |
                        <button onclick='remove(${dados.id})'>deletar</button>
                        </td>
                    </tr>
                    `     
                })                
}

// Remover da Lista
function remove(id){
    fetch(`${api_url_alunos}/${id}`,{
        method: 'DELETE',
        headers: {
            'Accept': 'application/json'
        }
    })
    .then(response => {
        if(response.status == 204){
            get_alunos();
        }else{
            alert("Erro");
        }
    })
 }

// Editar ID da Lista


function get_list(e) {
    console.log(e.target.dataset.name)
}

