with open('career.html', 'r', encoding='utf-8') as f: text = f.read()
replacements = {
    'high-tempo': 'high tempo',
    'high-performance': 'high performance',
    'high-performing': 'high performing',
    'performance-linked': 'performance linked',
    'cross-cultural': 'cross cultural',
    'high-level': 'high level',
    'real-world': 'real world',
    'senior-instructor-led': 'senior instructor led',
    'industry-leading': 'industry leading',
    'world-class': 'world class',
    'high-impact': 'high impact',
    'high-volume': 'high volume',
    'high-stakes': 'high stakes',
    'client-facing': 'client facing',
    '—': ' ',
    '–': ' '
}
for k, v in replacements.items(): text = text.replace(k, v)
with open('career.html', 'w', encoding='utf-8') as f: f.write(text)
