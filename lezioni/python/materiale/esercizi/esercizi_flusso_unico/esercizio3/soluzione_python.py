eta = 22
ha_patente = True

maggiorenne = eta >= 18
ha_sconto = (eta < 18) or (eta >= 65)
accesso_vip = maggiorenne and ha_patente
sprovvisto_documento = not ha_patente

print("È maggiorenne?:", maggiorenne)
print("Ha diritto allo sconto?:", ha_sconto)
print("Può accedere all'area VIP?:", accesso_vip)
print("È sprovvisto di documento?:", sprovvisto_documento)