<script>
  export let name = 'EVERYONE';
  import imgSrc from "../../assets/my_photo.jpg";
</script>

<main>
  <h1>Hello {name}!</h1>
  <!-- svelte-ignore a11y-img-redundant-alt -->
  <img width="300px" height="400px" src="{imgSrc}" alt='photo'/>
  <p>I'm technology enthusiast and I'm going to share my knowledge with you through my blog posts.</p>
  <p>
    Currently I'm working as Infrastructure developer. Mainly I focuse on Infrastructure as Code tools like Chef and Terraform. I have 2+ years knowledge of AWS cloud and also I'm certified with SAA.  
    In my free time I challenge myself such as doing CTF (capture the flag), diving into front-end development, building drone and many other.
  </p>
</main>

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
        font-size: 6rem;
        font-weight: 100;
        text-align: center;
    }

    p {
      max-width: 1000px;
      font-size: 2.5rem;
      margin: 20px auto;
    }

    @media (min-width: 640px) {
        main {
            max-width: none;
        }
    }
</style>
