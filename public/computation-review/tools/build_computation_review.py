#!/usr/bin/env python3
"""Computation-screen review page — same grammar as the FTA-audit digest (fixed left index, one view
at a time, per-cell / per-decision screen, comments to Supabase via comments-config.js with local
fallback + export, progress bar). Output: ../index.html.

Comments backend: its OWN table `computation_review_comments` (NOT the FTA table), same column schema
+ same project/URL/key, page id 'computation-review-2026-08', INSERT-only (a re-answer appends, never
overwrites). Adapter code is the FTA digest's, reused.

Screenshots: real-stack PNGs under ../img/{nonfz,fz}/, converted to .jpg at build; only files that
exist are referenced (graceful if a variant/crop is missing)."""
import re, json, os, csv, glob, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from computation_context import (CELLS, CELL_Q_CORRECT, CELL_Q_MODE, MAP_DECISIONS, MAP_GROUPS,
                                 SOLID, GLOSSARY, SECTIONS_GUIDE, IMG_CAPTIONS, BAND_IMG, FZ_CELL_IMG)

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(BASE, 'index.html')
IMG = os.path.join(BASE, 'img')
REPLICA_CSV = '/Users/mayureshsoni/Projects/nexdigm-corporate-tax-uae-wrapper/documents/computation-screen-replica-2026-08-16.csv'

BANDS = [('income', 'Income & accounting base'), ('addbacks', 'Add-backs'),
         ('deductions', 'Deductions & reliefs'), ('tax', 'Taxable income & tax'),
         ('other', 'On-screen (non-ladder)')]

# ---- screenshots are referenced as PNG directly (flat UI: smaller + sharper on text than JPEG) ----
def have(rel):  # rel is a .png relative path under img/
    return os.path.exists(os.path.join(IMG, rel))

def imgs_for_cell(c):
    want = list(BAND_IMG.get(c['band'], []))
    if c['id'] in FZ_CELL_IMG:
        want = FZ_CELL_IMG[c['id']] + want
    want.append('nonfz/comp-full.png' if c['variant'] != 'FZ' else 'fz/comp-full.png')
    seen, out = set(), []
    for w in want:
        if w not in seen and have(w):
            seen.add(w); out.append(w)
    return out

# ---- the full replica table (reference) ------------------------------------------------------------
replica_rows = []
if os.path.exists(REPLICA_CSV):
    with open(REPLICA_CSV, encoding='utf-8') as fh:
        for r in csv.DictReader(fh):
            replica_rows.append(r)

captions = {k: v for k, v in IMG_CAPTIONS.items() if have(k)}
all_imgs = [k for k in IMG_CAPTIONS if have(k)]

data = dict(
    meta=dict(date='2026-08-20 (v2 — your 17-18 Aug answers fed in)', screen='/staff/filings/:id/computation',
              build='origin/main fe853fc0, 20-Aug (money wave M1-M4 live; screenshots = the 16-Aug build)',
              src1='computation-screen-replica-2026-08-16.md', src2='return-to-computation-mapping-table-2026-08-16.md'),
    cells=CELLS, cellQcorrect=CELL_Q_CORRECT, cellQmode=CELL_Q_MODE,
    decisions=MAP_DECISIONS, mapgroups=MAP_GROUPS, bands=BANDS,
    solid=SOLID, glossary=GLOSSARY, sections=SECTIONS_GUIDE,
    captions=captions, allimgs=all_imgs, replica=replica_rows,
    imgmap={c['id']: imgs_for_cell(c) for c in CELLS},
    haveShots=bool(all_imgs))

CSS = r"""
:root{--bg:#f6f7f9;--card:#fff;--ink:#17202f;--muted:#5d6879;--line:#e2e6ee;--accent:#0f5fb4;--accent2:#e8f0fb;--warn:#b45309;--bad:#b91c1c;--good:#15803d;--chip:#eef1f6;--side:#0b1f3a}
*{box-sizing:border-box}html,body{height:100%}body{margin:0;font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--ink);background:var(--bg);display:flex}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}code{font:12.5px/1.4 ui-monospace,Menlo,monospace;background:var(--chip);padding:1px 4px;border-radius:4px}
aside{width:310px;flex:none;background:var(--side);color:#dbe4f3;height:100vh;position:sticky;top:0;overflow-y:auto;padding:18px 14px;display:flex;flex-direction:column;gap:4px}
aside h1{font-size:15px;margin:0 0 2px;color:#fff;font-weight:650;line-height:1.3}aside .sub{font-size:12px;color:#9fb1cc;margin-bottom:8px}
aside .grp{font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:#8ea2c2;margin:12px 6px 3px}
aside .grp.sub2{margin:7px 6px 2px 6px;color:#7d93b6;text-transform:none;letter-spacing:0;font-size:11.5px;font-style:italic}
aside a.nav{display:block;padding:6px 9px;border-radius:8px;color:#dbe4f3;font-size:13.5px;line-height:1.35}aside a.nav:hover{background:#163257;text-decoration:none}aside a.nav.on{background:#1f4a86;color:#fff}
aside a.nav .d{display:block;font-size:11.5px;color:#9fb1cc;margin-top:1px}aside a.nav.on .d{color:#c9d8f0}
aside a.nav.cell{padding:5px 9px 5px 30px;position:relative}aside a.nav.cell .b{position:absolute;left:8px;top:6px;width:16px;height:16px;border-radius:50%;background:#2b4c7e;color:#fff;font-size:10px;display:flex;align-items:center;justify-content:center}
aside a.nav.cell.done .b{background:var(--good)}
aside .prog{margin:8px 6px;font-size:12px;color:#c9d8f0}aside .prog .bar{height:6px;background:#1c3660;border-radius:4px;overflow:hidden;margin-top:4px}aside .prog .bar i{display:block;height:100%;background:#22c55e;width:0}
aside .cst{margin-top:auto;font-size:11.5px;color:#9fb1cc;padding:8px 6px;border-top:1px solid #1c3660}
main{flex:1;min-width:0;padding:22px 34px 90px;max-width:1120px}
.view{display:none}.view.on{display:block}
h2{font-size:22px;margin:0 0 6px;font-weight:660}h3{font-size:15px;margin:18px 0 6px;font-weight:650;color:#0f2b52}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:12px 0;box-shadow:0 1px 2px rgba(16,24,40,.04)}
.val.upd{background:#fffbeb;border:1px solid #fde68a;border-radius:8px;padding:8px 10px}
.val.ruled{background:#f0fdf4;border:1px solid #86efac;border-radius:8px;padding:8px 10px}
.k.kupd{color:#b45309}.k.kruled{color:#15803d}
aside a.nav.cell.ruled .b{background:#15803d}
.chip{display:inline-block;padding:3px 10px;border-radius:999px;font-size:12.5px;font-weight:600;background:var(--chip);color:var(--ink);white-space:nowrap}
.chip.ro{background:#e5e7eb;color:#374151}.chip.ed{background:#dcfce7;color:var(--good)}.chip.warn{background:#fef3c7;color:var(--warn)}.chip.fz{background:#ede9fe;color:#5b21b6}.chip.cls{background:#e0e7ff;color:#3730a3}
.imp{background:#fee2e2;color:var(--bad)}.imp.m{background:#fef3c7;color:var(--warn)}.imp.l{background:#e5e7eb;color:#374151}
.muted{color:var(--muted)}.small{font-size:13px}.foot{font-size:11.5px;color:#8b95a6;margin-top:6px}.foot code{font-size:11px;background:#f0f2f6}
.blk{display:grid;grid-template-columns:158px 1fr;gap:9px 14px;margin:8px 0}.blk .k{font-weight:650;color:#0f2b52;font-size:13.5px;padding-top:2px}.blk .k span{display:block;font-weight:400;color:var(--muted);font-size:11.5px}
.blk .val{background:#fbfcfe;border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.blk .val.logic{border-left:4px solid #0f5fb4}.blk .val.today{border-left:4px solid #7c3aed}.blk .val.feeds{border-left:4px solid #0891b2}.blk .val.open{border-left:4px solid #b45309}
.q{background:#eef6ff;border:1px solid #bfd7f5;border-radius:12px;padding:14px 16px;margin:14px 0}.q .qq{font-weight:650;font-size:16px;color:#0b3a73}
.thumbs{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0}.thumbs a{display:block;width:200px;border:1px solid var(--line);border-radius:8px;overflow:hidden;background:#fff}.thumbs a img{display:block;width:100%;height:120px;object-fit:cover;object-position:top}.thumbs a span{display:block;font-size:11px;padding:4px 6px;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.callbox{border:1px dashed #9db4d6;border-radius:12px;padding:12px 14px;background:#fff}
.callbox .qlabel{font-weight:650;font-size:13.5px;color:#0f2b52;margin:8px 0 3px}
.callbox .opts{display:flex;flex-direction:column;gap:5px;margin:4px 0 6px}.callbox .opts label{display:flex;gap:8px;align-items:flex-start;font-size:14px;cursor:pointer}
.callbox textarea{width:100%;min-height:60px;border:1px solid var(--line);border-radius:8px;padding:8px;font:inherit;font-size:14px}
.callbox input[type=text]{border:1px solid var(--line);border-radius:8px;padding:7px 9px;font:inherit;font-size:14px}
.callbox input.scf{width:100%;margin:2px 0 4px}
.row{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-top:8px}
button.btn{border:1px solid var(--accent);background:var(--accent);color:#fff;border-radius:8px;padding:8px 14px;font:inherit;font-size:14px;cursor:pointer}button.btn.sec{background:#fff;color:var(--accent)}
.clist{margin-top:8px}.clist .c{border-left:3px solid var(--accent);background:#f3f7fd;padding:6px 10px;margin:6px 0;border-radius:6px;font-size:13.5px}.c .who{font-weight:600}.c .when{color:var(--muted);font-size:12px;margin-left:6px}
.pager{display:flex;justify-content:space-between;margin:16px 0;gap:8px}
table.reg{width:100%;border-collapse:collapse;font-size:12.5px}table.reg th,table.reg td{border-bottom:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}table.reg th{background:#f1f4f9;position:sticky;top:0}
.tblwrap{overflow-x:auto;background:#fff;border:1px solid var(--line);border-radius:12px;max-height:78vh;overflow-y:auto}
#lb{position:fixed;inset:0;background:rgba(0,0,0,.86);display:none;z-index:50;overflow:auto;padding:24px}#lb.on{display:block}#lb img{max-width:100%;display:block;margin:0 auto;background:#fff}#lb .cap{color:#fff;text-align:center;margin:8px 0 12px;font-size:14px}#lb .x{position:fixed;top:12px;right:16px;color:#fff;font-size:28px;cursor:pointer}
.banner{background:#fff7ed;border:1px solid #fed7aa;color:#7c2d12;border-radius:10px;padding:10px 12px;font-size:13.5px;margin:10px 0}
.noshot{background:#f1f4f9;border:1px dashed var(--line);border-radius:8px;padding:8px 10px;color:var(--muted);font-size:12.5px;margin:8px 0}
@media(max-width:900px){body{display:block}aside{position:relative;height:auto;width:auto}main{padding:16px}.blk{grid-template-columns:1fr}.thumbs a{width:150px}}
@media print{aside,.callbox button,#lb{display:none}.view{display:block!important}}
"""

JS = r"""
const D=window.CR_DATA; const $=(s,el=document)=>el.querySelector(s); const $$=(s,el=document)=>Array.from(el.querySelectorAll(s));
function esc(s){return String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
function md(s){let h=esc(s);h=h.replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\*\*([^*]+)\*\*/g,'<b>$1</b>').replace(/\*([^*\n]+)\*/g,'<i>$1</i>');const L=h.split('\n');let o='',ul=false;for(const ln of L){if(/^\s*[-•]\s+/.test(ln)){if(!ul){o+='<ul>';ul=true;}o+='<li>'+ln.replace(/^\s*[-•]\s+/,'')+'</li>';}else{if(ul){o+='</ul>';ul=false;}if(ln.trim())o+='<p>'+ln+'</p>';}}if(ul)o+='</ul>';return o;}
function modeChip(m){let cls='ro';if(/blank/i.test(m))cls='ed';else if(/pre-filled|editable/i.test(m))cls='ed';else if(/NO source|disabled/i.test(m))cls='warn';return `<span class="chip ${cls}">${esc(m)}</span>`;}
function thumbs(list){return list&&list.length?`<div class="thumbs">${list.map(e=>`<a href="#" onclick="return lb('${e}')"><img loading="lazy" src="img/${e}" alt=""><span>${esc((D.captions[e]||e.split('/').pop()).slice(0,64))}</span></a>`).join('')}</div>`:'';}
// ---- comments backend (Supabase REST) with local fallback — reused from the FTA digest -----------
const CFG=window.CR_COMMENTS||null; const LS='computation-review-comments-v1'; let remote=[]; let live=false;
const loadLocal=()=>{try{return JSON.parse(localStorage.getItem(LS)||'[]');}catch(e){return[];}}; const saveLocal=a=>localStorage.setItem(LS,JSON.stringify(a));
const hdr=()=>({apikey:CFG.key,Authorization:'Bearer '+CFG.key,'Content-Type':'application/json'});
async function remoteFetch(){ if(!CFG||!CFG.url||!CFG.key) return; try{const r=await fetch(`${CFG.url}/rest/v1/${CFG.table}?page=eq.${encodeURIComponent(CFG.page)}&order=created_at.asc&select=*`,{headers:hdr()}); if(r.ok){remote=await r.json(); live=true;} else live=false;}catch(e){live=false;} status(); }
async function remotePost(c){ if(!CFG||!CFG.url||!CFG.key) return false; try{const r=await fetch(`${CFG.url}/rest/v1/${CFG.table}`,{method:'POST',headers:{...hdr(),Prefer:'return=minimal'},body:JSON.stringify({page:CFG.page,anchor:c.anchor,section:c.section||null,commenter:c.who,choice:c.choice||null,body:c.text||''})}); return r.ok;}catch(e){return false;} }
async function syncPending(){ const a=loadLocal(); let ch=false; for(const c of a){ if(!c.synced){ if(await remotePost(c)){c.synced=true;ch=true;} } } if(ch) saveLocal(a); }
function all(anchor){ const rem=remote.filter(c=>c.anchor===anchor).map(c=>({anchor:c.anchor,who:c.commenter,text:c.body,choice:c.choice,when:c.created_at,synced:true})); const loc=loadLocal().filter(c=>c.anchor===anchor&&!c.synced); return [...rem,...loc]; }
function status(){ const el=$('#cst'); if(!el) return; const pend=loadLocal().filter(c=>!c.synced).length; el.innerHTML = live? `● Answers save to the shared database${pend?` · ${pend} pending sync`:''}` : (CFG&&CFG.url? `● Database not reachable — answers kept on this device${pend?` (${pend})`:''}; they sync automatically when it is back` : `● Answers are kept on this device — use "Export my answers" to send them`) + `<br><a href="#" id="exp" style="color:#c9d8f0">Export my answers</a>`; $('#exp')&&$('#exp').addEventListener('click',e=>{e.preventDefault();exportAll();}); }
function renderC(anchor,el){ const l=all(anchor); el.innerHTML=l.length?l.map(c=>`<div class="c"><span class="who">${esc(c.who||'Anonymous')}</span>${c.choice?` <span class="chip">${esc(c.choice)}</span>`:''}<span class="when">${esc((c.when||'').toString().slice(0,16).replace('T',' '))}${c.synced?' · saved':' · on this device'}</span>${c.text?`<div>${esc(c.text).replace(/\n/g,'<br>')}</div>`:''}</div>`).join(''):`<div class="small muted">No answer yet.</div>`; }
// simple option box (mapping decisions + reference comments)
function callbox(anchor,section,label,options){ const id='cb-'+anchor.replace(/[^a-z0-9]/gi,'_'); return `<div class="callbox" data-anchor="${esc(anchor)}" data-section="${esc(section||'')}" data-kind="opt"><div class="qlabel">${esc(label)}</div>${options&&options.length?`<div class="opts">${options.map(o=>`<label><input type="radio" name="${id}" value="${esc(o)}"> ${esc(o)}</label>`).join('')}</div>`:''}<textarea placeholder="Your comment / ruling / condition (optional if you picked an option)…"></textarea><div class="row"><input type="text" class="who" placeholder="Your name" value="${esc(localStorage.getItem('cr-who')||'')}"><button class="btn save">Save answer</button><span class="small muted saved"></span></div><div class="clist"></div></div>`; }
// per-cell box: three questions (correct? / should come from / read-only or editable) + comment
function cellbox(anchor,section){ const id='cb-'+anchor.replace(/[^a-z0-9]/gi,'_'); const rc=D.cellQcorrect,rm=D.cellQmode;
  return `<div class="callbox" data-anchor="${esc(anchor)}" data-section="${esc(section||'')}" data-kind="cell">
  <div class="qlabel">1 · Is the logic correct?</div><div class="opts">${rc.map(o=>`<label><input type="radio" name="${id}-c" value="${esc(o)}"> ${esc(o)}</label>`).join('')}</div>
  <div class="qlabel">2 · Where should this cell come from?</div><input type="text" class="scf" placeholder="e.g. keep as-is · a named schedule · a specific return line …">
  <div class="qlabel">3 · Read-only or editable?</div><div class="opts">${rm.map(o=>`<label><input type="radio" name="${id}-m" value="${esc(o)}"> ${esc(o)}</label>`).join('')}</div>
  <div class="qlabel">Comment (optional)</div><textarea placeholder="Anything else…"></textarea>
  <div class="row"><input type="text" class="who" placeholder="Your name" value="${esc(localStorage.getItem('cr-who')||'')}"><button class="btn save">Save answer</button><span class="small muted saved"></span></div><div class="clist"></div></div>`; }
function wire(){ $$('.callbox').forEach(box=>{ const anchor=box.dataset.anchor, section=box.dataset.section, kind=box.dataset.kind; const list=$('.clist',box); renderC(anchor,list);
  $('.save',box).addEventListener('click',async()=>{ const who=$('.who',box).value.trim(); if(!who){alert('Please add your name so we know who answered.');$('.who',box).focus();return;} localStorage.setItem('cr-who',who);
    let choice='',text='';
    if(kind==='cell'){ const c=($('input[name$="-c"]:checked',box)||{}).value||''; const scf=$('.scf',box).value.trim(); const m=($('input[name$="-m"]:checked',box)||{}).value||''; const cm=$('textarea',box).value.trim();
      if(!c&&!scf&&!m&&!cm){alert('Answer at least one of the three questions, or add a comment.');return;}
      choice=c||''; const parts=[]; if(c)parts.push('Correct?: '+c); if(scf)parts.push('Should come from: '+scf); if(m)parts.push('Mode: '+m); if(cm)parts.push('Comment: '+cm); text=parts.join('\n'); }
    else { choice=($('input[type=radio]:checked',box)||{}).value||''; text=$('textarea',box).value.trim(); if(!choice&&!text){alert('Pick an option or write a comment.');return;} }
    const c={anchor,section,who,text,choice,when:new Date().toISOString(),synced:false}; const ok=await remotePost(c); c.synced=ok; const a=loadLocal(); a.push(c); saveLocal(a);
    if(kind==='cell'){$$('.scf,textarea',box).forEach(f=>f.value='');} else {$('textarea',box).value='';}
    $('.saved',box).textContent=ok?'Saved to the shared database ✓':'Saved on this device ✓ (will sync / export)'; if(ok) await remoteFetch(); renderC(anchor,list); status(); markDone(); }); }); }
function answeredSet(){ return new Set([...remote.map(c=>c.anchor),...loadLocal().map(c=>c.anchor)]); }
function markDone(){ const A=answeredSet(); let n=0; const total=D.cells.length+D.decisions.filter(d=>!d.answered).length;
  D.cells.forEach(c=>{const on=A.has('cell:'+c.id); if(on)n++; const a=$(`a.nav[data-view="cell-${c.id}"]`); a&&a.classList.toggle('done',on);});
  D.decisions.forEach(d=>{const on=A.has('map:'+d.id); if(on&&!d.answered)n++; const a=$(`a.nav[data-view="map-${d.id}"]`); a&&a.classList.toggle('done',on);});
  const p=$('#prog'); if(p){p.querySelector('span').textContent=`${n} of ${total} answered`; p.querySelector('i').style.width=(100*n/total)+'%';} }
function exportAll(){ const a=[...remote.map(c=>({anchor:c.anchor,who:c.commenter,choice:c.choice,text:c.body,when:c.created_at})),...loadLocal().filter(c=>!c.synced)]; const lines=['# Computation review — answers export','','Exported: '+new Date().toISOString(),'']; a.forEach(c=>lines.push(`- **${c.anchor}** · ${c.who} · ${c.when}${c.choice?' · **'+c.choice+'**':''}\n  ${(c.text||'').replace(/\n/g,'\n  ')}`)); const txt=lines.join('\n')+'\n\n```json\n'+JSON.stringify(a,null,1)+'\n```\n'; const blob=new Blob([txt],{type:'text/markdown'}); const u=URL.createObjectURL(blob); const l=document.createElement('a'); l.href=u; l.download='computation-review-answers-'+new Date().toISOString().slice(0,10)+'.md'; document.body.appendChild(l); l.click(); l.remove(); navigator.clipboard&&navigator.clipboard.writeText(txt).catch(()=>{}); alert('Answers exported (downloaded + copied). Please send the file to Mayuresh.'); }
// ---- views ----
function shotsBlock(list){ return list&&list.length? thumbs(list) : (D.haveShots? '' : `<div class="noshot">Screenshot not captured for this cell in this build. See the full-page shot under "What our screen looks like" if present.</div>`); }
function cellView(c,i){ const cells=D.cells; const prev=cells[i-1],next=cells[i+1]; const bandName=(D.bands.find(b=>b[0]===c.band)||[])[1]||''; const imgs=D.imgmap[c.id]||[];
 const vchip = c.variant==='FZ'?'<span class="chip fz">Free-Zone only</span>':'<span class="chip">Both variants</span>';
 const kls = c.klass?`<span class="chip cls">Class ${esc(c.klass)}</span>`:'';
 return `<section class="view" id="v-cell-${c.id}"><div class="small muted">Cell ${i+1} of ${cells.length} · ${esc(bandName)} · ${vchip} ${kls}</div>
 <h2>${esc(c.code)} — ${esc(c.label)}</h2>
 <div class="card"><div class="blk">
  <div class="k">Today's treatment <span>what the build does now</span></div><div class="val today">${modeChip(c.mode_today)}</div>
  <div class="k">What it does <span>in plain words</span></div><div class="val logic">${md(c.logic)}</div>
  <div class="k">Feeds in / out <span>return lines & downstream</span></div><div class="val feeds"><b>In:</b> ${md(c.feeds_in)}<br><b>Out:</b> ${md(c.feeds_out)}</div>
  ${c.update?`<div class="k kupd">Since 16-Aug</div><div class="val upd">${md(c.update)}</div>`:''}
  ${c.open?`<div class="k">Known open question</div><div class="val open">${md(c.open)}</div>`:''}
 </div>${shotsBlock(imgs)}<div class="foot">Source: <code>${esc(c.src)}</code> · computation-screen-replica-2026-08-16.md</div>
 <div class="q"><div class="qq">Your call — three questions</div>${cellbox('cell:'+c.id,bandName)}</div></div>
 <div class="pager">${prev?`<button class="btn sec" onclick="go('cell-${prev.id}')">← ${esc(prev.code)}</button>`:`<button class="btn sec" onclick="go('start')">← Start</button>`}${next?`<button class="btn" onclick="go('cell-${next.id}')">${esc(next.code)} →</button>`:`<button class="btn" onclick="go('map-'+D.decisions[0].id)">On to the mapping proposal →</button>`}</div></section>`; }
function mapView(d,i){ const ds=D.decisions; const prev=ds[i-1],next=ds[i+1]; const gname=(D.mapgroups.find(g=>g[0]===d.group)||[])[1]||'';
 return `<section class="view" id="v-map-${d.id}"><div class="small muted">Mapping decision ${i+1} of ${ds.length} · ${esc(gname)} · covers ${esc(d.covers)}</div>
 <h2>${esc(d.title)}</h2>
 <div class="card"><div class="blk">
  <div class="k">The line</div><div class="val">${md(d.line)}</div>
  <div class="k">Today <span>what the build does</span></div><div class="val today">${md(d.today)}</div>
  <div class="k">Hint / precedent</div><div class="val feeds">${md(d.hint)}</div>
  ${d.update?`<div class="k kupd">Since 16-Aug</div><div class="val upd">${md(d.update)}</div>`:''}
  ${d.answered?`<div class="k kruled">Already ruled ✓</div><div class="val ruled">${md(d.answered)}</div>`:''}
 </div><div class="foot">Source: <code>${esc(d.src)}</code> · return-to-computation-mapping-table-2026-08-16.md</div>
 ${d.answered?`<div class="q"><div class="qq">No answer needed</div><p class="small muted">This one is settled by your own answer above — it is shown so nothing moves without you seeing it. Comment only if you disagree.</p>${callbox('map:'+d.id,gname,'Comment (only if you disagree)',["I disagree — reopen (say why below)"])}</div>`:`<div class="q"><div class="qq">Your call</div><p>${md(d.question)}</p>${callbox('map:'+d.id,gname,'Answer',d.options)}</div>`}</div>
 <div class="pager">${prev?`<button class="btn sec" onclick="go('map-${prev.id}')">← Prev</button>`:`<button class="btn sec" onclick="go('cell-${D.cells[D.cells.length-1].id}')">← Last cell</button>`}${next?`<button class="btn" onclick="go('map-${next.id}')">Next →</button>`:`<button class="btn" onclick="go('solid')">Done — see what's solid →</button>`}</div></section>`; }
function render(){
  // nav
  let nav=`<a class="nav" data-view="start" href="#start">Start here<span class="d">${esc(D.sections[0][2])}</span></a>`;
  nav+=`<div class="grp">The 30 cells — answer each</div>`;
  D.bands.forEach(([bid,bname])=>{ const cs=D.cells.filter(c=>c.band===bid); if(!cs.length)return; nav+=`<div class="grp sub2">${esc(bname)}</div>`+cs.map(c=>`<a class="nav cell" data-view="cell-${c.id}" href="#cell-${c.id}"><span class="b">${esc(c.code.replace(/[^0-9QN]/g,'').slice(0,3)||'•')}</span>${esc(c.code)} · ${esc(c.label)}</a>`).join(''); });
  nav+=`<div class="prog" id="prog"><span>0 answered</span><div class="bar"><i></i></div></div>`;
  nav+=`<div class="grp">Mapping proposal (${D.decisions.length})</div>`;
  D.mapgroups.forEach(([gid,gname])=>{ const dd=D.decisions.filter(d=>d.group===gid); if(!dd.length)return; nav+=`<div class="grp sub2">${esc(gname)}</div>`+dd.map(d=>`<a class="nav cell${d.answered?' ruled':''}" data-view="map-${d.id}" href="#map-${d.id}"><span class="b">${d.answered?'✓':esc(d.id.replace(/[^0-9]/g,'')||'•')}</span>${esc(d.id)} · ${esc(d.title.replace(/^[^·]*·\s*/,'').slice(0,52))}</a>`).join(''); });
  nav+=`<div class="grp">Reference</div>`;
  D.sections.slice(3).forEach(([id,name,desc])=>{ nav+=`<a class="nav" data-view="${id}" href="#${id}">${esc(name)}<span class="d">${esc(desc)}</span></a>`; });
  $('#nav').innerHTML=nav;
  // views
  let v=`<section class="view" id="v-start"><h2>Start here</h2><div class="card">
  <p><b>What this is.</b> A top-to-bottom transcription of our built <b>Computation of Income</b> screen (<code>${esc(D.meta.screen)}</code>) — one card per line the preparer sees, in render order, with the exact logic behind each cell and a real screenshot to point at. It is built from the code we ship (build ${esc(D.meta.build)}), not a prototype. Your job: for each cell, say whether the logic is <b>right</b>, where it should <b>come from</b>, and whether it should be <b>read-only or editable</b>.</p>
  <h3>Where things stand — updated 20-Aug</h3>
  <div class="val ruled" style="margin:8px 0"><b>What we already know (fed in, nothing re-asked).</b> Your 17-18 Aug answers on the FTA-audit page became rulings and most are ALREADY BUILT: transitional excluded gains → computation (live) · Section-F feeds incl. QIF lines (live) · Qualifying-Group relief → C12 (live) · interest-cap inputs — income box, b/f + expired feed, bank/insurer gate (live) · TP upward auto-fill (building) · tax-loss formulas + QFZP split (ruled, building) · foreign-tax-credit per-stream cap (ruled, building) · S050 cumulative + rolling average (ruled). Decisions settled by those answers are marked <b>green ✓</b> in the left index — they need nothing from you.</div>
  <div class="val upd" style="margin:8px 0"><b>What we still need (the progress bar counts only these).</b> The 30 per-cell verdicts below, the still-open mapping decisions (equity-method, partnership and realisation-basis destinations · the QG #18 record · shipping double-surface · PE/FPE loss questions · UGL home · the Free-Zone sign map), and three NEW items from building your answers: <b>N-1</b> interest-cap day-count + first-year opening balances · <b>N-2</b> the Tax Loss Relief sheet presentation · <b>N-3</b> three feed signs to eyeball on the test portal.</div>
  <p class="small muted">The screenshots are from the 16-Aug build; the screen has since been reworked to your BRD shape (banners removed, the nine template notes render under the table, extract in the bottom bar) and the new QIF lines are not pictured — each affected card carries an amber "Since 16-Aug" note with what changed.</p>
  <h3>The three questions on every cell</h3>
  <div class="blk"><div class="k">1 · Correct?</div><div class="val">Is the logic behind the cell right — or wrong (say how)?</div>
  <div class="k">2 · Should come from?</div><div class="val">Where should the number originate — keep it as-is, a named schedule, or a specific return line?</div>
  <div class="k">3 · Read-only or editable?</div><div class="val">Should the preparer be able to type here — read-only (owned upstream), editable and pre-filled, or editable and blank?</div></div>
  <p class="small muted">Two chips you'll see: <span class="chip ro">Read-only</span> the number lives in one upstream place and can't be typed here · <span class="chip ed">Editable</span> you can type / overtype (pre-filled cells show an amber "schedule says X · Restore" strip when you override). "Class A/B/C", "seed", "feed", "gate" are all in the Glossary.</p>
  <h3>How to use this page</h3><p>Use the left index — it mirrors the screen's own order (Income &amp; accounting base → Add-backs → Deductions &amp; reliefs → Taxable income &amp; tax → the on-screen extras), then the <b>mapping proposal</b> (the auto-capture decisions — green ✓ ones are already ruled and need nothing), then the reference sections. Answer in place, add a line if you like, click <b>Save answer</b>. The progress bar on the left counts answered cells + decisions. Nothing is built until you have answered and Mayuresh confirms.</p>
  ${D.allimgs.length?`<h3>The screens we captured (real stack)</h3><p class="small muted">Full-page shots and per-band crops of our built Computation screen, plus the Return steps the figures come from — a fresh migrated database, the seeded Primary logged in through the real UI, zero injected data. Click any to zoom.</p>${thumbs(D.allimgs)}`:''}
  <div class="banner">Nothing here has been actioned. These annotations become rulings or build items only after your review. Where a line's destination is genuinely unpinned it is marked UNKNOWN — no cell was invented.</div>
  <div class="pager"><span></span><button class="btn" onclick="go('cell-${D.cells[0].id}')">Start with ${esc(D.cells[0].code)} →</button></div></div></section>`;
  D.cells.forEach((c,i)=>v+=cellView(c,i));
  D.decisions.forEach((d,i)=>v+=mapView(d,i));
  // solid
  v+=`<section class="view" id="v-solid"><h2>What's already correct</h2><p class="small muted">Cells whose logic is ruled and fed — the balanced picture.</p><div class="card"><ul>${D.solid.map(s=>`<li>${md(s)}</li>`).join('')}</ul></div><div class="pager"><button class="btn sec" onclick="go('map-'+D.decisions[D.decisions.length-1].id)">← Last decision</button><button class="btn sec" onclick="go('replica')">Full replica table →</button></div></section>`;
  // replica
  const cols=D.replica.length?Object.keys(D.replica[0]).slice(0,11):[];
  v+=`<section class="view" id="v-replica"><h2>Full replica table (reference)</h2><p class="small muted">Every cell with its logic, feeds and file:line — the CSV twin of the source replica. You do not need to read this; it is here so every claim on the cards traces to a line of code.</p><div class="tblwrap"><table class="reg"><thead><tr>${cols.map(c=>`<th>${esc(c)}</th>`).join('')}</tr></thead><tbody>${D.replica.map(r=>`<tr>${cols.map(c=>`<td>${esc(r[c]||'')}</td>`).join('')}</tr>`).join('')}</tbody></table></div></section>`;
  // glossary
  v+=`<section class="view" id="v-glossary"><h2>Glossary</h2><div class="card"><div class="blk">${D.glossary.map(([t,d])=>`<div class="k">${esc(t)}</div><div class="val">${md(d)}</div>`).join('')}</div></div></section>`;
  // sources
  v+=`<section class="view" id="v-sources"><h2>Sources &amp; method</h2><div class="card small">
  <p><b>Primary sources.</b> This page is generated from two code-faithful audit documents in the wrapper:</p>
  <ul><li><code>${esc(D.meta.src1)}</code> — the cell-by-cell replica of the built Computation screen (30 cells, logic + feeds + file:line per cell, open questions).</li>
  <li><code>${esc(D.meta.src2)}</code> — the return-to-computation auto-capture mapping (the 28 questions, the collisions, the unknown-destination cluster, the Free-Zone sign map).</li></ul>
  <p><b>Build of record.</b> ${esc(D.meta.build)}. The COI engine, the surface partition, the feed maps and the wire assembly are byte-identical across the small UI gap between the on-disk checkout and origin/main, so every logic claim holds and each is cited to a file:line.</p>
  <p><b>Screenshots.</b> Real-stack captures of our own built screen: a fresh migrated database, the seeded mapped Primary logged in through the real UI, zero injected data. ${D.haveShots?`${D.allimgs.length} screenshot(s) embedded.`:'No screenshots embedded in this build (the capture is reported separately).'}</p>
  <p><b>Comments.</b> Answers post to this page's own Supabase table <code>computation_review_comments</code> (separate from the FTA audit's table), page id <code>computation-review-2026-08</code>, insert-only. If the network is down they are kept in the browser and auto-sync on the next load; "Export my answers" (left panel) is the manual fallback. See README.md.</p></div></section>`;
  $('#views').innerHTML=v;
  wire(); status(); remoteFetch().then(()=>{syncPending().then(()=>{remoteFetch().then(()=>{$$('.callbox').forEach(b=>renderC(b.dataset.anchor,$('.clist',b)));markDone();});});}); markDone();
  go((location.hash||'#start').slice(1));
}
window.lb=function(e){$('#lb img').src='img/'+e;$('#lb .cap').textContent=(D.captions[e]||e);$('#lb').classList.add('on');return false;};
window.go=function(id){ if(!$('#v-'+id)) id='start'; $$('.view').forEach(x=>x.classList.remove('on')); $('#v-'+id).classList.add('on'); $$('aside a.nav').forEach(a=>a.classList.toggle('on',a.dataset.view===id)); if(location.hash!=='#'+id) history.replaceState(null,'','#'+id); window.scrollTo(0,0); const a=$(`aside a.nav.on`); a&&a.scrollIntoView({block:'nearest'}); };
window.addEventListener('hashchange',()=>go(location.hash.slice(1)));
document.addEventListener('DOMContentLoaded',()=>{render();$('#lb .x').addEventListener('click',()=>$('#lb').classList.remove('on'));$('#lb').addEventListener('click',ev=>{if(ev.target.id==='lb')$('#lb').classList.remove('on');});$$('aside a.nav').forEach(a=>a.addEventListener('click',ev=>{ev.preventDefault();go(a.dataset.view);}));});
"""

page = ("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
        "<title>Computation screen — Nexdigm CT product review</title>"
        f"<style>{CSS}</style><script src=\"comments-config.js\"></script></head><body>"
        f"<aside><h1>Computation of Income — screen review</h1><div class=\"sub\">Manthan review workbook · {data['meta']['date']} · build {data['meta']['build']}</div>"
        "<div id=\"nav\"></div><div class=\"cst\" id=\"cst\"></div></aside>"
        "<main id=\"views\"></main>"
        "<div id=\"lb\"><span class=\"x\">✕</span><div class=\"cap\"></div><img alt=\"screenshot\"></div>"
        f"<script>window.CR_DATA={json.dumps(data, ensure_ascii=False)};</script><script>{JS}</script></body></html>")

open(OUT, 'w', encoding='utf-8').write(page)
cfg = os.path.join(BASE, 'comments-config.js')
if not os.path.exists(cfg):
    open(cfg, 'w').write("window.CR_COMMENTS = { url: '', key: '', table: 'computation_review_comments', page: 'computation-review-2026-08' };\n")
print('written', OUT, os.path.getsize(OUT)//1024, 'KB;', len(CELLS), 'cells;', len(MAP_DECISIONS), 'decisions;',
      len(all_imgs), 'screenshots;', len(replica_rows), 'replica rows')
