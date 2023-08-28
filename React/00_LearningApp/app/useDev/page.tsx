'use client';

import Link from 'next/link'


import { useEffect, useRef, useState } from 'react'




function LearnDev() {
  const inputRef = useRef<HTMLInputElement>(null)


  const focusOnInput = () => {
      {inputRef.current && inputRef.current.focus()}
      console.log(inputRef.current?.value)
    }
  

  
  return (
    <main>
      <input ref={inputRef}/>
      <button onClick={focusOnInput}>Click to focus</button>
      <div><Link href='/' >home</Link></div>
    </main>
  );
}

export default LearnDev;
