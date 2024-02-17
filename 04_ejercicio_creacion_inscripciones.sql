CREATE TABLE Inscripciones(
	InscripcionID INT AUTO_INCREMENT PRIMARY KEY,
    EstudianteID INT,
    CursoID INT,
    FOREIGN KEY (EstudianteID) REFERENCES Estudiantes(EstudianteID),
    FOREIGN KEY (CursoID) REFERENCES Cursos(CursoID));