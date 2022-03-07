import justpy as jp

def app() :
    wp = jp.QuasarPage()

    divider = jp.QDiv(a = wp, classes = "q-pa-sm")
    h1 = jp.QDiv(a = wp, text = "Analysis of Course Reviews", classes = "text-h3 text-center")
    divider = jp.QDiv(a = wp, classes = "q-pa-sm")
    p1 = jp.QDiv(a = wp, text = "These graphs represent course review analysis", classes = "text-h5 text-center")
    divider = jp.QDiv(a = wp, classes = "q-pa-l")

    return wp

jp.justpy(app)