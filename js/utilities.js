function GeneraTitoli(nomiCartelle){
    let split = nomiCartelle.split("_");
    let titolo = "";
    for (let i = 1; i < split.length; i++) {
        titolo += split[i];
        if(i != split.length - 1)
            titolo += " ";
    }
    return titolo.toUpperCase();
}