import json, math
R=6371000
def hav(a,b):
    (lo1,la1),(lo2,la2)=a,b
    p1,p2=math.radians(la1),math.radians(la2);dp=p2-p1;dl=math.radians(lo2-lo1)
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(h))
river=[(79.7618,13.0214),(79.790,13.030),(79.8139,13.0400),(79.8418,13.0560),(79.852,13.080),(79.8602,13.0968),
 (79.885,13.100),(79.910,13.098),(79.935,13.097),(79.9614,13.1000),(79.990,13.100),(80.020,13.098),(80.050,13.097),
 (80.075,13.095),(80.098,13.091),(80.118,13.078),(80.140,13.072),(80.160,13.070),(80.185,13.066),(80.2008,13.0668),
 (80.212,13.0715),(80.225,13.0738),(80.236,13.0740),(80.2438,13.0719),(80.252,13.0700),(80.258,13.0695),(80.263,13.0675),
 (80.2690,13.0684),(80.2720,13.0705),(80.2750,13.0724),(80.2790,13.0712),(80.2820,13.0700),(80.2845,13.0689),(80.2890,13.0665)]
cum=[0]
for i in range(1,len(river)): cum.append(cum[-1]+hav(river[i-1],river[i]))
L=cum[-1]
def at(d):
    d=max(0,min(L,d))
    for i in range(1,len(river)):
        if cum[i]>=d:
            t=(d-cum[i-1])/(cum[i]-cum[i-1] or 1);a,b=river[i-1],river[i]
            return (round(a[0]+(b[0]-a[0])*t,5),round(a[1]+(b[1]-a[1])*t,5))
    return river[-1]
def dist_of(pt):
    best=(1e18,0)
    for k in range(0,int(L),25):
        q=at(k);dd=hav(q,pt)
        if dd<best[0]: best=(dd,k)
    return best[1]
def seg(d0,d1):
    pts=[at(d0)]+[p for p,c in zip(river,cum) if d0<c<d1]+[at(d1)]
    return [list(p) for p in pts]
F=[]
def add(kind,geom,coords,name,data,note,source="",src_url="",**kw):
    p=dict(layer=kind,name=name,data=data,note=note,source=source,source_url=src_url);p.update(kw)
    F.append({"type":"Feature","properties":p,"geometry":{"type":geom,"coordinates":coords}})
EST="Estimated"; SRC="Sourced"; PROP="Proposal (this project)"
CRRT="https://crrt.tn.gov.in/cooum_restoration"
DPR="https://www.dtnext.in/news/chennai/government-seeks-dpr-for-37-km-cooum-riverfront-development"
DAMS="https://www.inkl.com/news/heavy-rainfall-fills-check-dams-across-cooum-helps-clean-polluted-stretch"
PUD="https://www.dtnext.in/amp/story/news/tamilnadu/unpolluted-part-of-cooum-to-get-5th-check-dam"
SOR="https://wrd.tn.gov.in/wp-content/uploads/2024/09/SPID-1321-G.O-2D-No.12-WR-S1-Dept-dated-23.02.2022-1.pdf"
TW="https://www.inkl.com/news/plan-to-build-training-wall-at-mouth-of-cooum-to-prevent-sand-bar"
WB="https://blogs.worldbank.org/en/endpovertyinsouthasia/chennai-becomes-first-indian-city-recycle-wastewater-scale"
IAM="https://iamwarm.gov.in/IAMWARM/OLD/dpr-pdf/PhaseIV/Cooum.pdf"
add("river","LineString",[list(p) for p in river],"Cooum River, Kesavaram anicut to the sea",EST,
 f"Hand-traced through geocoded towns and bridges, about {L/1000:.0f} km here (official length about 65 km). Follows the real course only roughly; trace from OpenStreetMap before engineering use.","CRRT (length), Mapbox geocoding (waypoints)",CRRT)
d_par=dist_of((80.098,13.091))
add("restoration","LineString",seg(d_par,L),"Official restoration stretch: Paruthipattu to the mouth (32 km)",SRC,
 "Extent is from CRRT; the line uses the approximate trace.","CRRT",CRRT)
d_nap=dist_of((80.2845,13.0689)); d_per=dist_of((80.2750,13.0724)); d_dams=dist_of((80.2690,13.0684))
add("pilot","LineString",seg(d_nap,L),"Pilot stretch 1: Napier Bridge to river mouth (0.5 km)",SRC,"End points from the DPR tender news; line drawn on the approximate trace.","DT Next, Oct 2026",DPR)
add("pilot","LineString",seg(d_per,d_per+1200),"Pilot stretch 2: Periyar Bridge to Swami Sivananda Salai (1.2 km)",EST,"Named in the DPR tender; where Sivananda Salai meets the river is estimated (1.2 km below Periyar Bridge).","DT Next, Oct 2026",DPR)
add("pilot","LineString",seg(d_dams-2000,d_dams),"Pilot stretch 3: Link Road to Dams Road (2 km)",EST,"Named in the DPR tender; Dams Road end placed at the Anna Salai bridge, Link Road end estimated 2 km upstream.","DT Next, Oct 2026",DPR)
add("landmark","Point",[79.7618,13.0214],"Kesavaram anicut (source of the Cooum)",SRC,"Mapbox lists this as 'Pudu Kesavaram Dam', Arakkonam. Taken as the anicut where the Cooum leaves the Kosasthalaiyar; confirm on site.","Mapbox Search")
for n,c in [("Napier Bridge",[80.28449,13.06889]),("Periyar Bridge",[80.27503,13.07237]),("Anna Salai (Mount Road) bridge, Dams Road",[80.26902,13.06838])]:
    add("landmark","Point",c,n,SRC,"Bridge position from Mapbox.","Mapbox Search")
add("landmark","Point",[80.2890,13.0665],"River mouth at Marina (sand bar forms here)",EST,"Mouth closes with sand most of the year; dredged repeatedly.","IIT Madras Tech Talk","https://tech-talk.iitm.ac.in/?p=1154")
add("koyambedu","Point",[80.20076,13.06740],"Koyambedu treatment plant: 45 MLD tertiary (TTRO) water",SRC,
 "Less than 20 MLD of 45 MLD is used today. Releasing spare water as year-round base flow (~580 mcft a year) keeps the river moving and the mouth open. Plant pin from Mapbox.","World Bank; Citizen Matters",WB)
add("koyambedu","LineString",[[80.20076,13.06740],[80.2008,13.0668]],"Proposed treated-water outfall to river",PROP,"Short release pipe; route not surveyed.","Project research 02")
dams=[("Pudumavilangai check dam (existing)",(79.876,13.0985),"2.3 m high, 100 m wide, ₹7.8 cr; irrigates Kadambathur, Satharai, Agaram.",PUD),
 ("Putlur check dam (existing)",(79.945,13.0975),"One of five existing dams that held at least 130 mcft after a good monsoon.",DAMS),
 ("Paruthipattu check dam (existing)",(80.098,13.091),"Upstream end of the 32 km restoration stretch.",CRRT)]
for n,c,note,u in dams:
    add("checkdam","Point",list(c),n,EST,note+" Position estimated near the named village. Proposal: add adjustable shutters (₹0.5 to 1.5 cr each, +30 to 50% storage).","News / WRD",u,status="existing")
add("checkdam","Point",[80.020,13.0980],"Soranjeri check dam (sanctioned 2022, ₹5.62 cr)",EST,"Sanctioned by WRD G.O. 12 (2022). Site position not public; placed on the river between Aranvoyal and Paruthipattu.","WRD G.O. 12",SOR,status="proposed")
add("checkdam","Point",[79.83,13.048],"New shuttered check dam (candidate)",PROP,"Candidate for 2 to 3 more shuttered dams in years 1 to 3, near farm tanks.","Project research 02",status="proposed")
add("checkdam","Point",[79.99,13.1],"New shuttered check dam (candidate)",PROP,"Candidate site, as above.","Project research 02",status="proposed")
add("tanks","Polygon",[[[79.74,13.00],[79.80,12.985],[79.90,13.03],[80.00,13.06],[80.06,13.07],[80.06,13.13],[79.98,13.145],[79.88,13.135],[79.80,13.11],[79.745,13.07],[79.74,13.00]]],
 "Upper-zone irrigation tank cluster (~80 tanks, ~9,940 ha)",EST,"80 tanks with ~9,940 ha registered farmland in the sub-basin; 61 rural tanks irrigate ~6,630 ha in Kancheepuram, Thiruvallur and Vellore blocks. Outline is a rough zone, not individual tanks.","IAMWARM Cooum DPR",IAM)
# training walls
add("training","LineString",[[80.2884,13.0678],[80.2908,13.0680]],"North training wall (proposed, 265 m)",EST,"WRD plan with NIOT design, about ₹70 cr for both walls. Needs CRZ clearance, ~18 months. Alignment drawn schematically.","The Hindu via inkl",TW)
add("training","LineString",[[80.2884,13.0652],[80.2912,13.0654]],"South training wall (proposed, 310 m)",EST,"As above. Get the angle and height right: earlier Cooum walls failed.","The Hindu via inkl",TW)
# weirs, docks, shops, solar
weirs=[((80.2438,13.0719),"Chetpet"),((80.225,13.0738),"Aminjikarai"),((80.2008,13.0668),"Koyambedu")]
for c,n in weirs:
    add("weir","Point",list(at(dist_of(c))),f"Boating weir candidate: {n}",PROP,"Inflatable rubber or gated weir, 1 to 1.5 m, ₹10 to 30 cr; lies flat in floods. Build only after clean base flow exists.","Project research 02")
docks=[(80.2865,13.0678),(80.2750,13.0724),(80.2690,13.0684),(80.2438,13.0719),(80.225,13.0738),(80.2008,13.0668)]
for i,c in enumerate(docks,1):
    add("dock","Point",list(at(dist_of(c)+120)),f"Cleaning-robot dock {i}",PROP,"Charging and trash-offload point for river-cleaning robots and boats; placed beside bridges and weirs for road access.","Project research 01")
shops=[(80.2845,13.0689,"Napier Bridge entrance"),(80.2750,13.0724,"Periyar Bridge"),(80.2690,13.0684,"Anna Salai bridge"),(80.263,13.0675,"Pudupet small bridge"),
 (80.252,13.0700,"Egmore entrance"),(80.2438,13.0719,"Chetpet bridge"),(80.236,13.0740,"Shenoy Nagar entrance"),(80.225,13.0738,"Aminjikarai bridge"),
 (80.212,13.0715,"Arumbakkam entrance"),(80.185,13.066,"Maduravoyal entrance")]
for x,y,n in shops:
    add("shop","Point",list(at(dist_of((x,y))-150)),f"Leased shop cluster: {n}",PROP,"Free walk, paid shops. Model: 20 entrances × 10 shops + 15 bridges × 6 shops (~290 shops, 200 sq ft, ₹60 to 150 per sq ft a month).","Project research 01")
def offset(line,dy):
    return [[p[0],round(p[1]+dy,5)] for p in line]
d_koy=dist_of((80.2008,13.0668))
for a,b in [(d_koy,d_koy+5000),(d_koy+5500,d_dams-200)]:
    s=seg(a,b); add("solar","LineString",offset(s,0.0007),"Bank-top solar strip (north bank)",PROP,"About 10 MWp across ~10 km of banks, ~14 GWh a year, ~₹55 cr. Panels on banks and walkway canopies, never on the channel.","Project research 02")
    add("solar","LineString",offset(s,-0.0007),"Bank-top solar strip (south bank)",PROP,"As above.","Project research 02")
# illustrative outfalls
n=0
d=d_par
while d<L-300:
    n+=1; add("outfall","Point",list(at(d)),f"Sewage outfall marker {n} (illustrative)",EST,"118 outfalls found in 2014; 41 plugged by Nov 2025. Exact positions are not public, so these markers only show spread along the 32 km stretch, about one per 1.1 km.","Project brief")
    d+=1100
coast=[[80.300,13.16],[80.296,13.12],[80.293,13.10],[80.2905,13.08],[80.289,13.066],[80.2865,13.045],[80.284,13.02],[80.281,12.98]]
fc={"type":"FeatureCollection","properties":{"title":"Project Cooum river transformation model","built":"2026-11-25"},"features":F}
json.dump(fc,open('../data/cooum-river-model.geojson','w'),ensure_ascii=False,indent=0)
weather=[["25 Nov",2.9,100],["26 Nov",1.3,47],["27 Nov",7.1,100],["28 Nov",10.3,100],["29 Nov",0.1,11],["30 Nov",0.1,0],["1 Dec",0.5,31]]
html=open('template.html').read().replace('__DATA__',json.dumps(fc,ensure_ascii=False).replace('</','<\\/')).replace('__COAST__',json.dumps(coast)).replace('__WX__',json.dumps(weather)).replace('__N__',str(n)).replace('__LEN__',f"{L/1000:.0f}")
open('offline-svg-map.html','w').write(html)
print(len(F),n,round(L))
