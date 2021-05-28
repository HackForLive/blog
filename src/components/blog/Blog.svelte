<script>
  let htmlContent = ''
fetch('/build/petshop_cfg.html').then(response => {
  console.dir(response)
  return response.text();
}).then(html => {
  htmlContent = html
})
</script>

<main>
  <div class="content">{@html htmlContent}</div>
</main>

<style>
  main {
      /* text-align: center; */
      padding: 20x;
      font-size: 2rem;
      /* max-width: 240px; */
      /* margin: 0 auto; */
  }

  .content {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    width: 100%;
    max-width: 700px;
    margin: auto;
    flex-direction: column;
  }

  :global(pre) {
    text-align: left;
    padding: 10px;
  }
</style>
