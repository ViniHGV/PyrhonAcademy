import sqlite3

connector = sqlite3.connect("Academia.db")
cursor= connector.cursor()


sql = '''create table if not exists Aluno (
	CodMatricula integer primary key autoincrement,
	DataMatricula date,
	Nome string,
	Endereco string,
	Telefone string,
	DataNascimento date,
	Altura float,
	Peso float
)'''
cursor.execute(sql)

sql = '''create table if not exists Turma (
	id integer primary key autoincrement,
	NomeAtividade string,
	DiaHorarioAula string,
	DuracaoAula string,
	TipoTurma string,
	DataInicioTurma date,
	DataTerminoTurma date
)'''
cursor.execute(sql)

sql = '''create table if not exists Pagamento (
	id integer primary key autoincrement,
	TipoPagamento string,
	ValorPagamento float,
  Aluno integer,
  Turma integer,
	foreign key (Aluno) references Aluno(CodMatricula),
	foreign key (Turma) references Turma(id)
)'''
cursor.execute(sql)

sql = '''create table if not exists Instrutor (
	id integer primary key autoincrement,
	Nome string,
	RG string,
	DataNascimento date,
	Titulacao string,
	Email string,
  Turma integer,
	foreign key (Turma) references Turma(id)
)'''
cursor.execute(sql)

sql = '''create table if not exists Auxiliar (
	id integer primary key autoincrement,
	Nome string,
	RG string,
	DataNascimento date,
	Titulacao string,
	Email string,
  Alocacao integer,
	foreign key (Alocacao) references Turma(id)
)'''
cursor.execute(sql)

sql = '''create table if not exists Monitor (
	id integer primary key autoincrement,
  Aluno integer,
  Turma integer,
	foreign key (Aluno) references Aluno(CodMatricula),
	foreign key (Turma) references Turma(id)
)'''
cursor.execute(sql)

sql = '''create table if not exists Matricula (
	id integer primary key autoincrement,
  Aluno integer,
  Turma integer,
	Presencas integer,
	Ausencias integer,
	foreign key (Aluno) references Aluno(CodMatricula),
	foreign key (Turma) references  Turma(id)
)'''
cursor.execute(sql)

sql = '''create table if not exists AlunoMonitor (
	id integer primary key autoincrement,
  Aluno integer,
  Turma integer,
  Instrutor integer,
	foreign key (Aluno) references Aluno(CodMatricula)
	foreign key (Turma) references Turma(id)
	foreign key (Instrutor) references Instrutor(id)
)'''
cursor.execute(sql)


connector.commit()
cursor.close()
connector.close()