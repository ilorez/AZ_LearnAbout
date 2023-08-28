'use client';
import Footer from '@/compenents/Footer';
import Link from 'next/link'


import { useEffect, useState } from 'react'




function LearnState() {
  const [count, setCount] = useState<number>(0);
  const [success, setSuccess] = useState<boolean>(false);

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
      <button onClick={plusOne}>Increment</button>
      <Footer text="I'm footer"/>
      <div><Link href='/' >home</Link></div>
    </main>
  );
}

export default LearnState;
