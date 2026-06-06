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

probiz_advantage_html = """
<!-- THE PROBIZ ADVANTAGE -->
<section style="padding:100px 0;background:var(--clr-surface);">
<div class="container">
  <div class="text-center" style="margin-bottom:50px;">
    <div class="hero-badge-glam" style="display:inline-flex;margin-bottom:16px;">The Probiz Advantage</div>
    <h2 class="section-title serif">Why Leading Practices <span class="text-shimmer-gold">Partner With Us</span></h2>
    <p class="section-subtitle" style="margin:0 auto;">We combine certified expertise with proprietary technology to deliver unmatched revenue cycle performance.</p>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:30px;">
    <div style="background:#fff;padding:40px;border-radius:20px;box-shadow:var(--shadow-soft);border:1px solid rgba(15,29,74,0.08);transition:0.3s;" class="hover-up">
      <i class="fa-solid fa-bolt" style="font-size:2.5rem;color:var(--clr-gold);margin-bottom:20px;display:block;"></i>
      <h3 style="font-size:1.4rem;color:var(--clr-navy);margin-bottom:15px;">Maximized Clean Claim Rates</h3>
      <p style="color:var(--clr-text-muted);line-height:1.7;font-size:1rem;margin:0;">Our AI-driven scrubbing engine runs every claim against millions of payer-specific rules before submission, practically eliminating front-end rejections and accelerating your cash flow.</p>
    </div>
    <div style="background:#fff;padding:40px;border-radius:20px;box-shadow:var(--shadow-soft);border:1px solid rgba(15,29,74,0.08);transition:0.3s;" class="hover-up">
      <i class="fa-solid fa-user-shield" style="font-size:2.5rem;color:var(--clr-gold);margin-bottom:20px;display:block;"></i>
      <h3 style="font-size:1.4rem;color:var(--clr-navy);margin-bottom:15px;">Certified Specialist Teams</h3>
      <p style="color:var(--clr-text-muted);line-height:1.7;font-size:1rem;margin:0;">We don't use generalists. Your account is managed by specialty-specific certified coders who understand the nuances of your exact clinical discipline, ensuring maximum compliant reimbursement.</p>
    </div>
    <div style="background:#fff;padding:40px;border-radius:20px;box-shadow:var(--shadow-soft);border:1px solid rgba(15,29,74,0.08);transition:0.3s;" class="hover-up">
      <i class="fa-solid fa-chart-pie" style="font-size:2.5rem;color:var(--clr-gold);margin-bottom:20px;display:block;"></i>
      <h3 style="font-size:1.4rem;color:var(--clr-navy);margin-bottom:15px;">Real-Time Financial Analytics</h3>
      <p style="color:var(--clr-text-muted);line-height:1.7;font-size:1rem;margin:0;">Stop waiting for end-of-month reports. Our proprietary BI dashboards give you real-time visibility into collection rates, A/R aging, and denial trends.</p>
    </div>
    <div style="background:#fff;padding:40px;border-radius:20px;box-shadow:var(--shadow-soft);border:1px solid rgba(15,29,74,0.08);transition:0.3s;" class="hover-up">
      <i class="fa-solid fa-lock" style="font-size:2.5rem;color:var(--clr-gold);margin-bottom:20px;display:block;"></i>
      <h3 style="font-size:1.4rem;color:var(--clr-navy);margin-bottom:15px;">100% EHR Agnostic & Secure</h3>
      <p style="color:var(--clr-text-muted);line-height:1.7;font-size:1rem;margin:0;">We work seamlessly within your existing software via secure, HIPAA-compliant VPNs. Zero data migration required, and zero disruption to your clinical workflow.</p>
    </div>
  </div>
</div>
</section>

<!-- SEAMLESS ONBOARDING -->
<section style="padding:100px 0;background:#fff;">
<div class="container">
  <div style="display:grid;grid-template-columns:minmax(0, 1.2fr) minmax(0, 0.8fr);gap:60px;align-items:center;" class="onboarding-grid">
    <div class="reveal">
      <h2 class="section-title serif">A Seamless <span class="text-shimmer-gold">Transition Process</span></h2>
      <p style="font-size:1.1rem;color:var(--clr-text-muted);line-height:1.8;margin-bottom:40px;">Switching billing partners shouldn't disrupt your cash flow. Our meticulously engineered onboarding process ensures a smooth, parallel transition.</p>
      <ul style="list-style:none;padding:0;margin:0;">
        <li style="display:flex;gap:20px;margin-bottom:30px;">
          <div style="width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg, var(--clr-navy), var(--clr-gold));color:#fff;display:flex;align-items:center;justify-content:center;font-weight:bold;flex-shrink:0;box-shadow:var(--shadow-soft);">1</div>
          <div>
            <h4 style="color:var(--clr-navy);font-size:1.15rem;margin-bottom:8px;">Discovery & Integration</h4>
            <p style="color:var(--clr-text-muted);font-size:0.95rem;margin:0;line-height:1.6;">We establish secure remote access to your EHR/PMS and map your existing workflows without interrupting your current team.</p>
          </div>
        </li>
        <li style="display:flex;gap:20px;margin-bottom:30px;">
          <div style="width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg, var(--clr-navy), var(--clr-gold));color:#fff;display:flex;align-items:center;justify-content:center;font-weight:bold;flex-shrink:0;box-shadow:var(--shadow-soft);">2</div>
          <div>
            <h4 style="color:var(--clr-navy);font-size:1.15rem;margin-bottom:8px;">Historical Analysis</h4>
            <p style="color:var(--clr-text-muted);font-size:0.95rem;margin:0;line-height:1.6;">We audit your past claims to identify immediate revenue leakage, coding errors, and systemic denial trends.</p>
          </div>
        </li>
        <li style="display:flex;gap:20px;margin-bottom:30px;">
          <div style="width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg, var(--clr-navy), var(--clr-gold));color:#fff;display:flex;align-items:center;justify-content:center;font-weight:bold;flex-shrink:0;box-shadow:var(--shadow-soft);">3</div>
          <div>
            <h4 style="color:var(--clr-navy);font-size:1.15rem;margin-bottom:8px;">Custom Rule Building</h4>
            <p style="color:var(--clr-text-muted);font-size:0.95rem;margin:0;line-height:1.6;">Our AI scrubbing engine is programmed with your specific payer matrix and local coverage determinations to prevent future denials.</p>
          </div>
        </li>
        <li style="display:flex;gap:20px;">
          <div style="width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg, var(--clr-navy), var(--clr-gold));color:#fff;display:flex;align-items:center;justify-content:center;font-weight:bold;flex-shrink:0;box-shadow:var(--shadow-soft);">4</div>
          <div>
            <h4 style="color:var(--clr-navy);font-size:1.15rem;margin-bottom:8px;">Go-Live & Optimization</h4>
            <p style="color:var(--clr-text-muted);font-size:0.95rem;margin:0;line-height:1.6;">We take over day-to-day operations, instantly applying our optimized workflows to accelerate your cash flow and reduce days in A/R.</p>
          </div>
        </li>
      </ul>
    </div>
    <div class="reveal stagger-1" style="background:var(--clr-navy-dark);padding:50px;border-radius:30px;color:#fff;box-shadow:var(--shadow-deep);position:relative;overflow:hidden;text-align:center;">
      <div style="position:absolute;top:-50px;right:-50px;width:200px;height:200px;background:radial-gradient(circle, rgba(212,175,55,0.2) 0%, transparent 70%);"></div>
      <i class="fa-solid fa-sack-dollar" style="font-size:4rem;color:var(--clr-gold);margin-bottom:24px;"></i>
      <h3 style="font-size:2.2rem;margin-bottom:20px;font-family:serif;line-height:1.2;">The Cost of Inaction</h3>
      <p style="color:rgba(255,255,255,0.8);font-size:1.05rem;line-height:1.7;margin-bottom:30px;">Every day you wait to optimize your revenue cycle, you are losing money to timely filing limits, unappealed denials, and under-coded encounters. Stop accepting revenue leakage as a cost of doing business.</p>
      <a href="contact.html" class="btn btn-gold" style="padding:16px 32px;font-size:1.05rem;width:100%;">Stop Revenue Leakage Today</a>
    </div>
  </div>
</div>
<style>
@media(max-width:900px){ .onboarding-grid{grid-template-columns:1fr !important;} }
.hover-up:hover { transform:translateY(-8px); border-color:var(--clr-gold) !important; }
</style>
</section>
"""

global_faq_html = """
<!-- GLOBAL FAQ -->
<section style="padding:100px 0;background:var(--clr-surface);">
<div class="container">
  <div class="text-center" style="margin-bottom:50px;">
    <h2 class="section-title serif">Frequently Asked <span class="text-shimmer-gold">Questions</span></h2>
    <p class="section-subtitle" style="margin:0 auto;">Common questions about our process, integration, and security.</p>
  </div>
  <div class="faq-acc" style="max-width:900px;margin:0 auto;">
    <div class="facc-item reveal">
      <input type="checkbox" id="gfaq1" class="facc-input" style="display:none;"/>
      <label for="gfaq1" class="facc-label" style="display:flex;justify-content:space-between;align-items:center;padding:22px 30px;cursor:pointer;font-size:1.05rem;font-weight:700;color:var(--clr-navy);background:#fff;border:1px solid rgba(15,29,74,.08);border-radius:12px;">Do I need to change my EHR/EMR software?</label>
      <div class="facc-body" style="background:#fff;border:1px solid rgba(15,29,74,.08);border-top:none;border-radius:0 0 12px 12px;padding:0 30px;max-height:0;overflow:hidden;transition:.4s;"><p style="padding:20px 0;color:var(--clr-text-muted);line-height:1.7;margin:0;">No. Our team is fully trained on all major platforms including Epic, Cerner, eClinicalWorks, AdvancedMD, Athenahealth, and Kareo. We log directly into your existing system via a secure, HIPAA-compliant connection. Your front office workflow remains entirely unchanged.</p></div>
    </div>
    <div class="facc-item reveal" style="margin-top:16px;">
      <input type="checkbox" id="gfaq2" class="facc-input" style="display:none;"/>
      <label for="gfaq2" class="facc-label" style="display:flex;justify-content:space-between;align-items:center;padding:22px 30px;cursor:pointer;font-size:1.05rem;font-weight:700;color:var(--clr-navy);background:#fff;border:1px solid rgba(15,29,74,.08);border-radius:12px;">How is your service priced?</label>
      <div class="facc-body" style="background:#fff;border:1px solid rgba(15,29,74,.08);border-top:none;border-radius:0 0 12px 12px;padding:0 30px;max-height:0;overflow:hidden;transition:.4s;"><p style="padding:20px 0;color:var(--clr-text-muted);line-height:1.7;margin:0;">We operate primarily on a percentage-of-collections model. This means we don't get paid until you get paid, perfectly aligning our incentives with your practice's financial success. There are no hidden setup fees or rigid long-term lock-ins.</p></div>
    </div>
    <div class="facc-item reveal" style="margin-top:16px;">
      <input type="checkbox" id="gfaq3" class="facc-input" style="display:none;"/>
      <label for="gfaq3" class="facc-label" style="display:flex;justify-content:space-between;align-items:center;padding:22px 30px;cursor:pointer;font-size:1.05rem;font-weight:700;color:var(--clr-navy);background:#fff;border:1px solid rgba(15,29,74,.08);border-radius:12px;">Is my patient data secure?</label>
      <div class="facc-body" style="background:#fff;border:1px solid rgba(15,29,74,.08);border-top:none;border-radius:0 0 12px 12px;padding:0 30px;max-height:0;overflow:hidden;transition:.4s;"><p style="padding:20px 0;color:var(--clr-text-muted);line-height:1.7;margin:0;">Absolutely. We are fully HIPAA compliant. We operate under strict Business Associate Agreements (BAAs), utilizing AES-256 encryption, zero-trust network access, and mandatory multi-factor authentication. Patient data is never stored on unauthorized local devices.</p></div>
    </div>
  </div>
</div>
<style>
.facc-input:checked ~ .facc-body { max-height: 500px !important; }
.facc-input:checked ~ .facc-label::after { transform: rotate(45deg); }
.facc-label::after { content: '\f067'; font-family: 'Font Awesome 6 Free'; font-weight: 900; color: var(--clr-gold); transition: .3s; }
</style>
</section>
"""

for filename in target_files:
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if we already injected
    if 'THE PROBIZ ADVANTAGE' in content:
        continue
        
    # Determine what to inject
    injection = probiz_advantage_html
    if 'Frequently Asked Questions' not in content:
        injection += "\n" + global_faq_html
        
    # Find the CTA section to inject right before it
    # Most pages have <!-- CTA --> or a section with "contact.html" at the bottom
    
    if '<!-- CTA -->' in content:
        parts = content.split('<!-- CTA -->')
        new_content = parts[0] + injection + "\n<!-- CTA -->" + parts[1]
    elif '<footer' in content:
        # Fallback to right before footer
        parts = content.split('<footer')
        new_content = parts[0] + injection + "\n<footer" + parts[1]
    else:
        # Just append before body close
        new_content = content.replace('</body>', injection + '\n</body>')
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Bulk expansion complete!")
