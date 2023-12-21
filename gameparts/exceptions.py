class FieldIndexError(Exception):


    def __str__(self) -> str:
        #return super().__str__()
        return f'Введено значение за границами игрового поля'
 
    
    # Вот оно — новое исключение, унаследованное от базовго класса Exception.
class CellOccupiedError(Exception):

    def __str__(self):
        return 'Попытка изменить занятую ячейку'