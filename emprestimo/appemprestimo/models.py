from django.db import models

# Create your models here.
class Autor(models.Model):
    class Meta:
        nome_plural = "autores"
    
    name = models.CharField("nome",max_length=100)
    last_name = models.CharField("sobrenome", max_length=100)

    def __str__(self):
        return self.last_name.upper() + ',' + self.name


class Aluno(models.Model):
    SEXO_CHOICES = [
        ('MAS', 'Masculino'),
        ('FEM', 'Feminino'),
        ('OUT', 'Outros'),
    ]
    class Meta:
        nome_plural = "alunos"
    
    name = models.CharField("nome", max_length=100)
    last_name = models.CharField("sobrenome", max_length=100)
    registration = models.CharField("matricula", max_length=10)
    sex = models.CharField("sexo", choices=SEXO_CHOICES, default="Masculino")
    date_birth = models.DateField("data_nasc")
    email = models.EmailField("e-mail")


    def __str__(self):
        return self.last_name.upper() + ',' + self.name

    class Livro(models.Model):
        class Meta:
            nome_plural = "livros"
        title = models.CharField("titulo", max_length=50)
        author = models.ForeignKey("foreignkey_autor", Autor, on_delete=models.CASCADE)
        year_publication = models.IntegerField("ano_publicacao")

        def __str__(self):
            return "{}, ({}) ".format(self.title, self.year_publication)



    class Emprestimo(models.Model):
        class Meta:
            nome_plural = "emprestimos"
        user = models.ForeignKey("foreignkey_usuario", 'auth.User', on_delete=models.CASCADE)
        student = models.ForeignKey("foreignkey_aluno", Aluno, on_delete=models.CASCADE)
        date_withdrawn = models.DateField("data_retirada")
        date_devolution = models.DateField("data_devolucao")
        books = models.ForeignKey("livros", Livro, on_delete=models.CASCADE)
        returned = models.BooleanField("devolvido")

