"""Builds capacity_toolkit.xlsx. Run: python build_toolkit.py"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
wb=Workbook()
F=lambda **k: Font(name="Arial", size=10, **k)
H=Font(name="Arial", size=11, bold=True, color="002D5C")
INP=Font(name="Arial", size=10, color="0000FF")
YEL=PatternFill("solid", fgColor="FFFF00")
GREY=PatternFill("solid", fgColor="F2F2F2")
def hdr(ws, r, vals):
    for i,v in enumerate(vals):
        c=ws.cell(row=r, column=i+1, value=v); c.font=H; c.fill=GREY; c.alignment=Alignment(wrap_text=True, vertical="top")
def note(ws, r, text, col=1):
    c=ws.cell(row=r, column=col, value=text); c.font=Font(name="Arial", size=9, italic=True, color="666666"); c.alignment=Alignment(wrap_text=True, vertical="top")
def inp(ws,r,c,v): x=ws.cell(row=r,column=c,value=v); x.font=INP; x.fill=YEL; return x
def lab(ws,r,c,v,bold=False,grey=False):
    x=ws.cell(row=r,column=c,value=v); x.font=F(bold=bold, color="666666" if grey else None) if grey or bold else F(); return x

ws=wb.active; ws.title="Unit prices"
ws["A1"]="The Tradeoff Method: capacity toolkit"; ws["A1"].font=Font(name="Arial", size=14, bold=True, color="002D5C")
ws["A2"]="Unit prices and per-node capacities. Blue cells are inputs; edit them when cloud pricing moves (checked September 2026). Every other tab reads from here."; ws["A2"].font=F(italic=True)
hdr(ws,4,["Item","Value","Unit","Source / note"])
rows=[
("DAY_S","Seconds in a day (the book rounds 86,400 to 10^5)",100000,"s","Chapter 4, seven habits"),
("OBJ","Object storage, standard",20,"$ per TB-month","Appendix A.4; public list prices, Sept 2026"),
("OBJC","Object storage, cold tier",6,"$ per TB-month","Appendix A.4"),
("BLK","Block storage attached to a node",90,"$ per TB-month","Appendix A.4"),
("MEM","Memory in a managed cache",8,"$ per GB-month","Appendix A.4"),
("VCPU","Virtual CPU",0.04,"$ per hour","Appendix A.4"),
("SRV","Small always-on server",100,"$ per month","Appendix A.4"),
("DBM","Managed database node, mid-sized",500,"$ per month","Appendix A.4 (a few hundred)"),
("DBL","Managed database node, large",3000,"$ per month","Appendix A.4 (a few thousand)"),
("EGR","Egress to the internet, list",0.05,"$ per GB","Appendix A.4; the book uses the low end"),
("CDN","Egress through a CDN, negotiated",0.02,"$ per GB","Appendix A.4"),
("XR","Traffic between regions",0.015,"$ per GB","Appendix A.4"),
("TOKIN","Language model, input tokens",3,"$ per million","Appendix A.4; varies widely"),
("TOKOUT","Language model, output tokens",15,"$ per million","Appendix A.4"),
("EMB","Embedding model",0.10,"$ per million tokens","Appendix A.4"),
("ENG","Fully loaded engineer",100,"$ per hour","Appendix A.4; conventional planning figure"),
("APP","Application server, simple requests",30000,"per second per node","Appendix A.2"),
("RDBR","Relational node, point reads",12000,"per second per node","Appendix A.2"),
("RDBW","Relational node, random writes (B-tree)",20000,"per second per node","Appendix A.2"),
("LSM","Wide-column / key-value node, appends (LSM)",100000,"per second per node","Appendix A.2"),
("KV","In-memory store, operations",300000,"per second per node","Appendix A.2"),
("DISK","Usable disk of a database node",4,"TB per node","Appendix A.3"),
("RTTDC","Round trip within a data centre",0.8,"ms","Appendix A.1"),
("RTTC","Round trip, same continent",35,"ms","Appendix A.1"),
("RTTO","Round trip, across an ocean",120,"ms","Appendix A.1"),
]
N={}
for i,(k,label,val,unit,src) in enumerate(rows):
    r=5+i; lab(ws,r,1,label); inp(ws,r,2,val); lab(ws,r,3,unit); lab(ws,r,4,src,grey=True); N[k]=f"'Unit prices'!$B${r}"
for col,w in zip("ABCD",(44,12,22,46)): ws.column_dimensions[col].width=w

ws=wb.create_sheet("Envelope")
ws["A1"]="Envelope: rate, stored, moved, cost"; ws["A1"].font=H
ws["A2"]="Fill the blue cells for your brief. The example values are the notification service of Chapters 3 and 4; replace them."; ws["A2"].font=F(italic=True)
hdr(ws,4,["Input","Value","Unit","Note"])
inputs=[("Daily active users",20000000,"users"),("Actions per user per day",5,"actions"),("Peak multiple over average",5,"x"),
        ("Bytes per event stored",200,"bytes"),("Retention",30,"days"),("Replicas",1,"copies"),
        ("Bytes returned per request",1000,"bytes"),("Burst: total events",20000000,"events"),("Burst: window",600,"seconds")]
for i,(l,v,u) in enumerate(inputs):
    r=5+i; lab(ws,r,1,l); inp(ws,r,2,v); lab(ws,r,3,u)
hdr(ws,15,["Output","Value","Unit","Formula reads"])
out=[
("Average rate","=B5*B6/"+N["DAY_S"],"per second","users x actions / 10^5"),
("Peak rate","=B16*B7","per second","average x peak multiple"),
("Burst rate","=B12/B13","per second","burst total / window"),
("Events per day","=B5*B6","events",""),
("Stored at end of retention","=B19*B8*B9*B10/1E12","TB","events/day x bytes x days x replicas"),
("Storage cost, object","=B20*"+N["OBJ"],"$ per month","TB x object price"),
("Storage cost, block","=B20*"+N["BLK"],"$ per month","TB x block price"),
("Nodes by disk","=CEILING(B20/"+N["DISK"]+",1)","nodes","TB / usable disk per node"),
("Moved out, average","=B16*B11","bytes per second","rate x bytes returned"),
("Moved out per day","=B24*"+N["DAY_S"]+"/1E9","GB per day",""),
("Egress per day, list","=B25*"+N["EGR"],"$ per day",""),
("Egress per day, CDN","=B25*"+N["CDN"],"$ per day",""),
("Relational nodes for peak writes","=CEILING(B17/"+N["RDBW"]+",1)","nodes","peak / writes per node"),
("LSM nodes for peak appends","=CEILING(B17/"+N["LSM"]+",1)","nodes",""),
("In-memory nodes for peak ops","=CEILING(B17/"+N["KV"]+",1)","nodes",""),
]
for i,(l,f,u,n) in enumerate(out):
    r=16+i; lab(ws,r,1,l); c=ws.cell(row=r,column=2,value=f); c.font=F(); c.number_format='#,##0.###'; lab(ws,r,3,u); lab(ws,r,4,n,grey=True)
note(ws,32,"Binds: compare each output to the per-node figures on the Unit prices tab; the line closest to or beyond one node's capacity is the one that sets the design (Chapter 4).")
for col,w in zip("ABCD",(34,18,18,40)): ws.column_dimensions[col].width=w

ws=wb.create_sheet("Latency budget")
ws["A1"]="Latency budget splitter and fan-out tail"; ws["A1"].font=H
ws["A2"]="Enter the total budget and the hops in sequence. Headroom is what is left for the tail. The example is Chapter 4's 200 ms page."; ws["A2"].font=F(italic=True)
lab(ws,4,1,"Total budget (ms)"); inp(ws,4,2,200)
hdr(ws,6,["Hop (sequential)","ms","Note"])
hops=[("User's network to the edge",35,"outside your control; 20-50 ms"),("Application server work",10,""),("Cache",1,""),("Database on a miss",10,""),("Downstream service",50,"the largest item; a second sequential call breaks the budget"),("",0,""),("",0,"")]
for i,(l,v,n) in enumerate(hops):
    r=7+i; inp(ws,r,1,l); inp(ws,r,2,v); lab(ws,r,3,n,grey=True)
lab(ws,15,1,"Allocated (ms)",bold=True); ws["B15"]="=SUM(B7:B13)"
lab(ws,16,1,"Headroom for the tail (ms)",bold=True); ws["B16"]="=B4-B15"
lab(ws,17,1,"Largest hop (ms)",bold=True); ws["B17"]="=MAX(B7:B13)"
lab(ws,18,1,"A second sequential call to the largest hop breaks the budget?",bold=True); ws["B18"]='=IF(B15+B17>B4,"yes: make it parallel","no")'
ws["A21"]="Fan-out tail"; ws["A21"].font=H
lab(ws,22,1,"Services called in parallel (n)"); inp(ws,22,2,10)
lab(ws,23,1,"Chance each is slow"); inp(ws,23,2,0.01).number_format="0.0%"
lab(ws,24,1,"Chance the whole request is slow: 1-(1-p)^n",bold=True); ws["B24"]="=1-(1-B23)^B22"; ws["B24"].number_format="0.0%"
ws["A26"]="Chain availability"; ws["A26"].font=H
lab(ws,27,1,"Components in a synchronous chain"); inp(ws,27,2,5)
lab(ws,28,1,"Availability of each"); inp(ws,28,2,0.999).number_format="0.000%"
lab(ws,29,1,"Availability of the chain",bold=True); ws["B29"]="=B28^B27"; ws["B29"].number_format="0.000%"
for col,w in zip("ABC",(52,22,48)): ws.column_dimensions[col].width=w

ws=wb.create_sheet("Cost per thousand")
ws["A1"]="Cost per thousand requests, and the people line"; ws["A1"].font=H
ws["A2"]="The example is Chapter 4's thumbnail service: 50 ms of CPU, a 20 KB image kept a year, served once."; ws["A2"].font=F(italic=True)
hdr(ws,4,["Input","Value","Unit"])
cin=[("CPU per request",50,"ms"),("Bytes stored per request",20000,"bytes"),("Retention",12,"months"),("Bytes returned per request",20000,"bytes"),("Served through a CDN? (1 yes, 0 no)",0,"flag")]
for i,(l,v,u) in enumerate(cin):
    r=5+i; lab(ws,r,1,l); inp(ws,r,2,v); lab(ws,r,3,u)
hdr(ws,11,["Term","$ per 1,000 requests","Reads"])
terms=[("Compute","=B5/1000/3600*"+N["VCPU"]+"*1000","CPU seconds x vCPU price"),
       ("Storage","=B6/1E12*"+N["OBJ"]+"*B7*1000","bytes x object price x months"),
       ("Egress","=B8/1E9*IF(B9=1,"+N["CDN"]+","+N["EGR"]+")*1000","bytes x egress price")]
for i,(l,f,n) in enumerate(terms):
    r=12+i; lab(ws,r,1,l); c=ws.cell(row=r,column=2,value=f); c.number_format='$#,##0.0000'; lab(ws,r,3,n,grey=True)
lab(ws,15,1,"Total",bold=True); ws["B15"]="=SUM(B12:B14)"; ws["B15"].number_format='$#,##0.0000'
lab(ws,16,1,"Dominant term",bold=True); ws["B16"]='=INDEX(A12:A14,MATCH(MAX(B12:B14),B12:B14,0))'
ws["A19"]="People (Chapter 11)"; ws["A19"].font=H
lab(ws,20,1,"Engineer hours a year the component consumes"); inp(ws,20,2,150)
lab(ws,21,1,"Cost per year",bold=True); ws["B21"]="=B20*"+N["ENG"]; ws["B21"].number_format='$#,##0'
lab(ws,22,1,"Cost per month",bold=True); ws["B22"]="=B21/12"; ws["B22"].number_format='$#,##0'
note(ws,24,"Chapter 11's broker example: 150 hours a year is about $1,250 a month, against a $4,000 machine saving; the incidents are the missing term.")
for col,w in zip("ABC",(46,22,36)): ws.column_dimensions[col].width=w

ws=wb.create_sheet("Backlog")
ws["A1"]="Backlog and drain (Chapter 10)"; ws["A1"].font=H
ws["A2"]="The example is the notification burst: 33,000/s arriving for 600 s against 14,000/s of provider capacity."; ws["A2"].font=F(italic=True)
hdr(ws,4,["Input","Value","Unit"])
bin_=[("Arrival rate during the burst",33000,"per second"),("Service rate",14000,"per second"),("Burst duration",600,"seconds"),("Arrival rate after the burst",0,"per second"),("Bytes per queued item",500,"bytes"),
      ("Little's law: arrival rate",5000,"per second"),("Little's law: time each item spends inside",0.12,"seconds")]
for i,(l,v,u) in enumerate(bin_):
    r=5+i; lab(ws,r,1,l); inp(ws,r,2,v); lab(ws,r,3,u)
hdr(ws,13,["Output","Value","Unit"])
bo=[("Peak queue depth","=MAX(0,(B5-B6)*B7)","items"),("Queue storage at peak","=B14*B9/1E9","GB"),
    ("Drain time after the burst",'=IF(B6<=B8,"never: service does not exceed arrivals",B14/(B6-B8)/60)',"minutes"),
    ("Total time from burst start to empty",'=IF(B6<=B8,"never",B7/60+B16)',"minutes"),
    ("Items in the system (Little's law)","=B10*B11","items"),("Workers needed at that service time","=B10*B11","workers")]
for i,(l,f,u) in enumerate(bo):
    r=14+i; lab(ws,r,1,l,bold=True); c=ws.cell(row=r,column=2,value=f); c.number_format='#,##0.##'; lab(ws,r,3,u)
note(ws,21,"A backlog drains at the margin of service over arrivals, not at the service rate: doubling capacity does not halve the drain (Chapter 10).")
for col,w in zip("ABC",(46,26,16)): ws.column_dimensions[col].width=w
wb.save("capacity_toolkit.xlsx")
print("saved")
