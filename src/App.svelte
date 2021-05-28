<script>
    import Blog from './components/blog/Blog.svelte';
    import Home from './components/home/Home.svelte';
    import { Router, Route, Link } from "svelte-navigator";
</script>

<Router>
  <div class="router">
    <header class="header">
      <nav class="nav-wrapper">
        <Link class='link' to="/">Home</Link>
        <Link class='link' to="blog">Blog</Link>
      </nav>
    </header>
    <main class="main">
      <Route path="/">
        <Home/>
      </Route>

      <Route path="blog">
        <Blog/>
      </Route>
    </main>
    <footer class="footer">
      <p>&copy; 2021 Michael Hrabe</p>
    </footer>
  </div>
</Router>

<style>
    .router {
        width: 100%;
        height: 100%;
        /* max-width: 240px; */
        margin: 0 auto;
        display: grid;
        grid-template-rows: auto 1fr auto;
        grid-template-columns: 1fr;
    }

    .main{
      overflow-y: auto;
    }

    .header .nav-wrapper {
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: row;
    }

    .footer {
      display: flex;
      justify-content: space-around;
      align-items: center;
      flex-direction: row;
      font-size: 1.5rem;
    }

    .nav-wrapper :global(.link) { 
      color: black;
      text-transform: uppercase;
      text-decoration: none;
      font-size: 3rem;
      margin: 0 10px;
     }
</style>
