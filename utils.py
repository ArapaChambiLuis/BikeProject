from reportlab.pdfgen import canvas

c=canvas.Canvas("Equipo5.pdf")
c.drawString(150,200,"lo que sea")
c.save()