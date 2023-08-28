type footerProps = {
    text:string
    name?: string
}
function Footer({text,name}:footerProps){
    // console.log('render');
    return (
        <footer>
            {text}
        </footer>
    )
}
export default Footer;