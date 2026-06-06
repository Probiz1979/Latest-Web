import os

target_files = [
    "ai-billing-software.html",
    "ai-rule-engine.html",
    "ai-scribe.html",
    "ar-recovery.html",
    "bi-reporting.html",
    "chronic-care-management.html",
    "claims-submission.html",
    "credentialing.html",
    "data-integration.html",
    "denial-management.html",
    "healthcare-staffing.html",
    "hipaa-compliance.html",
    "hospital-billing.html",
    "imaging-billing.html",
    "laboratory-billing.html",
    "medical-billing-services.html",
    "medical-coding.html",
    "physician-billing.html",
    "qms-lean-six-sigma.html",
    "remote-patient-monitoring.html",
    "revenue-cycle-management.html",
    "rpa-services.html",
    "specialties.html"
]

base_dir = '/Users/muhammadumerali/Desktop/probiz_website/medical-billing'

mini_testimonial_html = """
<!-- CLIENT SUCCESS HIGHLIGHT -->
<section style="padding:100px 0;background:var(--clr-navy-dark);color:#fff;text-align:center;">
<div class="container reveal">
  <i class="fa-solid fa-quote-left" style="font-size:3rem;color:rgba(212,175,55,0.3);margin-bottom:20px;"></i>
  <p style="font-size:1.3rem;font-style:italic;max-width:800px;margin:0 auto 30px;line-height:1.7;">"Transitioning our operations to Probiz was seamless. Their specialized approach, proprietary AI workflows, and dedicated billing teams accelerated our cash flow in ways we didn't think were possible with an outsourced vendor."</p>
  <div style="display:flex;align-items:center;justify-content:center;gap:15px;">
    <div style="width:50px;height:50px;border-radius:50%;background:var(--clr-gold);display:flex;align-items:center;justify-content:center;font-weight:bold;color:var(--clr-navy);font-size:1.2rem;">C</div>
    <div style="text-align:left;">
      <h4 style="margin:0 0 4px;font-size:1.1rem;">Chief Financial Officer</h4>
      <span style="color:rgba(255,255,255,0.7);font-size:0.9rem;">Regional Healthcare Network</span>
    </div>
  </div>
</div>
</section>
"""

for filename in target_files:
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'CLIENT SUCCESS HIGHLIGHT' in content:
        continue
        
    if '<!-- GLOBAL FAQ -->' in content:
        parts = content.split('<!-- GLOBAL FAQ -->')
        new_content = parts[0] + mini_testimonial_html + "\n<!-- GLOBAL FAQ -->" + parts[1]
    elif '<!-- CTA -->' in content:
        parts = content.split('<!-- CTA -->')
        new_content = parts[0] + mini_testimonial_html + "\n<!-- CTA -->" + parts[1]
    else:
        new_content = content.replace('</body>', mini_testimonial_html + '\n</body>')
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Testimonial expansion complete!")
