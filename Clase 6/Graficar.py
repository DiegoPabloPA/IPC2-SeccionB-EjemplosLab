import os
class Graphviz:
    def Inicio(title,code):
        return """
            digraph  grafi{key}
                label=\"{tit}\";
                

                {body}

                {close}
        """.format(key='{',tit=title,body=code,close="}")
    
    def StartTable(border,cellspacing,cellpadding,code):
        return """
        <TABLE border=\"{opc1}\" cellspacing=\"{opc2}\" cellpadding=\"{opc3}\">
        {body}
        </TABLE>
        """.format(opc1=border,opc2=cellspacing,opc3=cellpadding,body=code)
    
    def NewRow(body):
        return """
        <TR>
            {columns}
        </TR>
        """.format(columns=body)
    def NewColumn(background,info):
        return """
        <TD bgcolor=\"{colorcell}\">
        {text}
        </TD>
        """.format(colorcell=background,text=info)


    def NodePerTable(id,tablestring):
        return """
        {ident}[shape=none label=<{table}>];
        """.format(ident=id,table=tablestring)

class GeneradorGrafico:
    def Graficar(Informacion):
        cabecera=""
        for muestra in Informacion['ListaEspecimenes']:
            temporal=Graphviz.NewColumn('#FFFFFF',muestra.nombre)
            temporal+=Graphviz.NewColumn(muestra.color,'')
            cabecera+=Graphviz.NewRow(temporal)
       

        cabecera=Graphviz.NodePerTable('colores',Graphviz.StartTable('1','1','2',cabecera))
        

        for matriz in Informacion['ListaMatrices']:
            code=cabecera+matriz['matriz'].GraficarMatriz()
            code=Graphviz.Inicio("Ejemplo",code)

            archie=open("./generado.dot","w")
            archie.write(code)
            archie.close()
            os.system("dot -Tpdf generado.dot -o ejemplo.pdf")
            os.system("Ejemplo.pdf")
    