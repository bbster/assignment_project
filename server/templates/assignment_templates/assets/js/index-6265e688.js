import{g as ne,h as Z,i as oe,j as H,u as re,k as ae,l as ie,w as _,m as R,s as V,c as ue}from"./index-d7f9cd18.js";function ee(e){return ae()?(ie(e),!0):!1}function W(){const e=new Set,n=r=>{e.delete(r)};return{on:r=>{e.add(r);const t=()=>n(r);return ee(t),{off:t}},off:n,trigger:r=>Promise.all(Array.from(e).map(t=>t(r)))}}function F(e){return typeof e=="function"?e():re(e)}const te=typeof window<"u"&&typeof document<"u",le=()=>{};function X(e,n=!1,i="Timeout"){return new Promise((d,r)=>{setTimeout(n?()=>r(i):d,e)})}function se(e,...n){return n.some(i=>i in e)}function $(...e){if(e.length!==1)return ne(...e);const n=e[0];return typeof n=="function"?Z(oe(()=>({get:n,set:le}))):H(n)}function z(e,n=!1){function i(o,{flush:u="sync",deep:f=!1,timeout:c,throwOnTimeout:T}={}){let p=null;const E=[new Promise(v=>{p=_(e,w=>{o(w)!==n&&(p==null||p(),v(w))},{flush:u,deep:f,immediate:!0})})];return c!=null&&E.push(X(c,T).then(()=>F(e)).finally(()=>p==null?void 0:p())),Promise.race(E)}function d(o,u){if(!R(o))return i(w=>w===o,u);const{flush:f="sync",deep:c=!1,timeout:T,throwOnTimeout:p}=u??{};let h=null;const v=[new Promise(w=>{h=_([e,o],([g,D])=>{n!==(g===D)&&(h==null||h(),w(g))},{flush:f,deep:c,immediate:!0})})];return T!=null&&v.push(X(T,p).then(()=>F(e)).finally(()=>(h==null||h(),F(e)))),Promise.race(v)}function r(o){return i(u=>!!u,o)}function t(o){return d(null,o)}function a(o){return d(void 0,o)}function b(o){return i(Number.isNaN,o)}function O(o,u){return i(f=>{const c=Array.from(f);return c.includes(o)||c.includes(F(o))},u)}function P(o){return C(1,o)}function C(o=1,u){let f=-1;return i(()=>(f+=1,f>=o),u)}return Array.isArray(F(e))?{toMatch:i,toContains:O,changed:P,changedTimes:C,get not(){return z(e,!n)}}:{toMatch:i,toBe:d,toBeTruthy:r,toBeNull:t,toBeNaN:b,toBeUndefined:a,changed:P,changedTimes:C,get not(){return z(e,!n)}}}function ce(e){return z(e)}function fe(e,n,i={}){const{immediate:d=!0}=i,r=H(!1);let t=null;function a(){t&&(clearTimeout(t),t=null)}function b(){r.value=!1,a()}function O(...P){a(),r.value=!0,t=setTimeout(()=>{r.value=!1,t=null,e(...P)},F(n))}return d&&(r.value=!0,te&&O()),ee(b),{isPending:Z(r),start:O,stop:b}}const de=te?window:void 0,pe={json:"application/json",text:"text/plain"};function Y(e){return e&&se(e,"immediate","refetch","initialData","timeout","beforeFetch","afterFetch","onFetchError","fetch","updateDataOnError")}function q(e){return typeof Headers<"u"&&e instanceof Headers?Object.fromEntries([...e.entries()]):e}function he(e,...n){var i;const d=typeof AbortController=="function";let r={},t={immediate:!0,refetch:!1,timeout:0,updateDataOnError:!1};const a={method:"GET",type:"text",payload:void 0};n.length>0&&(Y(n[0])?t={...t,...n[0]}:r=n[0]),n.length>1&&Y(n[1])&&(t={...t,...n[1]});const{fetch:b=(i=de)==null?void 0:i.fetch,initialData:O,timeout:P}=t,C=W(),o=W(),u=W(),f=H(!1),c=H(!1),T=H(!1),p=H(null),h=V(null),E=V(null),v=V(O||null),w=ue(()=>d&&c.value);let g,D;const G=()=>{d&&(g==null||g.abort(),g=new AbortController,g.signal.onabort=()=>T.value=!0,r={...r,signal:g.signal})},I=l=>{c.value=l,f.value=!l};P&&(D=fe(G,P,{immediate:!1}));const U=async(l=!1)=>{var y;G(),I(!0),E.value=null,p.value=null,T.value=!1;const m={method:a.method,headers:{}};if(a.payload){const M=q(m.headers),B=F(a.payload);!a.payloadType&&B&&Object.getPrototypeOf(B)===Object.prototype&&!(B instanceof FormData)&&(a.payloadType="json"),a.payloadType&&(M["Content-Type"]=(y=pe[a.payloadType])!=null?y:a.payloadType),m.body=a.payloadType==="json"?JSON.stringify(B):B}let S=!1;const A={url:F(e),options:{...m,...r},cancel:()=>{S=!0}};if(t.beforeFetch&&Object.assign(A,await t.beforeFetch(A)),S||!b)return I(!1),Promise.resolve(null);let x=null;return D&&D.start(),new Promise((M,B)=>{var L;b(A.url,{...m,...A.options,headers:{...q(m.headers),...q((L=A.options)==null?void 0:L.headers)}}).then(async s=>{if(h.value=s,p.value=s.status,x=await s[a.type](),!s.ok)throw v.value=O||null,new Error(s.statusText);return t.afterFetch&&({data:x}=await t.afterFetch({data:x,response:s})),v.value=x,C.trigger(s),M(s)}).catch(async s=>{let Q=s.message||s.name;return t.onFetchError&&({error:Q,data:x}=await t.onFetchError({data:x,error:s,response:h.value})),E.value=Q,t.updateDataOnError&&(v.value=x),o.trigger(s),l?B(s):M(null)}).finally(()=>{I(!1),D&&D.stop(),u.trigger(null)})})},K=$(t.refetch);_([K,$(e)],([l])=>l&&U(),{deep:!0});const k={isFinished:f,statusCode:p,response:h,error:E,data:v,isFetching:c,canAbort:w,aborted:T,abort:G,execute:U,onFetchResponse:C.on,onFetchError:o.on,onFetchFinally:u.on,get:j("GET"),put:j("PUT"),post:j("POST"),delete:j("DELETE"),patch:j("PATCH"),head:j("HEAD"),options:j("OPTIONS"),json:N("json"),text:N("text"),blob:N("blob"),arrayBuffer:N("arrayBuffer"),formData:N("formData")};function j(l){return(y,m)=>{if(!c.value)return a.method=l,a.payload=y,a.payloadType=m,R(a.payload)&&_([K,$(a.payload)],([S])=>S&&U(),{deep:!0}),{...k,then(S,A){return J().then(S,A)}}}}function J(){return new Promise((l,y)=>{ce(f).toBe(!0).then(()=>l(k)).catch(m=>y(m))})}function N(l){return()=>{if(!c.value)return a.type=l,{...k,then(y,m){return J().then(y,m)}}}}return t.immediate&&Promise.resolve().then(()=>U()),{...k,then(l,y){return J().then(l,y)}}}export{he as u};
