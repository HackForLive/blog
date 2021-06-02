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
      <div class="item">
        <p>{data.title}</p>
        <time>{data.date}</time>
        <a href={data.file}>click me</a>
      </div>
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

  .item {
    width: 70%;
    border-color: black;
    border-width: 5px;
    border-style: solid;
    border-radius: 5px;
    margin: 20px auto
  }

  /* :global(pre) {
    text-align: left;
    padding: 10px;
  } */
</style>
