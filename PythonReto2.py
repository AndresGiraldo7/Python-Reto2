def facturas(opcion:int, idCliente:int=0, idContrato:int=0, pago:float=0, db:dict={})->dict:
    porCobrar = 0


    if opcion == 3:
        return {'db': 'estado de contratos'}, db

    if opcion == 0 and not (idCliente in db.keys()) and pago == 0:
        db[idCliente] = {}
        return {f'{idCliente}': 'Cliente creado'}, db

    elif idCliente in db.keys():
        if opcion ==  1:
            db[idCliente][idContrato] = pago
            return "{"+f"'cliente': {idCliente}, 'contrato': {idContrato}, 'abono': 0, 'valor': {pago}"+"}", db
        if opcion == 2 and (idContrato in db[idCliente].keys()):
            porCobrar = db[idCliente][idContrato] - pago
            if pago == db[idCliente][idContrato]:
                db[idCliente].pop(idContrato)
                return "{"+f"'cliente': {idCliente}, 'contrato': {idContrato}, 'abono': {pago}, 'valor': {porCobrar}"+"}", db
            else:
                db[idCliente][idContrato] = porCobrar
            return "{"+f"'cliente': {idCliente}, 'contrato': {idContrato}, 'abono': {pago}, 'valor': {porCobrar}"+"}", db
        else:
            return {f'{idContrato}': 'No existe la contrato'}, db
    else:
        return {f'{idCliente}': 'No existe el cliente'}, db

msj , dbFacturas = facturas (0,
2541)
print (msj , dbFacturas )
msj , dbFacturas = facturas (1,
2541 , 1, 300000 , db=
dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (2,
2541 , 1, 25000.25487 , db
= dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (1,
2541 , 2, 500000 , db=
dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (2,
1429 , 5, 25000.25487 , db
= dbFacturas )