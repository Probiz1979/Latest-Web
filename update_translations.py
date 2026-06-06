import json

with open('translations.js', 'r', encoding='utf-8') as f:
    js_text = f.read()

json_text = js_text.split('const translations = ')[1]
if json_text.endswith(';\n'): json_text = json_text[:-2]
if json_text.endswith(';'): json_text = json_text[:-1]

data = json.loads(json_text)

# Define all keys to update. English is for reference (handled by HTML fallback), 
# but I need to update Arabic, French, German, Spanish.

updates = {
    # Home Page
    "hero_desc": {
        "en": "At the core of our work is a commitment to reliability and performance. We take ownership of every process we manage, ensuring that each interaction reflects professionalism and adds value to your business.",
        "ar": "في جوهر عملنا يكمن الالتزام بالموثوقية والأداء. نحن نتحمل مسؤولية كل عملية نديرها، لضمان أن يعكس كل تفاعل الاحترافية ويضيف قيمة لعملك.",
        "fr": "Au cœur de notre travail se trouve un engagement envers la fiabilité et la performance. Nous assumons la responsabilité de chaque processus que nous gérons, en veillant à ce que chaque interaction reflète notre professionnalisme et ajoute de la valeur à votre entreprise.",
        "de": "Im Mittelpunkt unserer Arbeit steht das Engagement für Zuverlässigkeit und Leistung. Wir übernehmen die Verantwortung für jeden von uns verwalteten Prozess und stellen sicher, dass jede Interaktion Professionalität widerspiegelt und Ihrem Unternehmen einen Mehrwert bringt.",
        "es": "En el núcleo de nuestro trabajo se encuentra el compromiso con la confiabilidad y el rendimiento. Asumimos la responsabilidad de cada proceso que gestionamos, asegurando que cada interacción refleje profesionalismo y agregue valor a su empresa."
    },
    # Services Page
    "t_220": {
        "en": "The services listed here represent the key areas where we have built our global expertise and capacity. Many of our strongest client engagements began with a custom brief.",
        "ar": "تمثل الخدمات المدرجة هنا المجالات الرئيسية التي بنينا فيها خبراتنا وقدراتنا العالمية. بدأت العديد من أقوى ارتباطاتنا مع العملاء بطلب مخصص.",
        "fr": "Les services répertoriés ici représentent les domaines clés dans lesquels nous avons bâti notre expertise et notre capacité mondiales. Plusieurs de nos engagements les plus solides auprès de nos clients ont débuté par une demande personnalisée.",
        "de": "Die hier aufgeführten Dienstleistungen stellen die Kernbereiche dar, in denen wir unsere globale Expertise und Kapazität aufgebaut haben. Viele unserer stärksten Kundenbeziehungen begannen mit einer individuellen Anfrage.",
        "es": "Los servicios enumerados aquí representan las áreas clave en las que hemos desarrollado nuestra experiencia y capacidad global. Muchos de nuestros compromisos más sólidos con los clientes comenzaron con una propuesta personalizada."
    },
    "t_224": {
        "en": "We manage complete outbound campaigns, inbound lead handling, follow up sequences, and appointment setting. We track everything meticulously and we report with total transparency so you always know what is working. Because we operate in several languages, we can run campaigns across diverse markets where tone and language nuance define success.",
        "ar": "نحن ندير حملات صادرة كاملة، ومعالجة للعملاء المحتملين الواردين، وتسلسلات المتابعة، وتحديد المواعيد. نحن نتتبع كل شيء بدقة ونعد التقارير بشفافية تامة حتى تعرف دائماً ما الذي يحقق نتائج. نظراً لأننا نعمل بعدة لغات، يمكننا إدارة حملات عبر أسواق متنوعة حيث تحدد نبرة الصوت وفروق اللغة الدقيقة النجاح.",
        "fr": "Nous gérons des campagnes sortantes complètes, la gestion des leads entrants, les séquences de suivi et la prise de rendez-vous. Nous suivons tout méticuleusement et nous rendons compte en toute transparence afin que vous sachiez toujours ce qui fonctionne. Comme nous opérons en plusieurs langues, nous pouvons mener des campagnes sur divers marchés où le ton et les nuances linguistiques définissent le succès.",
        "de": "Wir verwalten komplette Outbound-Kampagnen, Inbound-Lead-Handling, Follow-up-Sequenzen und Terminvereinbarungen. Wir verfolgen alles akribisch und berichten mit völliger Transparenz, damit Sie immer wissen, was funktioniert. Da wir in mehreren Sprachen operieren, können wir Kampagnen in verschiedenen Märkten durchführen, in denen Tonfall und sprachliche Nuancen über den Erfolg entscheiden.",
        "es": "Gestionamos campañas de salida completas, manejo de clientes potenciales de entrada, secuencias de seguimiento y programación de citas. Realizamos un seguimiento meticuloso de todo y reportamos con total transparencia para que siempre sepa qué está funcionando. Como operamos en varios idiomas, podemos realizar campañas en diversos mercados donde el tono y los matices del lenguaje definen el éxito."
    },
    "t_231": {
        "en": "All of our support functions are multilingual and operate globally. We serve clients who need to support their customers in several languages. This means your customers always get support in a language they understand well. We monitor feedback constantly and give you detailed reporting so you always know your service levels are meeting standards.",
        "ar": "تتميز جميع وظائف الدعم لدينا بتعدد اللغات وتعمل عالمياً. نحن نخدم العملاء الذين يحتاجون إلى دعم عملائهم بعدة لغات. وهذا يعني حصول عملائك دائماً على الدعم بلغة يفهمونها جيداً. نحن نراقب التعليقات باستمرار ونقدم لك تقارير مفصلة حتى تعرف دائماً أن مستويات الخدمة لديك تلبي المعايير.",
        "fr": "Toutes nos fonctions de support sont multilingues et opèrent à l'échelle mondiale. Nous servons des clients qui ont besoin de soutenir leurs clients en plusieurs langues. Cela signifie que vos clients bénéficient toujours d'une assistance dans une langue qu'ils comprennent bien. Nous surveillons constamment les retours et vous fournissons des rapports détaillés afin que vous sachiez toujours que vos niveaux de service répondent aux normes.",
        "de": "Alle unsere Supportfunktionen sind mehrsprachig und weltweit tätig. Wir bedienen Kunden, die ihre Kunden in mehreren Sprachen unterstützen müssen. Das bedeutet, dass Ihre Kunden immer Unterstützung in einer Sprache erhalten, die sie gut verstehen. Wir überwachen das Feedback ständig und erstellen detaillierte Berichte, damit Sie immer wissen, dass Ihr Servicestatus den Standards entspricht.",
        "es": "Todas nuestras funciones de soporte son multilingües y operan a nivel mundial. Servimos a clientes que necesitan brindar soporte a sus clientes en varios idiomas. Esto significa que sus clientes siempre reciben asistencia en un idioma que comprenden bien. Supervisamos los comentarios constantemente y le brindamos informes detallados para que siempre sepa que sus niveles de servicio cumplen con los estándares."
    },
    # Career Page
    "t_166": {
        "en": "A career at Probiz is not simply an employment arrangement. It represents an aggressively accelerated professional journey within one of the most dynamic, high performance, and culturally diverse BPO environments   surrounded by elite peers who push each other forward, mentored by experienced senior executives, and challenged daily to reach new and measurable performance standards.",
        "ar": "العمل في بروبيز ليس مجرد ترتيب توظيف. إنه يمثل رحلة مهنية متسارعة بقوة داخل واحدة من أكثر بيئات تعهيد العمليات التجارية ديناميكية وأداءً عالياً وتنوعاً ثقافياً ، محاطاً بأقران من النخبة الذين يدفعون بعضهم البعض إلى الأمام ، تحت إشراف مسؤولين تنفيذيين كبار ذوي خبرة، ويتم التحدي يومياً للوصول إلى معايير أداء جديدة وقابلة للقياس.",
        "fr": "Une carrière chez Probiz n'est pas simplement un contrat de travail. Elle représente un parcours professionnel accéléré de manière agressive au sein de l'un des environnements BPO les plus dynamiques, performants et culturellement diversifiés , entouré de pairs d'élite qui se poussent mutuellement, encadré par des cadres supérieurs expérimentés, et mis au défi quotidiennement d'atteindre de nouvelles normes de performance mesurables.",
        "de": "Eine Karriere bei Probiz ist nicht einfach nur ein Arbeitsverhältnis. Sie stellt einen aggressiv beschleunigten beruflichen Weg in einer der dynamischsten, leistungsstärksten und kulturell vielfältigsten BPO-Umgebungen dar, umgeben von Elite-Kollegen, die sich gegenseitig vorantreiben, betreut von erfahrenen Führungskräften und täglich herausgefordert, neue und messbare Leistungsstandards zu erreichen.",
        "es": "Una carrera en Probiz no es simplemente un acuerdo de empleo. Representa un viaje profesional agresivamente acelerado dentro de uno de los entornos de BPO más dinámicos, de alto rendimiento y culturalmente diversos, rodeado de colegas de élite que se impulsan mutuamente, guiados por ejecutivos senior experimentados y desafiados diariamente para alcanzar estándares de desempeño nuevos y medibles."
    },
    "t_167": {
        "en": "We invest heavily in internal training, structured development pathways, and performance linked internal promotion frameworks   ensuring that every high performing Probiz team member has a clearly defined and compelling upward trajectory within our organization for the long term.",
        "ar": "نحن نستثمر بكثافة في التدريب الداخلي، ومسارات التطوير المنظمة، وأطر الترقية الداخلية المرتبطة بالأداء ، مما يضمن حصول كل عضو متفوق في فريق بروبيز على مسار صعودي واضح وجذاب داخل منظمتنا على المدى الطويل.",
        "fr": "Nous investissons massivement dans la formation interne, les parcours de développement structurés et les cadres de promotion interne liés à la performance , garantissant que chaque membre de l'équipe Probiz performant dispose d'une trajectoire ascendante clairement définie et convaincante au sein de notre organisation sur le long terme.",
        "de": "Wir investieren stark in interne Schulungen, strukturierte Entwicklungspfade und leistungsbezogene interne Aufstiegsrahmen, um sicherzustellen, dass jedes leistungsstarke Probiz-Teammitglied langfristig einen klar definierten und überzeugenden Aufstiegsweg innerhalb unseres Unternehmens hat.",
        "es": "Invertimos fuertemente en capacitación interna, vías de desarrollo estructuradas y marcos de promoción interna vinculados al desempeño, asegurando que cada miembro del equipo de Probiz de alto rendimiento tenga una trayectoria ascendente claramente definida y convincente dentro de nuestra organización a largo plazo."
    },
    "t_175": {
        "en": "Internal Training",
        "ar": "التدريب الداخلي",
        "fr": "Formation Interne",
        "de": "Interne Schulung",
        "es": "Capacitación Interna"
    },
    "t_178": {
        "en": "Work from the very epicenter of global commerce. Our operations are embedded within the most prestigious commercial zones in the country, providing our team members with direct access to elite professional networks, industry leading events, UAE government initiatives, and world class physical and digital infrastructure that accelerates career progression on every dimension.",
        "ar": "اعمل من قلب التجارة العالمية. عملياتنا متجذرة في المناطق التجارية الأكثر رقياً في البلاد، مما يوفر لأعضاء فريقنا وصولاً مباشراً إلى شبكات مهنية من النخبة، والفعاليات الرائدة في الصناعة، ومبادرات حكومة الإمارات، والبنية التحتية المادية والرقمية عالمية المستوى التي تسرع التطور المهني في كل بُعد.",
        "fr": "Travaillez depuis l'épicentre même du commerce mondial. Nos opérations sont ancrées dans les zones commerciales les plus prestigieuses du pays, offrant aux membres de notre équipe un accès direct à des réseaux professionnels d'élite, à des événements de pointe au sein de l'industrie, à des initiatives du gouvernement des É.A.U et à une infrastructure physique et numérique de classe mondiale qui accélère la progression de carrière dans toutes ses dimensions.",
        "de": "Arbeiten Sie im Epizentrum des globalen Handels. Unsere Aktivitäten sind in den prestigeträchtigsten Gewerbegebieten des Landes angesiedelt und bieten unseren Teammitgliedern direkten Zugang zu erstklassigen beruflichen Netzwerken, branchenführenden Veranstaltungen, Regierungsinitiativen der V.A.E. sowie erstklassigen physischen und digitalen Infrastrukturen, die den beruflichen Aufstieg in jeder Hinsicht beschleunigen.",
        "es": "Trabaje desde el mismo epicentro del comercio mundial. Nuestras operaciones están integradas en las zonas comerciales más prestigiosas del país, brindando a los miembros de nuestro equipo acceso directo a redes profesionales de élite, eventos líderes de la industria, iniciativas gubernamentales de los E.A.U. e infraestructura física y digital de clase mundial que acelera la progresión profesional en todas las dimensiones."
    },
    "t_181": {
        "en": "Currently recruiting across high impact operational functions.",
        "ar": "نوم حاليا بالتوظيف عبر وظائف تشغيلية عالية التأثير.",
        "fr": "Nous recrutons actuellement pour des fonctions opérationnelles à fort impact.",
        "de": "Derzeit rekrutieren wir für operative Funktionen mit hoher Wirkung.",
        "es": "Actualmente reclutando en funciones operativas de alto impacto."
    },
    "t_183": {
        "en": "Drive enterprise B2B and B2C revenue campaigns globally. Multilingual candidates are strongly preferred for immediate deployment.",
        "ar": "قيادة حملات إيرادات المؤسسات B2B و B2C على مستوى العالم. يفضل المرشحون الذين يتقنون عدة لغات بشدة للنشر الفوري.",
        "fr": "Menez des campagnes de revenus d'entreprise B2B et B2C à l'échelle mondiale. Les candidats multilingues sont fortement privilégiés pour un déploiement immédiat.",
        "de": "Steuern Sie B2B- und B2C-Umsatzkampagnen weltweit. Mehrsprachige Kandidaten werden für den sofortigen Einsatz bevorzugt.",
        "es": "Impulse campañas de ingresos B2B y B2C para empresas a nivel mundial. Se prefieren candidatos multilingües para el despliegue inmediato."
    },
    "t_185": {
        "en": "Handle high volume, high stakes client interactions with empathy, precision, and brand alignment across multilingual channels simultaneously.",
        "ar": "التعامل مع تفاعلات العملاء عالية الحجم والمخاطر بتعاطف ودقة وتوافق مع العلامة التجارية عبر قنوات متعددة اللغات في وقت واحد.",
        "fr": "Gérez des interactions clients à volume élevé et à enjeux importants avec empathie, précision et alignement avec la marque sur plusieurs canaux multilingues simultanément.",
        "de": "Bearbeiten Sie Kundeninteraktionen mit hohem Volumen und hohem Risiko mit Empathie, Präzision und Markenabstimmung über mehrsprachige Kanäle gleichzeitig.",
        "es": "Gestione interacciones con clientes de alto volumen y gran importancia con empatía, precisión y alineación con la marca a través de canales multilingües simultáneamente."
    },
    "t_187": {
        "en": "Manage complete healthcare billing workflows and Revenue Cycle Management processes for global healthcare clients with regulatory precision and operational accuracy.",
        "ar": "إدارة سير عمل فواتير الرعاية الصحية الكاملة وعمليات إدارة دورة الإيرادات لعملاء الرعاية الصحية العالميين بدقة تنظيمية ودقة تشغيلية.",
        "fr": "Gérez les flux de travail complets de facturation des soins de santé et les processus de gestion du cycle de revenus pour les clients mondiaux du secteur de la santé avec une précision réglementaire et une exactitude opérationnelle.",
        "de": "Verwalten Sie komplette Abrechnungsabläufe im Gesundheitswesen und Revenue Cycle Management-Prozesse für globale Kunden im Gesundheitswesen mit regulatorischer Präzision und operativer Genauigkeit.",
        "es": "Gestione flujos de trabajo completos de facturación médica y procesos de gestión del ciclo de ingresos para clientes de atención médica globales con precisión regulatoria y exactitud operativa."
    },
    # About Page
    "t_108": {
        "en": "Our leadership brings over 25 years of hard operational experience scaling businesses around the world. This means we approach every client contract not merely as a service provider but as seasoned operational partners who understand how your business functions on a broader level.",
        "ar": "تتمتع قيادتنا بأكثر من 25 عاماً من الخبرة التشغيلية الميدانية في توسيع نطاق الأعمال حول العالم. وهذا يعني أننا نتعامل مع كل عقد عميل ليس مجرد مزود خدمة ولكن كشركاء تشغيليين متمرسين يفهمون كيفية عمل عملك على مستوى أوسع.",
        "fr": "Nos dirigeants apportent plus de 25 ans d'expérience opérationnelle solide dans le développement d'entreprises à travers le monde. Cela signifie que nous abordons chaque contrat client non seulement en tant que prestataire de services, mais en tant que partenaires opérationnels chevronnés qui comprennent le fonctionnement de votre entreprise à un niveau plus large.",
        "de": "Unsere Führung bringt über 25 Jahre fundierte operative Erfahrung in der Skalierung von Unternehmen auf der ganzen Welt mit. Das bedeutet, dass wir jeden Kundenvertrag nicht nur als Dienstleister, sondern als erfahrene operative Partner betrachten, die verstehen, wie Ihr Unternehmen auf einer breiteren Ebene funktioniert.",
        "es": "Nuestro liderazgo aporta más de 25 años de sólida experiencia operativa escalando negocios en todo el mundo. Esto significa que abordamos cada contrato de cliente no solo como un proveedor de servicios, sino como socios operativos experimentados que comprenden cómo funciona su negocio a un nivel más amplio."
    }
}

# Apply updates to data
for key, content in updates.items():
    for lang in ['ar', 'fr', 'de', 'es']:
        if lang in data:
            data[lang][key] = content[lang]

# Output
with open('translations.js', 'w', encoding='utf-8') as f:
    f.write('const translations = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n')

print("Translations updated successfully.")
