const fs=require('fs');
const palettes={green:['#91E552','#65BE36','#3F942B'],gold:['#FFE887','#F8C847','#DC9A25'],dark:['#385A55','#25423E','#193C37'],glass:['#B9F3F7','#6BCEDD','#42AABB'],grass:['#C1DE85','#94BB5D','#75964D'],water:['#A9E4EB','#7BCBD8','#58B1C4']};
function build(name){
 const blocks=[];const box=(x,y,z,w=1,d=1,h=1,p='green')=>blocks.push({x,y,z,w,d,h,p});
 const block=(x,y,z,p='green')=>box(x,y,z,1,1,1,p);
 if(name==='house'){
  box(-1,-1,-.35,9,8,.35,'grass');
  for(let z=0;z<4;z++)for(let x=0;x<7;x++)for(let y=0;y<5;y++)if(x===0||x===6||y===0||y===4){
   if(y===4&&x===3&&z<3)continue;
   block(x,y,z,(y===4&&(x===1||x===5)&&z===2)?'glass':'green');
  }
  box(3,3.98,0,1,.03,2.7,'dark');
  for(let level=0;level<4;level++)for(let x=level;x<7-level;x++)for(let y=-.5;y<5.5;y++)block(x,y,4+level,'gold');
  for(let z=5;z<8;z++)block(5,1,z,'green');
  box(4.8,.8,8,1.4,1.4,.3,'gold');box(2,5,0,3,1,.3,'gold');
 }else if(name==='bridge'){
  box(-1,-1,-.4,13,5,.3,'water');
  for(const x of [0,1,9,10])for(let y=0;y<3;y++)for(let z=0;z<4;z++)block(x,y,z);
  for(const x of [2,8])for(let y=0;y<3;y++)for(let z=2;z<4;z++)block(x,y,z);
  for(const x of [3,7])for(let y=0;y<3;y++)block(x,y,3);
  for(let x=0;x<11;x++)for(let y=0;y<3;y++)block(x,y,4,'gold');
  for(let x=0;x<11;x++)for(const y of [0,2]){block(x,y,5);if(x%2===0)block(x,y,6,'gold');}
 }else if(name==='tower'){
  box(-1.5,-1.5,-.4,7,7,.4,'grass');
  for(let z=0;z<10;z++)for(let x=0;x<4;x++)for(let y=0;y<4;y++)if(x===0||x===3||y===0||y===3){
   block(x,y,z,((z===3||z===6||z===8)&&((y===3&&x===1)||(x===3&&y===1)))?'glass':'green');
  }
  for(let x=-1;x<5;x++)for(let y=-1;y<5;y++)if(x===-1||x===4||y===-1||y===4)block(x,y,7,'gold');
  for(let level=0;level<3;level++){
   const offset=-1+level;for(let x=offset;x<5-level;x++)for(let y=offset;y<5-level;y++)block(x,y,10+level,'gold');
  }
  box(1.2,1.2,13,.6,.6,1.6,'green');box(1.8,1.2,13.5,1.4,.3,.9,'gold');
 }else{
  box(-1,-1,-.4,12,8,.4,'grass');
  for(let x=0;x<10;x++)for(let y=0;y<6;y++)if(x===0||x===9||y===0||y===5)for(let z=0;z<4;z++){
   if(y===5&&(x===4||x===5)&&z<3)continue;block(x,y,z);
  }
  for(const x0 of [0,7])for(const y0 of [0,3]){
   for(let z=0;z<6;z++)for(let x=x0;x<x0+3;x++)for(let y=y0;y<y0+3;y++)if(x===x0||x===x0+2||y===y0||y===y0+2)block(x,y,z,(z===3&&x===x0+1&&y===y0+2)?'glass':'green');
   for(let x=x0;x<x0+3;x++)for(let y=y0;y<y0+3;y++)if((x-x0)%2===0&&(y-y0)%2===0)block(x,y,6,'gold');
  }
  for(let x=3;x<7;x++)if(x!==4)block(x,5,4,'gold');
  box(4,4.96,0,2,.03,3,'dark');box(3.8,5,3,2.4,.85,.45,'gold');
  for(const x of [1,8]){box(x,1,6,.25,.25,3,'green');box(x+.25,1,8,1.6,.2,.8,'gold');}
 }
 const iso=([x,y,z])=>[(x-y)*25,(x+y)*12-z*27];
 // Assemble by height first, then back-to-front within each course. Drawing
 // order stays independent so falling bricks retain correct occlusion.
 const order=blocks.map((b,i)=>({b,i})).sort((a,b)=>a.b.z-b.b.z||(a.b.x+a.b.y)-(b.b.x+b.b.y));
 const rank=new Map(order.map((entry,i)=>[entry.i,i]));
 const points=[];const faces=[];
 for(const b of blocks){const{x,y,z,w,d,h,p}=b;const pts=[[x,y,z],[x+w,y,z],[x+w,y+d,z],[x,y+d,z],[x,y,z+h],[x+w,y,z+h],[x+w,y+d,z+h],[x,y+d,z+h]];pts.forEach(p=>points.push(iso(p)));
 const polys=[[[4,5,6,7],0],[[3,2,6,7],1],[[1,2,6,5],2]].map(([ids,c])=>`<polygon points="${ids.map(i=>iso(pts[i]).map(v=>v.toFixed(2)).join(',')).join(' ')}" fill="${palettes[p][c]}" stroke="${p==='glass'?'#3E939A':'#406126'}" stroke-opacity=".28" stroke-width=".7" stroke-linejoin="round"/>`).join('');
 const delay=blocks.indexOf(b)===0?0:150+3400*rank.get(blocks.indexOf(b))/(blocks.length-1);
 faces.push({depth:x+y+z*.02,polys:`<g class="build-piece" style="--delay:${Math.round(delay)}ms">${polys}</g>`});}
 faces.sort((a,b)=>a.depth-b.depth);
 const xs=points.map(p=>p[0]),ys=points.map(p=>p[1]);const left=Math.min(...xs)-24,top=Math.min(...ys)-24,width=Math.max(...xs)-left+24,height=Math.max(...ys)-top+32;
 const svg=`<svg xmlns="http://www.w3.org/2000/svg" viewBox="${left} ${top} ${width} ${height}"><defs><filter id="shadow" x="-25%" y="-25%" width="150%" height="165%"><feDropShadow dx="0" dy="8" stdDeviation="5" flood-color="#35501F" flood-opacity=".2"/></filter></defs><g filter="url(#shadow)">${faces.map(f=>f.polys).join('')}</g></svg>`;
 fs.writeFileSync('assets/game-build-'+name+'.svg',svg);console.log(name,blocks.length,'bricks');
 const motion=`<style>.build-piece{animation:brickLand 450ms cubic-bezier(.2,.75,.3,1.15) var(--delay) both;transform-box:fill-box;transform-origin:50% 100%}@keyframes brickLand{0%{opacity:0;transform:translateY(-60px)}12%{opacity:1}75%{transform:translateY(2px)}100%{opacity:1;transform:translateY(0)}}@media(prefers-reduced-motion:reduce){.build-piece{animation:none}}</style>`;
 fs.writeFileSync('assets/game-build-'+name+'-animated.svg',svg.replace('<defs>',motion+'<defs>'));
}
['house','bridge','tower','castle'].forEach(build);
// Front-facing versions of the same toy bricks used in the game models.
for(const name of ['green','gold','glass']){
 const [top,front,side]=palettes[name];
 const window=name==='glass'?'<rect x="3" y="8" width="18" height="18" rx="2" fill="#B5EEF2" fill-opacity=".25" stroke="#268B9D" stroke-width=".8"/><path d="M12 8v18M3 17h18" stroke="#E9FFFF" stroke-width="1.2"/><path d="m4 11 6-2" stroke="white" stroke-opacity=".7" stroke-width="1.4" stroke-linecap="round"/>':'';
 fs.writeFileSync('assets/game-build-unit-'+name+'.svg',`<svg xmlns="http://www.w3.org/2000/svg" width="28" height="30" viewBox="0 0 28 30"><defs><linearGradient id="face" x2=".25" y2="1"><stop stop-color="${top}"/><stop offset=".5" stop-color="${front}"/><stop offset="1" stop-color="${front}"/></linearGradient><linearGradient id="top" x2="1" y2="1"><stop stop-color="${top}"/><stop offset="1" stop-color="${front}"/></linearGradient></defs><g stroke="#406126" stroke-opacity=".32" stroke-width=".7" stroke-linejoin="round"><path fill="url(#top)" d="M.5 5 4.5.5H27.5L23.5 5Z"/><path fill="url(#face)" d="M.5 5h23v24H.5Z"/><path fill="${side}" d="m23.5 5 4-4.5v24l-4 4.5Z"/></g><path d="M2 7h19M2 7v19" fill="none" stroke="white" stroke-opacity=".35" stroke-width=".8"/><path d="M2 27h19" stroke="${side}" stroke-opacity=".28" stroke-width=".8"/>${window}</svg>`);
}
