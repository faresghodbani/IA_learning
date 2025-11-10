from apyori import apriori
import time

f = open('corpus.txt', 'r', encoding="utf-8")

def normalize(text):
    return text.strip('\n').replace("!", "").replace("?", "").replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("-", "")

stopwords = {'the', 'a', 'of', 'for', 'in', 'and', 'de', 'et', 'pour'}

transactions = []
for line in f:
    if len(line) > 1 and not line.startswith("#"):
        words = normalize(line.lower()).split()
        items = set()
        for word in words:
            if word not in stopwords:
                items.add(word)
        if len(items) != 0:
            transactions.append(sorted(items))

f.close()

start_time = time.time()
results = list(apriori(transactions, min_support=0.01, min_confidence=0.7, min_lift=1.2, min_length=2))
temps_exec = time.time() - start_time

output = open("resultats_apriori.txt", "w", encoding="utf-8-sig")
output.write("Introduction à l’Intelligence Artificielle\n")
output.write("TD5 : Règles d’association\n\n")
output.write(f"Temps d'exécution : {temps_exec:.4f} secondes\n\n")

for rule in results:
    for stat in rule.ordered_statistics:
        if stat.items_base and stat.items_add:
            output.write(f"Règle : {set(stat.items_base)} => {set(stat.items_add)}\n")
            output.write(f"Support : {rule.support}\n")
            output.write(f"Confiance : {stat.confidence}\n")
            output.write(f"Lift : {stat.lift}\n")
            output.write("------\n\n")

output.close()