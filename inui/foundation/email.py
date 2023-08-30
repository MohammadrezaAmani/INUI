class ALIGNMENT:
    """---
    title: Alignment
    description: Centering, images, text, buttons, and menus in HTML emails made easy.
    ---

    Foundation includes a handful of helpful alignment classes to add common positioning behaviors to elements.

    ---

    ## Text Alignment

    You can align text with the `.text-x` classes. These classes will apply to the large breakpoint as well as the small.

    ```html
    <style>.columns {border: 1px solid #333;}</style>
    <container>
      <row>
        <columns>
          <p class="text-left">Left (default)</p>
        </columns>
        <columns>
           <p class="text-center">center</p>
        </columns>
        <columns>
           <p class="text-right">right</p>
        </columns>
      </row>
    </container>
    ```

    If you need to change text alignment only on the small breakpoint, you can use the `.small-text-x` classes.


    ```html
    <style>.columns {border: 1px solid #333;}</style>
    <container>
      <row>
        <columns>
          <p class="small-text-left">Left on small</p>
        </columns>
        <columns>
           <p class="small-text-center">Center on small</p>
        </columns>
        <columns>
           <p class="small-text-right">Right on small</p>
        </columns>
      </row>
    </container>
    ```

    You can combine these classes to override the behavior on the small breakpoint.

    ```html
    <style>.columns {border: 1px solid #333;}</style>
    <container>
      <row>
        <columns>
          <p class="text-center small-text-left">Center, small left</p>
        </columns>
        <columns>
           <p class="text-right small-text-center">Right, small center</p>
        </columns>
      </row>
    </container>
    ```

    ---

    ## Centering Images

    Just wrap the `<center>` around an image you’ll be good to go. Inky will handle the magic behind the scenes! In the CSS version, you’ll add a `.float-center` class, `align="center"` attribute and wrap a <code>&lt;center&gt;</code> tag to make sure things are centered.

    ```html
    <container>
      <row>
        <columns>
          <center>
            <img src="https://placehold.it/200?text=center" alt="image of clever meme that made me chuckle">
          </center>
        </columns>
      </row>
    </container>
    ```

    So to be clear: with Inky you only need to wrap an image in `<center>` tag to reliably center it.

    In the CSS version, our centering recipe includes three ingredients:

    - `.float-center` class on the `<img>` element
    - `align="center"` attribute on the `<img>` element
    - Wrap the `<img>` with `<center>` tags (needed for Outlook 2007, 2010, and 2011)

    Also, it's not really a float, but the `.float-center` class to an element to engage the automatic margin centering trick. Note that this will only work on elements with an absolute width, which means not a percentage or auto width.

    If you need to center an image only on mobile clients, you can apply the `.small-float-center` class. A good use case would be centering an image smaller than the full column width on devices like an iPhone 5, iPhone 6, and Android 4.4.

    ```html
    <container>
      <row>
        <columns small="12" large="3" class="large-offset-1">
          <img class="small-float-center" src="https://placehold.it/200?text=small-center" alt="please don't forget me">
        </columns>
        <columns small="12" large="8">
          <h4 class="small-text-center">What is the deal?</h4>
          <p class="small-text-center">Sweet beast sun bathe or chase mice rub face on everything or leave dead animals as gifts for mark territory play time.</p>
        </columns>
      </row>
    </container>
    ```

    ---

    ## Aligning Images Left and Right

    You can also align images to the left or the right.

    ```html
    <container>
      <row>
        <columns>
          <img class="float-left" src="https://placehold.it/200?text=left" alt="">
          <img class="float-center" src="https://placehold.it/200?text=center" alt="">
          <img class="float-right" src="https://placehold.it/200?text=right" alt="">
        </columns>
      </row>
    </container>
    ```

    ---

    ## Centering a Button

    Wrap the button with `<center>` tags to center it.

    ```html
    <container>
      <row>
        <columns>
          <center>
            <button href="#">Centered Button</button>
          </center>
        </columns>
      </row>
    </container>
    ```

    ---

    ## Centering Columns

    Tables by nature take up as much space is available to them. Because of this, centering columns can be done by adding empty columns to left and right of the column to be centered.

    ```html
    <style>.columns {border: 1px solid #333;}</style>
    <container>
      <row>
        <columns></columns>
          <columns>Centering a column</columns>
        <columns></columns>
      </row>
      <row>
        <columns></columns>
          <columns small="3">Centering a column</columns>
        <columns></columns>
      </row>
      <row>
        <columns></columns>
          <columns small="7">Centering a column</columns>
        <columns></columns>
      </row>
    </container>
    ```

    If you don't add a size attribute like `small="x"` then the columns will be equal width.

    ---

    ## Centering a Menu

    Centering the menu is a common practice. Wrapping the menu in `<center>` tags will achieve this.

    ```html
    <center>
      <menu>
        <item href="https://zurb.com">Item</item>
        <item href="https://zurb.com">Item</item>
        <item href="https://zurb.com">Item</item>
      </menu>
    </center>
    ```

    ---

    ## Vertical Alignment

    You can vertically align your content within columns by using `valign` attribute. The available values are `top`, `middle`, and `bottom`.

    ```html
    <row>
      <columns large="3" valign="top">
        <img class="float-right" src="https://placehold.it/50" alt="">
      </columns>
      <columns large="3" valign="bottom">
        <h4>Bottom</h4>
      </columns>
      <columns large="3" valign="middle">
        <h4 style="margin-bottom: 0;" class="text-right">HEADLINE</h4>
        <p style="margin-bottom: 0;" class="text-right subheader">SUBHEADLINE</p>
      </columns>
      <columns large="3" valign="middle">
        <img class="small-float-center" src="https://placehold.it/250" alt="">
      </columns>
    </row>
    ```
    <br>"""

    pass


class BUTTON:
    """---
    title: Button
    description: Buttons are convenient tools when you need more traditional actions. To that end, Foundation has many easy to use button styles that you can customize or override to fit your needs.
    sass: scss/components/_button.scss
    ---

    Creating a bullet-proof button that works in all email clients requires a table nested inside of a table. Put the class `.button` on the outer `<table>`. Inside of the inner table, put an `<a>` with an `href` attribute containing your link.

    In Inky HTML, the `<button>` tag creates all of this markup for you.

    ```html
    <button href="#">Button</button>
    ```

    <div class="callout primary">
    - It's important to add an `href` attribute to your `<button>`'s to ensure that Outlook.com will not display `[undefined]` in your rendered email.<br>
    - Office 365 and Outlook.com require a valid url in the href attribute or you can use the # placeholder.
    </div>

    ---

    ## Sizing

    By default, buttons are sized by the content and padding within them. You can also size a button according to it's parent container (see Expanded section).

    Buttons can be made larger or smaller by adding the class `.tiny`, `.small`, or `.large` to a button's outer `<table>`.

    In Inky HTML, add the same class to the `<button>` tag.

    ```html
    <button href="#" class="tiny">Tiny Button</button>
    <button href="#" class="small">Small Button</button>
    <button href="#">Default Button</button>
    <button href="#" class="large">Large Button</button>
    ```

    Don't forget the `href=""` ;)

    ---

    ## Expanded

    To create an expanded button (full width of it's container), add the class `.expanded` to the outer `<table>` of the button, and wrap a `<center>` tag around the `<a>`.

    In Inky HTML, add the `.expanded` class to the `<button>` tag. If you want the button to be expanded on small only, add the `.small-expanded`.

    ```html
    <row>
      <column>
        <button href="#" class="expanded">Expanded Button</button>
        <button href="#" class="small-expanded">Expand small only</button>
      </column>
    </row>
    ```

    ---

    ## Coloring

    Change the background color of a button by adding the class `.secondary`, `.success`, `.warning`, or `.alert` to the outer `<table>` (or the `<button>` tag in Inky HTML).

    ```html
    <button href="#" class="secondary">Secondary Button</button>
    <button href="#" class="success">Success Button</button>
    <button href="#" class="warning">Warning Button</button>
    <button href="#" class="alert">Alert Button</button>
    ```

    ---

    ## Radius and Round

    Creating buttons with a radius or rounded edges (like a pill) can be achieved by adding the `.radius` or `.rounded` class to a button.

    *Note - border-radius is not supported on Outlook 2000-2013, Yahoo! Mail, and Android 4+ (Gmail)*

    *Note - In order to create `.radius` and `.rounded` buttons, the border needs to be removed.*

    ```html
    <button href="#" class="radius">Radius</button>
    <button href="#" class="rounded">Round</button>

    ```"""

    pass


class CALLOUT:
    """---
    title: Callout
    description: Formerly panels, callouts can be used to create sidebar panels or call out important content in an email.
    sass: scss/components/_callout.scss
    tags:
      - panel
      - alert
    ---

    ## Basics

    A Callout adds a border, background, and some padding. Callouts use a full table structure, with the class `.callout` on the outer `<table>` (for bottom margin) and the `.callout-inner` applied to the innermost `<th>`.

    When using [Inky](inky.html) HTML, the `<callout>` tag will create this structure for you. You can wrap them around a row or inside a column.

    ```html
    <row>
      <columns small="6">
        <p>Not in a callout :(</p>
      </columns>
      <columns small="6">
        <callout class="secondary">
          <p>I'm in a callout!</p>
        </callout>
      </columns>
    </row>

    <callout class="primary">
      <row>
        <columns small="12">
          <p>This whole row is in a callout!</p>
        </columns>
      </row>
    </callout>
    ```

    ---

    ## Coloring Classes

    The color of a callout can be changed by adding the class `.primary`, `.success`, `.warning`, or `.alert` to the element. A callout without a color class will have a white background.

    ```html
    <callout>
      <p>Successfully avoided Kraken. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>
    </callout>
    <callout class="primary">
      <p>Successfully avoided Kraken. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>
    </callout>

    <callout class="success">
      <p>Successfully avoided Kraken. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>
    </callout>

    <callout class="warning">
      <p>There may be Krakens around. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>
    </callout>

    <callout class="alert">
      <p>Incoming Kraken! Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>
    </callout>
    ```"""

    pass


class COMPATIBILITY:
    """---
    title: Compatibility
    description: Foundation for Emails is battle-tested in the trickiest email clients, like Microsoft Outlook.
    ---

    Foundation for Emails is designed for and tested on numerous email clients and devices. Here's the rundown on what type of compatibility to expect in general. Because email clients have varying CSS support and specific quirks, each individual component will have more information on compatibility.

    <table class="comparison-table">
      <thead>
        <tr>
          <td>Email Client/Device</td>
          <td class="marker">Compatibility</td>
        </tr>
      </thead>
      <tr>
        <td class="divider"><strong>Apple Mail:</strong></td>
        <td class="divider"></td>
      </tr>
      <tr>
        <td>Apple Mail 7</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>Apple Mail 8</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td class="divider"><strong>Outlook:</strong></td>
        <td class="divider"></td>
      </tr>
      <tr>
        <td>Outlook 2000</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>Outlook 2002</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>Outlook 2003</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>Outlook 2007</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>Outlook 2010</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>Outlook 2011</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>Outlook 2013</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>Outlook 2016</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td class="divider"><strong>Mobile:</strong></td>
        <td class="divider"></td>
      </tr>
      <tr>
        <td>Android 4.4</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>Gmail app for Android</td>
        <td class="marker mostly">&check; *</td>
      </tr>
      <tr>
        <td>iPhone 5</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>iPhone 6</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>iPad</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>iPad Mini</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td class="divider"><strong>Gmail:</strong></td>
        <td class="divider"></td>
      </tr>
      <tr>
        <td>In Internet Explorer</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>In Firefox</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>In Chrome</td>
        <td class="marker yes">&check;</td>
      </tr>
        <tr>
        <td class="divider"><strong>Google Apps:</strong></td>
        <td class="divider"></td>
      </tr>
      <tr>
        <td>In Internet Explorer</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>In Firefox</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>In Chrome</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td class="divider"><strong>Office 365:</strong></td>
        <td class="divider"></td>
      </tr>
      <tr>
        <td>In Internet Explorer</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>In Firefox</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>In Chrome</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td class="divider"><strong>Outlook.com:</strong></td>
        <td class="divider"></td>
      </tr>
      <tr>
        <td>In Internet Explorer</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>In Firefox</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>In Chrome</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td class="divider"><strong>Yahoo! Mail:</strong></td>
        <td class="divider"></td>
      </tr>
      <tr>
        <td>In Internet Explorer</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>In Firefox</td>
        <td class="marker yes">&check;</td>
      </tr>
      <tr>
        <td>In Chrome</td>
        <td class="marker yes">&check;</td>
      </tr>
    </table>

     ** *Gmail app for Android:** Works - does not recognize media queries so it will render large breakpoint.
    """

    pass


class CSS_GUIDE:
    """---
    title: Getting Started with CSS
    description: Get started with the CSS version of Foundation for Emails.
    ---

    Foundation for Emails takes the pain out of developing HTML emails by giving you a set of powerful, tested components out of the box. This includes a fully-responsive grid, buttons, callouts, menus, and more.

    In this Getting Started guide, we'll download Foundation for Emails, construct the basic grid, and then inline our email so it's ready to test.

    ---

    ## Installing

    If you haven't yet, download the starter files for Foundation for Emails. They include the boilerplate HTML needed for an email, and all of the CSS for Foundation.

    <a href="https://s3.amazonaws.com/zurb-foundation/foundation-emails.zip" class="large button">Download Foundation for Emails</a>

    Unzip the folder and open it in your text editor of choice.

    ---

    ## File Structure

    Here's a breakdown of the files in the folder you got:

    - `css/foundation-emails.css`: the Foundation for Emails CSS.
    - `index.html`: a blank boilerplate to get started.
    - `templates/`: a set of pre-made templates following common email layouts.

    We'll be writing a layout from scratch, so open up `index.html`.

    ---

    ## Boilerplate

    Inside `index.html`, you can see the boilerplate needed to make an HTML email work, with comments explaining what does what.

    ```html
    <!-- Emails use the XHTML Strict doctype -->
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="https://www.w3.org/1999/xhtml">
    <head>
      <!-- The character set should be utf-8 -->
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
      <meta name="viewport" content="width=device-width"/>
      <!-- Link to the email's CSS, which will be inlined into the email -->
      <link rel="stylesheet" href="assets/css/foundation-emails.css">
      <style>
        <!-- Your CSS to inline should be added here -->
      </style>
    </head>

    <body>
      <!-- Wrapper for the body of the email -->
      <table class="body" data-made-with-foundation>
        <tr>
          <!-- The class, align, and <center> tag center the container -->
          <td class="float-center" align="center" valign="top">
            <center>
              <!-- The content of your email goes here. -->
            </center>
          </td>
        </tr>
      </table>
    </body>
    </html>
    ```

    ---

    ## Grid Basics

    Foundation for Emails includes many common elements needed to make HTML emails: a grid, typography styles, buttons, callouts, and more.

    The markup required to create HTML emails that work in all email clients is *complicated*, and involves writing many tables. However, all of Foundation's components are thoroughly tested in every major email client, including the problematic ones like Outlook. The rigid structure ensures your designs don't look off in any email client.

    Let's start by building a basic grid. To do that, we need three pieces: a container, a row, and then some columns.

    ### Container

    Most Foundation for Emails components are full tables, including the container. Inside the `<center>` tag of `index.html`, add this table code:

    ```html
    <table class="container">
      <tr>
        <td></td>
      </tr>
    </table>
    ```

    The **container** will wrap the body of your entire email. It applies a maximum width to the body of the email. Every email needs this bit of boilerplate.

    ### Row

    Next, let's build the grid itself, starting with the row. **Rows** group columns together into a unit. Inside of your container, add this table:

    ```html
    <table class="row">
      <tr>
        <th></th>
      </tr>
    </table>
    ```

    ### Columns

    Columns divide your layout into horizontal sections that sit side-by-side. On small screens, these columns stack on top of each other to save space&mdash;unless you set them up to keep their layout on small screens.

    Inside of your row (the innermost `<tr>`), add one column using this code:

    ```html
    <table class="row">
      <tr>
        <th class="small-12 large-6 first columns">
          Column One
        </th>
        <th class="expander"></th>
      </tr>
    </table>
    ```

    In the above example, we used the classes `.small-12` and `.large-6` to define the size of the column on small vs. large email clients. Foundation uses a 12-column grid, so on mobile clients, the column stretches the full width of the page, and on desktop clients, the column is half the width of the row.

    Since this first column is half-width, we need a second one to go with it. *After* the `<th>` for the first column, add the code for the second column:

    ```html
    <table class="row">
      <tr>
        <th class="small-12 large-6 first columns">
          Column One
        </th>
        <th class="small-12 large-6 last columns">
          Column Two
        </th>
        <th class="expander"></th>
      </tr>
    </table>
    ```

    You may have noticed the `.first` and `.last` classes on the column. The first column in a row needs the `.first` class, and the last column in a row needs the `.last` class. This is explained more in the [First and Last Classes](grid.html#first-and-last-classes) section of the grid documentation.

    That's a lot of HTML! Let's look at what it is at a high level:

    ```html
    <!-- Container -->
      <!-- Row -->
        <!-- Column One -->
        <!-- Column Two -->
    ```

    The CSS classes are always on the outermost table element, so that's an easy way to identify where a component starts. The container starts at the table with the `.container` class, the row starts at the table with the `.row` class, and so on.

    ---

    ## Inlining

    Now that we have a basic email, the last thing we need to do before we can send it is *inline* it. This is the process of injecting all of the CSS for the email into the HTML, so that it works as a self-contained file.

    Email clients like Gmail and Outlook strip out `<style>` tag from the `<head>` and Gmails strips it from the `<body>` of the email as well. It's best to have your CSS written inline within your markup. Hand writing all your CSS inline in a style tag would be a real pain and would take a long time.

    Our [web inliner](https://get.foundation/emails/inliner.html) automates this process for you. To use it, paste in the contents of `index.html` into the HTML field, paste in the contents of `css/foundation-emails.css` into the CSS field, and then press "Inline!". Once it's done, you'll see a large soup of HTML that is your inlined email.

    Your email's CSS will include media queries for responsive styling which the inliner tool will move into the `<body>` so they are preserved.

    ---

    ## Testing

    Now that you have an inlined email, you'll need to test it in real email clients to verify that it looks correct. All of Foundation's built-in components have already been tested in every major email client, so we've done a lot of the work for you. However, you'll want to test your email before you send it out to the masses.

    The most popular tool for testing emails is [Litmus](https://litmus.com/). All you have to do is paste in the HTML of an email, and you get a live preview in any email client you want.

    It's up to you to choose what email clients are important to test in, but you can [see our compatibility list](compatibility.html) for recommendations.

    ---

    ## Next Steps

    You've successfully installed Foundation for Emails, and written, inlined, and tested your first email! To keep going with the framework, you can check out the documentation for the other framework components, including [buttons](button.html), [callouts](callout.html), [menus](menu.html).

    If you're interested in going in-depth on the framework with the Foundation team, [check out our master class on Foundation for Emails](https://zurb.com/university/responsive-emails-foundation), an on-demand video series that explores every aspect of email design workflow.
    """

    pass


class GEM_GUIDE:
    """---
    title: Getting Started with the Ruby Gem
    description: inky-rb is a gem that allows you to bring the power of Foundation for Emails into your Rails apps. It can be embedded into the Asset Pipeline, combining with a CSS inliner to let you generate awesomely responsive HTML emails that work across various clients.
    ---

    ## How It Works

    ![inky_gem_diagram.png](https://get.foundation/emails/docs/assets/img/inky_gem_diagram.png)

    **inky-rb** is a pure Ruby implementation of the Inky templating language that converts simple custom HTML tags like `<row>` and `<column>` into the complex table-based HTML required for emails.

    Using a CSS inliner like `premailer-rails` or `roadie`, you're able to keep your email templates lean by avoiding the need to manually embed styles in the markup. By parsing your email template, the inliner is able to locate your referenced stylesheet and go through all of the selectors specified within it, assigning the styles to matching elements within the document.

    The result of this approach is an HTML email, as styled or as responsive as you need it, with a fraction of the code required by writing emails the old fashioned way.

    ---

    ## Getting Started

    Installing inky-rb in your Rails application requires only a few simple steps. Get the ball rolling by adding the following to your app's Gemfile:

    ```ruby
    gem 'inky-rb', require: 'inky'
    # Stylesheet inlining for email
    gem 'premailer-rails'
    ```

    Then execute:

    ```bash
    bundle install
    ```

    Run the following command to set up the required styles and mailer layout:

    ```bash
    rails g inky:install
    ```

    (You can specify the generated mailer layout filename like so: `rails g inky:install some_name`)

    Rename your email templates to use the `.inky` file extension. Note that you'll still be able to use ERB within the `.inky` templates:

    ```ruby
    welcome.html      => welcome.html.inky
    pw_reset.html.erb => pw_reset.html.inky
    ```

    Done! You're now all set to start writing responsive emails in your Rails app.

    ---

    ## Standalone Assets

    To include only the Foundation for Emails styles in your Asset Pipeline, without the Inky templating language, use the [**foundation_emails**](https://github.com/zurb/foundation-emails/#using-the-ruby-gem) gem.
    """

    pass


class GLOBAL:
    """---
    title: Global Styles
    description: Our global CSS includes helpful resets to ensure consistent styling across email clients.
    sass: scss/_global.scss
    ---

    ## Font Sizing

    The default font size is set to 100% of the browser style sheet, usually 16 pixels. This ensures compatibility with browser-based text zoom or user-set defaults. If you're using the Sass version of Foundation, edit the `$global-font-size` variable to change the base font size. This can be a percentage value, or a pixel value.

    ---

    ## Colors

    All interactive elements in Foundation, such as links and buttons, use the same color. The default shade of blue you see all over Foundation comes from the `$primary-color` Sass variable.

    Many components can also be colored with four other colors: secondary, alert, success, and warning. Use these colors to give more context to UI elements and actions.

    <div class="row small-up-1 medium-up-3 large-up-5">
      <div class="column">
        <div class="docs-color-block">
          <div class="docs-color-block-primary" style="background-color: #2199e8"></div>
          <p>Primary</p>
        </div>
      </div>
      <div class="column">
        <div class="docs-color-block">
          <div class="docs-color-block-secondary"></div>
          <p>Secondary</p>
        </div>
      </div>
      <div class="column">
        <div class="docs-color-block">
          <div class="docs-color-block-success"></div>
          <p>Success</p>
        </div>
      </div>
      <div class="column">
        <div class="docs-color-block">
          <div class="docs-color-block-warning"></div>
          <p>Warning</p>
        </div>
      </div>
      <div class="column">
        <div class="docs-color-block">
          <div class="docs-color-block-alert"></div>
          <p>Alert</p>
        </div>
      </div>
      <div class="column">
        <div class="docs-color-block">
          <div class="docs-color-block-white"></div>
          <p>White</p>
        </div>
      </div>
      <div class="column">
        <div class="docs-color-block">
          <div class="docs-color-block-light-gray"></div>
          <p>Light Gray</p>
        </div>
      </div>
      <div class="column">
        <div class="docs-color-block">
          <div class="docs-color-block-medium-gray"></div>
          <p>Medium Gray</p>
        </div>
      </div>
      <div class="column">
        <div class="docs-color-block">
          <div class="docs-color-block-dark-gray"></div>
          <p>Dark Gray</p>
        </div>
      </div>
      <div class="column">
        <div class="docs-color-block">
          <div class="docs-color-block-black"></div>
          <p>Black</p>
        </div>
      </div>
    </div>

    ---

    ### Color Classes

    Some components, such as [buttons](button.html) and [callouts](callout.html), have *coloring classes*, which let you change the color of the element by adding the name of the color as a CSS class.

    ```html
    <button class="button" href="#">Primary Action</button>
    <button class="secondary button" href="#">Secondary Action</button>
    ```

    ```html
    <callout class="success">
      <p>Created a new folder. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    </callout>
    <callout class="alert">
      <p>Error fetching stick. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    </callout>
    ```

    ## Responsive Breakpoint

    Unlike Foundation for Sites, the Foundation for Emails CSS is written *desktop-first*. This is because many older desktop email clients don't support media queries, or `<style>` tags.

    **Your email layout shifts from desktop to mobile at 596 pixels.** This is the width of the container, plus the width of the gutters around the container. In the Sass version of Foundation, you can change the breakpoint by modifying these variables:

    - `$global-width`: width of the container. It's 580px by default.
    - `$global-gutter`: width of the grid gutter. It's padding to space columns away from each other or away from the edges of the container.
    - `$global-breakpoint`: The breakpoint at which the layout shifts. It's the variable that adds `$global-width` and `$global-gutter` together.
    """

    pass


class GRID:
    """---
    title: The Grid
    description: If you're familiar with the Foundation for Sites grid, you'll be right at home working with Foundation for Emails.
    sass: scss/grid/_grid.scss
    ---

    The grid has two core elements: the *row* and *column*. Rows define horizontal sections of content, and columns carve up the row into side-by-side sections.

    ## Container

    All emails should have a container element. This gives the email a maximum width for email clients on larger screens. It also orients the email in the center.

    A container is a full table, so it needs the tags `<table>`, `<tr>`, and finally `<td>`. The class `.container` goes on the `<table>`.

    ```html
    <container>All the rows go here</container>
    ```

    ---

    ## Rows

    A row is a `<table>` with a `<tbody>` and `<tr>`. Inside of this `<tr>`, you'll place each individual column. The `<table>` also has the class `.row`.

    In Inky HTML, use the `<row>` tag to create a row.

    ```html
    <container>
      <row>
        Columns go here
      </row>
    </container>
    ```

    ---

    ## Columns

    The structure of a column is a bit more involved. At the top level, a column is a `<th>` with the class `.columns`.

    Inside of the `<th>` is another full table. The content of your column goes inside of a `<th>`. Right below that table header should be *another* `<th>` with a class of `.expander`. This empty element helps the column expand to be full-width on small screens.

    Here's our full column syntax so far:

    ```html
    <th class="columns first last">
      <table>
        <tr>
          <th>This is a column. Columns contain your content.</th>
          <th class="expander"></th>
        </tr>
      </table>
    </th>
    ```

    In Inky HTML, use the `<columns>` class to create a column.

    ```html
    <columns>This is a column. Columns contain your content.</columns>
    ```

    ### Sizing

    A column has a *size* between 1 and 12&mdash;this is how many columns wide the element is. Foundation uses a 12-column grid, so 6 columns is half the width of the whole row.

    Set column sizes with the classes `.large-n` and `.small-n`, where `n` is how wide the column is. The `.small-` size is applied on mobile email clients, while the `.large-` size is applied on desktop email clients.

    In Inky HTML, set the attribute `small` or `large` on the `<columns>` tag with the size you want. If you don't fill in `small`, it will use 12 by default. If you fill in `small` but not `large`, `large` will use the same value as `small`.

    ```html
    <columns small="12" large="6"></columns>
    ```

    ### First and Last Classes

    The `.first` class adds the appropriate amount of padding-left to space the content away from the container’s edge. The `.last` class is added to your last set of columns in a row to add padding-right to the column. If you have columns in between `.first` and `.last`, these classes are not needed on the middle columns.

    The reason these classes exist is that CSS properties like `:last-child` don’t work in most email clients so a class is needed.

    In Inky HTML, these classes are added for you.

    ```html
    <columns large="4">One</columns>
    <columns large="4">Two</columns>
    <columns large="4">Three</columns>
    ```

    ### Expander

    The `.expander` prevents a rendering bug in Outlook that sometimes keeps the columns from expanding to full width. Instead of ignoring the width attribute and politely taking up only as much space as the content dictates (default `<th>` behavior), the presence of the expander `<th>` causes the content `<th>` to become “greedy” and take up as much space as is given to it, up to the value specified in the width (which is 100%). They’re set to not display, but they kick the total width up over 100%, which forces their sibling `<th>` to expand fully.

    ---

    ## Collapsing

    Collapsing a row removes the gutters from every column, which is the spacing between them. Add the class `.collapse` to a row to enable this.

    ```html
    <row class="collapse">
      <columns large="6"><img src="https://placehold.it/300x150/777777/&text=These columns touch" alt=""></columns>
      <columns large="6"><img src="https://placehold.it/300x150/999999/&text=These columns touch" alt=""></columns>
    </row>
    ```

    ---

    ## Offsets

    Offsets add spacing to the left of a column. Use this if all the columns in a row don't add up to 12, and you want to mess with the spacing between them.

    Use the class `.large-offset-n` to create an offset, where `n` is the amount of columns to offset by. So, for example, `.large-offset-3` would offset the column by 25% of the width of the row. Think of it as pushing the columns over from the left.

    ```html
    <row>
      <columns large="3" class="large-offset-3"><img src="https://placehold.it/150x150/999999/&text=offset column" alt=""></columns>
      <columns large="3"><img src="https://placehold.it/150x150/999999" alt=""></columns>
    </row>
    ```"""

    pass


class INDEX:
    """---
    title: Foundation for Emails
    description: Use Foundation for Emails to design responsive HTML emails that work in any email client.
    ---

    ## Getting Started

    There are two ways to get started with Foundation for Emails: the CSS version and the Sass version.

    The **CSS version** is a ZIP file download with all the HTML and CSS you need to get started writing an HTML email. You'll need to run your HTML through our web inliner before you can send them off.

    <a href="css-guide.html" class="large button">Get Started with CSS Version</a>

    The **Sass version** gives you more control over the visual styles of the framework, and a full build process, which includes a Sass compiler and image compression. It also includes Inky, our custom HTML language which makes writing code faster, a built-in inliner, and a live reloading server for testing. **The Sass version requires you to have Node.js installed.**

    <a href="sass-guide.html" class="large button">Get Started with Sass Version</a>

    ---

    ## What's in the Box?

    Get to know the pieces of Foundation.

    ### General

    <div class="row up-1 medium-up-2 large-up-3 docs-big-index">
      <div class="column"><a href="sass.html">
        <strong>Using Sass</strong>
        <p>Loading and customizing the Foundation for Emails Sass.</p>
      </a></div>
      <div class="column"><a href="inky.html">
        <strong>Using Inky</strong>
        <p>Our custom HTML tags for writing email components.</p>
      </a></div>
      <div class="column"><a href="zurb-stack.html">
        <strong>ZURB Stack</strong>
        <p>An all-in-one solution for email development.</p>
      </a></div>
      <div class="column"><a href="compatibility.html">
        <strong>Compatibility</strong>
        <p>Foundation works with every key email client&mdash;even Outlook.</p>
      </a></div>
      <div class="column"><a href="migration.html">
        <strong>Migrate from Ink</strong>
        <p>Upgrade your Ink emails to Foundation for Emails 2.</p>
      </a></div>
    </div>

    ### Components

    <div class="row up-1 medium-up-2 large-up-3 docs-big-index">
      <div class="column"><a href="grid.html">
        <strong>The Grid</strong>
        <p>A fully responsive grid with support for small and large layouts.</p>
      </a></div>
      <div class="column"><a href="global.html">
        <strong>Global Styles</strong>
        <p>Core framework styles and Sass variables.</p>
      </a></div>
      <div class="column"><a href="alignment.html">
        <strong>Alignment Classes</strong>
        <p>Utility classes to align text and images.</p>
      </a></div>
      <div class="column"><a href="button.html">
        <strong>Buttons</strong>
        <p>Buttons with support for multiple sizes and colors.</p>
      </a></div>
      <div class="column"><a href="callout.html">
        <strong>Callout</strong>
        <p>Colored panels to use for sectioning or calls to action.</p>
      </a></div>
      <div class="column"><a href="menu.html">
        <strong>Menu</strong>
        <p>Horizontal or vertical list of links.</p>
      </a></div>
      <div class="column"><a href="spacer.html">
        <strong>Spacer</strong>
        <p>Create consistant vertical spacing between elements.</p>
      </a></div>
      <div class="column"><a href="wrapper.html">
        <strong>Wrapper</strong>
        <p>Helps create full width or fluid backgrounds.</p>
      </a></div>
      <div class="column"><a href="typography.html">
        <strong>Typography</strong>
        <p>Core styles for paragraphs, headings, and more.</p>
      </a></div>
      <div class="column"><a href="visibility.html">
        <strong>Visibility</strong>
        <p>Utility classes to control how content appears at different screen sizes.</p>
      </a></div>
    </div>"""

    pass


class INKY:
    """---
    title: Inky
    description: Inky is a templating language that converts simple HTML tags into the complex table HTML required for emails.
    library: true
    ---

    ## Overview

    HTML emails require tables upon tables *upon tables* to work properly. Although Foundation for Emails takes a lot of the pain out of constructing these tables, we've made it even easier with **Inky**, a templating language that converts simple HTML tags like `<row>` and `<columns>` into complex table HTML.

    Inky keeps you out of a sea of tables and focused on your email. Check out this example&mdash;click "Switch to Inky" to see the difference.

    ```html
    <container>
      <row>
        <columns>Put content in me!</columns>
      </row>
    </container>
    ```
    <div class="callout warning">
    The Inky templating language is part of the [ZURB Stack and the Sass version](zurb-stack.html). <br><a href="#how-to-inky">More on how to get Inky into your workflow</a>
    </div>

    ---

    ## Tags

    Inky currently supports these custom tags:

    - **Grid:**
      - `<container>`
      - `<row>`
      - `<columns>`
    - **Button:** `<button>`
    - **Callout:** `<callout>`
    - **Menu:**
      - `<menu>`
      - `<item>`

    ---

    ## FAQ

    Here are some frequently asked questions about Inky:

    **What’s a templating language?**

    Essentially, it is just custom HTML tags. Things like `<row>` and `<columns>` are understood by this language. Since email clients only work with table-based HTML, these tags don’t actually make it into your recipient’s inbox. Instead it’s translated into the table-based HTML needed for our approach to responsive emails.

    **How does it work?**

    We run a Gulp task that runs through your code, identifies our custom Inky tags, and translates them into valid HTML. For the more tech-savvy, you can [check out our task on our Github Repo](https://github.com/foundation/foundation-emails/blob/v2.0.0/gulpfile.js#L149).

    <a id="how-to-inky"></a>
    **How do I start Inky?**

    Inky is built into the ZURB Stack, but you can also use Inky standalone, or integrate it into your own build process. [Refer to the Inky readme to learn more.](https://github.com/zurb/inky#usage)

    **Do I have to have the Gulp tasks running for Inky to work?**

    Yes. In order for Inky to watch your files for changes, you need to be running either `npm start` or `npm run build` to see your changes reflected.

    **Do I have to use Inky? What if I just want to code my own email in tables?**

    You aren’t required to use Inky in your emails. You can write only in tables, or mix tables and Inky within the same email.

    **What are all of Inky’s tags and components?**

    You can check out all of the syntax and examples in the components section of the docs. We recommend you start off with [the grid](grid.html).

    **I found a bug&mdash;what should I do?**

    Foundation for Emails is completely open sourced and we love engaging with the community. Feel free to file a bug, or even crush the bug, through our [GitHub repo](https://github.com/zurb/inky/issues).
    """

    pass


class MEDIA_QUERY:
    """---
    title: Media Queries
    description: Use media queries to design responsive HTML emails that work in any email client.
    ---

    ## Default Media Query

    CSS media queries allow us to adjust the display and orientation of content at different screen sizes.

    Foundation for Emails has one breakpoint:

    - Small: 596 pixels or smaller.

    Many components can be modified at different screen sizes using special breakpoint classes. The grid is the most obvious example.

    **CSS Version**
    You can define the width of your columns on each breakpoint by using the grid with classes. `.small-6` creates a six column wide container (50%) width on the small breakpont. You can override this behavior on the large breakpoint by definining another size like `.large-4`.

    **Inky Version**
    In Inky, you can define the width by using the `small="x"` and `large="x"` attributes.

    ```html
    <style>
      .columns {border: 1px solid #333;}
    </style>

    <row>
      <columns small="6" large="4">4 columns, 6 columns on small</columns>
      <columns small="6" large="8">8 columns, 6 columns on small</columns>
    </row>
    ```

    ---

    ## Using the Media Query

    The media query will wrap the styles you wish to affect. Because there is only one breakpoint to consider and it's a max-width, your mobile styles or overrides will go in a media query. If you're using the CSS version of Foundation, use this media query to imitate the core breakpoint:

    ```scss
    /* Small only */
    @media screen and (max-width: 596px) {}
    ```

    The Sass version of Foundation uses a convenient variable to set the breakpoint width. Use this media query to imitate the core breakpoint:

    ```scss
    /* Small only */
    @media only screen and (max-width: #{$global-breakpoint}) {}
    ```

    ### Example usage

    ```scss
    .newsletter-title {
      text-transform: uppercase;
      font-size: 9px;
      padding-left: 40px;
      font-weight: bold;

      @media only screen and (max-width: #{$global-breakpoint}) {
        padding-left: 0;
      }
    }
    ```

    ```scss
    @media only screen and (max-width: #{$global-breakpoint}) {
      p {
        font-size: 19px;
        font-weight: 600;
      }
    }
    ```

    ---

    ## Changing the Breakpoint

    Changing the breakpoint is easy in the Sass version. In the `_settings.scss` you can control the width of this breakpoint.

    ```scss
    $global-breakpoint: $global-width + $global-gutter;
    ```

    The `$global-breakpoint` is a combined width of the `$global-width` and the `$global gutter`. You could hard-code a pixel value here instead of the variables or change the `$global-width` (recommended) as it takes account for the gutter calculation.

    ```scss
    $global-width: 580px;
    ```


    """

    pass


class MENU:
    """---
    title: Menu
    description: Use the menu component to create a horizontal or vertical list of links.
    sass: scss/components/_menu.scss
    ---

    ## Basics

    A menu is a `<table>` with a class of `.menu` and a `<tr>` inside of it. Each link in the menu is a `<th class="menu-item">` with an `<a>` inside of it.

    In Inky HTML, use the tag `<menu>` to make a menu, and the tag `<item>` to make an item.

    ```html
    <menu>
      <item href="https://zurb.com">Item</item>
      <item href="https://zurb.com">Item</item>
      <item href="https://zurb.com">Item</item>
    </menu>
    ```

    <div class="callout primary">
    - It's important to add an `href` attribute to your `<item>`'s to ensure that Outlook.com will not display `[undefined]` in your rendered email.<br>
    - Office 365 and Outlook.com require a valid url in the href attribute or you can use the # placeholder.
    </div>

    ---

    ## Vertical Menu

    Menus align horizontally by default. To switch to a vertical menu, add the class `.vertical` to the menu.

    ```html
    <menu class="vertical">
      <item href="https://zurb.com">Item</item>
      <item href="https://zurb.com">Item</item>
      <item href="https://zurb.com">Item</item>
    </menu>
    ```

    ---

    ## Vertical Menu on the Small Breakpoint

    Menus align horizontally by default. To switch to a vertical menu on the small breakpoint only, add the class `.small-vertical` to the menu. This works well because the email clients that support media queries fall into the small breakpoint like iPhones and Android 4.4.

    ```html
    <menu class="small-vertical">
      <item href="https://zurb.com">Item</item>
      <item href="https://zurb.com">Item</item>
      <item href="https://zurb.com">Item</item>
    </menu>
    ```"""

    pass


class MIGRATION:
    """---
    title: Foundation for Emails 2 Migration Guide
    description: This guide describes the changes required to migrate a Foundation for Emails template from version 1 (formerly Ink) to Foundation for Emails 2.
    tags:
      - upgrade
    ---

    ## What’s new?

    - **Streamlined and updated responsive grid:** We’ve simplified the markup in the new version so it’s faster and easier to code. The new responsive grid in Emails 2 requires fewer tags and classes. It’s also now responsive on Android Native!
    - **Inky templating language:** With Inky you can write less code and get more done. The Inky language gets you out of tables and into a simpler, more web-like, HTML.
    - **Built with Sass:** Now faster than ever, you can easily make sweeping visual changes to your email that reflect your brand styles - all within one settings file.
    - **ZURB Stack:** All kinds of task automation - [Panini](https://get.foundation/sites/docs/panini.html), our Handlebars templates, compiling Sass, BrowserSync, image compression, and auto inlining are built in to speed up your workflow.

    ---

    ## Overview

    First off, you'll want to choose a version to get started with.
    <br>[CSS version](css-guide.html) or the [Sass version with Inky](sass-guide.html)

    When migrating, the following items can be translated easily from 1 to 2:
    - Boilerplate
    - Visibility
    - Typography
    - Text helper classes
    - Container
    - Panel
    - Media Queries

    Other areas may require more changes to work correctly including:
    - Grid
    - Sub-grid (now part of Grid)
    - Button class

    What’s new that you might want to use:
    - Menu - Horizontal
    - Menu - Vertical

    ---

    ## HTML

    With Foundation for Emails 2, confusing and tedious tables are a thing of the past. The new Inky markup will save you time and energy coding your emails. It looks like:

    ```html
    <container>
      <row>
        <column small="12" large="4">
          Content
        </column>
        <column small="12" large="8">
          Content
        </column>
      </row>
    </container>
    ```

    You can use it to create the grid structure, buttons, and other components. We’ll go into this in detail in the components section. We'll explain more in the <a href="#grid">Grid section</a>.

    ---

    ## CSS & Sass

    Foundation for Emails 2 is available in a Sass version which let’s you quickly change common CSS values with some simple variables within the settings.

    These are some CSS classes that are no longer needed for proper spacing:
    - `.wrapper`
    - `.wrapper-last`
    - `.text-pad`
    - `.text-pad-left`
    - `.text-pad-right`

    Some helper classes have changed:

    `.center` was used in version 1 to center text.

    Version 2 now has more alignment classes:
    - `.text-center`: centers text
    - `.text-left`: aligns text to the left
    - `.text-right`: aligns text to the right
    - `.small-text-center`: centers text on the small breakpoint
    - `.small-text-left`: left aligns text on the small breakpoint
    - `.small-text-right`: right aligns text on the small breakpoint
    - `float-center`: centers an image (see the [alignment docs](alignment.html) for best practices.)

    ---

    ## Ink 1.0 Components

    ### Grid

    #### Old Markup

    In the Ink 1.0, we needed extra tags to support a wrapper element. This used to control the gutter and margins of a column.

    ```html
    <table class="container">
      <tr>
        <td>

          <table class="row">
            <tr>
              <td class="wrapper last">

                <table class="twelve columns">
                  <tr>
                    <td class="text-pad">

                    </td>
                    <td class="expander"></td>
                  </tr>
                </table>

              </td>
            </tr>
          </table>

        </td>
      </tr>
    </table>
    ```

    #### New Markup

    In Foundation for Emails 2, we’ve eliminated another tag in an effort to simplify your markup. Gutters are now directly applied to the column element itself. We still need to identify the last column with a `.last` class, and now the first column element with the `.first` class. If you have columns in the middle of first and last, they don't need a `.first` or `.last` class.

    Also, we stitched `<td>`'s to `<th>`'s because that allows Android 4 native to be responsive - win!

    ```html
    <table class="container">
      <tr>
        <td>
          <table class="row">
            <tr>
              <th class="first last small-12 large-12 columns">

              </th>
            </tr>
          </table>
        <th class="expander"></th>
        </td>
      </tr>
    </table>
    ```

    #### New Markup (Inky HTML)

    ```html
    <container>
      <row>
        <columns small="12" large="12">

        </columns>
      </row>
    </container>
    ```

    ---

    ### Sub-grid

    In an effort to unify the thinking across the Foundation family, we’ve removed the sub-columns and moved towards a fully functional small grid.

    #### Old Markup

    ```html
    <table class="container">
      <tr>
        <td class="wrapper last">

          <table class="twelve columns">
            <tr>
              <td class="six sub-columns">

              </td>
              <td class="six sub-columns last">

              </td>
              <td class="expander"></td>
            </tr>
          </table>

        </td>
      </tr>
    </table>
    ```

    #### New Markup (Plain HTML)

    ```html
    <table class="container">
      <tr>
        <td>

          <table class="row">
            <tr>
              <th class="first large-6 small-6 columns">

              </th>

              <th class="last large-6 small-6 columns">

              </th>
              <th class="expander"></th>
            </tr>
          </table>

        </td>
      </tr>
    </table>
    ```

    #### New Markup (Inky HTML)

    ```html
    <container>
      <row>
        <columns small="6">

        </columns>
        <columns small="6">

        </columns>
      </row>
    </container>
    ```

    ---

    ### Block Grid

    The block grid has a minor syntax change with identifying the number of elements that are displayed in the row. We’ve moved to the convention of `.up-x`, instead of `.x-up`.

    #### Old Markup

    ```html
    <table class="block-grid three-up">
      <tr>
        <td>
          Thing 1
        </td><td> <!-- Make sure the tags are directly next to each other -->
          Thing 2
        </td><td> <!-- Make sure the tags are directly next to each other -->
          Thing 3
        </td>
      </tr>
    </table>
    ```

    #### New Markup (Plain HTML)

    ```html
    <table class="block-grid up-3">
      <tr>
        <th class="column first">
          Thing 1
        </th><th class="column"> <!-- Make sure the tags are directly next to each other -->
          Thing 2
        </th><th class="column last"> <!-- Make sure the tags are directly next to each other -->
          Thing 3
        </th>
      </tr>
    </table>
    ```

    #### New Markup (Inky HTML)

    ```html
    <block-grid up="3">
      <column>Thing 1</column>
      <column>Thing 2</column>
      <column>Thing 3</column>
    </block-grid>
    ```

    ---

    ### Offset Columns

    Because we’ve eliminated the wrapper, offsets are now directly applied to the column itself.

    #### Old Markup

    ```html
    <table class="row">
      <tr>
        <td class="wrapper offset-by-four">

          <table class="eight columns">
            <tr>
              <td class="panel">

              </td>
              <td class="expander"></td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
    ```

    #### New Markup (Plain HTML)

    ```html
    <table class="row">
      <tr>
        <th class="small-4 small-offset-8 large-4 large-offset-8 columns">

        </th>
       </tr>
    </table>
    ```

    #### New Markup (Inky HTML)

    ```html
    <row>
      <columns small="4" large="4" class="small-offset-8 large-offset-8">

      </columns>
    </row>
    ```

    Offsets now can be used on the small breakpoint or the large, or both. They will shift over a set of columns over from the left.

    ---

    ### Buttons

    In the previous version of F4E the text inside of the button was the only clickable element. In F4E 2, we’ve taken a hybrid approach of using padding and borders to increase the clickable area. It requires one more table but the result is a much bigger touch target which is good for usability.

    #### Old Markup

    ```html
    <table class="button">
      <tr>
        <td>
          <a href="#">Button Label</a>
        </td>
      </tr>
    </table>
    ```

    #### New Markup (Plain HTML)

    ```html
    <table class="button">
      <tr>
        <td>
          <table>
            <tr>
              <td>
                <a href="https://zurb.com">I am successful</a>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
    ```

    #### New Markup (Inky HTML)

    ```html
    <button href="https://zurb.com"></button>
    ```

    Centering a button is easier now, just wrap the button with `<center>` tags.

    ---

    ### Panels

    In an effort to unify the terminology across the Foundation family `panels` are now called `callouts`.

    #### Old Markup

    ```html
    <table class="twelve columns">
      <tr>
        <td class="panel">
          Panel content
        </td>
        <td class="expander"></td>
      </tr>
    </table>
    ```

    #### New Markup (Plain HTML)

    ```html
    <table class="callout">
      <tr>
        <td class="callout-inner">

        </td>
        <td class="expander"></td>
      </tr>
    </table>
    ```

    #### New Markup (Inky HTML)

    ```html
    <row>
      <columns small="6">
        <p>One Word</p>
      </columns>
      <columns small="6">
        <callout class="secondary">
          <p>I'm in a callout!</p>
        </callout>
      </columns>
    </row>

    <callout class="primary">
      <row>
        <columns small="12">
          <row>
            <columns small="6">
              <p>This whole row is in a callout!</p>
            </columns>
            <columns small="6">
              <p>This whole row is in a callout!</p>
            </columns>
          </row>
        </columns>
      </row>
    </callout>
    ```

    You can wrap a callout around a `<row>` or the content inside a `<column>`.

    ---

    ## New Components

    ### Menu

    #### Old Markup (Plain HTML)

    ```html
    <table class="container">
      <tr>
        <td>

          <table class="menu">
            <tr>
              <td>
                <table>
                  <tr>
                    <th class="menu-item">
                      <a href="https://google.com">Nav 1</a>
                    </th>
                    <th class="menu-item">
                      <a href="https://google.com">Nav 2</a>
                    </th>
                    <th class="menu-item">
                      <a href="https://google.com">Nav 3</a>
                    </th>
                  </tr>
                </table>
              </td>
            </tr>
          </table>

        </td>
      </tr>
    </table>
    ```

    #### New Markup (Inky HTML)

    ```html
    <menu>
      <item href="one.html">Item One</item>
      <item href="one.html">Item Two</item>
      <item href="one.html">Item Three</item>
    </menu>
    ```

    The menu component can be used to create a simple set of links comonly used in headers, for social icons or in footers. Adding the `.vertical` class will change the orientation. You can even make it vertical on the small breakpoint only with `.small-vertical`.

    ### Spacer

    #### New Markup (Inky HTML)

    ```html
    <spacer size="100"></spacer>
    ```

    The spacer component creates consistant vertical spacing between or inside of elements. The size `size="x"` attribute allows you to set the height in pixels of vertical spacing you need.

    ### Wrapper

    #### New Markup (Inky HTML)

    ```html
    <wrapper>
      content here
    </wrapper>
    ```

    The wrapper component allows you to wrap content to target CSS within it. You can add classes to it so you can easily create a full with background.

    ## Dependencies

    The CSS version works exactly like the one we distributed with Ink 1.0. Check out our [getting started guide](css-guide.html) to learn more.

    To use the Sass version with the Inky markup language you'll want to install the Foundation for Emails project template. We have another [getting started guide](sass-guide.html) just for the Sass version of Foundation.
    """

    pass


class PANINI:
    """---
    title: Panini
    description: A flat file compiler that powers our prototyping template. Create pages with consistent layouts and reusable partials with ease.
    library:
      github: https://github.com/zurb/panini
      docs: https://github.com/zurb/panini
    ---

    {{{{raw}}}}

    If you've ever created a static site, maybe you had five pages that all shared the same header and footer. You create your first page, and then copy and paste the common elements to the next page. But now if you need to make a change to the header, the change has to be made across multiple files. You can do this with Emails in your campaigns too!

    Panini is a flat file compiler that uses the concepts of templates, pages, and partials&mdash;powered by the [Handlebars](https://handlebarsjs.com/) templating language&mdash;to streamline the process of creating static prototypes.

    Our [prototyping template](https://github.com/zurb/foundation-emails-template) uses Panini, along with a host of other tools for processing Sass and images, to make creating optimized templates easy. It's already been configured to utilize all of the features below, but if you want to learn the specifics of how to configure the library, head over to the [Panini GitHub page](https://github.com/zurb/panini).

    ---

    ## Basics: Templates & Pages

    A **template** is a common layout that every page in your design shares. It's possible to have multiple templates, but generally you'll only need one, and a page can only use one template. In the prototyping template, the default layout is found under `src/layouts/default.html`.

    Here's what a basic template might look like:

    ```handlebars
    <html>
      <head>
        <title>Definitely an Email!</title>
      </head>
      <body>
        <header class="header"><!-- ... --></header>
        {{> body}}
        <footer class="footer"><!-- ... --></footer>
      </body>
    </html>
    ```

    In the middle of the HTML is a bit of Handlebars code: `{{> body}}`. This is where the pages you write are injected when Panini runs, giving you a series of complete HTML files at the end.

    The **pages** make up the guts of your layouts. These files will just have the middle section of the design, since the layout already covers the top and bottom. The prototyping template includes one blank page to get you started, under `src/pages/index.html`.

    A basic page might look like this:

    ```html
    <h1>Page Title</h1>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Praesentium ducimus eligendi, reiciendis corporis quam facere quaerat qui, aspernatur molestiae velit, vero ea quisquam laborum corrupti repudiandae totam, at aliquam esse.</p>
    ```

    Note that there's no `<html>` or `<body>` tags, and no header or footer. This code will be injected into the `{{> body}}` declaration when Panini assembles your pages.

    In the prototyping template, these finished files are compiled into a standalone folder called `dist` (short for "distribution"), which also includes your processed CSS, JavaScript, and images. This folder can easily be uploaded to any ESP (Email Service Provider).

    ---

    ## Partials

    Partials are a feature of Handlebars which allow you to inject HTML anywhere in a page or layout. They're really useful when you need to repeat certain chunks of code throughout your pages, or to keep individual files from getting too cluttered with HTML.

    Here's an example of a layout file that divides its key sections into partials:

    ```handlebars
    <html>
      <head>
        <title>Definitely STILL an Email!</title>
      </head>
      <body>
        {{> header}}
        {{> body}}
        {{> footer}}
      </body>
    </html>
    ```

    The `{{> }}` syntax tells Handlebars to look for an HTML file with that name, and inject it at that place. In this example, we have files called `header.html`, `navigation.html`, and `footer.html`. In the prototyping template, these files all exist within `src/partials`.

    ---

    ## Page Variables

    Pages have a few built-in variables, which can be used within the page template itself, or within a layout or partial being used in tandem with the page.

    ### page

    Prints the name of the current page, without its original file extension. In the below example, if the page is `index.html`, `{{page}}` will become `index`.

    ```handlebars
    <p>You are here: {{page}}</p>
    ```

    ### root

    Use `{{root}}` before a file path to make sure it works no matter what folder the current page is in.

    For example, a path to an external CSS file will need to be different if the current page is at the root level of your site, or in a sub-folder.

    Here's how you'd use it with a `<link>` tag:

    ```handlebars
    <link rel="stylesheet" href="{{root}}assets/css/app.css">
    ```

    If the page is `index.html`, the path will look like this:

    ```html
    <link rel="stylesheet" href="assets/css/app.css">
    ```

    If the page is `folder/page.html`, the path will look like this:

    ```html
    <link rel="stylesheet" href="../assets/css/app.css">
    ```

    The `../` is added only on pages in a sub-folder, so the CSS can still be properly loaded.

    ---

    ## Helpers

    Helpers are special functions that manipulate content on the page. In addition to [Handlebars's built-in helpers](https://handlebarsjs.com/guide/builtin-helpers.html), Panini includes a few custom helpers and you can add your own.

    ### ifpage

    Displays the HTML inside the helper only on specific pages. In the below example, the HTML inside the helper will only show up on the `index.html` page.

    ```handlebars
    {{#ifpage 'index'}}
      <p>This is definitely the Index page.</p>
    {{/ifpage}}
    ```

    You can also check for multiple pages. If *any* name in the list matches the current page, the HTML will appear.

    ```handlebars
    {{#ifpage 'index' 'about'}}
      <p>This is definitely either the Index or About page.</p>
    {{/ifpage}}
    ```

    ### unlesspage

    The opposite of `#ifpage`, `#unlesspage` will only display the HTML inside of it if the current page is *not* in the parameters.

    ```handlebars
    {{#unlesspage 'index'}}
      <p>This is definitely <em>not</em> the Index page.</p>
    {{/unlesspage}}
    ```

    ### repeat

    Repeats the content inside of it `n` number of times. Use this to easily print lots of duplicate HTML in a prototype.

    ```handlebars
    <ul>
      {{#repeat 5}}
      <li>Five hundred ninety-nine US dollars</li>
      {{/repeat}}
    </ul>
    ```

    ### markdown

    Converts Markdown into HTML.

    ```handlebars
    {{#markdown}}
    # Heading 1
    Lorem ipsum [dolor sit amet](https://html5zombo.com), consectetur adipisicing elit. Nam dolor, perferendis. Mollitia aut dolorum, est amet libero eos ad facere pariatur, ullam dolorem similique fugit, debitis impedit, eligendi officiis dolores.
    {{/markdown}}
    ```

    ### Custom Helpers

    If you don't see the right helper, you can write your own. Add a javascript file to 'src/helpers', restart npm, then call it in your templates.

    ```javascript
    // Example file src/helpers/bold.js
    module.exports = function(options) {
      // options.fn(this) = Handlebars content between {{#bold}} HERE {{/bold}}
      var bolder = '<strong>' + options.fn(this) + '</strong>';
      return bolder;
    }
    ```
    Then in your projects call your custom `{{#bold}}` helper

    ```handlebars
    {{#bold}}ideas{{/bold}}
    ```

    ---

    ## Custom Data

    Custom data can be added to your pages. This data can then be inserted into your HTML through Handlebars. There are two ways to add data to a project.

    To add variables to a specific page only, add it at the top of the page's HTML as a [Front Matter](https://jekyllrb.com/docs/frontmatter/) block. Let's say the below content is inside `src/pages/index.html`.

    ```html
    ---
    title: Page Title
    description: Lorem ipsum.
    ---

    <!-- The rest of your HTML is down here. -->
    ```

    Now, you can insert the values of these variables into the `index.html` page, *or* the `default.html` layout. To insert a variable, wrap the name of the variable in double curly braces, like so:

    ```handlebars
    <h1>{{ title }}</h1>
    ```

    Variables can also be added globally by creating an external JSON or YML file, and adding it to the `src/data` folder in your project. Let's create a file called `breakfast.yml`:

    ```yaml
    - eggs
    - bacon
    - toast
    ```

    Panini will load in the contents of this YML file as a variable called `{{ breakfast }}`. Because it's an array, we can loop through it using Handlebars's `{{#each}}` helper:

    ```handlebars
    <ul class="breakfast-items">
      {{#each breakfast}}
        <li>{{ this }}</li>
      {{/each}}
    </ul>
    ```

    This code will print three `<li>`s, one for each item in the file.

    ## Tutorials

    [Staying D.R.Y. with Panini](https://zurb.com/university/lessons/staying-d-r-y-with-panini)
    Panini comes with tons of Handlebars helpers built in, like a repeat helper or markdown parser, but in this lesson we’ll take a look at creating a custom month/year helper for an HTML email.


    {{{{/raw}}}}"""

    pass


class SASS_GUIDE:
    """---
    title: Getting Started with Sass
    description: Get started with the Sass-powered ZURB Stack for writing HTML emails.
    ---

    Foundation for Emails takes the pain out of developing HTML emails by giving you a set of powerful, tested components out of the box. This includes a fully-responsive grid, buttons, callouts, menus, and more.

    The Sass workflow for Foundation for Emails is backed by the [ZURB Email Stack](zurb-stack.html), an all-in-one build system for creating HTML emails. This workflow requires a bit more up-front setup, but the tooling makes it wicked fast to code, and keeps your code amazingly clean with our new custom HTML tags in Inky.

    The ZURB Stack workflow also includes Handlebars, allowing you to write emails as templates instead of static files. Lastly, you can easily make sweeping design changes with the Sass [settings file](sass.html#the-settings-file). Here’s everything that’s packaged in this template:

    - Inky HTML
    - Sass
    - Handlebars templates
    - BrowserSync
    - Image compression
    - Inlining

    In this Getting Started guide, we'll download Foundation for Emails, construct the basic grid, and then inline our email so it's ready to test.

    ---

    ## Requirements

    To use the Sass version of Foundation for Emails, you need Node.js installed on your computer. Node is compatible with Windows, OS X, and Linux&mdash;the [Node.js website](https://nodejs.org/) has installers for every operating system.

    ---

    ## Installing

    We'll use the Foundation CLI to set up a new project. If you already have the Foundation CLI installed from Foundation for Sites, you can skip this first command.

    ```bash
    npm install --global foundation-cli
    ```

    If you run into any permission errors (EACCESS) on OS X or Linux, you can try prefixing the command with `sudo`.

    ```bash
    sudo npm install --global foundation-cli
    ```

    Once the CLI is installed on your machine, it’s super easy to fire up a blank Foundation for Emails project. Move into the folder you store your projects in, and then run this command:

    ```bash
    foundation new --framework emails
    ```

    The CLI will ask you for a project name, which is used as the name of the folder to install in. After that, the project template will be downloaded, and the various dependencies installed. The entire process takes over a minute.

    ---

    ## Running the Server

    After your project has been installed, run `cd project`, where `project` is the name of the project just created. Then run:

    ```bash
    npm start
    ```

    This will kick off the build process, which includes HTML parsing, Sass, image compression, and a server. When the initial build finishes, your browser will pop open a new tab pointing to your project. You'll be seeing a blank `index.html` file.

    ---

    ## File Structure

    You'll do all of your work in the `src` folder of your project. The various HTML files, Sass files, and images inside of `src` are compiled to a new folder called `dist/` (as in "distribution"), which contains the final HTML and CSS for your emails. These are the files you'll upload to Litmus, Campaign Monitor, etc. for testing, or load into your email campaign service.

    Here's a breakdown of the files in the `src` folder:

    - `assets/`: Sass and image files.
    - `layouts/`: Boilerplate HTML that wraps all of your emails.
    - `pages/`: HTML files for emails.
    - `partials/`: Reusable chunks of HTML that can be injected into pages.

    ---

    ## Boilerplate

    Inside `src/layouts/default.html`, you can see the boilerplate needed to make an HTML work. Below we've annotated this boilerplate, explaining what does what.

    {{{{raw}}}}

    ```html
    <!-- Emails use the XHTML Strict doctype -->
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="https://www.w3.org/1999/xhtml">
    <head>
      <!-- The character set should be utf-8 -->
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
      <!-- Enables media queries -->
      <meta name="viewport" content="width=device-width"/>
      <!-- Link to the email's CSS, which will be inlined into the email -->
      <link rel="stylesheet" href="assets/css/foundation-emails.css">
    </head>

    <body>
      <!-- Injection point for the inline <style> element. Don't remove this comment! -->
      <!-- <style> -->
      <!-- Wrapper for the body of the email -->
      <table class="body" data-made-with-foundation>
        <tr>
          <!-- The class, align, and <center> tag center the container -->
          <td class="float-center" align="center" valign="top">
            <center>
              <!-- The body of each email you write is injected here -->
              {{> body}}
            </center>
          </td>
        </tr>
      </table>
    </body>
    </html>
    ```

    {{{{/raw}}}}

    ---

    ## Grid Basics

    Foundation for Emails includes many common elements needed to make HTML emails: a grid, typography styles, buttons, callouts, and more.

    The markup required to create HTML emails that work in all email clients is *complicated*, and involves writing many tables. However, the ZURB Stack includes Inky, a templating language that converts simple HTML tags to the complex HTML required for the components.

    Let's build a basic grid.

    ```html
    <container>
      <row>
        <columns small="12" large="6">Column One</columns>
        <columns small="12" large="6">Column Two</columns>
      </row>
    </container>
    ```

    Here we're using all three of the key layout elements: the container, row, and column.

    A **container** will wrap the body of your email. It applies a maximum width to the body of the email.

    **Rows** are used to group sets of **columns** together. Columns divide your layout into horizontal sections that sit side-by-side. On small screens, these columns stack on top of each other to save space&mdash;unless you set them up to keep their layout on small screens.

    In the above example, we used the attribute `large` on the `<column>` tag to define a size for that column *on large screens*. Foundation uses a 12-column grid, and since `large="6"`, that means each column will take up half the width of the row. On a small screen, each columns will be full width and the second column will stack underneath.

    ---

    ## Inlining

    Now that we have a basic email, the last thing we need to do before we can send it is *inline* it. This is the process of injecting all of the CSS for the email into the HTML, so that it works as a self-contained file.

    Email clients like Gmail and Outlook strip out `<style>` tag from the `<head>` and Gmails strips it from the `<body>` of the email as well. It's best to have your CSS written inline within your markup. Hand writing all your CSS inline in a style tag would be a real pain and would take a long time.

    The build process doesn't inline by default. To do a full inlining process as you build, quit the process you have running in your command line, and run `npm run build` instead. This does the same build process, but adds the inlining step at the end.

    Your email's CSS will include media queries for responsive styling which the inliner tool will move into the `<body>` so they are preserved.

    When the email opens up in the browser, it will look the same. But try viewing the source code of the page, and you'll see a mess of code like this:

    ```html
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html xmlns="https://www.w3.org/1999/xhtml" lang="en" xml:lang="en" style="background:#cacaca;min-height:100%"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">...
    ```

    ---

    ## Testing

    Now that you have an inlined email, you'll need to test it in real email clients to verify that it looks correct. All of Foundation's built-in components have already been tested in every major email client, so we've done a lot of the work for you. However, you'll want to test your email before you send it out to the masses.

    The most popular tool for testing emails is [Litmus](https://litmus.com/). All you have to do is paste in the HTML of an email, and you get a live preview in any email client you want.

    It's up to you to choose what email clients are important to test in, but you can [see our compatibility list](compatibility.html) for recommendations.

    ---

    ## Next Steps

    You've successfully installed Foundation for Emails, and written, inlined, and tested your first email! To keep going with the framework, you can check out the documentation for the other framework components, including [buttons](button.html), [callouts](callout.html), [menus](menu.html).

    If you're interested in going in-depth on the framework with the Foundation team, [check out our master class on Foundation for Emails](https://zurb.com/university/responsive-emails-foundation), an on-demand video series that explores every aspect of email design workflow.
    """

    pass


class SASS:
    """---
    title: Using Sass
    description: Foundation for Emails is written in Sass, which allows us to make the codebase customizable and flexible.
    ---

    <div class="primary callout">
      <p>Not familiar with Sass? The [official tutorial](https://sass-lang.com/guide) on sass-lang.com is a great place to start.</p>
    </div>

    ## Compatibility

    <img src="https://get.foundation/emails/docs/assets/img/logos/sass-logo.svg" alt="Sass logo" class="float-right" style="width: 150px; height: 150px; margin-left: 1rem;">

    **Foundation for Emails can be compiled with Ruby Sass and dart-sass.** We tend to stick to the latest versions of both compilers when possible. Our documentation, as well as the ZURB Email Stack, are compiled with [sass](https://github.com/sass/dart-sass). We recommend these versions of either compiler:

    - Ruby Sass **3.4+**
    - dart-sass **1.35.2+**

    ---

    ## Loading the Framework

    If you're using the [ZURB Email Stack](zurb-stack.html) to create emails, Sass has already been set up for you. However, it's also easy to incorporate the Foundation for Emails Sass into your own email workflow.

    To get started, first install the framework files using Bower or npm.

    ```bash
    npm install foundation-emails --save
    ```

    Next, add the framework files as an import path in Sass. How you do this depends on your build process, but the path is the same regardless: `[packages_folder]/foundation-emails/scss`

    Here's an example using grunt-contrib-sass:

    ```js
    grunt.initConfig({
      sass: {
        dist: {
        options: {
            loadPath: ['node_modules/foundation-emails/scss']
          }
        }
      }
    });
    ```

    If you're using Compass, open your project's `config.rb` and add the import path there:

    ```ruby
    add_import_path "node_modules/foundation-emails/scss"
    ```

    Finally, add an `@import` statement to the top of your main Sass file.

    ```scss
    @import 'foundation-emails';
    ```

    You're also going to want a settings file for your project, which will allow you to modify the default styles of Foundation for Emails. **[Download the latest settings file here](https://raw.githubusercontent.com/zurb/foundation-emails/master/scss/settings/_settings.scss)**, add it to your project as `_settings.scss`, then import it *before* Foundation itself.

    ```scss
    @import 'settings';
    @import 'foundation-emails';
    ```

    ---

    ## The Settings File

    All Foundation projects include a **settings file**, named `_settings.scss`. If you're using the ZURB Stack, you can find the settings file under `src/assets/scss/`. If you're installing the framework standalone using Bower or npm, there's a settings file included in those packages, which you can copy into your own Sass folder to work with.

    Every component includes a set of variables that modify core structural or visual styles. If there's something you can't customize with a variable, you can just write your own CSS to add it.

    <div class="callout warning">
      <p>Once you've set up a new project, your settings file can't be automatically updated when new versions change, add, or remove variables. Keep tabs on new <a href="https://github.com/zurb/foundation-emails/releases">Foundation releases</a> so you know when things change.</p>
    </div>

    Here's an example set of settings variables. These change the default styling of [buttons](button.html):

    ```scss
    // Text color of buttons.
    $button-color: $white;

    // Text color of buttons with a light background.
    $button-color-alt: $medium-gray;

    // Font weight of buttons.
    $button-font-weight: bold;

    // Background color of buttons.
    $button-background: $primary-color;

    // Border around buttons.
    $button-border: 2px solid $button-background;
    ```

    We put together some [Best Practices on Sass file structure](https://zurb.com/university/lessons/avoid-a-cluttered-mess-sensible-sass-file-structure) that will help you keep your project clean.
    """

    pass


class SPACER:
    """---
    title: Spacer
    description: Vertical spacing in emails is inconsistent. The spacer component will help you create the space you need, the same on every device and client.
    tags:
      - spacing
      - height
      - margin
      - padding
    ---

    ## Basics

    Vertical spacing between email clients is not as simple as it sounds, in fact, it’s consistently inconsistent. Versions of Outlook don’t respect margin and padding the same and `<br>`’s are different all over the place.

    The spacer is used to create vertical spacing between elements. The size `size="x"` attribute allows you to set the height in pixels of vertical spacing you need.

    When using [Inky](inky.html) HTML, the `<spacer>` tag will create this structure for you. You can use them between rows, containers or inside wrappers, rows, columns, and containers. In this example, this spacer will create 100px of vertical spacing:

    ```html
    <p>Stuff on top</p>
    <spacer size="100"></spacer>
    <p>Stuff on bottom</p>
    ```

    The Inky `<spacer>` tag also allows you to specify contextual spacer sizes for small or large screens. In the example below, there will be 40px of vertical spacing on small screens, and 100px of spacing on large screens.


    ```html
    <p>Stuff above...</p>
    <spacer size-sm="40" size-lg="100"></spacer>
    <p>...stuff below.</p>
    ```

    Specify both `size-sm` and `size-lg` or use just one of those attributes to render a spacer only on the corresponding size screen.
    """

    pass


class STYLING:
    """---
    title: CSS with Inky
    description: Coding with Inky is easy and fun! Because some of the CSS classes are generated by Inky, we created a guide to help you style your email.
    ---
    """

    pass


class THUMBNAIL:
    """---
    title: Thumbnail
    description: Spruce up an image tag with our thumbnail style.
    published: false
    ---

    The `.thumbnail` class can be applied directly to an `<img>` element, or an `<a>` that wraps it. Make sure the `<img>` has an alt attribute that describes the contents of the image.

    The thumbnail style adds padding and a box shadow to an image. To use it, just add the class `.thumbnail` to an image element.

    ```html
    <img src="https://placehold.it/200x200" class="thumbnail">
    ```

    <!-- <table class="thumbnail">
      <tr>
        <td><img src="//placehold.it/300x300" class="thumbnail" /></td>
      </tr>
    </table> -->"""

    pass


class TIPS_TRICKS:
    """---
    title: Tips &amp; Tricks
    description: We've put together some Responsive Emails Tips &amp; Tricks that will help you navigate the mine field that is coding HTML emails.
    ---

    Coding responsive emails can be a real pain. This guide will help you through some of the the most common issues you'd face. It's a living document and will get updates periodically.

    ## Why Foundation for Emails

    Most responsive emails are built on templates. They’re simple, easy to drop content into and are usually well-tested. Templates have a serious cost though. "Oh, so you want to do anything other than change the colors and text?" Sorry … you’re out of luck, Chuck. Templates tend to be hard to customize heavily or to extend. For that you need a framework.

    A framework is a collection of reusable code and design patterns which gives users a solid, tested base upon which to build. Not a bunch of visual styles you can just bolt on as an afterthought and call it a day.

    - Frameworks give you the solid base of a template, but the extensibility of custom code. You can make your template fit your content, not the other way around.
    - Additionally, a framework gives you a common codebase to structure your projects around. So if new team members work on the project, they don't have to re-invent the wheel. You can spend less time coding your email and more time optimizing your campaigns.

    ## Need to know

    The sad truth about creating or coding HTML emails is that tables are the only things that are universally supported when it comes to email design. If you came from the world of building websites, this may seem like a stepping into Doc Brown's Delorean, charging up the Flux-capacitor, and going back to the year 1996. Suddenly your CSS is written with inline style tags, useful CSS properties don't work and you're burried in a sea of table tags.

    <div class="callout secondary tip">General rule of thumb: your email is not going to look identical in every client. And that’s OK.</div>

    It's not all doom and gloom though, and we're all in this together. Foundation for Emails helps by getting you away from tables (Sass version), helping you with an organized project structure, and a well tested codebase to make this much easier. We've put together this guide and [links to resources](https://get.foundation/emails/resources.html) from our friends to help you along as well as a new [Responsive Emails master class](https://zurb.com/university/responsive-emails-foundation) to become a HTML email pro.

    ---

    ## HTML

    #### Email Container Width

    The email equivalent of the browser window is the "viewport", or the area in an email client dedicated to showing the actual email. This varies quite a bit.

    Foundation for Emails' default container with around 600px wide. That's because the majority of email clients have a preview pane that is around 550-700 pixels. With the Sass version, you can easily customize this width by adjusting the `$global-width` variable.

    The height of your email doesn't matter as much because people scroll. It still helps to have your most compelling content towards the top.

    #### Structure and alignment:

    When it comes to making emails, divs aren’t a thing. Don’t kill the messenger, but it’s true. It's not fun finding out we can't just use a `<div>` with auto left and right margins for centering, or background colors; it won't work with most email clients. `<div>`'s can still be used for targeting CSS and for grouping semantically related elements, but shouldn’t be used for structural purposes or spacing.

    Instead, you can use the `<wrapper>` Inky tag to create background colors and target elements inside. [More on Wrapper &#8594;](wrapper.html)

    Use tables instead. For those of you who haven’t used tables since Netscape Navigator (or ever) here’s a quick recap.

    There are three main tags in a table.

    ```html
    <table>
      <tr>
        <td></td>
      </tr>
    </table>
    ```

    The `<table>` tag wraps the entire table. The `<tr>` tag denotes a row. The `<td>` tag is used to wrap a table cell.

    Some web browsers may be forgiving, but it’s important to include all three tags. Don’t get lazy and skip the `<tr>`. Email clients can be unpredictable, so the first step to good rendering is to have valid markup.

    *It makes debugging and sharing code a lot easier when you’re consistent. It lets other developers get oriented within the code and makes it easier to tell what you’re looking at, just like consistent indentation and comments.*

    While semantic, the “table row” and “table data” elements aren’t that helpful for creating row and column layouts. They’re designed for spreadsheets or other *non-uniform* grids. They can’t be used structurally.

    Instead, we use nested tables. Think a bunch of single-cell spreadsheets being nested.

    Where we would have divs in website land…

    ```html
    <div class="row">
      <div class="small-12 columns">
        <!-- Content -->
      </div>
    </div>
    ```

    …we have tables in email world.

    ```html
    <table class="row">
      <tbody>
        <tr>
          <th class="small-12 columns first last">
            <table>
              <tr>
                <th>
                  <!-- Content -->
                </th>
                <th class="expander"></th>
              </tr>
            </table>
          </th>
        </tr>
      </tbody>
    </table>
    ```

    Table elements have their own special “display” values. Sometimes we can override them to display as block elements, but more on that later. The display value (in combination with the HTML schema specified in the DOCTYPE), specifies the rules for rendering each element.

    Tables have all sorts of fancy HTML attributes…not all of which can be set in CSS. This is unfortunate because separation of concerns dictates that we should try and keep our structure in the markup (HTML) and styles in the CSS. Some inliners will take care of this for you.

    ```html
    <table align="center" valign="top" cellspacing="0">
      …
    </table>
    ```

    Speaking of CSS, you should only set classes and IDs on tables or `<td>` tags, not `<tr>` tags. If you need to apply padding, only do that on a `<td>` as well. Been there, done that — we had a lot of trouble with this while building the first version of Foundation for Emails. Your milage may vary, but just trying to help you out by saving you some time.

    ---

    ## CSS

    #### CSS Support
    Support of CSS properties varies greatly between email clients. You're best off sticking with the basics and not getting too fancy.

    This CSS compatibility chart will really save you some pain when writing CSS:
    [CSS Support Chart](https://www.campaignmonitor.com/css/)

    <img src="https://get.foundation/emails/docs/assets/img/campaign-monitor-css-guide.jpg" alt="">

    For some things you can do and work-arounds, see the <a href="#progressive-enhancement">Progressive Enhancement</a> section below.

    ---

    #### Inlining CSS

    Gmail strips the `<head>` (and, consequently, `<style>`) tags from your email. Therefore your email's CSS needs to be inlined. You know, like old school CSS:

    ```html
    <table class="menu" style="padding:0;text-align:center;vertical-align:top;width:auto">
    ```

    Because media queries cannot be inlined, they need to be moved into the `<body>` of the email. Our inliner does that for you.

    If you're using Sass with the ZURB stack, you enjoy the luxury of automatic inlining when running `npm run build`. Your file will be copied into the `dist ` folder where you will find it minified and inlined. You'll want to do this before you test or send your email.

    If you are using the CSS version, you can use our [web inliner](https://get.foundation/emails/inliner-v2.html).

    ---

    #### Margin and Padding:

    - Outlook 2007, 2010, and 2013 does not support "padding" in `<p>`, `<div>` or `<a>` tags. Use margin instead.
    - Forget about using CSS positioning like `top`, `bottom`, `relative`, `absolute`.
    - Margin is universally supported BUT you may see some inconsistencies in Outlook 2007, 2010, and 2013. Padding is safer. Also, it is known that Outlook.com does not support the margin property. The odd thing is Outlook.com does support margin with a capital "M".
    Use it like this:

    ```scss
    margin: 10px;
    Margin: 10px;  // fallback for Outlook.com
    ```

    - `<br>` tags are ok, but you won't get pixel perfect results and you can quickly fill up your code with messyness.
    - **Your best option** for vertical spacing is to use the `<spacer>` component in Foundation for Emails. It works consistently on all email clients and lets you set the height with the size attribute. So `<spacer size="32"></spacer>` will create 32px of vertical space.

    ---

    #### Colors:

    - It's better to use full 6 digit hex codes colors in HTML emails (#ffffff vs #fff). Although all the major email clients support short hex colors, Outlook.com (Hotmail), Lotus Notes 6.5, 7 and 8 do not.
    - RGB's are supported all the major email clients but RGBA's are only supported in IOS, Apple Mail, Gmail, and Android 4 (Gmail).
    - Background colors work across all email clients as well as color for fonts.
    - iOS devices sometimes render dates/times and phone numbers in blue irrespective of CSS declarations. A good workaround is to include the the CSS snippet from https://removebluelinks.com/ in combination with wrapping the affected content with `<font color="XXXXXX"></font>` to ensure it gets rendered in the color required.

    ---

    ## JavaScript

    Nope. JavaScript is not a reality in most popular emails. It will be blocked for security reasons.

    ---

    ## Images

    #### Blocked Images

    Beware of blocked images. Many email clients block images by default. “Many” being pretty much everybody except Apple Mail/iOS and Gmail. When this happens, email clients offer an option to display images but you're relying on your customer to know this.

    Q: What’s a designer to do?

    A: Always use an ALT tag.

    ALT tags are very important for accessibility. They will show when images are blocked so your customers can tell an image is supposed to be there.

    ```html
    <img height=“390” width=“580” src=“hero.jpg” alt=“ALT tags are important for accessibility *and* overprotective mail clients” />
    ```

    Some clients even let you style the ALT text.

    To style ALT text, place your font styles inline on the image.

    ```html
    <img height=“390” width=“580” src=“hero.jpg” alt=“Company Name” style=“font-size:45px; font-family: serif; font-weight: bold; color: #b31b1b;” />
    ```

    #### Retina Images

    OK, so I got my readers to allow images…now what about Retina?

    Fun fact: Your email client is better at resizing images than Photoshop is.

    The problem is Outlook and Thunderbird like to show images in their *ahem* full glory.

    The solution is inline size attributes.

    ```html
    <img height=“390” width=“580” src=“hero.jpg” alt=“I can be your hero, baby…” />
    ```

    #### Image File Size

    Reduce Image Size. There is no guarantee the recipient of your email will have wifi and waiting for images to load is guaranteed to annoy some of your recipients.

    #### Gif's and Video in Emails

    Animated GIFs have *surprisingly* good support. As usual, there are caveats. Outlook only shows the first frame of the animation. Make sure your call to action is visible in the first frame.

    Video's in emails are not supported except in Apple Mail and Outlook 2011. [See how Litmus explores background video in HTML Emails](https://litmus.com/blog/how-to-code-html5-video-background-in-email)

    #### Quick Tips on Images

    Remember to use full paths to images, not relative paths. (e.g. https://www.yourserver.com/email/images/logo.gif).

    Also, link to images from your own server, not anyone elses. If you don't control it you never know when that url will change.

    ---

    ## Buttons

    #### Images for Buttons

    Images get blocked. So if you have an important CTA image that looks like a button, it will likely get missed. And that defeats the purpose of your email.

    ---

    ## Email File Size

    Sending an email with a file size between 15KB-100KB is ideal. Some email clients will send the email to spam if the file size is greater.

    Emails can get cut off by the ‘This message has only partially downloaded’ in iOS Apple Mail the Gmail app for iOS. The user will be prompted to "Download entire message" or "Download remaining X KB".

    Problems

    - This could cause the email open to not be registered
    - Your email's call to action could be missed

    Causes

    - Making the HTML file size less than 20kb (20540 characters) - not including images or the plain-text version. This character count includes things like inline styles, HTML tags, and spaces, and other HTML entities.
    - Downloading the message over cellular data, not WiFi. Can't do much about this one.

    Solution?

    - Create emails that are short and to the point. Too many call-to-actions's, topics, or long emails don't tend to work that well anyways.
    - Minify your HTML. The ZURB Stack comes with a setting to minify the HTML if you run `npm run build`. This will remove white-space which adds to the charachter count and file size. Our [web inliner](https://get.foundation/emails/inliner.html) also has an option to remove (compress) whitespace between your charachters.

    ---

    ## Responsive Best Practices

    #### Font Size

    Increase Text Size. Don’t make users squint to read what you sent them.  Shorten the message a bit and increase the size (including links and CTAs) to make sure they are able to see and understand everything clearly.

    Text should never be smaller than 11 pixels. For comparison, the body style in Foundation uses a font size of 16 pixels at the large size, which is the default text-size setting.

    Apple suggests 17px for mobile devices and Google recommends up to 21px for body copy.

    #### Typography

    <img src="https://group-mail.com/wp-content/uploads/Screen-shot-2011-08-12-at-2.58.47-PM.png" alt="">

    Use fonts that are recognizeable to most users.

    In general, use a single font throughout your email. Mixing several different fonts can make your email seem fragmented and sloppy. Instead, use one font and just a few styles and sizes.

    <img src="https://developer.apple.com/ios/human-interface-guidelines/images/TypographyGraphic_2x.png" alt="">

    <a id="progressive-enhancement"></a>
    ## Progressive Enhancement

    Do progressively enhance. ZURB and Foundation for Emails builds Outlook-first. Meaning, design for the most constrained platform you support, then add features. It's a great idea to know what devices your emails are being opened on and at what rate. Email Service Providers like Campaign Monitor and Mailchimp track this for you.

    <img src="https://get.foundation/emails/docs/assets/img/cm-email-client-stats.png" alt="image of graph">

    Let's imagine the vast majority of your audience uses Apple Mail. You'd be able to get away with using CSS keyframe animation and SVG masks.

    If you're not sure where to start, you can see the [Email Client Market Share](https://emailclientmarketshare.com/) by Litmus

    #### Button Size and Touch Targets

    Apple’s iPhone Human Interface Guidelines recommends a minimum target size of 44 pixels wide 44 pixels tall.

    Microsoft’s Windows Phone UI Design and Interaction Guide suggests a touch target size of 34px with a minimum touch target size of 26px.

    Nokia’s developer guidelines suggest that the target size should be no smaller than 1cm x 1cm square or 28 x 28 pixels.

    While these guidelines give a general measurement for touch targets, they’re not consistent with each other, nor are they consistent with the actual size of the human finger. In fact, their suggested sizes are much smaller than the average finger, which can lead to touch target problems for users on mobile devices.

    ---

    ## Testing

    Testing costs money. Not testing costs you customers.

    So test, test, and test again. After you have an inlined version of your email, you should test it on as many devices and email clients as you can.

    The two top testing services out there are:
    [Litmus](https://litmus.com/)
    [Email on Acid](https://www.emailonacid.com/)

    If you're not sure where to start, you can see the [Email Client Market Share](https://emailclientmarketshare.com/) by Litmus

    Foundation for Emails is tested on the most popular clients. You can also test on the clients listed in our [compatability guide](compatibility.html)

    These services make testing on lots of email clients and devices much faster. Try to hit the main categories: a Windows machine, a Mac, an iPhone, an Android, a tablet. Still, nothing beats testing on a real device.

    ---

    ## Sending your Emails

    ESP's are made for sending thousands and thousands of emails, they can help you get emails out without being deemed a spammer.

    ESP's like Campain Monitor and Mailchimp cost money, but they can save you huge headaches and costs down the road.

    Try not to look like SPAM. Pretty obvious, but just writing good code and honest copy should keep you out of the can here. Your HTML email is definitely NOT the place for a Viagra joke.

    OBEY THE LAW. The CAN-SPAM act became law on Jan. 1, 2004. It says there many things you must do as a commercial email-er. Highlights are basically don't be deceptive, and that you MUST include a physical mailing address as well as a working unsubscribe link.

    ---

    ## Design Tips

    Just like in web design, it doesn't hurt to think above the fold. Meaning what users will see before they have to scroll.

    Use your footer like a footer. This is a great place for lots of things including phone numbers and addresses, about information, unsubscribe options, and perhaps a little reminder of what this email is and why the reader is on the list.
    """

    pass


class TYPOGRAPHY:
    """---
    title: Typography
    description: Typography in Foundation for Emails is meant to make your life easier by providing clean, attractive, simple default styles for all of the most basic typographical elements.
    sass: scss/components/_typography.scss
    ---

    ## Paragraphs

    This is a paragraph. Paragraphs are preset with a font size, line height and spacing to match the overall vertical rhythm. To show what a paragraph looks like this needs a little more content—so, did you know that female Giant Squids on average are around twice the size of (and around 10 feet longer than) their potential mates? Pretty cool. Use the `<strong>` and `<em>` tags to denote text that should be displayed or read with emphasis. Browsers will <strong>bold</strong> and <em>italicize</em> them, while screen readers will read the words with <em>emphasis</em>.

    ```html
    <p>This is a paragraph. Paragraphs are preset with a font size, line height and spacing to match the overall vertical rhythm. To show what a paragraph looks like this needs a little more content—so, did you know that female Giant Squids on average are around twice the size of (and around 10 feet longer than) their potential mates? Pretty cool. Use the `<strong>` and `<em>` tags to denote text that should be displayed or read with emphasis. Browsers will <strong>bold</strong> and <em>italicize</em> them, while screen readers will read the words with <em>emphasis</em>.</p>
    ```

    ---

    ## Header

    Foundation includes styles for all headings.

    ```html
    <h1>h1. This is a very large header.</h1>
    <h2>h2. This is a large header.</h2>
    <h3>h3. This is a medium header.</h3>
    <h4>h4. This is a moderate header.</h4>
    <h5>h5. This is a small header.</h5>
    <h6>h6. This is a tiny header.</h6>
    ```

    ---

    ### Header Sizes

    The framework includes two typographic scales&mdash;one uses a narrow range of sizes for small- and medium-sized screens, and the other uses a wider range of sizes for large-sized screens. You can change these scales, or add new ones for other breakpoints, by editing the `$hx-font-size` variables in your project's <a href="sass.html#the-settings-file">Settings File</a>.

    Header  | Default |
    --------|---------|
    `<h1>`  | 34px    |
    `<h2>`  | 30px    |
    `<h3>`  | 28px    |
    `<h4>`  | 24px    |
    `<h5>`  | 20px    |
    `<h6>`  | 18px    |

    ---

    ## Small Header Segments

    By inserting a `<small>` element into a header Foundation will scale the header font size down for an inline element, allowing you to use this for subtitles or other secondary header text.

    ```html
    <h3>Foundation for Emails <small>Version 2</small></h3>
    ```

    ---

    ## Text Sizes

     You can change the size of text in paragraphs with `.text-` classes. These classes will apply to the large breakpoint as well as the small.

     ```html
     <container>
       <row>
         <columns>
           <p class="text-xs">Extra small</p>
           <p class="text-sm">Small</p>
           <p class="text-lg">Large</p>
           <p class="text-xl">Extra large</p>
           <p class="text-xxl">Extra extra large</p>
         </columns>
       </row>
     </container>
     ```

     ---

    ## Links

    Links are very standard, and the color is preset to the Foundation primary color. [Learn more about Foundation's global colors](global.html).

    ```html
    <p>Links are very standard, and the color is preset to the Foundation primary color. <a href="global.html">Learn more about Foundation's global colors.</a></p>
    ```

    ---

    ## Dividers

    Use dividers to define thematic breaks between paragraphs or sections of your email.

    ```html
    <h-line></h-line>
    ```"""

    pass


class VISIBILITY:
    """---
    title: Visibility Classes
    description: Selectively show content for different screen sizes.
    tags:
      - show
      - hide
    ---

    Visibility classes allow you to control what content appears on what screen size.

    Foundation for Emails has two breakpoints: *small*, which is any email client under 596 pixels wide, and *large*, any client over 596 pixels. This means small generally correlates to mobile clients, and large correlates to desktop clients.

    Due to Outlook's lack of support for certain CSS properties, the Foundation for Emails visibility classes should be used in conjunction with conditional comments to ensure that the content is properly hidden (or shown) in Outlook 2007, 2010, 2013 and 2016. For instance, in order to hide an element in MS Outlook as well as in e-mail forwarded from MS Outlook, make sure to wrap that element with `<!--[if !mso]><!-->` and `<!--<![endif]-->` conditional formatting.

    <div class="primary callout">
      <p>If you're using a visibility class on an image, be sure to apply it to the parent element, not to the image itself.</p>
    </div>

    **To show content only on mobile clients,** add the class `.hide-for-large` to a div wrapping the element that needs to be hidden.

    **To show content only on desktop clients,** add the class `.show-for-large` to the element.

    ```html
    <!--[if !mso]><!-->
    <div class="hide-for-large">
      <callout class="primary">
        <p>This callout will only appear on small screens.</p>
      </callout>
    </div>
    <!--<![endif]-->

    <callout class="show-for-large alert">
      <p>This callout will only appear on large screens.</p>
    </callout>
    ```"""

    pass


class WRAPPER:
    """---
    title: Wrapper
    description: Wrapper creates the necessary structure to wrap elements so that full width backgrounds can be applied.
    tags:
      - full width
      - fliud
      - header
      - footer
    ---

    ## Basics

    When using [Inky](inky.html) HTML, the `<wrapper>` tag will create a `<table>`, `<tr>`, `<th>` structure needed to create consistent full width backgrounds. You can add classes to the wrapper to target CSS properties on it or target elements within it. The `.wrapper-inner` class is available to add padding to the wrapper.

    ```html
    <wrapper>
      content
    </wrapper>
    ```

    ## Full (fluid) width header or footer

    Creating a fluid header with the `<wrapper>` component is pretty straight forward. Wrapping a `<container>` will keep your content bound to the width of the container. Add a class to the `<wrapper class="">` to add a background color.

    ```html
    <style type="text/css">
    .header {
      background: #8a8a8a;
    }

    .header .columns {
      padding-bottom: 0;
    }

    .header p {
      color: #fff;
      margin-bottom: 0;
    }

    .header .wrapper-inner {
      padding: 20px; /*controls the height of the header*/
    }

    .header .container {
      background: #8a8a8a;
    }

    .wrapper.secondary {
      background: #f3f3f3;
    }
    </style>

    <wrapper class="header" bgcolor="#8a8a8a">
      <container>
        <row class="collapse">
          <columns small="6" valign="middle">
            <img src="https://placehold.it/200x50/663399">
          </columns>
          <columns small="6" valign="middle">
            <p class="text-right">BASIC</p>
          </columns>
        </row>
      </container>
    </wrapper>
    ```

    Using this structure outside of the container will yield a fluid width background that expands to the width of the email client's viewport.

    """

    pass


class ZURB_STACK:
    """---
    title: ZURB Stack
    descripiton: The ZURB email stack is a boilerplate that gives you everything you need to develop and test HTML emails.
    ---

    Email and web development can get complicated fast. We’ve introduced the ZURB Stack which helps you get started faster and lets you do more - without having to spend time finding the right tool for the job. The ZURB Stack includes:

    ## Gulp
    This is our task runner of choice for Foundation. Gulp lets us queue up tasks to execute. This lets us do cool things like inlining automagically updating your browser. It’s what the Stack is built on. [Find out more about Gulp](https://gulpjs.com/).

    ## Sass
    We use Libsass as our CSS preprocessor of choice. If you’re not familiar with Sass, it lets you use variables, nesting, and mixins (to name a few). [Learn more about Sass](https://sass-lang.com/).

    ## Inlining
    One of the biggest headaches and time-sucks used to be inlining your HTML email. Well, no more! We’re using gulp-inline to to scan your CSS file and automatically inject your CSS when you’re ready. Just run `npm run build` in your project when you’re ready to inline.

    ## Build Options
    By default the inliner works without removing whitespaces and inlining for you, you have to change your settings in the inliner function (`function inliner(css)`) on your gulpfile.babel.js which is the root of your project. To change these settings go and update this part of the function as you wish: ``` .pipe($.htmlmin, { collapseWhitespace: true, minifyCSS: true }); ```.

    ## Panini
    This is our flat file generator for Foundation. Just like it’s real-world counterpart, it takes a set of ingredients and flattens them into one delicious item. This lets you separate things like the header and footer content into partials, letting you focus on your code when you’re building. It’s built off of Handlebars, which let’s you keep things super organized with partial files and repeatable sections. Checkout our [Panini Repo](https://github.com/zurb/panini).

    ## BrowserSync
    BrowserSync is awesome. It’s the specific tool in our ZURB Stack that let’s you see your code changes in the browser in real-time. Just save your code and watch the magic happen in your browser. [Learn more about BrowserSync](https://www.browsersync.io/).

    ## Image Compression
    Finally, we’ve added gulp-imagemin which intelligently reduces the file-size of your png, jpeg, gif, and svg images. This lets your emails load at lightning speeds! [Check out the gulp-imagemin repo](https://github.com/sindresorhus/gulp-imagemin).

    ## Migrating a Project to 2.2.1
    Updating Foundation for Emails is quite easy. Navigate to your package.json file in the root of your project folder. You'll want to change the dependency from your current version (around line 16) to version `2.2.1`.

    After that you will need to update to the latest version of inky. In the same package.json file, find the section devDependcies. (around line 41). Change your current version of inky to `^1.3.6`.

    Once that is completed, you will need to update the app.scss file.  In order to be able to use Foundation for Sites and Emails together without conflicts, the Foundation for Emails CSS file’s name has changed from `foundation` to `foundation-emails`. If you are using the CSS version you can change the name from `foundation.min.css` to `foundation-emails.min.css`.

    Next, open up command line and navigate to the root of your project folder. Run `npm install`. Once completed, run `foundation build`.

    ---

    The ZURB Stack is just a starting place that lets you do all of the things mentioned above! You can totally rip out or add to the ZURB Stack’s gulp file to make your perfect email environment.
    """

    pass
