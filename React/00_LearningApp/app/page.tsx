import Image from 'next/image'
import Link from 'next/link'
import styles from './page.module.css'
import Header from '@/compenents/Header'
import Footer from '@/compenents/Footer'




function Home() {
  let showFooter = true;
  return (
    <main>
      <Header title="I'm Header" navContent="I'm nav inside header"/>
      <p style={{color:"red",backgroundColor:'yellow'}}>Hello world main</p>
      {showFooter && <Footer text="I'm Footer"/>}
      <Link href="/about">About</Link>
      <br />
      <Link href="/useStateAndEffect">useState</Link>
    </main>
  )
}

export default Home;
