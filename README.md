# AStar
## AI homework Páll Dávid &amp; Böjthe Róbert Zoltán

- A kezdeti állapotot két féle képpen lehet meghívni:
    - "-input {nev.txt}" == fileból beolvassa, pl: python main.py -input put_in.txt
    - "-rand {matrix mérete} {keverésben lévő lépés szám}" == egy random kezdőállapotot generál, pl: python main.py -rand 3 199
    
- A heurisztika kiválasztása kötelező a "-h" segítségével
    - "-h 1" == rossz helyen levo ̋ csempék száma
    - "-h 2" == Manhattan
    
-  "–solseq" == A standard kimenetre írja a teljes megoldási szekvenciát

- "–pcost" == A standard kimenetre írja a megoldás költségét

- "–nvisited" == A standard kimenetre írja a meglátogatott csomópontok számát

- Az üress mezőnek a 0-os érték felel meg


### Példahívás a programra: "python main.py -rand 3 199 -h 1 -solseq -pcost -nvisited"
