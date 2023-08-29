import Header from '@/components/Header';
import styles from './page.module.css'
import Footer from '@/components/Footer';
// import bootstrap from '@/bootstrap/css/bootstrap.min.css'
import 'bootstrap/dist/css/bootstrap.min.css';

function Home() {
    return (
      <>
        <Header />
        <main className='btn btn-primary'>
            I'm main of page
        </main>
        <Footer />
      </>
    )
}
export default Home;
