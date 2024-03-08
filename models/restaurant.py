from models.review import Review
class Restaurant:
    """Representa um restaurante e suas características."""
    
    restaurants=[]
    
    def __init__(self, name, category):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        
        self._name = name.title()
        self._category = category.capitalize()
        self._active = False
        self._ratings = []
        Restaurant.restaurants.append(self)
        
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        
        return f'{self._name} | {self._category} | {self.active}'
    
    @classmethod
    def show_restaurants(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        
        print(f'{'Nome do Restaurante'.ljust(10)}|{'Categoria do Restaurante'.ljust(10)}|{'Avaliação'.ljust(10)}|{'Ativo?'}')
        for restaurantes in cls.restaurants:
            print(f'{restaurantes._name.ljust(19)}|{restaurantes._category.ljust(24)}|{str(restaurantes.rating).ljust(10)}|{restaurantes.active}')
    
    @property
    def active(self):
        """Retorna uma string indicando o estado de atividade do restaurante."""
        
        return "Sim" if self._active else "Não"
    
    def activate_restaurant(self):
        """Alterna o estado de atividade do restaurante."""
        
        self._active = not self._active
        
    def add_rating(self,name,rating):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        
        if 0 <= rating <=5:
            review = Review(name,rating)
            self._ratings.append(review)
            
        
    @property
    def rating(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        
        if not self._ratings:
            return '-'
        else:
            avarage = round(sum(ratings._rating for ratings in self._ratings)/len(self._ratings), 1)
            if avarage > 10:
                return 10
            else:
                return avarage