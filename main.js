class MyHeader extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
            <nav>
                <div class="logo">Twitter<b>Pilot</b></div>
                    <input type="checkbox" id="click">
                    <label for="click" class="menubar">
                        <i class="fa fa-bars"></i>
                    </label>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">Our Team</a></li>
                        <li><a href="#">Documentation</a></li>
                        <li><a href="#">Contact Us</a></li>
                    </ul>
            </nav>
        `
    }
}

customElements.define('my-header', MyHeader)


class MyFooter extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
        <footer>
        <p>&copy 2023 TwitterPilot by Team Kingsley and Goodness</p>
        <p><i class="fa-solid fa-paper-plane"></i> info@twitterpilot.com</p>
            
                <div class="social-icons">
                    <a href="https://facebook.com/odimkingsley1"><i class="fa-brands fa-facebook"></i></a>
                    <a href="https://linkedin.com/in/odimkingsley"><i class="fa-brands fa-linkedin"></i></a>
                    <a href="https://instagram.com/okekings1"><i class="fa-brands fa-instagram"></i></a>
                    <a href="https://twitter.com/odimkingsley1"><i class="fa-brands fa-twitter"></i></a>
                    <a href="https://github.com/okekingscodes"><i class="fa-brands fa-github"></i></a>
                </div>
    </footer>
        `
    }
}

customElements.define('my-footer', MyFooter)