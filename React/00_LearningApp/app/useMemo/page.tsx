'use client';

import Link from 'next/link'


import { useEffect, useMemo, useState } from 'react'

function bigCalculater(){
  let number = 0;
  for(let i=0;i<1000;i++){
    number += i
    // console.log(i)
  }
  return number
}


function learnUseMemo() {
  const [count, setCount] = useState<number>(0);
  const [success, setSuccess] = useState<boolean>(false);
  const memoNumber = useMemo(()=>
    bigCalculater()
  ,[success])

  const plusOne = () => {
    setCount(count + 1);
    if(count % 10 === 0){
      setSuccess(!success);
    }
  };
  useEffect(()=>{
    console.log('success has changed');
  },[success]);
  
  return (
    <main>
      <p>Count: {count}</p>
      <p>memoNumber: {memoNumber}</p>
      <button onClick={plusOne}>Increment</button>
      <div><Link href='/' >home</Link></div>
    </main>
  );
}

export default learnUseMemo;
