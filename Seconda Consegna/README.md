## Content based recommender:

* costruire il vector space model per la collezione di testi create nelle scorse lezioni (oppure utilizzare i testi delle notizie Ansa resi disponibili)
* cold start: scegliere un documento e trovare i documenti simili (coseno)
* warm start: scegliere alcuni documenti di vostro interesse e generare dei suggerimenti basati sui contenuti dei documenti scelti  (coseno) 
    
## Suggerimenti:
        
* utilizzare un array associativo per gestire il lessico ed associare un codice numerico a ciascun termine
* il lessico ed il vector space model possono essere salvati e riutilizzati (sono validi fino a che non cambia il contenuto della collezione)
    
## Altre attività (facoltative):
        
* provare con una misura di distanza diversa
* utilizzare i contatore delle occorrenze di ciascun termine e numero di documenti per termine per calcolare TF/IDF

===

Obiettivi: utilizzare le librerie scipy/numpy per il calcolo delle similarità tra documenti e gensim per gestione del corpus e topic modelling
 
## Training
 
* generare matrici e vettori casuali
* calcolare prodotti tra vettori e tra matrice e vettore (ATTENZIONE, il prodotto di due vettori deve essere un numero. Controllare il risultato!!!)
* calcolare le distanze tra due vettori utilizzando il paccehtto scipy.spatial.distance (http://docs.scipy.org/doc/scipy-0.14.0/reference/spatial.distance.html#module-scipy.spatial.distance)
* calcolare SVD per una matrice casuale 300x30
* moltiplicare le matrici ottenute e sottrarre la matrice originale dal risultato. Verificare la differenza
* seguire i tutorial di gensim
 
## Esercitazione
 
* modificare l'esercitazione 2 utilizzando le funzioni di distanza di numpy
* (utilizzando la libreria GenSim) trovare, per diversi valori di K, i K topic principali nei documenti estratti per l'esercitazione 1
* confrontare i risultati della ricerca per similarità con quelli ottenuti nell'esercitazione 2 (o nel punto I)
 
===

## Consegnare al prof

Al termine della prima esercitazione consegnare:

* file sorgenti (zip oppure tar.gz)
* relazione contenente:
    * descrizione sintetica del procedimento seguito
    * confronto dei risultati (parte iniziale lista suggerimenti) ottenuti con i diversi metodi 
    * confronto dei tempi di esecuzione
