type footerProps = {
    text:string
    name?: string
}
function Footer({text,name}:footerProps){
    return (
        <footer>
            {text}
        </footer>
    )
}
export default Footer;