# hachage_bitcoin
programme hachage , explication simple mais efficace du fonctionnement du blockchain pour le minage des bitcoin d'apres le cours

https://www.youtube.com/results?search_query=python+au+lycee+bitcoin

les fichiers graphiz preuve de travail permettent d expliquer visuellement les etapes 

la preuve intiale [0,0,0,0,0,0]  et la transaction "Abel +35" est convertit [0, 0, 0, 65, 98, 1, 8, 32, 43, 32, 51, 53] 

on definit une liste =  preuve intiale [0,0,0,0,0,0] + la transaction soit [0,0,0,0,0,0,0, 0, 0, 65, 98, 1, 8, 32, 43, 32, 51, 53] 

et on calcul une preuve de travail de cette liste , tel que cette preuve soit <= Max [0,0,7]

c est a dire , on prend au hasard une preuve de travail [1,2,3,4,5,6] 

on fait le hachage de [0,0,0,0,0,0,0, 0, 0, 65, 98, 1, 8, 32, 43, 32, 51, 53 , 1,2,3,4,5,6] 

si le resultat est <= Max [0,0,7] , pour les 3 premiers elements du hachage alors la preuve de travail est trouvee

exemple du cours 

Le livre : [[0, 0, 0, 0, 0, 0], 'Abel +35', [71, 15, 6, 8, 29, 7]]

le hachage est  [0, 0, 1, 20, 17, 23]  avec la preuve [71, 15, 6, 8, 29, 7]

la liste  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 65, 98, 1, 8, 32, 43, 51, 53]  et le hachage de cette liste + preuve [71, 15, 6, 8, 29, 7] est : [0, 0, 1, 20, 17, 23]

la verification est  True

Le livre : [[0, 0, 0, 0, 0, 0], 'Abel +35', [71, 15, 6, 8, 29, 7], 'Bob -77', [50, 11, 6, 22, 78, 93]]

le hachage est  [0, 0, 1, 15, 64, 60]  avec la preuve [50, 11, 6, 22, 78, 93]

la liste  [71, 15, 6, 8, 29, 7, 0, 0, 0, 0, 0, 66, 11, 98, 32, 45, 55, 55]  et le hachage de cette liste + preuve [50, 11, 6, 22, 78, 93] est : [0, 0, 1, 15, 64, 60]

la verification est  True

Le livre : [[0, 0, 0, 0, 0, 0], 'Abel +35', [71, 15, 6, 8, 29, 7], 'Bob -77', [50, 11, 6, 22, 78, 93], 'Camille -25', [38, 2, 30, 15, 18, 81]]

le hachage est  [0, 0, 3, 37, 23, 71]  avec la preuve [38, 2, 30, 15, 18, 81]

la liste  [50, 11, 6, 22, 78, 93, 0, 67, 97, 9, 5, 8, 8, 1, 32, 45, 50, 53]  et le hachage de cette liste + preuve [38, 2, 30, 15, 18, 81] est : [0, 0, 3, 37, 23, 71]

la verification est  True

