var api_url = 'http://localhost:8000/api/v1/professores';

//funcao para pegar todos
function get_all(){
    //Fetch metodo JavaScript para acessar e manipular HTTP, tais como os pedidos e respostas. 
    fetch(api_url)
    
    .then(response =>response.text())
    .then(function(text) {
        //variavel body acessando o documento, html manipulando tag tbodyprofessores
        let tbody = document.getElementById('tbody-professores');
        //variavel let dados convertendo text para json
        let dados = JSON.parse(text);
        //tbody innerHtml recebe uma lista vazia
        tbody.innerHTML = '';

        //variavel dados que recebe o nosso texte entra em um foreach
        //criamos variavel de professor
        dados.forEach(professor => {
        //tbody inner html incrementando dados convertidos para incrementar nos hmtl
        tbody.innerHTML += ` <tr>
            <td>${professor.id}</td>
            <td>${professor.nome}</td>
            <td>${professor.idade}</td>
            <td>${professor.email}</td>
            <td>
                <a href="profsave.html?id=${professor.id}">editar</a> |
                <button onclick='remove(${professor.id})'>deletar</button>
            </td>
        </tr>
        `;
      });
    })
}

//Buscar por professor
function search(){
    //variavel id aluno acessando documento html acessando campo idbuscae seu valor
    let id_professor = document.getElementById('id-busca').value;
    //imprimindo id_aluno
    console.log(id_professor)
    // se id aluno for diferente de vazio
    if(id_professor != ''){
        //acesse api url da nossa string
        api_url = `${api_url}/${id_professor}`
    }
    else{
        return;
    }
 
 
    fetch(api_url)
    .then(response => response.text())
    .then(function(text) {
      let tbody = document.getElementById('tbody-professores');     
      let professor = JSON.parse(text);
      console.log(professor);    
      
      tbody.innerHTML = ` <tr>
        <td>${professor.id}</td>
        <td>${professor.nome}</td>
        <td>${professor.idade}</td>
        <td>${professor.email}</td>
        <td>
            <a href="profsave.html?id=${professor.id}">editar</a> |
            <button onclick='remove(${professor.id})'>deletar</button>
        </td>
      </tr>`;
    });
 }

// ela realiza uma busca de aluno por id e retorna professor Json
function get_by_id(id_professor){
    let professor = fetch(`${api_url}/${id_professor}`)
    .then(response => response.text())
    .then(function(text) {    
        return JSON.parse(text);
    });   
    return professor;
 }
 
 
function load_professor(id_professor){
    get_by_id(id_professor).then(professor =>{
        document.getElementById("id").value = professor.id;
        document.getElementById("nome").value = professor.nome;
        document.getElementById("idade").value = professor.idade;
        document.getElementById("email").value = professor.email;
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
        professor = {"id":id, "nome": nome, "idade": idade, "email": email}
        update(professor);
    }
    else{
        professor = {"nome": nome, "idade": idade, "email": email}
        create(professor);
    }       
}
 
 
function update(professor){
    let mensagem = document.getElementById("mensagem");
    fetch(`${api_url}/${professor.id}`,{
        method: 'PUT',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(professor)
    })

    .then(response => {
        if(response.status == 202){
            mensagem.innerHTML = "Alterado com sucesso";
        }else{
            mensagem.innerHTML = "Erro";
        }
    })
}
 
 
function create(professor){
    let mensagem = document.getElementById("mensagem");
    fetch(api_url,{
        method: 'POST',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(professor)
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