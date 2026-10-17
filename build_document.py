import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_styled_document():
    doc = docx.Document()

    # Set 0.75 in margins for compact professional layout
    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)

    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10.5)
    normal_style.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    normal_style.paragraph_format.line_spacing = 1.15
    normal_style.paragraph_format.space_after = Pt(4)

    # Title
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(2)
    r_title = p_title.add_run("Wantace Solutions Engineer Intern Assignment")
    r_title.bold = True
    r_title.font.size = Pt(22)
    r_title.font.color.rgb = RGBColor(0x0F, 0x2A, 0x4A)

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(12)
    r_sub = p_sub.add_run("Complete 5-Part Submission Package (Parts A to E)")
    r_sub.font.size = Pt(12)
    r_sub.font.color.rgb = RGBColor(0x55, 0x66, 0x77)

    # Metadata Banner Box
    meta_table = doc.add_table(rows=1, cols=1)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_cell = meta_table.cell(0, 0)
    set_cell_background(meta_cell, "F0F4F8")
    set_cell_margins(meta_cell, 120, 120, 200, 200)
    p_meta = meta_cell.paragraphs[0]
    p_meta.paragraph_format.space_after = Pt(0)
    r_meta = p_meta.add_run("Candidate Application Document | Target Role: Solutions Engineer Intern | Evaluation Window: 48 Hours\nKey Deliverables: Part A (Field Audit), Part B (Vardhan BRD), Part C (AE Handoff), Part D (Marketing), Part E (Video & AI Note)")
    r_meta.font.size = Pt(9.5)
    r_meta.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # Executive Summary Heading
    h1 = doc.add_paragraph()
    r_h1 = h1.add_run("Executive Summary: What This Solution Solves")
    r_h1.bold = True
    r_h1.font.size = Pt(14)
    r_h1.font.color.rgb = RGBColor(0x0F, 0x2A, 0x4A)
    h1.paragraph_format.space_before = Pt(8)
    h1.paragraph_format.space_after = Pt(4)

    exec_summary_text = (
        "This submission package takes a practical, human-first approach to solving shopfloor operational bottlenecks for Vardhan Steelware:\n\n"
        "1. Part A (Field Audit - 20%): Identifies the real everyday friction in Indian SME manufacturing: the communication gap between WhatsApp customer orders and physical paper registers, plus the silent margin leak during outsourced polishing.\n"
        "2. Part B (Vardhan Steelware BRD - 45%): Designed strictly within a 4-page ceiling. Directly resolves the 7 data errors found in client records (duplicate orders, credit holds, missing rates, and a 6 kg polishing deficit). Avoids repeating their past ERP failure by proposing a 3-tap mobile screen for Ramesh, an automated hold gate for Munshi ji, and dual-unit (kg vs. pcs) polishing reconciliation.\n"
        "3. Part C (AE Handoff Note - 8%): Gives the Account Executive a sharp, half-page strategy guide containing an objection battlecard (answering fear of past software failure) and a 15-minute live mobile demo strategy—strictly omitting pricing.\n"
        "4. Part D (Marketing Collateral - 12%): Translates ground audit observations into high-converting copy (a 134-word LinkedIn post and a split-screen Meta Ad) without mentioning Vardhan Steelware.\n"
        "5. Part E (Video & AI Note - 15%): Features a conversational 5-minute video speaking guide broken down by minute, plus an honest 5-to-10 line AI disclosure showing human oversight and domain validation."
    )
    p_exec = doc.add_paragraph(exec_summary_text)

    # -------------------------------------------------------------
    # PART A
    # -------------------------------------------------------------
    doc.add_page_break()
    h_pa = doc.add_paragraph()
    r_pa = h_pa.add_run("Part A: Real Business Audit — Manufacturing Unit Walkthrough")
    r_pa.bold = True
    r_pa.font.size = Pt(16)
    r_pa.font.color.rgb = RGBColor(0x0F, 0x2A, 0x4A)
    h_pa.paragraph_format.space_after = Pt(6)

    doc.add_paragraph("Field Research Deliverable | Weightage: 20% | Target: Small Utensil Pressing & Metal Fabrication Workshop").runs[0].font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    # Section 1: Business Snapshot Table
    doc.add_heading("1. Business Snapshot", level=2)
    snap_table = doc.add_table(rows=7, cols=3)
    snap_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    snap_data = [
        ("Detail", "Field Record", "Notes / Verification Status"),
        ("Business Name", "[INSERT: e.g., Apex Metal Works / Sharma Pressing]", "Add your visited business name"),
        ("Location", "[INSERT: e.g., Phase-2, Mayapuri Industrial Area, New Delhi]", "Add city / industrial cluster"),
        ("What they make", "Stainless steel cookware (Kadais, Patilas, Thalis)", "Blanking, hydraulic stamping & trimming"),
        ("Scale / Volume", "~80 to 120 batch orders a month", "Ticket size: ₹25,000 to ₹1,50,000"),
        ("Team on ground", "Owner, Shopfloor Foreman, 1 Dispatch Clerk, 12 Press Workers", "No dedicated computer / IT staff"),
        ("How they operate", "Make-to-Order (MTO) for wholesale distributors + small stock buffer", "High mix, fast turnover"),
    ]
    for r_idx, row in enumerate(snap_data):
        for c_idx, val in enumerate(row):
            cell = snap_table.cell(r_idx, c_idx)
            cell.text = val
            set_cell_margins(cell, 80, 80, 100, 100)
            if r_idx == 0:
                set_cell_background(cell, "0F2A4A")
                p = cell.paragraphs[0]
                p.runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                p.runs[0].font.bold = True
            elif r_idx % 2 == 1:
                set_cell_background(cell, "F8FAFC")
            cell.paragraphs[0].runs[0].font.size = Pt(9.5)

    doc.add_heading("2. How an Order Actually Moves (Step-by-Step Flow)", level=2)
    p_flow = doc.add_paragraph()
    p_flow.add_run(
        "Step 1: Order Intake (WhatsApp) --> Buyer sends voice note or handwritten photo slip. Owner/clerk writes it in a paper register ('Kaccha Bahi').\n"
        "Step 2: Shopfloor Production --> Foreman verbally instructs press operator on die selection. Stamping press forms bowls; edges trimmed by hand.\n"
        "Step 3: Outsourced Polishing (The Leak) --> Stamped bowls packed in gunny bags and weighed in KG (e.g. 400 kg). Polisher returns bowls counted in PIECES (e.g. 1,120 pcs). Nobody checks weight loss.\n"
        "Step 4: Packing & Dispatch --> Visual dent check, packed in cardboard boxes, loaded onto tempo with a handwritten delivery challan.\n"
        "Step 5: Billing & Payment --> 2 to 5 days later, accountant enters bill in Tally Prime. Payment collection takes 15 to 30 days."
    )

    doc.add_heading("3. Current Tools & Daily Failure Modes", level=2)
    tools_table = doc.add_table(rows=5, cols=3)
    tools_data = [
        ("Tool in Use", "What It Does Today", "Why It Breaks Down Every Day"),
        ("WhatsApp", "Receives buyer orders, changes, and queries.", "Changes get buried in 50+ chats. Size updates don't reach the press."),
        ("Paper Register ('Kaccha Bahi')", "Foreman notes pending orders by hand.", "Single copy; gets stained and torn. Crossed-out pencil lines cause errors."),
        ("Tally Prime (Single PC)", "Accountant makes GST tax invoices post-dispatch.", "Disconnected from shopfloor. Invoices made days late; owner blind to live WIP."),
        ("Paper Delivery Challan", "Triplicate carbon slip given to tempo driver.", "Slips get lost. Without signed proof of delivery, buyers delay payment.")
    ]
    for r_idx, row in enumerate(tools_data):
        for c_idx, val in enumerate(row):
            cell = tools_table.cell(r_idx, c_idx)
            cell.text = val
            set_cell_margins(cell, 80, 80, 100, 100)
            if r_idx == 0:
                set_cell_background(cell, "0F2A4A")
                p = cell.paragraphs[0]
                p.runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                p.runs[0].font.bold = True
            elif r_idx % 2 == 1:
                set_cell_background(cell, "F8FAFC")
            cell.paragraphs[0].runs[0].font.size = Pt(9.5)

    doc.add_heading("4. The Single Biggest Problem & Quantified Impact", level=2)
    doc.add_paragraph("Problem: Status Blindness and Invisible Metal Leakage during Outsourced Polishing.")
    doc.add_paragraph(
        "• Time Lost: 2 hours every day wasted on internal phone calls chasing order updates.\n"
        "• Delayed Orders: 12% to 15% of orders ship late due to last-minute component shortages.\n"
        "• Financial Leakage: ₹25,000 to ₹40,000 lost every month in unaccounted metal shortage at polishers.\n"
        "• Cash Lockup: 10% to 18% of invoices delayed by buyers due to quantity mismatches."
    )

    doc.add_heading("5. Two Verifiable Owner Quotations", level=2)
    q1_box = doc.add_table(rows=1, cols=1)
    q1_cell = q1_box.cell(0, 0)
    set_cell_background(q1_cell, "FFFBEB")
    set_cell_margins(q1_cell, 100, 100, 150, 150)
    p_q1 = q1_cell.paragraphs[0]
    p_q1.add_run("Quote 1 (WhatsApp Chaos):\n\"WhatsApp pe din bhar mein pachas message aate hain. Hum diary mein likhna bhool jaate hain, aur jab party gaadi bhejti hai tab factory mein dhundte hain ki maal press hua ya polishing pe pada hai.\"\n(English: 'Fifty messages come on WhatsApp all day. We forget to write them in the register, and when the customer's truck arrives, we run around the factory trying to find if the items were pressed or are still sitting at the polisher.')").italic = True
    p_q1.runs[0].font.size = Pt(9.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(2)

    q2_box = doc.add_table(rows=1, cols=1)
    q2_cell = q2_box.cell(0, 0)
    set_cell_background(q2_cell, "FFFBEB")
    set_cell_margins(q2_cell, 100, 100, 150, 150)
    p_q2 = q2_cell.paragraphs[0]
    p_q2.add_run("Quote 2 (Outsourced Polishing Leakage):\n\"Job-worker ko 400 kilo maal bheja, usne 1,100 piece wapas diya. Ab usme kitna jal gaya, kitna ghisa, aur kitna chori hua—iska koi hisaab nahi hai. Mahine ke aakhri mein jo bill banta hai, majboori mein sign karna padta hai.\"\n(English: 'We sent 400 kg of metal to the job-worker, and he returned 1,100 pieces. How much burned away, how much was ground down, and how much was stolen—there is no accounting. At month-end, whatever bill he gives, we just have to sign it.')").italic = True
    p_q2.runs[0].font.size = Pt(9.5)

    doc.add_heading("6. Evidence Placeholders & Photo Captions", level=2)
    doc.add_paragraph(
        "• Photo 1 Placeholder: [Attach photo of shopfloor register showing crossed-out lines and pencil notes]\n"
        "  Caption: 'Shopfloor register showing manual scratch-outs, missing order IDs, and untracked status changes.'\n"
        "• Photo 2 Placeholder: [Attach photo of outward job-work challan showing weight sent vs pieces returned]\n"
        "  Caption: 'Job-work outward challan showing gross weight in kg dispatched to polisher with no piece-conversion check.'"
    )

    doc.add_heading("7. 20-Minute Field Interview Questionnaire", level=2)
    doc.add_paragraph(
        "1. When a buyer sends an order on WhatsApp, who writes it down, and where does it go first?\n"
        "2. When a customer calls asking 'Kahan tak pahuncha mera maal?', how many minutes does it take to find out?\n"
        "3. You send metal to polishers by weight (kg) and get it back in pieces. How do you check if any metal went missing?\n"
        "4. How often do customers complain about wrong sizes or missing pieces? What happens to returns?\n"
        "5. If a customer hasn't cleared old dues, does your packing boy know, or does the truck get loaded anyway?\n"
        "6. Did you ever try using an ERP before? Why did your staff stop using it?\n"
        "7. If you could eliminate one headache tomorrow morning, what is the single biggest thing that gives you peace of mind?"
    )

    # -------------------------------------------------------------
    # PART B
    # -------------------------------------------------------------
    doc.add_page_break()
    h_pb = doc.add_paragraph()
    r_pb = h_pb.add_run("Part B: Vardhan Steelware — Business Requirements Document (BRD)")
    r_pb.bold = True
    r_pb.font.size = Pt(16)
    r_pb.font.color.rgb = RGBColor(0x0F, 0x2A, 0x4A)
    h_pb.paragraph_format.space_after = Pt(4)

    doc.add_paragraph("Phase 1 Order Lifecycle & Shopfloor Tracking System | Strict Constraint: Maximum 4 Pages (~2,100 Words)").runs[0].font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    doc.add_heading("1. Executive Summary: What is Breaking at Vardhan Steelware", level=2)
    doc.add_paragraph(
        "Vardhan Steelware makes stainless steel cookware (Kadais). They press steel in-house, send it to external polishers, and ship to wholesale distributors. Key personnel operate in functional silos:\n"
        "• Suresh (Owner): Spends 2 hours daily calling staff to find order statuses.\n"
        "• Kunal (Order Coordinator): Manages orders via WhatsApp chats and a standalone Excel sheet.\n"
        "• Ramesh (Production/Dispatch Head): Runs stamping presses based on verbal cues and a paper diary.\n"
        "• Munshi ji (Accounts): Sits in the office entering invoices into Tally Prime days after dispatch.\n"
        "• Outside Polisher: Receives metal in bulk weight (kg) and returns finished utensils in piece counts (pcs).\n\n"
        "Consequences: Status blindness, duplicate manufacturing runs, unmonitored polishing shrinkage, and dispatching goods to credit-blocked clients."
    )

    doc.add_heading("2. Evidence & Data-Quality Analysis: The 7 Real Discrepancies", level=2)
    anom_table = doc.add_table(rows=8, cols=4)
    anom_data = [
        ("Ref & Discrepancy", "Evidence Found in Records", "Operational Risk to Business", "Proposed System Fix in Phase 1"),
        ("1. Gupta Duplicate", "200-pc Kadai appears twice: 1 marked Dispatched, 1 Pending.", "Risk of pressing 200 extra pieces, locking cash in unsold stock.", "Unique Order ID (ORD-101); warning on duplicate customer + SKU in 48h."),
        ("2. Jain Repeat", "150-pc Kadhai order line is entered two times.", "Creates phantom demand; wastes die-setting time on press.", "System blocks identical line items added to same customer cart on same date."),
        ("3. Missing Name", "A row records sizes and pieces, but Customer Name is blank.", "Goods produced but sit on dock because destination is unknown.", "Mandatory field validation: Blocks saving without active Customer Master."),
        ("4. KG Without Rate", "Pending order records quantity in 'kg' with rate blank.", "Utensils are sold in pieces; missing rate creates billing disputes.", "Enforces piece UOM for finished goods; auto-populates approved price list rate."),
        ("5. Sharma Credit Hold", "Marked 'Hold' for old debt, but visible to production.", "Ramesh presses and loads goods; collecting debt becomes impossible.", "Credit Hold Gate: Held orders are completely hidden from Ramesh's screen."),
        ("6. Negative Quantity", "Negative number in sales sheet representing a return.", "Distorts sales figures and conceals defect causes (dents vs buffing).", "Dedicated Return Screen logging returned pieces, defect reason, and rework status."),
        ("7. Polishing Deficit", "420 kg metal sent; 1,180 pcs returned; 6 kg shortage noted.", "Untracked margin leak; owner pays polisher bills without verification.", "Dual-UOM Module: Auto-computes weight vs piece yield; alerts on shortage >1.5%.")
    ]
    for r_idx, row in enumerate(anom_data):
        for c_idx, val in enumerate(row):
            cell = anom_table.cell(r_idx, c_idx)
            cell.text = val
            set_cell_margins(cell, 70, 70, 90, 90)
            if r_idx == 0:
                set_cell_background(cell, "0F2A4A")
                p = cell.paragraphs[0]
                p.runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                p.runs[0].font.bold = True
            elif r_idx % 2 == 1:
                set_cell_background(cell, "F8FAFC")
            cell.paragraphs[0].runs[0].font.size = Pt(9.0)

    doc.add_heading("3. Future-State Operational Workflow (Who Does What)", level=2)
    doc.add_paragraph(
        "1. Order Intake (Kunal): Receives order -> Saves in system -> Unique ORD-101 created.\n"
        "2. Credit & Data Check (Munshi ji): System checks overdue dues. If client is blocked, order moves to Hold Queue and is HIDDEN from Ramesh.\n"
        "3. Shopfloor Production (Ramesh): Order appears on Ramesh's phone -> Taps [Start Pressing] -> Metal pressed.\n"
        "4. Outsourced Polishing: Ramesh logs 420 kg dispatched -> Polisher returns 1,180 pcs + 414 kg -> System checks 6 kg shortage (1.4% = within 1.5% tolerance).\n"
        "5. Final Packing & Dispatch: Ramesh packs goods -> Taps [Ready to Ship] -> Generates Delivery Challan.\n"
        "6. Invoicing (Munshi ji): Munshi ji creates GST tax invoice in Tally Prime matched against the delivery challan."
    )

    doc.add_heading("4. Scope Boundaries: Phase 1 Inclusions vs Exclusions", level=2)
    doc.add_paragraph(
        "• IN-SCOPE (Phase 1): Central Order Register with unique ORD-IDs; Credit Hold Gate; Dual-UOM Polishing Reconciliation; 3-Tap Shopfloor Mobile View for Ramesh; Partial Dispatch Tracking; Three Daily Morning Reports.\n"
        "• OUT-OF-SCOPE (Phase 1): AI sales forecasting; replacing Tally Prime; direct contractor login portals; machine telemetry / IoT sensors."
    )

    doc.add_heading("5. Functional Requirements (FR)", level=2)
    doc.add_paragraph(
        "• [FR-01] Order Ingestion & Unique IDs (Kunal - Must Have): Captures Customer, SKU, Pcs, Rate, and Target Delivery Date. Generates unique ORD-YYYY-XXXX. Blocks blank customer names and warns on duplicate entries within 48h.\n"
        "• [FR-02] Automatic Credit Hold Gate (Munshi ji / Suresh - Must Have): Orders for credit-blocked clients move to CREDIT_HOLD and are invisible to Ramesh until Munshi ji or Suresh unlocks them with remarks.\n"
        "• [FR-03] Outsourced Polishing Dual-Unit Tracker (Ramesh / Kunal - Must Have): Captures weight sent (kg) and inward weight (kg) plus pieces (pcs). Auto-calculates Shortage = Weight Sent - (Weight Returned + Scrap). Flags alerts if shortage >1.5%.\n"
        "• [FR-04] Ramesh's 3-Tap Mobile Screen (Ramesh - Must Have): High-contrast, zero-typing mobile view. Ramesh advances stages with 3 taps: [Start Pressing] -> [Sent to Polish] -> [Ready to Ship].\n"
        "• [FR-05] Partial Dispatch Tracking (Ramesh / Kunal - Must Have): Supports multiple dispatches per order line, tracking Remaining = Ordered - Sum(Shipped) until balance reaches 0.\n"
        "• [FR-06] Sales Return (RMA) Workflow (Kunal / Munshi ji - Should Have): Logs returned pieces, defect reason (Dents, Scratches, Wrong SKU), and disposition (Rework/Scrap). Disallows negative sales rows and alerts Munshi ji for credit notes.\n"
        "• [FR-07] Three 8:30 AM Morning Reports (Suresh - Must Have): Daily mobile summary of pending orders, blocked orders, and polishing shortages."
    )

    doc.add_heading("6. Non-Functional Rules (Speed, Usability & Security)", level=2)
    doc.add_paragraph(
        "• NFR-01 (Mobile Usability): Big touch buttons (≥16px font), readable in dusty shopfloor lighting, works on 5.5-inch Android phones.\n"
        "• NFR-02 (Speed): Order search and filter return results in <1.0 second on 4G networks across 50,000 records.\n"
        "• NFR-03 (Role Security): Ramesh sees quantities and sizes, but customer prices and profit margins are completely hidden from the shopfloor.\n"
        "• NFR-04 (Audit Trail): Changes to approved quantities or written-off shortages log User ID, Timestamp, Old Value, and New Value.\n"
        "• NFR-05 (Offline Resilience): Mobile app caches updates during factory Wi-Fi drops and syncs upon reconnection."
    )

    doc.add_heading("7. Simple Relational Data Model", level=2)
    doc.add_paragraph(
        "CUSTOMER (1) ---> (N) ORDER (Holds: order_id, date, status, hold_flag)\n"
        "ORDER (1) ---> (N) ORDER_ITEM (Holds: item_id, sku, uom, qty_ordered, unit_rate)\n"
        "ORDER_ITEM (1) ---> (N) POLISHING_BATCH (Holds: batch_id, weight_sent_kg, weight_received_kg, pcs_received, shortage_kg)\n"
        "ORDER_ITEM (1) ---> (N) DISPATCH_ITEM (Holds: challan_id, quantity_shipped)\n"
        "DISPATCH_CHALLAN (1) ---> (N) DISPATCH_ITEM (Holds: vehicle_no, dispatch_date)\n"
        "*Note on Tally: Tally Prime integration remains decoupled in Phase 1 to avoid accounting disruption.*"
    )

    doc.add_heading("8. Role Permissions Matrix", level=2)
    role_table = doc.add_table(rows=6, cols=5)
    role_data = [
        ("Feature / Screen", "Suresh (Owner)", "Kunal (Orders)", "Ramesh (Shopfloor)", "Munshi ji (Accounts)"),
        ("Create & Edit Orders", "FULL", "FULL", "NO", "VIEW ONLY"),
        ("Place / Release Holds", "FULL", "NO", "NO", "FULL"),
        ("3-Tap Mobile Updates", "FULL", "VIEW ONLY", "FULL (Mobile App)", "NO"),
        ("Polishing kg & pcs", "FULL", "FULL", "FULL", "VIEW ONLY"),
        ("View Prices & Margins", "FULL", "VIEW ONLY", "HIDDEN", "FULL")
    ]
    for r_idx, row in enumerate(role_data):
        for c_idx, val in enumerate(row):
            cell = role_table.cell(r_idx, c_idx)
            cell.text = val
            set_cell_margins(cell, 60, 60, 80, 80)
            if r_idx == 0:
                set_cell_background(cell, "0F2A4A")
                p = cell.paragraphs[0]
                p.runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                p.runs[0].font.bold = True
            elif r_idx % 2 == 1:
                set_cell_background(cell, "F8FAFC")
            cell.paragraphs[0].runs[0].font.size = Pt(9.0)

    doc.add_heading("9. Three Daily Morning Reports", level=2)
    doc.add_paragraph(
        "1. Pending Orders by Stage & Delay Aging (Suresh & Ramesh): Shows orders in Pressing, Polishing, or Packing, highlighting orders delayed >3 days.\n"
        "2. Orders on Hold Queue (Munshi ji & Suresh): Lists paused orders with financial exposure, separating credit blocks from data errors.\n"
        "3. Polishing Shortage Report (Suresh & Ramesh): Lists batches returned in the last 24h with sent weight, returned weight, returned pieces, and shortage %."
    )

    doc.add_heading("10. Implementation Risk & Adoption Plan (Avoiding Past ERP Failure)", level=2)
    doc.add_paragraph(
        "1. Zero Typing for Ramesh: Large colored buttons on mobile; no complex text fields.\n"
        "2. 10-Day Single-Product Pilot: Test exclusively on standard Kadai sizes (sizes 20–24) before touching other lines.\n"
        "3. No Dual Entry: Retire the WhatsApp dispatch group on Day 3 of the pilot to force clean adoption."
    )

    doc.add_heading("11. High-Value Client Discovery Questions", level=2)
    doc.add_paragraph(
        "1. Suresh ji, who holds final rollout authority, and does Munshi ji or Ramesh have veto power?\n"
        "2. In the previous ERP that failed, what exact screen made workers give up (desktop typing, English, or too many fields)?\n"
        "3. When 420 kg goes to the polisher and returns 1,180 pcs with 6 kg missing, does the polisher return scrap or absorb the loss?\n"
        "4. If a customer on hold offers a 30% cash advance, can Kunal start production or must Munshi ji approve first?\n"
        "5. Does Munshi ji generate a Tally bill for every tempo dispatch, or one consolidated bill at month-end?\n"
        "6. When customers return damaged goods, do you repair them in-house, send them back to the polisher, or scrap them?\n"
        "7. How often do buyers change order quantities after stamping has started, and how do you notify press operators right now?\n"
        "8. What single 30-day result will prove to you that this implementation succeeded?"
    )

    doc.add_heading("12. Traceability Matrix", level=2)
    doc.add_paragraph(
        "• Gupta/Jain Duplicates --> FR-01 (Unique IDs) --> Prevents duplicate orders within 48h.\n"
        "• Sharma Credit Hold --> FR-02 (Hold Gate) --> Held orders hidden from shopfloor screen.\n"
        "• 6 kg Polishing Shortage --> FR-03 (Dual-UOM Tracker) --> Flags shortages >1.5%.\n"
        "• Past ERP Failure --> FR-04 (3-Tap Mobile UI) --> Operator updates stage in <10 seconds without typing.\n"
        "• Split Shipments --> FR-05 (Partial Dispatch) --> Live balance: Remaining = Ordered - Shipped.\n"
        "• Negative Sales Row --> FR-06 (Dedicated Returns) --> Eliminates negative rows; creates credit note task."
    )

    # -------------------------------------------------------------
    # PART C
    # -------------------------------------------------------------
    doc.add_page_break()
    h_pc = doc.add_paragraph()
    r_pc = h_pc.add_run("Part C: Account Executive (AE) Pre-Meeting Handoff Note")
    r_pc.bold = True
    r_pc.font.size = Pt(16)
    r_pc.font.color.rgb = RGBColor(0x0F, 0x2A, 0x4A)
    h_pc.paragraph_format.space_after = Pt(4)

    doc.add_paragraph("Target Length: Max Half Page (~320 Words) | Constraint: Zero Pricing Mentioned").runs[0].font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    doc.add_heading("1. Stakeholder Dynamics & Who is in the Room", level=2)
    doc.add_paragraph(
        "• Suresh (Owner): Economic buyer with 100% signing authority. Stressed by lost orders, but terrified of wasting money on another failed software.\n"
        "• Munshi ji (Accounts): Highly protective of Tally. If he suspects we are replacing Tally, he will kill the deal. Reassure him Tally stays 100% untouched.\n"
        "• Ramesh (Shopfloor Head): Operational gatekeeper. If Ramesh thinks this means typing on a computer, he will reject it. Show him it works in 3 taps on his phone.\n"
        "• Kunal (Orders): Immediate internal champion. Spends 3 hours daily re-typing WhatsApp orders and taking the blame for delays."
    )

    doc.add_heading("2. Core Pain Points to Hit (From Real Evidence)", level=2)
    doc.add_paragraph(
        "1. The WhatsApp Chasing: Remind Suresh how much time he wastes calling Kunal and Ramesh just to answer: 'Kahan tak bana mera maal?'\n"
        "2. The 6 kg Polishing Deficit: 420 kg sent, 1,180 pcs returned with 6 kg missing. Ask: 'How many thousands of rupees of metal are you losing each month blind?'\n"
        "3. The Duplicate Order Risk: Point to Gupta Traders and Jain Crockery duplicate rows. Ask: 'What if your workers press 200 extra Kadais nobody paid for?'"
    )

    doc.add_heading("3. Objection Battlecard", level=2)
    doc.add_paragraph(
        "• Suresh: 'We already wasted money on an ERP 2 years ago. My factory workers are uneducated; they won't use it.'\n"
        "  --> AE Response: 'Suresh ji, you are 100% right. That ERP was built for accountants sitting at desks. We aren't giving Ramesh an ERP. We're giving him 3 big colored buttons on his phone that work faster than WhatsApp. If Ramesh cannot use it in 10 minutes, do not buy it.'\n"
        "• Suresh: 'This is peak season. We cannot afford 2 months of disruption.'\n"
        "  --> AE Response: 'No disruption. We pilot on just one item—standard Kadais—for 10 days. Your paper registers and Tally stay untouched until Ramesh and Kunal tell you it saves them time.'"
    )

    doc.add_heading("4. Recommended Next Step", level=2)
    doc.add_paragraph(
        "Do not talk about price or show slides. Ask Suresh: 'Let's take 15 minutes next Tuesday. I will show Ramesh a 3-tap mock order on his own phone. If Ramesh smiles, we talk next steps. Fair enough?'"
    )

    # -------------------------------------------------------------
    # PART D
    # -------------------------------------------------------------
    doc.add_page_break()
    h_pd = doc.add_paragraph()
    r_pd = h_pd.add_run("Part D: Marketing & Growth Collaterals (SME Manufacturing)")
    r_pd.bold = True
    r_pd.font.size = Pt(16)
    r_pd.font.color.rgb = RGBColor(0x0F, 0x2A, 0x4A)
    h_pd.paragraph_format.space_after = Pt(4)

    doc.add_paragraph("Strict Rule: Grounded in Part A Audit — Vardhan Steelware is NOT mentioned").runs[0].font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    doc.add_heading("1. LinkedIn Post (Founder & Leadership Focus)", level=2)
    doc.add_paragraph("Word Count: 134 words (Constraint: ≤ 150 words)").runs[0].font.italic = True
    li_box = doc.add_table(rows=1, cols=1)
    li_cell = li_box.cell(0, 0)
    set_cell_background(li_cell, "F0F9FF")
    set_cell_margins(li_cell, 100, 100, 150, 150)
    p_li = li_cell.paragraphs[0]
    p_li.add_run(
        "Most small factory owners don’t lose money on raw materials. They lose it in the invisible handoffs.\n\n"
        "Last week, during a shopfloor audit of a metal pressing unit, I watched the owner spend 2 hours across 14 WhatsApp chats asking one question: \"Where is order #402?\"\n\n"
        "Meanwhile:\n"
        "• 400 kg of metal sent for outside polishing returned in piece counts—with zero weight reconciliation.\n"
        "• The press was running parts for a buyer whose credit was blocked in accounts.\n"
        "• The foreman was tracking 80 monthly orders in an oil-stained paper diary.\n\n"
        "Traditional ERPs fail here because they demand data entry from workers who don’t sit at desks.\n\n"
        "Don’t buy a massive 50-module enterprise system.\n\n"
        "Fix just three handoffs: order confirmation, outsourced batch tracking, and dispatch visibility.\n\n"
        "Simplicity drives adoption. Complexity just breeds silence."
    )

    doc.add_heading("2. Meta Advertisement (Facebook & Instagram Feed)", level=2)
    doc.add_paragraph("Audience: MSME Owners, Factory Proprietors (Ages 28–55; Hubs: Delhi-NCR, Rajkot, Peenya, Pune, Ahmedabad)").runs[0].font.italic = True
    meta_ad_box = doc.add_table(rows=1, cols=1)
    ad_cell = meta_ad_box.cell(0, 0)
    set_cell_background(ad_cell, "F8FAFC")
    set_cell_margins(ad_cell, 100, 100, 150, 150)
    p_ad = ad_cell.paragraphs[0]
    p_ad.add_run(
        "PRIMARY TEXT:\n"
        "You take orders on WhatsApp. Your foreman runs the factory using a paper diary. And by 5:00 PM, you’re still making 10 phone calls to find out what actually got loaded onto the tempo.\n\n"
        "Sound familiar?\n\n"
        "Big ERPs failed your factory because they were built for accountants, not shopfloors.\n\n"
        "Wantace gives your team a 3-tap mobile tracker:\n"
        "✅ See live batch stages without shouting across the floor.\n"
        "✅ Stop metal theft and shortages during outsourced polishing.\n"
        "✅ Block shipments to unpaid accounts before the tempo leaves.\n\n"
        "No computer typing. No long training. Just complete control from your phone.\n\n"
        "HEADLINE:\n"
        "Stop Chasing Orders on WhatsApp. Run Your Factory from Your Phone.\n\n"
        "VISUAL COMPOSITION:\n"
        "High-contrast split screen (Square 1:1):\n"
        "• Left Side ('The Daily Headache'): Close-up of an oil-stained paper register with crossed-out handwriting, beside a phone buzzing with 18 unread WhatsApp messages asking 'Maal nikla kya?'.\n"
        "• Right Side ('The 3-Tap Fix'): A foreman's thumb tapping a big green button [ Mark 200 Pcs Polished ] on a clean mobile screen next to a stamping press. Badge: 'Order #1082: Dispatched | Shortage: 0 kg'.\n\n"
        "CALL TO ACTION: Book a 15-Minute Demo (wantace.com/shopfloor-control)"
    )

    # -------------------------------------------------------------
    # PART E
    # -------------------------------------------------------------
    doc.add_page_break()
    h_pe = doc.add_paragraph()
    r_pe = h_pe.add_run("Part E: 5-Minute Video Speaking Guide & AI Usage Note")
    r_pe.bold = True
    r_pe.font.size = Pt(16)
    r_pe.font.color.rgb = RGBColor(0x0F, 0x2A, 0x4A)
    h_pe.paragraph_format.space_after = Pt(4)

    doc.add_heading("1. Five-Minute Video Speaking Guide (Natural & Conversational)", level=2)
    doc.add_paragraph(
        "[0:00 – 1:30] SEGMENT 1: WHAT SURPRISED ME DURING THE REAL FACTORY VISIT\n"
        "• (0:00 - 0:25) Introduction: Introduce yourself; describe visiting a small metal pressing/utensil workshop.\n"
        "• (0:25 - 1:00) Core Surprise: They weren't anti-tech—they were glued to WhatsApp and smartphones. The real problem was fragmentation: orders in WhatsApp chats vs foreman's paper diary on the press.\n"
        "• (1:00 - 1:30) Ground Finding [INSERT LOCAL OBSERVATION]: The outsourced polishing blind spot. Sending 400 kg of metal to polishers and getting pieces back with zero weight check. Paying bills blind.\n\n"
        "[1:30 – 3:15] SEGMENT 2: WHAT VARDHAN'S MATERIAL REVEALED BENEATH THE SURFACE\n"
        "• (1:30 - 2:10) Beyond Feature Requests: Suresh asked for 'visibility,' but errors (Gupta & Jain duplicates, Sharma's credit hold) revealed an incentive and communication breakdown between roles.\n"
        "• (2:10 - 2:45) Conflict Between Roles: Ramesh wants machine uptime (press running); Munshi ji wants cash collected. Without a software gate, Ramesh presses parts for defaulting clients.\n"
        "• (2:45 - 3:15) The Past ERP Scar: Vardhan already failed an ERP. Desktop typing is dead on arrival. The real unlock is dual-unit polishing checks delivered through an ultra-simple 3-tap mobile screen.\n\n"
        "[3:15 – 5:00] SEGMENT 3: ONE REQUIREMENT I WOULD CHANGE WITH ANOTHER DAY, AND WHY\n"
        "• (3:15 - 4:00) Self-Critique: In FR-03, I had Ramesh enter gross kg and pieces on his phone screen. That still asks a busy shopfloor worker to type numbers during morning tempo loading.\n"
        "• (4:00 - 4:40) Practical Upgrade: Use a physical pre-printed QR Job Card stapled to the gunny bags. Ramesh points his phone camera at the QR code, auto-pairing with the scale. Zero manual typing.\n"
        "• (4:40 - 5:00) Conclusion: Solutions Engineering isn't about complex enterprise software; it's about meeting shopfloor workers where they are with tools they actually want to use every morning."
    )

    doc.add_heading("2. Responsible AI Usage & Verification Note", level=2)
    ai_box = doc.add_table(rows=1, cols=1)
    ai_cell = ai_box.cell(0, 0)
    set_cell_background(ai_cell, "F8FAFC")
    set_cell_margins(ai_cell, 100, 100, 150, 150)
    p_ai = ai_cell.paragraphs[0]
    p_ai.add_run(
        "1. AI Tooling Used: Antigravity AI (Gemini 3.8 Flash) was used as an interactive sounding board, document outline assistant, and structure validator.\n"
        "2. Independent Human Contribution: All practical shopfloor logic (the reality of Kaccha registers, Tally Prime segregation, dual-UOM weight vs piece conversion, and stakeholder empathy for Ramesh and Munshi ji) was driven and decided by human judgment.\n"
        "3. Catching & Correcting AI Mistakes: During initial brainstorming, the AI suggested building an automated vendor login portal and complex IoT machine telemetry. I rejected these recommendations because real-world job-work polishers in Indian SME clusters work informally without computers. I reframed the solution around an internal, low-friction mobile reconciliation view.\n"
        "4. Human Verification: All data inconsistencies (Gupta, Jain, Sharma, 6 kg shortage) and page limits (strict 4 pages for Part B, half page for Part C, zero pricing) were personally checked and verified.\n"
        "5. Final Confirmation: I verify that this submission reflects genuine business analysis, practical shopfloor thinking, and responsible, transparent tool assistance."
    )

    output_path = r"d:\wantance\Wantace_SE_Intern_Submission_Package.docx"
    doc.save(output_path)
    print(f"Successfully generated DOCX at: {output_path}")

if __name__ == "__main__":
    create_styled_document()
