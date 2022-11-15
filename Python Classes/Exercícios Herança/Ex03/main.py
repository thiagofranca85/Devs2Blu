from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

contaPF = PessoaFisica('thiago', '654987321', 5000)
print("*** PESSOA FISICA ***")
print(contaPF)
contaPF.segundo_titular = 'Segundo Titular PF'
print("*** PESSOA FISICA ALTERAÇÕES ***")
print(contaPF)

contaPJ = PessoaJuridica('empresa', '4984654654', 5156165465)
print("*** PESSOA JURIDICA ***")
print(contaPJ)
contaPJ.segundo_titular = 'Segundo Titular PJ'
print("*** PESSOA JURIDICA ALTERAÇÕES ***")
print(contaPJ)