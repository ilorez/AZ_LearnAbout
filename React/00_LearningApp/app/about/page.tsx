import Link from 'next/link' 
import styles from './page.module.css'




function About() {
  let showFooter = true;
  return (
    <main>
      <h2 className={styles.myStyle}>I'm about page</h2>
      <Link href="/">Go Home</Link>
    </main>
  )
}

export default About;
