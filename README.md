# Corso di commercio elettronico #

Questo progetto contiene i file python richiesti dal professor Silvestri durante il corso di Commercio Elettronico a Informatica Ca'Foscari, as2014-2015.
Per uso strettamente personale

### Prima consegna ###

Lo scopo di questa esercitazione è la creazione di una collezione di documenti di testo a partire da un insieme di pagine web di interesse.

* scegliere un sito web
* ricerca su Google limitata ad un sito (es: "site:www.ansa.it parlamento")
* parsing dei risultati per trovare gli url delle pagine trovate (attenzione: ci sono anche altri link da non considerare come quelli alla copia in cache).
* get delle pagine individuate (salvare su file e non scaricare nuovamente se esiste già)
* parsing e salvataggio di testo ed eventuali attributi delle pagine
* creare il lessico, aggiornare un contatore delle occorrenze di ciascun termine (totali e numero di documenti distinti). Ordinare per frequenza descrescente, esportare i dati e tracciare dei grafici (x:rank, y: frequenza) utilizzando sia scale lineari che logaritmiche.

===========================

GRUPPI: 1-2 persone, relazioni individuali. Ogni persona deve utilizzare parole diverse per la ricerca delle pagine.
Suggerimento: disabilitare Javascript sul browser e guardare il contenuto del risultato di una ricerca
Consegnare (entro fine ottobre): codice sorgente, relazione individuale di una pagina (max 2) con grafici e commenti

===========================

Utilizzo di LaTeX ed R per costruire la documentazione in modo dinamico dal file di output


### Seconda consegna ###

Content based recommender:

* costruire il vector space model per la collezione di testi create nelle scorse lezioni (oppure utilizzare i testi delle notizie Ansa resi disponibili)
* cold start: scegliere un documento e trovare i documenti simili (coseno)
* warm start: scegliere alcuni documenti di vostro interesse e generare dei suggerimenti basati sui contenuti dei documenti scelti  (coseno) 
    
===========================   

suggerimenti:

* utilizzare un array associativo per gestire il lessico ed associare un codice numerico a ciascun termine
* il lessico ed il vector space model possono essere salvati e riutilizzati (sono validi fino a che non cambia il contenuto della collezione)

===========================
    
Altre attività:

* provare con una misura di distanza diversa
* utilizzare i contatore delle occorrenze di ciascun termine e numero di documenti per termine per calcolare TF/IDF
