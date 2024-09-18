<?php
include 'header.php';
include 'product_cardgroup/productClass.php';
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>iBanana</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" integrity="sha512-Kc323vGBEqzTmouAECnVceyQqyqdsSiqLQISBL29aUW4U/M7pSPA/gEUZQqv1cwx4OnYxTxve5UMg5GT6L4JJg==" crossorigin="anonymous" referrerpolicy="no-referrer"   />
    <style>
        .card-footer .h2 {
            font-size: 1em;
            padding-left: 5px;
        }

        button.px-5 {
            padding: 5px 1em 5px 1em !important;
        }

        .long-para {
            text-align: justify;
        }

        .section-title {
            margin-bottom: 10px;
            text-align: center;
        }

        section {
            margin-bottom: 25px;
        }

        /*Slideshow css */
        .slideshow-container {
            max-width: 1000px;
            position: relative;
            margin: auto;
        }

        /* Caption text */
        .text {
            color: #f2f2f2;
            font-size: 15px;
            padding: 8px 12px;
            position: absolute;
            bottom: 8px;
            width: 100%;
            text-align: center;
        }

        /* Number text (1/3 etc) */
        .numbertext {
            color: #f2f2f2;
            font-size: 12px;
            padding: 8px 12px;
            position: absolute;
            top: 0;
        }

        /* The dots/bullets/indicators */
        .dot {
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #bbb;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
        }

        .active {
            background-color: #717171;
        }

        /* Fading animation */
        .fade {
            animation-name: fade;
            animation-duration: 3s;
        }

        @keyframes fade {
            from {
                opacity: .4
            }

            to {
                opacity: 1
            }
        }

        /* On smaller screens, decrease text size */
        @media only screen and (max-width: 300px) {
            .text {
                font-size: 11px
            }
        }
    </style>

    <link href="node_modules/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="node_modules/bootstrap/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</head>

<body>
    <main>
        <section id="Home">
            <br>
            <div class="slideshow-container">

                <div class="mySlides fade">
                    <div class="numbertext">1 / 3</div>
                    <div style="width:100%;height:300;background-color:black;display:flex;justify-content:center;">
                        <img src="images/1.png" style="height:300">
                    </div>
                    <div class="text">iBanana - Computer Hardware Store</div>
                </div>

                <div class="mySlides fade">
                    <div class="numbertext">2 / 3</div>
                    <div style="width:100%;height:300;background-color:black;display:flex;justify-content:center;">
                        <img src="images/2.png" style="height:300">
                    </div>
                    <div class="text">10.10 Promotion Up to 70% off</div>
                </div>

                <div class="mySlides fade">
                    <div class="numbertext">3 / 3</div>
                    <div style="width:100%;height:300;background-color:black;display:flex;justify-content:center;">
                        <img src="images/3.png" style="height:300">
                    </div>
                    <div class="text">We are proudly announced as the largest tech store in Malaysia!</div>
                </div>

            </div>
            <br>

            <div style="text-align:center">
                <span class="dot"></span>
                <span class="dot"></span>
                <span class="dot"></span>
            </div>

            <script>
                let slideIndex = 0;
                showSlides();

                function showSlides() {
                    let i;
                    let slides = document.getElementsByClassName("mySlides");
                    let dots = document.getElementsByClassName("dot");
                    for (i = 0; i < slides.length; i++) {
                        slides[i].style.display = "none";
                    }
                    slideIndex++;
                    if (slideIndex > slides.length) {
                        slideIndex = 1
                    }
                    for (i = 0; i < dots.length; i++) {
                        dots[i].className = dots[i].className.replace(" active", "");
                    }
                    slides[slideIndex - 1].style.display = "block";
                    dots[slideIndex - 1].className += " active";
                    setTimeout(showSlides, 2000); // Change image every 2 seconds
                }
            </script>
        </section>
        <br>
        <section id="AboutUs">
            <h1 class="section-title">About Us</h1><br>
            <p class="long-para">At iBanana, we believe that tech should be simple, reliable,
                and accessible to everyone. Established with a passion for
                innovation, we specialize in providing high-quality computer
                hardware tailored to meet the diverse needs of both enthusiasts
                and everyday users. From cutting-edge CPUs to powerful GPUs,
                sleek cases, and all the components in between, we’ve got everything
                you need to build or upgrade your dream setup.</p>

            <p class="long-para">Our team of tech experts is dedicated to offering not just products,
                but personalized advice, ensuring that every customer walks away with the
                perfect solution for their needs. Whether you're a gamer, a content creator,
                or someone looking to optimize your workspace, iBanana is here to help
                you make informed decisions.</p>

            <p class="long-para">At iBanana, it’s all about empowering you to get the most out of your tech.
                We source from top brands, stay ahead of the latest trends, and maintain
                competitive prices so you can focus on what matters most—your performance.</p>
        </section>
        <br>
        <section id="Products">
            <h1 class="section-title">Products</h1>
            <?php
            include 'product_cardgroup/cpu_cardgroup.php';
            include 'product_cardgroup/cooler_cardgroup.php';
            include 'product_cardgroup/case_cardgroup.php';
            include 'product_cardgroup/gpu_cardgroup.php';
            include 'product_cardgroup/ram_cardgroup.php';
            include 'product_cardgroup/psu_cardgroup.php';
            include 'product_cardgroup/ssd_cardgroup.php';
            include 'product_cardgroup/hdd_cardgroup.php';
            include 'product_cardgroup/monitor_cardgroup.php';
            include 'product_cardgroup/motherboard_cardgroup.php';
            ?>
        </section>
        <br>
        <section id="ContactUs">
            <h1 class="section-title">Contact Us</h1>
            <p class="long-para">At iBanana, we’re always here to help! Whether you need expert advice on building your next rig,
                troubleshooting a product, or simply have a question about our services, feel free to reach out.
                We look forward to connecting with you!</p>
            <p><b>Store Location: </b><br>123 Tech Ave, Suite 101 <br>Kuala Lumpur, Malaysia</p>
            <p><b>Customer Support:</b><br>
                Phone: +60 12 345 6789<br>
                Email: support@ibanana.my</p>
            <p><b>Business Hours:</b><br>
                Monday – Friday: 10:00 AM – 8:00 PM<br>
                Saturday: 10:00 AM – 6:00 PM<br>
                Closed on Sundays and Public Holidays</p>
            <p><b>Follow Us:</b><br>
                Stay updated on our latest offers and product releases by following us on social media:<br>
                Facebook: @iBananaTech<br>
                Instagram: @iBananaOfficial<br>
                Twitter: @iBananaMY</p>
        </section>
        <div class="container_chatbot">
            <div class="chatbox">
                <div class="chatbox__support">
                    <div class="chatbox__header">
                        <div class="chatbox__image--header">
                            <img src="images/chatbot-icon.png" alt="image" width=50 height=50>
                        </div>
                        <div class="chatbox__content--header">
                            <h4 class="chatbox__heading--header">Chat support</h4>
                            <p class="chatbox__description--header">Hi. My name is Samantha. How can I help you?</p>
                        </div>
                    </div>
                    <div class="chatbox__messages">
                        <div></div>
                    </div>
                    <div class="chatbox__footer">
                        <input type="text" placeholder="Write a message...">
                        <button class="chatbox__send--footer send__button">Send</button>
                    </div>
                </div>
                <div class="chatbox__button">
                    <button><img src="./images/chatbox-icon.svg" /></button>
                </div>
            </div>
        </div>
        <script>
            $SCRIPT_ROOT = window.location.protocol + '//' + window.location.hostname;
        </script>
        <script src="./app.js"></script>
    </main>
</body>

<?php include 'footer.php' ?>
<script></script>

</html>
