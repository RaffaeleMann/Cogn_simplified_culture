# Diritto alla cultura e disabilità cognitiva
## L'IA generativa può supportare la comunicazione in ambito culturale?
 
> Repository del dataset e dei risultati del contributo presentato ad AItLA 2025 - XXV Congresso Internazionale dell'Associazione Italiana di Linguistica Applicata *"La semplificazione linguistica per la comunicazione: tecnologie in contesto"* - Università di Macerata (Italia), 19-21 febbraio 2025.
 
---
 
## Panoramica
 
Questo repository contiene il dataset e i risultati della valutazione di uno studio che indaga se i modelli del linguaggio di grandi dimensioni (LLM) possano supportare la comunicazione accessibile in ambito culturale.
Lo studio testa in particolare la capacità di **Claude Sonnet 3.5** e **ChatGPT-4** di semplificare descrizioni tecniche di beni culturali per persone con disabilità cognitive, mediante zero-shot prompting in lingua italiana.
Lo valutazione  combina misure linguistiche **quantitative** (leggibilità, complessità sintattica, varietà lessicale) con un'**annotazione manuale qualitativa** condotta da due linguisti esperti, raggiungendo un accordo complessivo tra annotatori del 96,56% (κ di Cohen = 0,91).
 
---
 
## Corpus
 
Il corpus è composto da **200 descrizioni tecniche in lingua italiana** (circa 7.741 parole in totale), tratte dalle schede di catalogo in formato aperto del **Catalogo Generale dei Beni Culturali** del Ministero della Cultura (MiC), relative a diverse tipologie di beni culturali.

Il dipinto raffigura un santo apostolo, a mezzo busto, con un libro in mano e tenente sotto il braccio una croce astile. La figura è barbuta e torce il collo, voltandosi all'indietro e rivolgendo lo sguardo verso l'alto. I colori sono mantenuti in tonalità piuttosto basse e soffocati dallo sporco.
 
Ciascuna descrizione è rappresentativa di un registro formale e specialistico caratterizzato da:
- costruzioni sintattiche subordinate e implicite complesse (participi, gerundi, passivi)
- terminologia di dominio (es. *a mezzo busto*, *croce astile*)
- linguaggio figurato e alta densità informativa (soffocato dallo sporco)

**Esempio di descrizione tecnica proveniente dal corpus:**
 
> Il dipinto raffigura un santo apostolo, a mezzo busto, con un libro in mano e tenente sotto il braccio una croce astile. La figura è barbuta e torce il collo, voltandosi all'indietro e rivolgendo lo sguardo verso l'alto. I colori sono mantenuti in tonalità piuttosto basse e soffocati dallo sporco.
--- 

## Metodologia
 
### Modelli  
| Modello | Sviluppatore |
|---|---|
| Claude Sonnet 3.5 | Anthropic |
| ChatGPT-4 | OpenAI |

> Modelli testati in data 07/01/2025
### Prompt
Sono stati utilizzati tre prompt zero-shot, progettati con un livello di specificità crescente:
 
| Prompt | Descrizione |
|---|---|
| **P1** | Semplifica per persone con disabilità cognitive queste descrizioni tecniche |
| **P2** | Per ogni descrizione tecnica, dammi in output una descrizione semplificata per persone con disabilità cognitive da inserire in un pannello informativo in un museo |
| **P3** | Per ogni descrizione tecnica del dominio dei beni culturali, dammi in output una descrizione semplificata per persone con disabilità cognitive da inserire in un pannello informativo in un museo mantenendo tutte le informazioni |
 
---

## Struttura del repository
 
```
.
├── dati/
│    ├── ChatGPT_P1.tsv
│    ├── ChatGPT_P2.tsv
│    ├── ChatGPT_P3.tsv
│    ├── Claude_Sonnet_P1.tsv
│    ├── Claude_Sonnet_P2.tsv
│    ├── Claude_Sonnet_P3.tsv
|    └── README.md
├── valutazione/
│    ├── P1_ChatGPT_annotazione_qualitativa.tsv
│    ├── P1_Claude_Sonnet_annotazione_qualitativa.tsv
│    ├── P2_ChatGPT_annotazione_qualitativa.tsv
│    ├── P2_Claude_Sonnet_annotazione_qualitativa.tsv
│    ├── P3_ChatGPT_annotazione_qualitativa.tsv
│    ├── P3_Claude_Sonnet_annotazione_qualitativa.tsv
|    └── README.md         
├── risultati/
│    ├── README.md 
└── README.md
```


---
 
## Licenza
 
Il dataset e i file di annotazione presenti in questo repository sono rilasciati con licenza **Creative Commons Attribution 4.0 International (CC BY 4.0)**.
 
È possibile condividere e adattare liberamente il materiale per qualsiasi scopo, a condizione di attribuire adeguata paternità, fornire un collegamento alla licenza e indicare eventuali modifiche apportate.
 
📄 [Testo completo della licenza CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it)
 
> Le schede di catalogo di origine sono tratte dal **Catalogo Generale dei Beni Culturali (MiC)**, disponibile in formato aperto. Per le condizioni d'uso specifiche della fonte originale, si rimanda al sito istituzionale del MiC.
 
---
 
## Citazione
 
Se utilizzi questo dataset o questi risultati nella tua ricerca, cita il contributo come segue:

Speranza, G., Di Buono, M. P., & Manna, R. (in press). Diritto alla cultura e  disabilità cognitiva. L'IA generativa può supportare la comunicazione in ambito  culturale? In *Atti del XXV Congresso Internazionale AItLA "La semplificazione linguistica per la comunicazione: tecnologie in contesto"*. Università di Macerata, 19-21 febbraio 2025.
