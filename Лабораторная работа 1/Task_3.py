# TODO Найдите количество книг, которое можно разместить на дискете
symbols_ = 25
stroka = 50
stranica = 100
disk = 1.44
inf_objem = disk * 1024 *1024
objem_kniga = 4* symbols_ * stroka * stranica
print("Количество книг, помещающихся на дискету:", round(inf_objem//objem_kniga))
