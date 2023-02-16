var api_url = 'http://localhost:8000/api/v1/alunos';

//funcao para pegar todos
function get_all(){
    //Fetch metodo JavaScript para acessar e manipular HTTP, tais como os pedidos e respostas. 
    fetch(api_url)
    
    .then(response =>response.text())
    .then(function(text) {
        //variavel body acessando o documento, html manipulando tag tbodyalunos
        let tbody = document.getElementById('tbody-alunos');
        //variavel let dados convertendo text para json
        let dados = JSON.parse(text);
        //tbody innerHtml recebe uma lista vazia
        tbody.innerHTML = '';

        //variavel dados que recebe o nosso texte entra em um foreach
        //criamos variavel de aluno
        dados.forEach(aluno => {
        //tbody inner html incrementando dados convertidos para incrementar nos hmtl
        tbody.innerHTML += ` <tr>
            <td>${aluno.id}</td>
            <td>${aluno.nome}</td>
            <td>${aluno.idade}</td>
            <td>${aluno.email}</td>
            <td>
                <a href="alunosave.html?id=${aluno.id}">editar</a> |
                <button onclick='remove(${aluno.id})'>deletar</button>
            </td>
        </tr>
        `;
      });
    })
}

//Buscar por aluno
function search(){
    //variavel id aluno acessando documento html acessando campo idbuscae seu valor
    let id_aluno = document.getElementById('id-busca').value;
    //imprimindo id_aluno
    console.log(id_aluno)
    // se id aluno for diferente de vazio
    if(id_aluno != ''){
        //acesse api url da nossa string
        api_url = `${api_url}/${id_aluno}`
    }
    else{
        return;
    }
 
 
    fetch(api_url)
    .then(response => response.text())
    .then(function(text) {
      let tbody = document.getElementById('tbody-alunos');     
      let aluno = JSON.parse(text);
      console.log(aluno);    
      
      tbody.innerHTML = ` <tr>
        <td>${aluno.id}</td>
        <td>${aluno.nome}</td>
        <td>${aluno.idade}</td>
        <td>${aluno.email}</td>
        <td>
            <a href="alunosave.html?id=${aluno.id}">editar</a> |
            <button onclick='remove(${aluno.id})'>deletar</button>
        </td>
      </tr>`;
    });
 }

// ela realiza uma busca de aluno por id e retorna aluno Json
function get_by_id(id_aluno){
    let aluno = fetch(`${api_url}/${id_aluno}`)
    .then(response => response.text())
    .then(function(text) {    
        return JSON.parse(text);
    });   
    return aluno;
 }
 
 
function load_aluno(id_aluno){
    get_by_id(id_aluno).then(aluno =>{
        document.getElementById("id").value = aluno.id;
        document.getElementById("nome").value = aluno.nome;
        document.getElementById("idade").value = aluno.idade;
        document.getElementById("email").value = aluno.email;
    });
  
}
 
//Botao salvar tanto para criar quanto editar
function save(){
    let id = document.getElementById("id").value;
    let nome = document.getElementById("nome").value;
    let idade = document.getElementById("idade").value;
    let email = document.getElementById("email").value;
       
    if(id != ''){
        console.log('editar')
        aluno = {"id":id, "nome": nome, "idade": idade, "email": email}
        update(aluno);
    }
    else{
        aluno = {"nome": nome, "idade": idade, "email": email}
        create(aluno);
    }       
}
 
 
function update(aluno){
    let mensagem = document.getElementById("mensagem");
    fetch(`${api_url}/${aluno.id}`,{
        method: 'PUT',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(aluno)
    })

    .then(response => {
        if(response.status == 202){
            mensagem.innerHTML = "Alterado com sucesso";
        }else{
            mensagem.innerHTML = "Erro";
        }
    })
}
 
 
function create(aluno){
    let mensagem = document.getElementById("mensagem");
    fetch(api_url,{
        method: 'POST',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(aluno)
    })
    .then(response => {
        if(response.status == 201){
         
            mensagem.innerHTML = "Criado com sucesso";
        }else{
            mensagem.innerHTML = "Erro";
        }
    })
}
 
function remove(id){
    fetch(`${api_url}/${id}`,{
        method: 'DELETE',
        headers: {
            'Accept': 'application/json'
        }
    })
    .then(response => {
        if(response.status == 204){
            get_all();
        }else{
            alert("Erro");
        }
    })
}