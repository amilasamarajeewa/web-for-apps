async function loadApps(){
const grid=document.getElementById("grid"), updated=document.getElementById("updated");
try{
const r=await fetch("data/apps.json?"+Date.now(),{cache:"no-store"}); if(!r.ok) throw 0;
const d=await r.json(); grid.innerHTML="";
if(d.updated_at) updated.textContent="Catalogue updated "+new Date(d.updated_at).toLocaleDateString();
if(!d.apps.length){grid.innerHTML='<div class="loading">No apps found.</div>';return}
for(const a of d.apps){
const card=document.createElement("article");card.className="card";
const shots=(a.screenshots||[]).slice(0,4).map(x=>`<img loading="lazy" src="${esc(x)}" alt="">`).join("");
card.innerHTML=`<div class="top"><img class="icon" loading="lazy" src="${esc(a.icon||"assets/default-icon.svg")}" alt=""><div><h3 class="title">${esc(a.name)}</h3><div class="dev">${esc(a.developer||"AS TechnoArt")}</div></div></div><p class="desc">${esc(a.short_description||a.description||"Discover this app on Google Play.")}</p><div class="meta">${a.category?`<span class="pill">${esc(a.category)}</span>`:""}${a.updated?`<span class="pill">Updated ${esc(a.updated)}</span>`:""}</div>${shots?`<div class="screens">${shots}</div>`:""}<a class="play" href="${esc(a.url)}" target="_blank" rel="noopener">View on Google Play ↗</a>`;
grid.appendChild(card)}
}catch(e){grid.innerHTML='<div class="loading">App data could not be loaded.</div>'}
}
function esc(v){return String(v??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"}[c]))}loadApps();
