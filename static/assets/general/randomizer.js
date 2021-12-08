const hexCode = () => {
    const x = Math.floor(Math.random()*16777215).toString(16);
    const y = "#" + x;

    var bgColors=new Array("#AAAAA", "#FFFFF", "#DDDFFF", "#CCCCCC", "#333333", "#FFCC11", "#FFFFFF", "#DDDD00x")

    document.body.style.background=bgColors[Math.floor(Math.random()*bgColors.length)]
}
genNew.addEventListener("click", setBg);
setBg();