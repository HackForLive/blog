<script>
// import { link } from "fs";
// import { dataset_dev } from "svelte/internal";

  let blogData = ''
fetch('/build/blog_data.html').then(response => {
  console.dir(response)
  return response.json();
}).then(json => {
  blogData = json
})
</script>

<main>
  <div class="content">
    {#each blogData as data}
      <p>{data.title}</p>
      <time>{data.date}</time>
      <a href={data.file}>click me</a>
    {/each}
  </div>
</main>

<style>
  main {
      padding: 20x;
      font-size: 2rem;
  }

  .content {
    display: flex;
    align-items: flex-start;
    justify-content: center;
    text-align: left;
    width: 100%;
    max-width: 700px;
    margin: auto;
    flex-direction: column;
  }

  :global(pre) {
    text-align: left;
    padding: 10px;
  }

  :global(li) {
    text-align: left;
    padding: 10px;
  }

  :global(h1) {
    text-align: left;
    padding: 10px;
  }

  :global(h2) {
    text-align: left;
    padding: 10px;
  }
</style>
