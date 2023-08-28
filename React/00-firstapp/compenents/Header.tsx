type headerProps = {
    title:string
    navContent:string
}
function Header(props:headerProps){
    return (
        <>
        <h1>{props.title}</h1>
        <nav>{props.navContent}</nav>
        </>
        )
}
export default Header;