import json

with open('translations.js', 'r', encoding='utf-8') as f:
    js_text = f.read()

json_text = js_text.split('const translations = ')[1]
if json_text.endswith(';\n'): json_text = json_text[:-2]
if json_text.endswith(';'): json_text = json_text[:-1]

data = json.loads(json_text)

# Provide our new translations for "hero_desc"
data['ar']['hero_desc'] = "في جوهر عملنا يكمن الالتزام بالموثوقية والأداء. نحن نتحمل مسؤولية كل عملية نديرها، لضمان أن يعكس كل تفاعل الاحترافية ويضيف قيمة لعملك."
data['fr']['hero_desc'] = "Au cœur de notre travail se trouve un engagement envers la fiabilité et la performance. Nous assumons la responsabilité de chaque processus que nous gérons, en veillant à ce que chaque interaction reflète notre professionnalisme et ajoute de la valeur à votre entreprise."
data['de']['hero_desc'] = "Im Mittelpunkt unserer Arbeit steht das Engagement für Zuverlässigkeit und Leistung. Wir übernehmen die Verantwortung für jeden von uns verwalteten Prozess und stellen sicher, dass jede Interaktion Professionalität widerspiegelt und Ihrem Unternehmen einen Mehrwert bringt."
data['es']['hero_desc'] = "En el núcleo de nuestro trabajo se encuentra el compromiso con la confiabilidad y el rendimiento. Asumimos la responsabilidad de cada proceso que gestionamos, asegurando que cada interacción refleje profesionalismo y agregue valor a su empresa."

with open('translations.js', 'w', encoding='utf-8') as f:
    f.write('const translations = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n')

print("Translations updated!")
