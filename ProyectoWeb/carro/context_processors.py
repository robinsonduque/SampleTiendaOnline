def totalProductos(request):
    total = 0
    if request.user.is_authenticated:
        try:
            for key, value in request.session["carro"].items():
                total = total + (float(value["precio"]) * value["cantidad"])
        except:
            request.session["carro"]={}
    return {"totalProductos": total}
 