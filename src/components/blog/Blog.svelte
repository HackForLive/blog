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
      padding: 20x;
      font-size: 2rem;
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
