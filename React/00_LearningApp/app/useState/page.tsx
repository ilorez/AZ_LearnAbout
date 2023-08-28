'use client';
import Footer from '@/compenents/Footer';
import Link from 'next/link'


import { useState } from 'react'




function LearnState() {
  const [count, setCount] = useState<number>(0);

  const plusOne = () => {
    setCount(count + 1);
  };

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
