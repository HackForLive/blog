<script>
    import Blog from './components/blog/Blog.svelte';
    import Home from './components/home/Home.svelte';
    import { Router, Route, Link } from "svelte-navigator";
</script>

<Router>
  <header>
    <h1>History</h1>

    <nav>
      <Link to="/">Home</Link>
      <Link to="blog">Blog</Link>
    </nav>
  </header>
  <main>
    <Route path="/">
      <Home/>
    </Route>

    <Route path="blog">
      <Blog/>
    </Route>
  </main>
</Router>

<style>
    main {
        text-align: center;
        padding: 1em;
        max-width: 240px;
        margin: 0 auto;
    }

    h1 {
        color: #ff3e00;
        text-transform: uppercase;
        font-size: 4em;
        font-weight: 100;
    }

    @media (min-width: 640px) {
        main {
            max-width: none;
        }
    }
</style>
