 /*name="saqi";
console.log(name);
roll_no=12
console.log(roll_no)
 name ="aqib";
console.log(name)
let  num1=parseInt(prompt("enter the first number"));
let num2=parseInt(prompt("enter the second number"));
let choice=prompt("enter the choice ");
let res;
console.log(typeof(num1));
if(choice==='1')
{res= num1+num2;
    console.log(res);
 }
 res= choice==1?"true":"error";
 console.log(res);
res= num1-num2;
res= num1*num2;
res= num1/num2;
res= num1%num2;
res= num1**num2;
let celius_tem=parseFloat(prompt("enter the temperature"));
let frhehid_tem=(celius_tem*9/5)+32;
console.log("frhehide temperature="+frhehid_tem);*/
let number = 5; 
let string = '';
for(let i = 1; i <= number; i++){
  for(let j = 1; j <= i; j++){
    string += '*';
  }
  string += "\n";
}
console.log(string);
let star='';
for(let i=1;i<5;i++){//rows
    for(let k=5;k<i;k--){//left space manag
       star += " " ;
    }
    for(let z=1;z<=i;z++){ //print * inner and right space manage
     star+='* ';

    }
    star+="\n";
} 
//pyramid code
console.log(star);
let n1 = 5; 
for (let i = 1; i <= n1; i++) { 
	let str = "* "; 
	let space = ' '; 
	console.log(space.repeat((n1 - i)) + str.repeat(i * 2 - 1)); 
}

let size=5;
for (let i = 1; i <= size; i++) { 
    let line = ""; 
    for (let j = 1; j <= size; j++) { 
        line += "*  "; 
    } 
    console.log(line,'\n'); 
    //console.log('\n');    
} 
let n = 5; 
for (let i = 1; i <= n; i++) { 
	let str = "* "; 
	let space = ' '; 
	console.log(space.repeat((n - i)) + str.repeat(i)); 
} 

for (let i = n - 1; i >= 1; i--) { 
	let str = "* "; 
	let space = ' '; 
	console.log(space.repeat(n - i) + str.repeat(i)); 
}
