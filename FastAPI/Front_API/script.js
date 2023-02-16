var api_url_alunos = 'http://localhost:8000/api/v1/alunos';
var api_url_usuarios = 'http://localhost:8000/api/v1/usuarios';
var api_url_professores = 'http://localhost:8000/api/v1/professores';

// Puxa a lista conforme valor do Button "data-name" no HTML
function get_list(e) {
    let list = e.target.dataset.name;
  
    fetch(`http://127.0.0.1:8000/api/v1/${list}s`)
      .then(response => response.json())
      .then(data => {
        let thead = document.getElementById("thead-lista");
        let tbody = document.getElementById("tbody-lista");
  
        tbody.innerHTML = "";
        thead.innerHTML =
          `<thead>
            <th>ID</th>
            <th>Nome</th>
            <th>Idade</th>
            <th>Email</th>
            <th>Ações</th>
          </thead>`;
  
        data.forEach(item => {
          tbody.innerHTML += `
            <tr>
              <td>${item.id}</td>
              <td>${item.nome}</td>
              <td>${item.idade}</td>
              <td>${item.email}</td>
              <td>
                <a href="edit.html?id=${item.id}">Editar</a>
                <button onclick="remove(${list.id}, '${list.__typename}', event)">Deletar</button>
              </td>
            </tr>`;
        });
      });
  }
  

// Seleciona uma lista e um ID e busca.
function get_by_id(){
    let list = document.getElementById('lista_busca').value
    let id = document.getElementById('id_busca').value    

    fetch(`http://127.0.0.1:8000/api/v1/${list}/${id}`)
        .then(Response => Response.text())
        .then(
            text => {
                let data = JSON.parse(text)      
                let thead = document.getElementById("thead-lista")
                let tbody = document.getElementById("tbody-lista")
                tbody.innerHTML = "";
                thead.innerHTML =
                `                
                <thead>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Idade</th>
                    <th>Email</th>
                </thead>
                `
                    tbody.innerHTML += `
                    <tr>
                        <td>${data.id}</td>
                        <td>${data.nome}</td>
                        <td>${data.idade}</td>
                        <td>${data.email}</td>
                        <td>
                        <a href="edit.html?id=${data.id}">editar</a> |
                        <button onclick='remove(${data.id})'>deletar</button>
                        </td>
                    </tr>
                    `     
                    }
            )                
}

function remove(id, endpoint, event) {
    fetch(`http://127.0.0.1:8000/api/v1/${endpoint}/${id}`, {
      method: 'DELETE',
      headers: {
        'Accept': 'application/json'
      }
    })
    .then(response => {
      if (response.status == 204) {
        // Refresh the list after successful removal
        get_list({target: {dataset: {name: endpoint}}});
      } else {
        // Display an error message if the removal was not successful
        alert('Falhou em remover o item.');
      }
    });
  }
  

function edit(id, endpoint) {
    // fetch the resource with the specified id
    fetch(`http://127.0.0.1:8000/api/v1/${endpoint}/${id}`)
        .then(response => response.json())
        .then(data => {
        // populate the form fields with the data
        document.getElementById('input-nome').value = data.nome;
        document.getElementById('input-idade').value = data.idade;
        document.getElementById('input-email').value = data.email;
        document.getElementById('form-alunos').setAttribute('onsubmit', `update(event, ${id}, '${endpoint}')`);
        document.getElementById('btn-form').textContent = 'Atualizar';
        }
    )
}