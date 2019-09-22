from django.db import models

# Create your models here.
class Autor(models.Model):
    class Meta:
        verbose_name_plural = "autores"
    
    name = models.CharField("nome",max_length=100)
    last_name = models.CharField("sobrenome", max_length=100)

    def __str__(self):
        return self.last_name.upper() + ',' + self.name


class Aluno(models.Model):
    class Meta:
        verbose_name_plural = "alunos"
    SEXO_CHOICES = [
        ('MAS', 'Masculino'),
        ('FEM', 'Feminino'),
        ('OUT', 'Outros'),
    ]
    name = models.CharField("nome", max_length=100)
    last_name = models.CharField("sobrenome", max_length=100)
    registration = models.CharField("matricula", max_length=10, unique=True)
    sex = models.CharField("sexo", choices=SEXO_CHOICES, default="Masculino", max_length=3)
    date_birth = models.DateField("data_nasc")
    email = models.EmailField("e-mail")


    def __str__(self):
        return self.last_name.upper() + ',' + self.name

class Livro(models.Model):
    class Meta:
         verbose_name_plural = "livros"
    title = models.CharField("titulo", max_length=50)
    author = models.ForeignKey( Autor, on_delete=models.CASCADE)
    year_publication = models.IntegerField("ano_publicacao")

    def __str__(self):
        return "{}, ({}) ".format(self.title, self.year_publication)



class Emprestimo(models.Model):
    class Meta:
        verbose_name_plural = "emprestimos"
    user = models.ForeignKey( 'auth.User', on_delete=models.CASCADE)
    student = models.ForeignKey( Aluno, on_delete=models.CASCADE)
    date_withdrawn = models.DateField("data_retirada")
    date_devolution = models.DateField("data_devolucao")
    books = models.ManyToManyField(Livro)
    returned = models.BooleanField("devolvido")

