import{S as E,i as w,s as I,e as d,t as y,b as l,d as c,f as D,g as r,k as u,l as N,m as o,D as p,o as k}from"../chunks/index.fef17017.js";import{g as V,b as M}from"../chunks/navigation.5b46ca50.js";import{b as P,c as R}from"../chunks/auth.20fa37d7.js";function S(g){let t,a,s,e,f,i,v;return{c(){t=d("main"),a=d("div"),s=d("div"),e=d("div"),f=y(`Nos vemos :D!
				`),i=d("p"),v=y("Redirigiendo..."),this.h()},l(n){t=l(n,"MAIN",{class:!0});var m=c(t);a=l(m,"DIV",{class:!0});var _=c(a);s=l(_,"DIV",{class:!0});var b=c(s);e=l(b,"DIV",{class:!0});var h=c(e);f=D(h,`Nos vemos :D!
				`),i=l(h,"P",{});var x=c(i);v=D(x,"Redirigiendo..."),x.forEach(r),h.forEach(r),b.forEach(r),_.forEach(r),m.forEach(r),this.h()},h(){u(e,"class","text-center"),u(s,"class","p-4 sm:p-7"),u(a,"class","mt-7 bg-white border border-gray-200 rounded-xl shadow-sm dark:bg-gray-800 dark:border-gray-700"),u(t,"class","w-full max-w-md mx-auto p-6")},m(n,m){N(n,t,m),o(t,a),o(a,s),o(s,e),o(e,f),o(e,i),o(i,v)},p,i:p,o:p,d(n){n&&r(t)}}}function T(g){let t=null;return k(async()=>{await P(),t=setTimeout(()=>{V("/")},2500)}),M(()=>{R(),t&&clearTimeout(t)}),[]}class C extends E{constructor(t){super(),w(this,t,T,S,I,{})}}export{C as default};
