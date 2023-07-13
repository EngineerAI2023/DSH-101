# TODO Найдите количество книг, которое можно разместить на дискете
symbols_ = 25
stroka = 50
stranica = 100
inf_objem = 1.44 * 1024 *1024
objem_kniga = 4* 25 * 50 * 100
print("Количество книг, помещающихся на дискету:", round(inf_objem//objem_kniga))
