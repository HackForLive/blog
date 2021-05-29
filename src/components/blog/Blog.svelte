<script>
  let htmlContent = ''
fetch('/build/h1.html').then(response => {
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
