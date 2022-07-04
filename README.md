# hachage_bitcoin
programme hachage , explication simple mais efficace du fonctionnement du blockchain pour le minage des bitcoin d'apres le cours

https://www.youtube.com/results?search_query=python+au+lycee+bitcoin

les fichiers graphiz preuve de travail permettent d expliquer visuellement les etapes 

la preuve intiale [0,0,0,0,0,0]  et la transaction "Abel +35" est convertit [0, 0, 0, 65, 98, 1, 8, 32, 43, 32, 51, 53] 

on definit une liste =  preuve intiale [0,0,0,0,0,0] + la transaction soit [0,0,0,0,0,0,0, 0, 0, 65, 98, 1, 8, 32, 43, 32, 51, 53] 

et on calcule une preuve de travail de cette liste , tel que cette preuve soit <= Max [0,0,7]

c est a dire , on prend au hasard une preuve de travail [1,2,3,4,5,6] 

on fait le hachage de [0,0,0,0,0,0,0, 0, 0, 65, 98, 1, 8, 32, 43, 32, 51, 53 , 1,2,3,4,5,6] 

si le resultat est <= Max [0,0,7] , pour les 3 premiers elements du hachage alors la preuve de travail est trouvee



