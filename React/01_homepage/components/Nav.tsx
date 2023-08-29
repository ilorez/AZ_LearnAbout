import Link from "next/link";


function Nav(){
    return (
        <nav>
            <ul>
                <li><Link href='#'>About</Link></li>
                <li><Link href='#'>Contact Us</Link></li>
                <li><Link href='#'>Privacy</Link></li>
            </ul>
        </nav>
    )
}
export default Nav;