class ABIDE:
    """---
    title: Abide
    description: Abide is a form validation library that extends the HTML5 validation API with custom validators.
    sass: scss/forms/_error.scss
    js: js/foundation.abide.js
    video: '4bN0qr5pxjs'
    tags:
      - forms
      - validation
    ---

    ## Abide Demo

    These input types create a text field: `text`, `date`, `datetime`, `datetime-local`, `email`, `month`, `number`, `password`, `search`, `tel`, `time`, `url` and `week`. Note the use of the novalidate attribute to disable any browser validation that could conflict with Abide.

    <p>
      <a class="" data-open-video="0:27"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/brettsmason/pen/wdXRWP?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <form data-abide novalidate>
      <div data-abide-error class="alert callout" style="display: none;">
        <p><i class="fi-alert"></i> There are some errors in your form.</p>
      </div>
      <div class="grid-container">
        <div class="grid-x grid-margin-x">
          <div class="cell small-12">
            <label>Number Required
              <input type="text" placeholder="1234" aria-describedby="example1Hint1" aria-errormessage="example1Error1" required pattern="number">
              <span class="form-error">
                Yo, you had better fill this out, it's required.
              </span>
            </label>
          <p class="help-text" id="example1Hint1">Here's how you use this input field!</p>
          </div>
          <div class="cell small-12">
            <label>Password Required
              <input type="password" id="password" placeholder="yeti4preZ" aria-describedby="example1Hint2" aria-errormessage="example1Error2" required >
              <span class="form-error">
                I'm required!
              </span>
            </label>
            <p class="help-text" id="example1Hint2">Enter a password please.</p>
          </div>
          <div class="cell small-12">
            <label>Re-enter Password
              <input type="password" placeholder="yeti4preZ" aria-describedby="example1Hint3" aria-errormessage="example1Error3" required pattern="alpha_numeric" data-equalto="password">
              <span class="form-error">
                Hey, passwords are supposed to match!
              </span>
            </label>
            <p class="help-text" id="example1Hint3">This field is using the `data-equalto="password"` attribute, causing it to match the password field above.</p>
          </div>
        </div>
      </div>
      <div class="grid-container">
        <div class="grid-x grid-margin-x">
          <div class="cell large-6">
            <label>URL Pattern, not required, but throws error if it doesn't match the Regular Expression for a valid URL.
              <input type="text" placeholder="https://get.foundation" pattern="url">
            </label>
          </div>
          <div class="cell large-6">
            <label>Website Pattern, not required, but throws error if it doesn't match the Regular Expression for a valid URL or a Domain.
              <input type="text" placeholder="https://get.foundation or get.foundation" pattern="website">
            </label>
          </div>
        </div>
      </div>
      <div class="grid-container">
        <div class="grid-x grid-margin-x">
          <div class="cell large-6">
            <label>European Cars, Choose One, it can't be the blank option.
              <select id="select" required>
                <option value=""></option>
                <option value="volvo">Volvo</option>
                <option value="saab">Saab</option>
                <option value="mercedes">Mercedes</option>
                <option value="audi">Audi</option>
              </select>
            </label>
          </div>
          <fieldset class="cell large-6">
            <legend>Check these out</legend>
            <input id="checkbox1" type="checkbox"><label for="checkbox1">Checkbox 1</label>
            <input id="checkbox2" type="checkbox" required><label for="checkbox2">Checkbox 2</label>
            <input id="checkbox3" type="checkbox"><label for="checkbox3">Checkbox 3</label>
          </fieldset>
        </div>
      </div>
      <div class="grid-container">
        <div class="grid-x grid-margin-x">
          <fieldset class="cell large-6">
            <legend>Choose Your Favorite - not required, you can leave this one blank.</legend>
            <input type="radio" name="pockets" value="Red" id="pocketsRed"><label for="pocketsRed">Red</label>
            <input type="radio" name="pockets" value="Blue" id="pocketsBlue"><label for="pocketsBlue">Blue</label>
            <input type="radio" name="pockets" value="Yellow" id="pocketsYellow"><label for="pocketsYellow">Yellow</label>
          </fieldset>
          <fieldset class="cell large-6">
            <legend>Choose Your Favorite, and this is required, so you have to pick one.</legend>
            <input type="radio" name="pokemon" value="Red" id="pokemonRed"><label for="pokemonRed">Red</label>
            <input type="radio" name="pokemon" value="Blue" id="pokemonBlue" required><label for="pokemonBlue">Blue</label>
            <input type="radio" name="pokemon" value="Yellow" id="pokemonYellow"><label for="pokemonYellow">Yellow</label>
          </fieldset>
        </div>
      </div>
      <div class="grid-container">
        <div class="grid-x grid-margin-x">
          <fieldset class="cell large-6">
            <button class="button" type="submit" value="Submit">Submit</button>
          </fieldset>
          <fieldset class="cell large-6">
            <button class="button" type="reset" value="Reset">Reset</button>
          </fieldset>
        </div>
      </div>
    </form>
    ```
    ---

    <p>&nbsp;</p>

    <div class="alert callout">
      <p><i class="fi-alert"></i> There are some errors in your form.</p>
    </div>

    <label class="is-invalid-label">
      Required Thing
      <input type="text" class="is-invalid-input" aria-describedby="exemple2Error" data-invalid aria-invalid="true">
      <span class="form-error is-visible" id="exemple2Error">
        Yo, you had better fill this out.
      </span>
    </label>

    <label class="is-invalid-label">
      Required Thing
      <textarea type="text" class="is-invalid-input" data-invalid aria-invalid="true"></textarea>
    </label>

    ---

    ### Form Errors

    Abide automatically detects Form Errors of an input by their class (`.form-error` by default, see the `formErrorSelector` option) when they are siblings of the input or inside the same parent.

    When the Form Errors cannot be placed next to its field, like in an Input Group, the relation can be declared with `[data-form-error-for]` attribute.

    ```html
    <form data-abide novalidate>
      <div data-abide-error class="sr-only">
        There are some errors in your form.
      </div>

      <div>
        Amount
        <div class="input-group">
          <span class="input-group-label">$</span>
          <input class="input-group-field" id="example3Input" type="number" required pattern="number"/>
        </div>
        <label class="form-error" data-form-error-for="example3Input">Amount is required.</label>
      </div>

      <button class="button" type="submit" value="Submit">Submit</button>
    </form>
    ```

    You can specify validator-specific error messages using `[data-form-error-on]`
    attribute, for example:

    - `data-form-error-on="required"`
    - `data-form-error-on="pattern"`
    - `data-form-error-on="equalTo"`
    - `data-form-error-on="your_custom_validator"`

    ```html
    <form data-abide novalidate>
      <label>Email Required
        <input type="text" required pattern="email">
        <span class="form-error" data-form-error-on="required">
          Yo, you had better fill this out, it's required.
        </span>
        <span class="form-error" data-form-error-on="pattern">
          Invalid Email
        </span>
      </label>
      <button class="button" type="submit" value="Submit">Submit</button>
    </form>
    ```

    ## Initial State

    ```html
    <form data-abide>
      <!-- Add "display: none" right away -->
      <div data-abide-error class="alert callout" aria-live="assertive" style="display: none;">
        <p><i class="fi-alert"></i> There are some errors in your form.</p>
      </div>
      <label>
        Name
        <input id="example4Input" aria-describedby="example4Error" type="text" required>
        <span id="example4Error" class="form-error">This field is required.</span>
      </label>
    </form>
    ```

    ## Error State

    ```html
    <form data-abide>
      <!-- Add role="alert" -->
      <!-- Add "display: block" -->
      <div data-abide-error class="alert callout" aria-live="assertive" role="alert" style="display: block;">
        <p><i class="fi-alert"></i> There are some errors in your form.</p>
      </div>
      <!-- Add "is-invalid-label" -->
      <label class="is-invalid-label">
        Name
        <!-- Add "is-invalid-input" -->
        <!-- Add aria-invalid="true" -->
        <input id="example4Input" aria-describedby="example4Error" type="text" required
          class="is-invalid-input" aria-invalid="true">
        <!-- Add "is-visible" -->
        <span id="example4Error" class="form-error is-visible">This field is required.</span>
      </label>
    </form>
    ```

    ---

    ## Ignored Inputs

    ```html
    <form data-abide>
      <div class="grid-x grid-margin-x">
        <div class="cell small-12">
          <label>Nothing Required!
            <input type="text" placeholder="Use me, or don't" aria-describedby="example5Hint1" data-abide-ignore>
          </label>
          <p class="help-text" id="example5Hint1">This input is ignored by Abide using `data-abide-ignore`</p>
        </div>
        <div class="cell small-12">
          <label>Disabled!
            <input type="text" placeholder="Disabled input" aria-describedby="example5Hint2" disabled>
          </label>
          <p class="help-text" id="example5Hint2">This input is ignored by Abide using `disabled`</p>
        </div>
        <div class="cell small-12">
          <label>Hidden!
            <input type="hidden" placeholder="Hidden input" aria-describedby="example5Hint3" >
          </label>
          <p class="help-text" id="example5Hint3">This input is ignored by Abide using `type="hidden"`</p>
        </div>
      </div>
      <div class="grid-container">
        <div class="grid-x grid-margin-x">
          <fieldset class="cell small-12">
            <button class="button" type="submit" value="Submit">Submit</button>
          </fieldset>
          <fieldset class="cell small-12">
            <button class="button" type="reset" value="Reset">Reset</button>
          </fieldset>
        </div>
      </div>
    </form>
    ```

    ## Required Radio & Checkbox

    If you add `required` to a radio or checkbox input the whole group gets considered as required. This means at least one of the inputs must be checked.
    Checkbox inputs support the additional attribute `data-min-required` what lets you specify how many checkboxes in the group must be checked (default is one).


    ```html
    <form data-abide novalidate>
      <div class="grid-x grid-margin-x align-bottom">
        <div class="cell medium-6 large-4">
          <fieldset>
            <legend>Radio Group</legend>
            <input type="radio" name="exampleRadio" id="exampleRadioA" value="A">
            <label for="exampleRadioA">A</label>
            <input required type="radio" name="exampleRadio" id="exampleRadioB" value="B">
            <label for="exampleRadioB">B</label>
            <input type="radio" name="exampleRadio" id="exampleRadioC" value="C">
            <label for="exampleRadioC">C</label>
          </fieldset>
        </div>
        <div class="cell medium-6 large-4">
          <fieldset>
            <legend>Checkbox Group</legend>
            <input data-min-required="2" type="checkbox" name="exampleCheckbox" id="exampleCheckboxA" value="A">
            <label for="exampleCheckboxA">A</label>
            <input required type="checkbox" name="exampleCheckbox" id="exampleCheckboxB" value="B">
            <label for="exampleCheckboxB">B</label>
            <input type="checkbox" name="exampleCheckbox" id="exampleCheckboxC" value="C">
            <label for="exampleCheckboxC">C</label>
          </fieldset>
        </div>
        <div class="cell large-4">
          <button class="button" type="submit">Submit</button>
        </div>
      </div>
    </form>
    ```

    ---

    ## Event Listener
    Setup event listener after foundation is initialized (especially for formvalid/forminvalid). Easier to chain via document selector.
    * valid.zf.abide and invalid.zf.abide are field level events, triggered in validateInput function
      *   ev.target is the DOM field element,
      *   elem is jQuery selector for field element
    * formvalid.zf.abide and forminvalid.zf.abide are form events, triggered in validateForm function
      *   ev.target is the DOM form element,
      *   frm is jQuery selector for form element

    ```javascript
    $(document)
      // field element is invalid
      .on("invalid.zf.abide", function(ev,elem) {
        console.log("Field id "+ev.target.id+" is invalid");
      })
      // field element is valid
      .on("valid.zf.abide", function(ev,elem) {
        console.log("Field name "+elem.attr('name')+" is valid");
      })
      // form validation failed
      .on("forminvalid.zf.abide", function(ev,frm) {
        console.log("Form id "+ev.target.id+" is invalid");
      })
      // form validation passed, form will submit if submit event not returned false
      .on("formvalid.zf.abide", function(ev,frm) {
        console.log("Form id "+frm.attr('id')+" is valid");
        // ajax post form
      })
      // to prevent form from submitting upon successful validation
      .on("submit", function(ev) {
        ev.preventDefault();
        console.log("Submit for form id "+ev.target.id+" intercepted");
      });
    // You can bind field or form event selectively
    $("#foo").on("invalid.zf.abide", function(ev,el) {
      alert("Input field foo is invalid");
    });
    $("#bar").on("formvalid.zf.abide", function(ev,frm) {
      alert("Form is valid, finally!");
      // do something perhaps
    });
      ```

    ## Builtin Patterns and Validators

    The following patterns and validators are already built in:

    `alpha`,
    `alpha_numeric`,
    `card`,
    `color`
    `cvv`,
    `date`,
    `dateISO`,
    `datetime`,
    `day_month_year`,
    `domain`,
    `email`,
    `integer`,
    `month_day_year`,
    `number`,
    `time`,
    `url`

    Apart from these standard patterns, we have a `website` pattern too which is basically a combo of both `domain` and `url` pattern and we recommend you to use this `website` pattern for validating websites.

    They are defined by regular expressions as you can see below. Note, that the patterns that relate to text such as `alpha` and `alpha_numeric` do not consider special characters from other languages. You need to add these special characters yourself to the regular expressions. For instance, for the German language you need to add:

    ```JS
    alpha : /^[a-zäöüßA-ZÄÖÜ]+$/,
    alpha_numeric : /^[a-zäöüßA-ZÄÖÜ0-9]+$/,
    ```

    Then you need to customize the builtin patterns as explained in the next section. Otherwise Abide will produce an error if a special character is input in your text field which is validated with `pattern="alpha"` or  `pattern="alpha_numeric"`.

    Here are the definitions of the builtin patterns:

    ```JS
    alpha : /^[a-zA-Z]+$/,
    alpha_numeric : /^[a-zA-Z0-9]+$/,
    integer : /^[-+]?\d+$/,
    number : /^[-+]?\d*(?:[\.\,]\d+)?$/,

    // amex, visa, diners
    card : /^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$/,
    cvv : /^([0-9]){3,4}$/,

    // https://www.whatwg.org/specs/web-apps/current-work/multipage/states-of-the-type-attribute.html#valid-e-mail-address
    email : /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$/,

    // From CommonRegexJS (@talyssonoc)
    // https://github.com/talyssonoc/CommonRegexJS/blob/e2901b9f57222bc14069dc8f0598d5f412555411/lib/commonregex.js#L76
    // For more restrictive URL Regexs, see https://mathiasbynens.be/demo/url-regex.
    url: /^((?:(https?|ftps?|file|ssh|sftp):\/\/|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}\/)(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))*\))+(?:\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))$/,

    // abc.de
    domain : /^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,8}$/,

    datetime : /^([0-2][0-9]{3})\-([0-1][0-9])\-([0-3][0-9])T([0-5][0-9])\:([0-5][0-9])\:([0-5][0-9])(Z|([\-\+]([0-1][0-9])\:00))$/,
    // YYYY-MM-DD
    date : /(?:19|20)[0-9]{2}-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-9])|(?:(?!02)(?:0[1-9]|1[0-2])-(?:30))|(?:(?:0[13578]|1[02])-31))$/,
    // HH:MM:SS
    time : /^(0[0-9]|1[0-9]|2[0-3])(:[0-5][0-9]){2}$/,
    dateISO : /^\d{4}[\/\-]\d{1,2}[\/\-]\d{1,2}$/,
    // MM/DD/YYYY
    month_day_year : /^(0[1-9]|1[012])[- \/.](0[1-9]|[12][0-9]|3[01])[- \/.]\d{4}$/,
    // DD/MM/YYYY
    day_month_year : /^(0[1-9]|[12][0-9]|3[01])[- \/.](0[1-9]|1[012])[- \/.]\d{4}$/,

    // #FFF or #FFFFFF
    color : /^#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$/,

    // Domain || URL
    website: {
      test: (text) => {
        return Abide.defaults.patterns['domain'].test(text) || Abide.defaults.patterns['url'].test(text);
      }
    }
    ```


    ## Adding Custom Pattern and Validator
    * Override builtin patterns and validators before foundation is initialized
    * Add new patterns and validators before or after foundation is initialized

    ```javascript
    function myCustomValidator(
      $el,      /* jQuery element to validate */
      required, /* is the element required according to the `[required]` attribute */
      parent    /* parent of the jQuery element `$el` */
    ) {
      if (!required) return true;
      var from = $('#'+$el.attr('data-greater-than')).val(),
          to = $el.val();
      return (parseInt(to) > parseInt(from));
    };

    // Set default options
    Foundation.Abide.defaults.patterns['dashes_only'] = /^[0-9-]*$/;
    Foundation.Abide.defaults.validators['greater_than'] = myCustomValidator;

    // Initialize Foundation
    $(document).foundation();
    ```
    ```html
    <input id="phone" type="text" pattern="dashes_only" required >
    <input id="min" type="number" required >
    <input id="max" type="number" data-validator="greater_than" data-greater-than="min" required>
    ```

    ## jQuery Conflict

    When creating a type `submit` button, make sure to _avoid_ using `name="submit"` otherwise your form won't submit. This is due to [jQuery limitations](https://api.jquery.com/submit/) (see Additional Notes).

    ## Accessibility

    By default, Abide will add some accessibility attributes to your form elements. It is highly recommended to keep this option active as it improve the usability of your forms for disabled people. [Lean more about Accessibility in Foundation](accessibility.html).

    However, if you think the attributes added by Abide are not correct, you can disable it by setting `a11yAttributes` (or `[data-a11y-attributes]`) to `false`.
    """

    pass


class ACCESSIBILITY:
    """---
    title: Accessibility
    description: Foundation for Sites is a fully-accessible framework. Here are some general guidelines to keep in mind as you make your pages accessible.
    ---

    In addition to the accessibility features built into Foundation's components, be sure to follow best practices for making your site more accessible.

    <div class="primary callout">
      <p>Care about accessibility or want to contribute? Submit a Pull Request or get into the [conversation on GitHub](https://github.com/foundation/foundation-sites/labels/accessibility).</p>
    </div>

    ## Basic Principles

    - **Structure your document properly.** Use the right HTML tags for the job when marking up navigation, lists, links, controls, and so on.
    - **Label everything.** If a control or form element has no text label, add one. You can use the [visibility classes](visibility.html#accessibility) to hide labels visually while maintaining accessibility. Use the `alt` attribute on all images to describe what they are.
    - **Don't rely on purely visual cues.** The content of a page should make sense even if page is being read to the user, or if the user is colorblind and can't make use of color-based labeling.
    - **Make everything usable on a keyboard and mouse.** Lucky for you, all of our components work with keyboards, mice, and touch screens out of the box.

    ---

    ## Types of Disabilities

    ### Visual

    Visually-impaired users may have low vision or be completely blind. For low vision users, proper typographic contrast is important, both size and color. Foreground colors should stand out from background colors. You can use tools to calculate the contrast ratio of your foreground and background colors. The contrast ratio should at least be 1:4.5 for normal text and 3:1 for large text.
    Blind users consume the web by reading it using a [screen reader](https://en.wikipedia.org/wiki/Screen_reader). Screen readers read the content of a web page out loud, or write it out as Braille, using certain cues from the HTML to infer meaning.

    ### Motor

    Users with motor disabilities may have trouble using a mouse, or don't use a mouse at all. For this reason, it's very important that your site is fully keyboard-accessible. Visually-impaired users also typically navigate websites using only their keyboard.

    When using only the keyboard, the <kbd>tab</kbd> key is the primary way to navigate through a page. However, most screen readers include many shortcut keys to skip around a page. For example, a screen reader can read every heading on a page, or every link, making it easier to find the right content on the page.

    More complex components like menus, tabs, or sliders can also typically be used with arrow keys, not just the <kbd>tab</kbd> keys. All of our JavaScript plugins provide advanced keyboard support by default.

    ### Auditory

    If your site has video, provide captions so that users who are deaf or hard-of-hearing can properly view the content.

    ---

    ## Foundation and Accessibility

    All of Foundation's components are keyboard-accessible and screen reader-friendly. All of our code examples include the required accessibility hooks, but there may be instances where you, as the developer, need to fine-tune the specifics of how those hooks are used. Our JavaScript plugins will automatically add many required attributes to the HTML for you. Refer to each component's documentation to learn how to ensure your markup is screen reader-friendly.

    Foundation's CSS makes use of the library [what-input](https://github.com/ten1seven/what-input), which can detect the user's current input device and adjust CSS accordingly. We use it to disable outlines for mouse users, but not keyboard users, who need the outline to know what element on the page has focus.

    If you're using the Sass version of Foundation, you can use this mixin to enable the feature on your own components:

    ```scss
    .element {
      @include disable-mouse-outline;
      // ...
    }
    ```

    ---

    ## Learn More

    ### Resources

    - [WCAG 2.0 Guide](https://www.w3.org/TR/UNDERSTANDING-WCAG20/)
    - [MDN accessibility documentation](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
    - [w3.org Introduction to Accessibility](https://www.w3.org/WAI/intro/accessibility.php)
    - [Section 508 government requirements](https://www.section508.gov/)
    - [WebAIM certification and training](https://webaim.org/)
    - [Web Accessibility Checklist](https://a11yproject.com/checklist.html)

    ### Tools

    - [Tenon accessibility checker](https://tenon.io/index.php)
    - [WAVE Chrome plugin - free accessibility checker](https://wave.webaim.org)
    - [Color Contrast Checker](https://webaim.org/resources/contrastchecker)
    - [ChromeVox screen reader plugin for Chrome](https://www.chromevox.com)
    - [JAWS screen reader for Windows](https://www.freedomscientific.com/Products/Blindness/Jaws)
    - [NVDA screen reader for Windows - Free](https://www.nvaccess.org/download/)"""

    pass


class ACCORDION_MENU:
    """---
    title: Accordion Menu
    sass: scss/components/_accordion-menu.scss
    js: js/foundation.accordionMenu.js
    description: Change a basic vertical Menu into a expandable accordion menu with the Accordion Menu plugin.
    video: FXZIZ9N4aeI
    ---

    ## Basics

    Accordion menus follow the basic [Menu](menu.html) syntax of `<ul>`, `<li>`, and `<a>`. To convert a basic menu into an accordion, add the attribute `data-accordion-menu`. You probably also want it to be vertical, so add the class `.vertical` as well.

    Any `<a>` will behave like a standard link. However, any `<a>` paired with a nested `<ul>` menu will then slide that sub-menu up and down when clicked on.

    <a class="" data-open-video="1:03"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>

    <div class="primary callout">
      <p>You can use the built-in <code>.nested</code> class to add an indent to a nested menu.</p>
    </div>

    <div class="primary callout">
      <p>To have a sub-menu already open when the page loads, add the class <code>.is-active</code> to that sub-menu.</p>
    </div>


    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/qmKEQr?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="vertical menu accordion-menu" data-accordion-menu>
      <li>
        <a href="#">Item 1</a>
        <ul class="menu vertical nested">
          <li><a href="#">Item 1A</a></li>
          <li><a href="#">Item 1B</a></li>
        </ul>
      </li>
      <li><a href="#">Item 2</a></li>
    </ul>
    ```

    <ul class="vertical menu accordion-menu" data-accordion-menu style="max-width: 250px">
      <li>
        <a href="#">Item 1</a>
        <ul class="menu vertical nested">
          <li>
            <a href="#">Item 1A</a>
            <ul class="menu vertical nested">
              <li><a href="#">Item 1Ai</a></li>
              <li><a href="#">Item 1Aii</a></li>
              <li><a href="#">Item 1Aiii</a></li>
            </ul>
          </li>
          <li><a href="#">Item 1B</a></li>
          <li><a href="#">Item 1C</a></li>
        </ul>
      </li>
      <li>
        <a href="#">Item 2</a>
        <ul class="menu vertical nested">
          <li><a href="#">Item 2A</a></li>
          <li><a href="#">Item 2B</a></li>
        </ul>
      </li>
      <li><a href="#">Item 3</a></li>
    </ul>

    <br>

    ## Submenu Toggle

    Accordion menus can have a separate submenu toggle. This allows the parent item to have its own link, but still allows the submenu to be opened/closed.
    You need to add the class `accordion-menu` as well as the data attribute `data-submenu-toggle="true"` for this to work correctly.

    ```html
    <ul class="vertical menu accordion-menu" data-accordion-menu data-submenu-toggle="true">
      <li>
        <a href="https://get.foundation/" target="_blank">Link here, dropdown there →</a>
        <ul class="menu vertical nested">
          <li>
            <a href="#">Item 1A</a>
            <ul class="menu vertical nested">
              <li><a href="#">Item 1Ai</a></li>
              <li><a href="#">Item 1Aii</a></li>
              <li><a href="#">Item 1Aiii</a></li>
            </ul>
          </li>
          <li><a href="#">Item 1B</a></li>
          <li><a href="#">Item 1C</a></li>
        </ul>
      </li>
      <li>
        <a href="#">Item 2</a>
        <ul class="menu vertical nested">
          <li><a href="#">Item 2A</a></li>
          <li><a href="#">Item 2B</a></li>
        </ul>
      </li>
      <li><a href="#">Item 3</a></li>
    </ul>
    ```

    <ul class="vertical menu accordion-menu" data-accordion-menu data-submenu-toggle="true" style="max-width: 300px">
      <li>
        <a href="https://get.foundation/" target="_blank">Link here, dropdown there →</a>
        <ul class="menu vertical nested">
          <li>
            <a href="#">Item 1A</a>
            <ul class="menu vertical nested">
              <li><a href="#">Item 1Ai</a></li>
              <li><a href="#">Item 1Aii</a></li>
              <li><a href="#">Item 1Aiii</a></li>
            </ul>
          </li>
          <li><a href="#">Item 1B</a></li>
          <li><a href="#">Item 1C</a></li>
        </ul>
      </li>
      <li>
        <a href="https://get.foundation/" target="_blank">Link here, dropdown there →</a>
        <ul class="menu vertical nested">
          <li><a href="#">Item 2A</a></li>
          <li><a href="#">Item 2B</a></li>
        </ul>
      </li>
      <li><a href="#">Item 3</a></li>
    </ul>"""

    pass


class ACCORDION:
    """---
    title: Accordion
    description: Accordions are elements that help you organize and navigate multiple documents in a single container. They can be used for switching between items in the container.
    sass: scss/components/_accordion.scss
    js: js/foundation.accordion.js
    video: 'y_BX7saf65Q'
    ---

    ## Basics

    The container for an accordion needs the class `.accordion`, and the attribute `data-accordion`. Note that in these examples, we use a `<ul>`, but you can use any element you want.

    ```html
    <ul class="accordion" data-accordion></ul>
    ```

    Inside the accordion, place a series of panes with the class `.accordion-item` and the attribute `data-accordion-item`. To mark which pane should be open by default, add the class `.is-active` to that pane.

    Each pane has a **title**, an `<a>` with the class `.accordion-title`, and a **content area**, an element with the class `.accordion-content` and the attribute `data-tab-content`.

    <p>
      <a class="" data-open-video="1:25"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/WjzKqa?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="accordion" data-accordion>
      <li class="accordion-item is-active" data-accordion-item>
        <!-- Accordion tab title -->
        <a href="#" class="accordion-title">Accordion 1</a>

        <!-- Accordion tab content: it would start in the open state due to using the `is-active` state class. -->
        <div class="accordion-content" data-tab-content>
          <p>Panel 1. Lorem ipsum dolor</p>
          <a href="#">Nowhere to Go</a>
        </div>
      </li>
      <!-- ... -->
    </ul>
    ```

    Once you put it all together, here's what you get!

    <ul class="accordion" data-accordion>
      <li class="accordion-item is-active" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 1</a>
        <div class="accordion-content" data-tab-content >
          <p>Panel 1. Lorem ipsum dolor</p>
          <a href="#">Nowhere to Go</a>
        </div>
      </li>
      <li class="accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 2</a>
        <div class="accordion-content" data-tab-content>
          <textarea></textarea>
          <button class="button">I do nothing!</button>
        </div>
      </li>
      <li class="accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 3</a>
        <div class="accordion-content" data-tab-content>
          Type your name!
          <input type="text"></input>
        </div>
      </li>
    </ul>

    ---

    ## Advanced Options

    ### Multi-expand

    By default, only one pane of an accordion can be open at a time. This can be changed by setting the `multiExpand` option to `true`.

    <p>
      <a class="" data-open-video="5:11"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/ybEErg?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>


    ```html
    <ul class="accordion" data-accordion data-multi-expand="true">
      <!-- ... -->
    </ul>
    ```

    <ul class="accordion" data-accordion data-multi-expand="true">
      <li class="accordion-item is-active" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 1</a>
        <div class="accordion-content" data-tab-content >
          Panel 1. Lorem ipsum dolor
        </div>
      </li>
      <li class="accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 2</a>
        <div class="accordion-content" data-tab-content>
          Panel 2. Lorem ipsum dolor
        </div>
      </li>
      <li class="accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 3</a>
        <div class="accordion-content" data-tab-content>
          Panel 3. Lorem ipsum dolor
        </div>
      </li>
    </ul>

    ---

    ### All Closed

    By default, at least one pane in an accordion must be open. This can be changed by setting `allowAllClosed` option to `true`.

    <p>
      <a class="" data-open-video="6:09"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/zwaaVp?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="accordion" data-accordion data-allow-all-closed="true">
      <!-- ... -->
    </ul>
    ```

    <ul class="accordion" data-accordion data-allow-all-closed="true">
      <li class="accordion-item is-active" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 1</a>
        <div class="accordion-content" data-tab-content >
          Panel 1. Lorem ipsum dolor
        </div>
      </li>
      <li class="accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 2</a>
        <div class="accordion-content" data-tab-content>
          Panel 2. Lorem ipsum dolor
        </div>
      </li>
      <li class="accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 3</a>
        <div class="accordion-content" data-tab-content>
          Panel 3. Lorem ipsum dolor
        </div>
      </li>
    </ul>

    ---

    ### Disabled

    There may be times where you want to disable pane switching on an accordion. This can be accomplished by setting the `disabled` option.

    <div class="warning callout">
      <p>The `disabled` option disables all up, down, and toggle methods of an accordion.  If you wish to manipulate a disabled accordion with <a href='#javascript-reference'>JavaScript</a>, you will need to remove the `disabled` option from the accordion.</p>
    </div>

    ```html
    <ul class="accordion" data-accordion disabled>
      <li class="accordion-item is-active" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 1</a>
        <div class="accordion-content" data-tab-content>
          Panel 1. I'm open because I'm loaded that way, but you can't close me
        </div>
      </li>
      <li class="accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 2, you can't open me.</a>
        <div class="accordion-content" data-tab-content>
          Panel 2. Lorem ipsum dolor
        </div>
      </li>
      <li class="accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 3, you can't open me.</a>
        <div class="accordion-content" data-tab-content>
          Panel 3. Lorem ipsum dolor
        </div>
      </li>
    </ul>
    ```
    ---

    ## Accordion and URLs

    ### Browser history

    When the `data-deep-link` option is set to `true`, the current state of the accordion is recorded by adding a hash with the accordion panel ID to the browser URL when a accordion opens. By default, accordion *replace* the browser history (using `history.replaceState()`). Modify this behavior by using attribute `data-update-history="true"` to *append* to the browser history (using `history.pushState()`). In the latter case the browser back button will track each click that opens a accordion panel.

    By using deep linking (see below), the open state of a page's tabset may be shared by copy-pasting the browser URL.

    ### Deep linking

    Add the attribute `data-deep-link="true"` to a accordion to:
    - modify the browser history when a accordion panel is clicked
    - allow users to open a particular accordion panel at page load with a hash-appended URL

    ```html
    <ul class="accordion" data-accordion data-deep-link="true" data-update-history="true" data-deep-link-smudge="true" data-deep-link-smudge-delay="500" id="deeplinked-accordion">
      <li class="accordion-item is-active" data-accordion-item>
        <a href="#deeplink1" class="accordion-title">Accordion 1</a>
        <div class="accordion-content" data-tab-content id="deeplink1">
          Panel 1. Lorem ipsum dolor
        </div>
      </li>
      <li class="accordion-item" data-accordion-item>
        <a href="#deeplink2" class="accordion-title">Accordion 2</a>
        <div class="accordion-content" data-tab-content id="deeplink2">
          Panel 2. Lorem ipsum dolor
        </div>
      </li>
      <li class="accordion-item" data-accordion-item>
        <a href="#deeplink3" class="accordion-title">Accordion 3</a>
        <div class="accordion-content" data-tab-content id="deeplink3">
          Panel 3. Lorem ipsum dolor
        </div>
      </li>
    </ul>
    ```
    For example, <a target="_blank" href="#deeplink3">https://example.com/#deeplink3</a> will open the third accordion panel at page load. This example will open a new browser tab and scroll you to the open accordion panel.

    When linking directly to a accordion panel, it might not be obvious that the content appears within a accordion panel. An additional attribute `data-deep-link-smudge` rolls the page up slightly after deep linking (to a horizontal accordion) so that the accordion is at the top of the viewport.

    ```html
    <ul class="accordion" data-deep-link="true" data-deep-link-smudge="true" data-deep-link-smudge-delay="600" data-accordion id="deeplinked-accordion-with-smudge">
    ```"""

    pass


class BADGE:
    """---
    title: Badge
    description: The badge is a basic component that displays a number. It's useful for calling out a number of unread items.
    sass: scss/components/_badge.scss
    video: '_S_OO9NiWQ8'
    ---

    ## Basics

    Add the `.badge` class to an element to create a badge. In the below example, we're using `<span>`, but any tag will work fine.

    <p>
      <a class="" data-open-video="1:28"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/vmrPOM?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <span class="badge">1</span>
    ```

    <br>

    A badge will typically be describing another element on the page. To bind the two elements together, give the badge a unique ID, and reference that ID in an `aria-describedby` attribute on the main element.

    ```html
    <h1 aria-describedby="messageCount">Unread Messages</h1>
    <span class="badge" id="messageCount">1</span>
    ```

    Finally, the content itself might need more context for users that use screen readers. You can add extra text inside the badge using the `.show-for-sr` class.

    ```html
    <span class="badge" id="messageCount">1 <span class="show-for-sr">unread message</span></span>
    ```

    ---

    ## Coloring

    Add color classes to give badges additional meaning.

    <p>
      <a class="" data-open-video="2:05"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/MmXxWm?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <span class="badge primary">1</span>
    <span class="badge secondary">2</span>
    <span class="badge success">3</span>
    <span class="badge alert">A</span>
    <span class="badge warning">B</span>
    ```

    ---

    ### Custom Colors

    If you're using the Sass version of Foundation, you can customize the badge classes by editing the `$badge-palette` map in your settings file. The badge palette defaults to `$foundation-palette`.

    If you don't need certain colors from the default palette, simply remove them from the list.

    ```scss
    $badge-palette: map-remove($foundation-palette, (
        primary,
        secondary
    )) !default;
    ```

    Or you can add more colors to the default palette.

    ```scss
    $badge-palette: map-merge($foundation-palette, (
        purple: #bb00ff
    )) !default;
    ```

    Or you can define your own custom badge palette.

    ```scss
    $badge-palette: (
        black: #000000,
        red: #ff0000,
        purple: #bb00ff
    ) !default;
    ```

    ---

    ### Text Colors

    The text color for each badge class is determined by either `$badge-color` or `$badge-color-alt`, whichever settings variable has more contrast.

    <div class="primary callout">
      <p>The default settings meet WCAG 2.0 level AA contrast requirements. Be sure to [check the contrast](https://webaim.org/resources/contrastchecker/) when changing color variables. To give all badges the same color text, set `$badge-color` and `$badge-color-alt` to the same value &mdash; but know that doing so may decrease accessibility.</p>
    </div>

    ---

    ## Icons

    An icon can be used in place of text. We're using the Foundation icon font here, but any icon fonts or image-based icons will work fine.

    <p>
      <a class="" data-open-video="0:39"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/jmKJXa?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <span class="badge secondary"><i class="fi-share"></i></span>
    <span class="badge success"><i class="fi-check"></i></span>
    <span class="badge warning"><i class="fi-wrench"></i></span>
    ```"""

    pass


class BREADCRUMBS:
    """---
    title: Breadcrumbs
    description: Breadcrumbs come in handy to show a navigation trail for users clicking through your site.
    video: 'vQz-Kv5f_Ts'
    sass: scss/components/_breadcrumbs.scss
    ---

    To make a set of breadcrumb links, just add the class `.breadcrumbs` to a `<ul>`, and then add links inside of the `<li>` elements. The current page doesn't require a link or a class, but you should add some explanatory text for AT that indicates which item is the current page.

    To mark a disabled item, add the class `.disabled` to the `<li>`, and just use plain text instead of a link.

    <a class="" data-open-video="2:05"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>

    <div class="warning callout">
      <p>We use a CSS <code>::after</code> element containing a slash character to create the separator between items. Some screen readers will read this character out loud&mdash;if this is an issue, you can use a background image or a separate element with <code>aria-hidden="true"</code> to create the separator instead.</p>
    </div>


    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/MmGeMx?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    <div class="warning callout">
      <p>If your site is visited by search engines, then you should consider adding Schema.org structure data. This will allow your site to appear more attractive in search results. </p>
      <p>For more information, see <a href="https://developers.google.com/search/docs/data-types/breadcrumbs">Breadcrumbs - Google Developers</a>, <a href="https://schema.org/BreadcrumbList">BreadcrumbList - schema.org</a>.</p>
    </div>

    ```html
    <nav aria-label="You are here:" role="navigation">
      <ul class="breadcrumbs">
        <li><a href="#">Home</a></li>
        <li><a href="#">Features</a></li>
        <li class="disabled">Gene Splicing</li>
        <li>
          <span class="show-for-sr">Current: </span> Cloning
        </li>
      </ul>
    </nav>
    ```"""

    pass


class BUTTON_GROUP:
    """---
    title: Button Group
    description: Button groups are containers for related action items. They're great when you need to display a group of actions in a bar. These build off the button styles and work perfectly with the grid.
    video: PRjMAuvwX44
    sass: scss/components/_button-group.scss
    tags:
      - split button
    flexbox: true
    ---

    ## Basics

    Add the `.button-group` class to a container, and inside it place any number of buttons. The buttons are separated by a small border.

    <p>
      <a class="" data-open-video="0:40"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/JNvXam?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="button-group">
      <a class="button">One</a>
      <a class="button">Two</a>
      <a class="button">Three</a>
    </div>
    ```

    ---

    ## Sizing

    Button groups can be sized with the same classes as standard buttons: `.tiny`, `.small`, and `.large`.

    <p>
      <a class="" data-open-video="0:40"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/dWeMwL?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="small button-group">
      <a class="button">Small</a>
      <a class="button">Button</a>
      <a class="button">Group</a>
    </div>
    ```

    ---

    ## Coloring

    Buttons within a button group can be colored individually with the `.secondary`, `.success`, `.warning`, and `.alert` classes.

    <p>
      <a class="" data-open-video="0:40"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/KmRzEq?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="button-group">
      <a class="secondary button">View</a>
      <a class="success button">Edit</a>
      <a class="warning button">Share</a>
      <a class="alert button">Delete</a>
    </div>
    ```

    The entire group can also be colored using the same classes.

    ```html
    <div class="primary button-group">
      <a class="button">Harder</a>
      <a class="button">Better</a>
      <a class="button">Faster</a>
      <a class="button">Stronger</a>
    </div>
    ```

    ---

    ## Hollow and clear

    Buttons within a button group can be given hollow and clear styles individually by adding a class `.hollow` or `.clear` respectively.

    ```html
    <div class="button-group">
      <a class="secondary button hollow">View</a>
      <a class="success button hollow">Edit</a>
      <a class="warning button hollow">Share</a>
      <a class="alert button hollow">Delete</a>
    </div>

    <div class="button-group">
      <a class="secondary button clear">View</a>
      <a class="success button clear">Edit</a>
      <a class="warning button clear">Share</a>
      <a class="alert button clear">Delete</a>
    </div>
    ```

    The entire group can also be given hollow or clear styles using the same class.

    ```html
    <div class="button-group hollow">
      <a class="secondary button">View</a>
      <a class="success button">Edit</a>
      <a class="warning button">Share</a>
      <a class="alert button">Delete</a>
    </div>

    <div class="button-group clear">
      <a class="secondary button">View</a>
      <a class="success button">Edit</a>
      <a class="warning button">Share</a>
      <a class="alert button">Delete</a>
    </div>
    ```

    ---

    ## No Gaps

    When using a single color for the button-group, you might want to remove the `1px` spacing between the buttons. You can use `no-gaps` to just the same.

    ```html
    <div class="primary button-group no-gaps">
      <a class="button">Harder</a>
      <a class="button">Better</a>
      <a class="button">Faster</a>
      <a class="button">Stronger</a>
    </div>
    ```

    You can use `no-gaps` on `hollow` styles.

    ```html
    <div class="primary button-group hollow no-gaps">
      <a class="button">Harder</a>
      <a class="button">Better</a>
      <a class="button">Faster</a>
      <a class="button">Stronger</a>
    </div>
    ```

    You can use `no-gaps` with all grouped/individual styles.

    ```html
    <div class="button-group no-gaps">
      <a class="secondary button">View</a>
      <a class="success button">Share</a>
      <a class="warning button hollow">Edit</a>
      <a class="alert button clear">Delete</a>
    </div>
    ```

    ---

    ## Even-width Group

    Add the `.expanded` class to the container to make a full-width button group. Each item will automatically size itself based on how many buttons there are, up to a maximum of six.

    <p>
      <a class="" data-open-video="2:49"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/bWMpXB?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="expanded button-group">
      <a class="button">Expanded</a>
      <a class="button">Button</a>
      <a class="button">Group</a>
    </div>
    ```

    ---

    ## Stacking

    A button group can be made vertical with the `.stacked` class. You can also use `.stacked-for-small` to only stack a button group on small screens, or `.stacked-for-medium` to only stack on small and medium screens.

    <p>
      <a class="" data-open-video="5:14"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/bWMemL?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="stacked-for-small button-group">
      <a class="button">How</a>
      <a class="button">Low</a>
      <a class="button">Can</a>
      <a class="button">You</a>
      <a class="button">Go</a>
    </div>
    ```

    ---

    ## Split Buttons

    To build a split button, just create a button group with two buttons.


    To create a button with only an arrow, add the class `.arrow-only`. Note that the button still needs a label for screen readers, which can be embedded inside the button with a `.show-for-sr` element. In the example below, an assistive device will read the arrow button as "Show menu".

    <p>
      <a class="" data-open-video="7:32"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/GmdjKM?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="button-group">
      <a class="button">Primary Action</a>
      <a class="dropdown button arrow-only">
        <span class="show-for-sr">Show menu</span>
      </a>
    </div>
    ```

    ---

    ## Flexbox Button Group

    The buttons in a button group can be positioned using the [Flexbox Utility](/sites/docs/flexbox-utilities.html#vanilla-flexbox-helper-classes) classes in Foundation. You can use `.align-center`, `.align-right`, `.align-spaced`, or `.align-justify`.

    ```html
    <div class="button-group align-center">
      <a class="button">One</a>
      <a class="button">Two</a>
      <a class="button">Three</a>
    </div>

    <div class="button-group align-right">
      <a class="button">One</a>
      <a class="button">Two</a>
      <a class="button">Three</a>
    </div>

    <div class="button-group align-spaced">
      <a class="button">One</a>
      <a class="button">Two</a>
      <a class="button">Three</a>
    </div>

    <div class="button-group align-justify">
      <a class="button">One</a>
      <a class="button">Two</a>
      <a class="button">Three</a>
    </div>
    ```

    <article class="docs-component" id="docs-flexbox-buttongroup">
    <div class="button-group align-center">
      <a class="button">One</a>
      <a class="button">Two</a>
      <a class="button">Three</a>
    </div>

    <div class="button-group align-right">
      <a class="button">One</a>
      <a class="button">Two</a>
      <a class="button">Three</a>
    </div>

    <div class="button-group align-spaced">
      <a class="button">One</a>
      <a class="button">Two</a>
      <a class="button">Three</a>
    </div>

    <div class="button-group align-justify">
      <a class="button">One</a>
      <a class="button">Two</a>
      <a class="button">Three</a>
    </div>
    </article>"""

    pass


class BUTTON:
    """---
    title: Button
    description: Buttons are convenient tools when you need more traditional actions. To that end, Foundation has many easy to use button styles that you can customize or override to fit your needs.
    video: iEAtuFk4-LQ
    sass: scss/components/_button.scss
    tags:
      - dropdown button
    ---

    ## Basics

    A basic button can be created with minimal markup. Because buttons can be used for many purposes, it's important to use the right tag.

    - Use the `<a>` tag if the button is a link to another page, or a link to an anchor within a page. Generally anchors don't require JavaScript to work.
    - Use the `<button>` tag if the button performs an action that changes something on the current page. `<button>` elements almost always require JavaScript to function.

    <a class="" data-open-video="0:34"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    <div class="primary callout">
      <p>Add the attribute <code>type="button"</code> to <code>&lt;button&gt;</code> elements, unless the button submits a form, in which case you should add the class `.submit` and remove <code>type="button"</code></p>
    </div>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/wdmZME?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <!-- Anchors (links) -->
    <a href="about.html" class="button">Learn More</a>
    <a href="#features" class="button">View All Features</a>

    <!-- Buttons (actions) -->
    <button class="submit success button">Save</button>
    <button type="button" class="alert button">Delete</button>
    ```

    ---

    ## Sizing

    Additional classes can be added to your button to change its size and shape.

    <p>
      <a class="" data-open-video="3:23"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/JNLVRb?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <a class="button tiny" href="#">So Tiny</a>
    <a class="button small" href="#">So Small</a>
    <a class="button" href="#">So Basic</a>
    <a class="button large" href="#">So Large</a>
    <a class="button expanded" href="#">Such Expand</a>
    <a class="button small expanded" href="#">Wow, Small Expand</a>
    ```

    ### Responsive Expanded buttons

    If you are using the Sass version, you can activate these additional responsive button expand classes by changing the `$button-responsive-expanded` variable to true. (It is false by default to reduce CSS file size.)

    For CSS download users, you can [get the CSS here](https://gist.github.com/rafibomb/2497ca75ceedfa3f5ccf3ba146eae295) and add it to your stylesheet.

    ```html
    <a class="button small small-only-expanded" href="#">Wow, Expand only on small viewport</a>
    <a class="button small medium-only-expanded" href="#">Expand only on medium viewport</a>
    <a class="button small large-only-expanded" href="#">Expand only on large viewport</a>

    <a class="button small medium-expanded" href="#">Wow, Expand on medium and larger</a>
    <a class="button small large-expanded" href="#">Expand on large and larger</a>

    <a class="button small medium-down-expanded" href="#">Expand on medium and smaller</a>
    <a class="button small large-down-expanded" href="#">Expand on large and smaller</a>
    ```

    ---

    ## Coloring

    Add color classes to give buttons additional meaning.

    <p>
      <a class="" data-open-video="5:41"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>


    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/ZKjxOy?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <a class="button primary" href="#">Primary</a>
    <a class="button secondary" href="#">Secondary</a>
    <a class="button success" href="#">Success</a>
    <a class="button alert" href="#">Alert</a>
    <a class="button warning" href="#">Warning</a>
    ```

    ---

    ### Custom Colors

    If you're using the Sass version of Foundation, you can customize the button classes by editing the `$button-palette` map in your settings file. The button palette defaults to `$foundation-palette`.

    If you don't need certain colors from the default palette, simply remove them from the list.

    ```scss
    $button-palette: map-remove($foundation-palette, (
        primary,
        secondary
    ));
    ```

    Or you can add more colors to the default palette.

    ```scss
    $button-palette: map-merge($foundation-palette, (
        purple: #bb00ff
    ));
    ```

    Or you can define your own custom button palette.

    ```scss
    $button-palette: (
        black: #000000,
        red: #ff0000,
        purple: #bb00ff
    );
    ```

    ---

    ### Text Colors

    The text color for each button class is determined by either `$button-color` or `$button-color-alt`, whichever settings variable has more contrast.

    <div class="primary callout">
      <p>The default settings meet WCAG 2.0 level AA contrast requirements. Be sure to [check the contrast](https://webaim.org/resources/contrastchecker/) when changing color variables. To give all buttons the same color text, set `$button-color` and `$button-color-alt` to the same value &mdash; but know that doing so may decrease accessibility.</p>
    </div>

    ---

    ## Hollow Style

    Add the `.hollow` class to a button to give it a hollow style. Change the `$button-fill` variable in your settings file to `hollow` to make this the default style. Changing this setting will remove the `.hollow` class from your CSS.

    ```html
    <button class="hollow button" href="#">Primary</button>
    <button class="hollow button secondary" href="#">Secondary</button>
    <button class="hollow button success" href="#">Success</button>
    <button class="hollow button alert" href="#">Alert</button>
    <button class="hollow button warning" href="#">Warning</button>
    <button class="hollow button" href="#" disabled>Disabled</button>
    ```

    ---

    ## Disabled Buttons

    The `.disabled` class will give buttons a faded appearance. The class is a purely visual style, and won't actually disable a control. For `<button>` elements, you can add the `disabled` attribute to both disable and style it. If you want to disable a link, you should add the `aria-disabled` attribute to mark it as disabled for assistive technology.

    <p>
      <a class="" data-open-video="8:32"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-video-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/xdjVOp?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <a class="button disabled" href="#" aria-disabled>Disabled</a>
    <button type="button" class="button primary" disabled>Disabled</button>
    <button type="button" class="button secondary" disabled>Disabled</button>
    <button type="button" class="button success" disabled>Disabled</button>
    <button type="button" class="button alert" disabled>Disabled</button>
    <button type="button" class="button warning" disabled>Disabled</button>
    ```

    Alternatively, you can also use disabled hollow buttons.

    ```html
    <a class="button hollow disabled" href="#" aria-disabled>Disabled</a>
    <button type="button" class="button hollow primary" disabled>Disabled</button>
    <button type="button" class="button hollow secondary" disabled>Disabled</button>
    <button type="button" class="button hollow success" disabled>Disabled</button>
    <button type="button" class="button hollow alert" disabled>Disabled</button>
    <button type="button" class="button hollow warning" disabled>Disabled</button>
    ```

    ---

    ## Clear Style

    Add the `.clear` class to a button to give it a clear style. Change the `$button-fill` variable in your settings file to `clear` to make this the default style. Changing this setting will remove the `.clear` class from your CSS.

    <p>
      <a class="" data-open-video="7:37"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>


    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/LymNyB?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <a class="clear button" href="#">Primary</a>
    <a class="clear button secondary" href="#">Secondary</a>
    <a class="clear button success" href="#">Success</a>
    <a class="clear button alert" href="#">Alert</a>
    <a class="clear button warning" href="#">Warning</a>
    <a class="clear button" href="#" disabled>Disabled</a>
    ```

    <p>This is especially useful as a secondary action button. This way you get proper spacing and line-height. Example:</p>

    <button class="button primary" href="#">Primary Action</button>
    <button class="clear button" href="#">Secondary Action</button>


    ---

    ## Dropdown Arrows

    Add a dropdown arrow to your button with the `.dropdown` class.

    <div class="primary callout">
      <p>This doesn't add dropdown functionality automatically. To do that, you can attach our <a href="dropdown.html">Dropdown plugin</a>.</p>
    </div>

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/PmeNOY?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <button class="dropdown button tiny">Dropdown Button</button>
    <button class="dropdown button small">Dropdown Button</button>
    <button class="dropdown button">Dropdown Button</button>
    <button class="dropdown button large">Dropdown Button</button>
    <button class="dropdown button expanded">Dropdown Button</button>
    ```

    ---

    ## Accessibility

    Make sure that the text of the button is descriptive. If for some reason, your button contains no readable text (for example, just a symbol or icon), add screen reader-only text to the button to clarify its purpose. The symbol or icon should be wrapped in an element with the attribute `aria-hidden="true"`, to prevent screen readers from trying to pronounce the symbol.

    Use the `.show-for-sr` class to define screen reader-only text.

    ```html
    <button class="button" type="button">
      <!-- Screen readers will see "close" -->
      <span class="show-for-sr">Close</span>
      <!-- Visual users will see the X, but not the "Close" text -->
      <span aria-hidden="true"><i class="fi-x"></i></span>
    </button>
    ```"""

    pass


class CALLOUT:
    """---
    title: Callout
    description: Callouts combine panels and alerts from Foundation 5 into one generic container component.
    video: yQdu0oSuaCo
    sass: scss/components/_callout.scss
    tags:
      - panel
      - alert
    ---

    ## Basics

    A callout is just an element with a `.callout` class applied. You can put any kind of content inside.

    <p>
      <a class="" data-open-video="0:33"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/WjyGVB?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="callout">
      <h5>This is a callout.</h5>
      <p>It has an easy to override visual style, and is appropriately subdued.</p>
      <a href="#">It's dangerous to go alone, take this.</a>
    </div>
    ```

    ---

    ## Coloring

    Callouts can be colored using the `.secondary`, `.primary`, `.success`, `.warning`, or `.alert` classes. Links inside the callout will be tinted to match the color of the callout.

    <p>
      <a class="" data-open-video="2:02"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/JNZbGy?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="callout secondary">
      <h5>This is a secondary callout</h5>
      <p>It has an easy to override visual style, and is appropriately subdued.</p>
      <a href="#">It's dangerous to go alone, take this.</a>
    </div>
    ```

    <div class="callout secondary">
      <h5>This is a secondary callout</h5>
      <p>It has an easy to override visual style, and is appropriately subdued.</p>
      <a href="#">It's dangerous to go alone, take this.</a>
    </div>

    <div class="callout primary">
      <h5>This is a primary callout</h5>
      <p>It has an easy to override visual style, and is appropriately subdued.</p>
      <a href="#">It's dangerous to go alone, take this.</a>
    </div>

    <div class="callout success">
      <h5>This is a success callout</h5>
      <p>It has an easy to override visual style, and is appropriately subdued.</p>
      <a href="#">It's dangerous to go alone, take this.</a>
    </div>

    <div class="callout warning">
      <h5>This is a warning callout</h5>
      <p>It has an easy to override visual style, and is appropriately subdued.</p>
      <a href="#">It's dangerous to go alone, take this.</a>
    </div>

    <div class="callout alert">
      <h5>This is an alert callout</h5>
      <p>It has an easy to override visual style, and is appropriately subdued.</p>
      <a href="#">It's dangerous to go alone, take this.</a>
    </div>

    ---

    ## Sizing

    Callouts can be sized using the `.small` and `.large` classes. These will affect the padding around content to be smaller and larger respectively.

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/ybEVVe?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="callout small">
      <h5>This is a small callout</h5>
      <p>It has an easy to override visual style, and is appropriately subdued.</p>
      <a href="#">It's dangerous to go alone, take this.</a>
    </div>

    <div class="callout large">
      <h5>This is a large callout</h5>
      <p>It has an easy to override visual style, and is appropriately subdued.</p>
      <a href="#">It's dangerous to go alone, take this.</a>
    </div>
    ```

    ---

    ## Making Closable

    Pair the callout with the [close button](close-button.html) component and `data-closable` attribute to create a dismissable alert box.

    <a class="" data-open-video="4:47"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    <div class="callout primary">
      <p>Any element can be used as a close trigger, not just close button. Adding the attribute <code>data-close</code> to any element within the callout will turn it into a close trigger.</p>
      <p>When using the <code>data-closable</code> attribute, you can optionally add <a href="https://get.foundation/sites/docs/motion-ui.html">Motion UI</a> classes to the attribute to change the closing animation. If no class is added, the plugin defaults to jQuery's <code>.fadeOut()</code> function.</p>
    </div>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/eWKBBd?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="callout alert" data-closable>
      <h5>This is Important!</h5>
      <p>But when you're done reading it, click the close button in the corner to dismiss this alert.</p>
      <p>I'm using the default <code>data-closable</code> parameters, and simply fade out.</p>
      <button class="close-button" aria-label="Dismiss alert" type="button" data-close>
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    <div class="callout success" data-closable="slide-out-right">
      <h5>This a friendly message.</h5>
      <p>And when you're done with me, I can be closed using a Motion UI animation.</p>
      <button class="close-button" aria-label="Dismiss alert" type="button" data-close>
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    ```"""

    pass


class CARD:
    """---
    title: Card
    description: Cards are a popular and flexible UI component.
    video: 'OMwg8UsrLrM'
    sass: scss/components/_card.scss
    tags:
      - card
    flex: true
    ---

    ## Basics

    A card is just an element with a `.card` class applied. You can put any kind of content inside.
    Make sure you wrap your content in a `.card-section` element in order to achieve the traditional card look.

    A card container has no padding, allowing you to place full-bleed images inside. Use the `.card-divider` and `.card-section` classes to sub-divide a card.

    <div class="callout primary">

    The `.card` and `.card-divider` elements are flexbox containers. This allows you to use [Flexbox Utilities](flexbox-utilities.html) to create more flexible layouts.

    </div>


    <p>
      <a class="" data-open-video="0:32"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/oWMEpo?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="card" style="width: 300px;">
      <div class="card-divider">
        This is a header
      </div>
      <img src="assets/img/generic/rectangle-1.jpg">
      <div class="card-section">
        <h4>This is a card.</h4>
        <p>It has an easy to override visual style, and is appropriately subdued.</p>
      </div>
    </div>
    ```

    <div class="alert callout">
      <p><strong>Browser Bug (IE 11 - Flexbug): </strong>On IE 11, when using the card with image, you may see a lot of whitespace under each image that happens to match the original image size. The bug can be reproduced <a href="https://codepen.io/IamManchanda/pen/MmNqEX?editors=1100">here</a> on an IE11 browser. Use <code>.card-image</code> class to wrap your image to resolve this.</p>
    </div>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/aWrWQq?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="card-image">
      <img src="assets/img/generic/rectangle-1.jpg">
    </div>
    ```

    ---

    ### Card Divider

    You can also include a `.card-divider` element as a title, footer or to break up content.

    <p>
      <a class="" data-open-video="1:30"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/PmyPbL?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="card" style="width: 300px;">
      <div class="card-divider">
        <h4>I'm featured</h4>
      </div>
      <img src="assets/img/generic/rectangle-1.jpg">
      <div class="card-section">
        <p>This card makes use of the card-divider element.</p>
      </div>
    </div>
    ```

    ---

    ### Images

    Images play nicely with cards. Simply include one outside of the `.card-section` element to span nicely to the edges. Or move the image inside the `.card-section` to have padding around the image.

    <p>
      <a class="" data-open-video="2:12"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/QvBQvR?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <!-- image has no padding -->
    <div class="card">
      <img src="assets/img/generic/rectangle-1.jpg">
      <div class="card-section">
        <p>This is a simple card with an image.</p>
      </div>
    </div>

    <!-- image has padding -->
    <div class="card">
      <div class="card-section">
        <img src="assets/img/generic/rectangle-1.jpg">
      </div>
      <div class="card-section">
        <p>This is a simple card with an image inside a `.card-section`.</p>
      </div>
    </div>
    ```

    <div class="grid-x grid-margin-x small-up-3">
      <div class="cell">
        <div class="card">
          <img src="assets/img/generic/rectangle-1.jpg">
          <div class="card-section">
            <p>This is a simple card with an image.</p>
          </div>
        </div>
      </div>
      <div class="cell">
        <div class="card">
          <div class="card-section">
            <img src="assets/img/generic/rectangle-1.jpg">
          </div>
          <div class="card-section">
            <p>This is a simple card with an image inside a `.card-section`.</p>
          </div>
        </div>
      </div>
    </div>

    ```html
    <div class="card">
      <div class="card-section">
        <p>Images work just fine below the content too!</p>
      </div>
      <img src="assets/img/generic/rectangle-1.jpg">
    </div>
    ```

    <div class="grid-x grid-margin-x small-up-3">
      <div class="cell">
        <div class="card">
          <div class="card-section">
            <p>Images work just fine below the content too!</p>
          </div>
          <img src="assets/img/generic/rectangle-1.jpg">
        </div>
      </div>
    </div>

    ---

    ## Sizing

    You can either set the width of cards with custom css or add them into the Foundation grid.

    <p>
      <a class="" data-open-video="0:34"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/PmabmL?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-container">
      <div class="grid-x grid-margin-x small-up-2 medium-up-3">
        <div class="cell">
          <div class="card">
            <img src="assets/img/generic/rectangle-1.jpg">
            <div class="card-section">
            <h4>This is a row of cards.</h4>
              <p>This row of cards is embedded in an X-Y Block Grid.</p>
            </div>
          </div>
        </div>
        <div class="cell">
          <div class="card">
            <img src="assets/img/generic/rectangle-1.jpg">
            <div class="card-section">
              <h4>This is a card.</h4>
              <p>It has an easy to override visual style, and is appropriately subdued.</p>
            </div>
          </div>
        </div>
        <div class="cell">
          <div class="card">
            <img src="assets/img/generic/rectangle-1.jpg">
            <div class="card-section">
              <h4>This is a card.</h4>
              <p>It has an easy to override visual style, and is appropriately subdued.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="grid-x grid-margin-x small-up-2 medium-up-3">
      <div class="cell">
        <div class="card">
          <img src="assets/img/generic/rectangle-1.jpg">
          <div class="card-section">
            <h4>This is a row of cards.</h4>
            <p>This row of cards is embedded in an Flex Block Grid.</p>
          </div>
        </div>
      </div>
      <div class="cell">
        <div class="card">
          <img src="assets/img/generic/rectangle-1.jpg">
          <div class="card-section">
            <h4>This is a card.</h4>
            <p>It has an easy to override visual style, and is appropriately subdued.</p>
          </div>
        </div>
      </div>
      <div class="cell">
        <div class="card">
          <img src="assets/img/generic/rectangle-1.jpg">
          <div class="card-section">
            <h4>This is a card.</h4>
            <p>It has an easy to override visual style, and is appropriately subdued.</p>
          </div>
        </div>
      </div>
    </div>
    ```"""

    pass


class CLOSE_BUTTON:
    """---
    title: Close Button
    description: The humble close button can be used anywhere you need something to go away on click.
    video: '0cvJbo7ItpU'
    sass: scss/components/_close-button.scss
    ---

    A close button is a `<button>` element with the class `.close-button`. We use the multiplication symbol (`&times;`) as the X icon. This icon is wrapped in a `<span>` with the attribute `aria-hidden="true"`, so screen readers don't read the X icon.

    The button is also labeled with `aria-label` to clarify what the button's purpose is.

    <p>
      <a class="" data-open-video="1:07"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ncoden/pen/vVrrjG?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="callout" data-closable>
      <button class="close-button" aria-label="Close alert" type="button" data-close>
        <span aria-hidden="true">&times;</span>
      </button>
      <p>Look at this close button!</p>
    </div>
    ```

    ---

    ## Making Closable

    <div class="callout primary">
      <p>The close button on its own doesn't close elements, but you can use it with <a href="toggler.html">Toggler</a>, <a href="reveal.html">Reveal</a>, <a href="off-canvas.html">Off-canvas</a>, and other plugins that have open and close behaviors.</p>
    </div>

    <div class="primary callout">
      <p>Any element can be used as a close trigger, not just close button. Adding the attribute <code>data-close</code> to any element within the callout will turn it into a close trigger.</p>
    </div>

    The below example pairs the callout with the close button component and `data-closable` attribute to create a dismissible alert box.

    <a class="" data-open-video="4:24"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/JNvEox?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="callout" data-closable>
      <p>You can so totally close this!</p>
      <button class="close-button" aria-label="Dismiss alert" type="button" data-close>
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    <div class="success callout" data-closable="slide-out-right">
      <p>You can close me too, and I close using a Motion UI animation.</p>
      <button class="close-button" aria-label="Dismiss alert" type="button" data-close>
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    ```"""

    pass


class COMPATIBILITY:
    """---
    title: Compatibility
    description: Foundation is tested across many browsers and devices, and works back as far as IE9 and Android 2.
    tags:
      - support
      - browser
    ---

    ## Overview

    <table class="docs-compat-table">
      <tr>
        <td>Chrome</td>
        <td class="works" rowspan="7">Last Two Versions</td>
      </tr>
      <tr><td>Firefox</td></tr>
      <tr><td>Safari</td></tr>
      <tr><td>Opera</td></tr>
      <tr><td>Mobile Safari<sup>1</sup></td></tr>
      <tr><td>IE Mobile</td></tr>
      <tr><td>Edge</td></tr>
      <tr>
        <td>Internet Explorer</td>
        <td class="works">Versions 9+</td>
      </tr>
      <tr>
        <td>Android Browser</td>
        <td class="works">Versions 4.4+</td>
      </tr>
    </table>

    <sup>1</sup>iOS 7+ is actively supported but with some known bugs.

    ---

    ## What Won't Work?

    - **The Grid:** Foundation's grid uses `box-sizing: border-box` to apply gutters to columns, but this property isn't supported in IE8.
    - **Desktop Styles:** Because the framework is written mobile-first, browsers that don't support media queries will display the mobile styles of the site.
    - **JavaScript:** Our plugins use a number of handy ECMAScript 5 features that aren't supported in IE8.
    """

    pass


class DRILLDOWN_MENU:
    """---
    title: Drilldown Menu
    description: Drilldown is one of Foundation's three menu patterns, which converts a series of nested lists into a vertical drilldown menu.
    video: 8qPQRXl52hI
    scss: scss/components/_drilldown.scss
    js: js/foundation.drilldown.js
    ---

    ## Basics

    Drilldowns use the standard [Menu](menu.html#nested-style) syntax, using `<ul>`, `<li>`, and `<a>`. Add `data-drilldown` to the root menu to set up the drilldown.

    To create sub-menus, place a `<ul>` *next to* an `<a>`. Clicking that `<a>` will then open the `<ul>` that it's next to.

    Any `<a>` without a submenu will function like a normal link.

    <p>
      <a class="" data-open-video="0:54"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/JNZodd?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="vertical menu drilldown" data-drilldown>
      <li><a href="#">One</a></li>
      <li>
        <a href="#">Two</a>
        <ul class="menu vertical nested">
          <li><a href="#">Two A</a></li>
          <li><a href="#">Two B</a></li>
          <li><a href="#">Two C</a></li>
          <li><a href="#">Two D</a></li>
        </ul>
      </li>
      <li><a href="#">Three</a></li>
      <li><a href="#">Four</a></li>
    </ul>
    ```

    <div class="primary callout">
      <p>The drilldown menu takes on the height of the tallest menu in the hierarchy, so the menu doesn't change height as the user navigates it.</p>
    </div>

    <ul class="vertical menu drilldown" data-drilldown style="max-width: 250px" id="m1">
      <li>
        <a href="#">Item 1</a>
        <ul class="menu vertical nested">
          <li>
            <a href="#">Item 1A</a>
            <ul class="menu vertical nested">
              <li><a href="#Item-1Aa">Item 1Aa</a></li>
              <li><a href="#Item-1Ba">Item 1Ba</a></li>
              <li><a href="#Item-1Ca">Item 1Ca</a></li>
              <li><a href="#Item-1Da">Item 1Da</a></li>
              <li><a href="#Item-1Ea">Item 1Ea</a></li>
            </ul>
          </li>
          <li><a href="#Item-1B">Item 1B</a></li>
          <li><a href="#Item-1C">Item 1C</a></li>
          <li><a href="#Item-1D">Item 1D</a></li>
          <li><a href="#Item-1E">Item 1E</a></li>
        </ul>
      </li>
      <li>
        <a href="#">Item 2</a>
        <ul class="menu vertical nested">
          <li><a href="#Item-2A">Item 2A</a></li>
          <li><a href="#Item-2B">Item 2B</a></li>
          <li><a href="#Item-2C">Item 2C</a></li>
          <li><a href="#Item-2D">Item 2D</a></li>
          <li><a href="#Item-2E">Item 2E</a></li>
        </ul>
      </li>
      <li>
        <a href="#">Item 3</a>
        <ul class="menu vertical nested">
          <li><a href="#Item-3A">Item 3A</a></li>
          <li><a href="#Item-3B">Item 3B</a></li>
          <li><a href="#Item-3C">Item 3C</a></li>
          <li><a href="#Item-3D">Item 3D</a></li>
          <li><a href="#Item-3E">Item 3E</a></li>
        </ul>
      </li>
      <li><a href="#Item-4"> Item 4</a></li>
    </ul>

    ## autoHeight

    <div class="secondary callout">
      <p>If you like to set the height to auto you can also set the autoHeight and animateHeight params</p>
      <button class="button expanded" onclick="$('#m3').foundation('_destroy');if($('#m3').data('autoHeight')){$('#m3').data('autoHeight',false);$(this).html('autoHeight is Off');}else{$('#m3').data('autoHeight',true);$(this).html('autoHeight is On');}new Foundation.Drilldown($('#m3'));return false;">autoHeight is On</button>
    </div>

    <p>
    <a class="" data-open-video="4:39"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/mmKyrw?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="vertical menu drilldown" data-drilldown data-auto-height="true" data-animate-height="true">
      <!--  -->
    </ul>
    ```

    <ul class="vertical menu drilldown" data-drilldown data-auto-height="true" data-animate-height="true" style="max-width: 250px" id="m3">
      <li>
        <a href="#">Item 1</a>
        <ul class="menu vertical nested">
          <li>
            <a href="#">Item 1A</a>
            <ul class="menu vertical nested">
              <li><a href="#Item-1Aa">Item 1Aa</a></li>
              <li><a href="#Item-1Ba">Item 1Ba</a></li>
            </ul>
          </li>
          <li><a href="#Item-1B">Item 1B</a></li>
          <li><a href="#Item-1C">Item 1C</a></li>
          <li><a href="#Item-1D">Item 1D</a></li>
          <li><a href="#Item-1E">Item 1E</a></li>
        </ul>
      </li>
      <li>
        <a href="#">Item 2</a>
        <ul class="menu vertical nested">
          <li><a href="#Item-2A">Item 2A</a></li>
          <li><a href="#Item-2B">Item 2B</a></li>
          <li><a href="#Item-2C">Item 2C</a></li>
          <li><a href="#Item-2D">Item 2D</a></li>
          <li><a href="#Item-2E">Item 2E</a></li>
        </ul>
      </li>
      <li>
        <a href="#">Item 3</a>
        <ul class="menu vertical nested">
          <li><a href="#Item-3A">Item 3A</a></li>
          <li><a href="#Item-3B">Item 3B</a></li>
          <li><a href="#Item-3C">Item 3C</a></li>
          <li><a href="#Item-3D">Item 3D</a></li>
          <li>
            <a href="#Item-3E">Item 3E</a>
            <ul class="menu vertical nested">
              <li><a href="#Item-3EA">Item 3EA</a></li>
              <li><a href="#Item-3EB">Item 3EB</a></li>
              <li><a href="#Item-3EC">Item 3EC</a></li>
              <li><a href="#Item-3ED">Item 3ED</a></li>
              <li><a href="#Item-3EE">Item 3EE</a></li>
              <li><a href="#Item-3EA">Item 3EA</a></li>
              <li><a href="#Item-3EB">Item 3EB</a></li>
              <li><a href="#Item-3EC">Item 3EC</a></li>
              <li><a href="#Item-3ED">Item 3ED</a></li>
              <li><a href="#Item-3EE">Item 3EE</a></li>
              <li><a href="#Item-3EA">Item 3EA</a></li>
              <li><a href="#Item-3EB">Item 3EB</a></li>
              <li><a href="#Item-3EC">Item 3EC</a></li>
              <li><a href="#Item-3ED">Item 3ED</a></li>
              <li><a href="#Item-3EE">Item 3EE</a></li>
            </ul>
          </li>
        </ul>
      </li>
      <li><a href="#Item-4"> Item 4</a></li>
      <li><a href="#Item-5"> Item 5</a></li>
      <li><a href="#Item-6"> Item 6</a></li>
      <li><a href="#Item-7"> Item 7</a></li>
      <li><a href="#Item-8"> Item 8</a></li>
    </ul>

    ## ScrollTop Drilldown

    <div class="callout">Scroll to the top of the menu when selecting a submenu/navigating back using the menu back button. Can be useful with a longer menu to provide a better user experience.</div>


    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/jmKEwX?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="vertical menu drilldown" data-drilldown data-scroll-top="true">
      <!--  -->
    </ul>
    ```

    <ul class="vertical menu drilldown" data-drilldown data-scroll-top="true" data-auto-height="true" data-animate-height="true" style="max-width: 250px" id="m2">
      <li><a href="#">Item</a></li>
      <li><a href="#">Item</a></li>
      <li><a href="#">Item</a></li>
      <li><a href="#">Item</a></li>
      <li><a href="#">Item</a></li>
      <li><a href="#">Item</a></li>
      <li><a href="#">Item</a></li>
      <li><a href="#">Item</a></li>
      <li><a href="#">Item</a></li>
      <li><a href="#">Item</a></li>
      <li> <a href="#">Item</a>
        <ul class="vertical menu nested">
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li><a href="#">Item</a></li>
          <li> <a href="#">Item</a>
            <ul class="vertical menu nested">
              <li><a href="#">Item</a></li>
            </ul>
          </li>
        </ul>
      </li>
      <li><a href="#">Item</a></li>
    </ul>

    ---

    ## Custom Styling

    The drilldown plugin automatically adds a back button to the top of each nested menu. To style this control, target the `.js-drilldown-back` class:

    ```css
    .js-drilldown-back {
      // ...
    }
    ```"""

    pass


class DROPDOWN_MENU:
    """---
    title: Dropdown Menu
    description: Change a basic Menu into an expandable dropdown menu with the Dropdown Menu plugin.
    video: 'KfnRuKBKrbw'
    sass: scss/components/_dropdown-menu.scss
    js: js/foundation.dropdownMenu.js
    ---

    ## Horizontal

    Dropdown menus build on the [Menu](menu.html) component's syntax. Add the class `.dropdown` and the attribute `data-dropdown-menu` to the menu container to set up the dropdown.

    ```html
    <ul class="dropdown menu" data-dropdown-menu>
      <li><a href="#">Item 1</a></li>
      <li><a href="#">Item 2</a></li>
      <li><a href="#">Item 3</a></li>
      <li><a href="#">Item 4</a></li>
    </ul>
    ```

    To create dropdown menus, nest a new `<ul>` inside an `<li>`. You can nest further to create more levels of dropdowns.

    <a class="" data-open-video="0:53"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>

    <div class="primary callout">
      <p>Note that the <code>&lt;ul&gt;</code> goes <em>after</em> the <code>&lt;a&gt;</code>, and not inside of it.</p>
    </div>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/XRYWPO?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="dropdown menu" data-dropdown-menu>
      <li>
        <a href="#">Item 1</a>
        <ul class="menu">
          <li><a href="#">Item 1A</a></li>
          <!-- ... -->
        </ul>
      </li>
      <li><a href="#">Item 2</a></li>
      <li><a href="#">Item 3</a></li>
      <li><a href="#">Item 4</a></li>
    </ul>
    ```

    <ul class="dropdown menu" data-dropdown-menu>
      <li>
        <a href="#Item-1">Item 1</a>
        <ul class="menu">
          <li><a href="#Item-1A">Item 1A</a></li>
          <li>
            <a href="#Item-1B">Item 1B</a>
            <ul class="menu">
              <li><a href="#Item-1Bi">Item 1B i</a></li>
              <li><a href="#Item-1Bii">Item 1B ii</a></li>
              <li>
                <a href="#Item-1Biii">Item 1B iii</a>
                <ul class="menu">
                  <li><a href="#Item-1Biiialpha">Item 1B iii alpha</a></li>
                  <li><a href="#Item-1Biiiomega">Item 1B iii omega</a></li>
                </ul>
              </li>
              <li>
                <a href="#Item-1Biv">Item 1B iv</a>
                <ul class="menu">
                  <li><a href="#Item-1Bivalpha">Item 1B iv alpha</a></li>
                </ul>
              </li>
            </ul>
          </li>
          <li><a href="#Item-1C">Item 1C</a></li>
        </ul>
      </li>
      <li>
        <a href="#Item-2">Item 2</a>
        <ul class="menu">
          <li><a href="#Item-2A">Item 2A</a></li>
          <li><a href="#Item-2B">Item 2B</a></li>
        </ul>
      </li>
      <li><a href="#Item-3">Item 3</a></li>
      <li><a href="#Item-4">Item 4</a></li>
    </ul>

    ---

    ## Vertical

    Add the `.vertical` class to the top-level menu to make it vertical. Sub-menus are automatically vertical, regardless of the orientation of the top-level menu.

    <div class="primary callout">
      <p>Menus are block-level elements, which means they stretch to fill the width of their container. To make the below example less goofy, we've hard-coded a <code>max-width</code> on the menu.</p>
    </div>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/LyrYaE?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="vertical dropdown menu" data-dropdown-menu style="max-width: 250px;">
      <li>
        <a href="#">Item 1</a>
        <ul class="vertical menu nested">
          <li><a href="#">Item 1A</a></li>
          <!-- ... -->
        </ul>
      </li>
      <li><a href="#">Item 2</a></li>
      <li><a href="#">Item 3</a></li>
      <li><a href="#">Item 4</a></li>
      <!-- ... -->
    </ul>
    ```

    <ul class="vertical dropdown menu" data-dropdown-menu style="max-width: 250px;">
      <li>
        <a href="#Item-1">Item 1</a>
        <ul class="vertical menu nested">
          <li><a href="#Item-1A">Item 1A</a></li>
          <li>
            <a href="#Item-1B">Item 1B</a>
            <ul class="vertical menu nested">
              <li><a href="#Item-1Bi">Item 1B i</a></li>
              <li><a href="#Item-1Bii">Item 1B ii</a></li>
              <li>
                <a href="#Item-1Biii">Item 1B iii</a>
                <ul class="vertical menu nested">
                  <li><a href="#Item-1Biiialpha">Item 1B iii alpha</a></li>
                  <li><a href="#Item-1Biiiomega">Item 1B iii omega</a></li>
                </ul>
              </li>
              <li>
                <a href="#Item-1Biv">Item 1B iv</a>
                <ul class="vertical menu nested">
                  <li><a href="#Item-1Bivalpha">Item 1B iv alpha</a></li>
                </ul>
              </li>
            </ul>
          </li>
          <li><a href="#Item-1C">Item 1C</a></li>
        </ul>
      </li>
      <li>
        <a href="#Item-2">Item 2</a>
        <ul class="vertical menu nested">
          <li><a href="#Item-2A">Item 2A</a></li>
          <li><a href="#Item-2B">Item 2B</a></li>
        </ul>
      </li>
      <li><a href="#Item-3">Item 3</a></li>
      <li><a href="#Item-4">Item 4</a></li>
    </ul>

    ---

    ## Sticky Navigation

    See the documentation for the [Sticky](sticky.html#sticky-navigation) plugin to see how to easily make a sticky nav bar.

    ---

    ### Preventing FOUC

    Before the JavaScript on your page loads, the dropdown menus will not have arrows. However, once the JavaScript file has loaded, the arrows will appear causing a [flash of unstyled content](https://en.wikipedia.org/wiki/Flash_of_unstyled_content). You can prevent this by adding the `.is-dropdown-submenu-parent` class manually.

    ```html
    <ul class="dropdown menu" data-dropdown-menu>
      <li class="is-dropdown-submenu-parent">
        <a href="#">Item 1</a>
        <ul class="menu">
          <li><a href="#">Item 1A</a></li>
          <!-- ... -->
        </ul>
      </li>
      <li><a href="#">Item 2</a></li>
      <li><a href="#">Item 3</a></li>
      <li><a href="#">Item 4</a></li>
    </ul>
    ```"""

    pass


class DROPDOWN:
    """---
    title: Dropdown
    description: Dropdown panes are little happy sprites which can be revealed on click or hover.
    sass: scss/components/_dropdown.scss
    js: js/foundation.dropdown.js
    video: '0F68zptD_nQ'
    ---

    <div class="primary callout">
      <p>You might be looking for <a href="dropdown-menu.html">dropdown menus</a>, which are a separate plugin.</p>
    </div>

    ## Basics

    To create a dropdown pane, add the class `.dropdown-pane` and the attribute `data-dropdown` to an element. Give the dropdown a unique ID as well.

    To create the dropdown trigger, add `data-toggle` to a `<button>`. The value of `data-toggle` is the ID of the dropdown.

    <p>
      <a class="" data-open-video="0:47"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/NjzByp?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>


    ```html
    <button class="button" type="button" data-toggle="example-dropdown">Toggle Dropdown</button>
    <div class="dropdown-pane" id="example-dropdown" data-dropdown data-auto-focus="true">
      Example form in a dropdown.
      <form>
        <div class="grid-container">
          <div class="grid-x grid-margin-x">
            <div class="cell medium-6">
              <label>Name
                <input type="text" placeholder="Kirk, James T.">
              </label>
            </div>
            <div class="cell medium-6">
              <label>Rank
                <input type="text" placeholder="Captain">
              </label>
            </div>
          </div>
        </div>
      </form>
    </div>

    <button class="button" type="button" data-toggle="example-dropdown-1">Hoverable Dropdown</button>
    <div class="dropdown-pane" id="example-dropdown-1" data-dropdown data-hover="true" data-hover-pane="true">
      Just some junk that needs to be said. Or not. Your choice.
    </div>
    ```

    ---

    ## Positioning

    By default, a dropdown anchors below the button that opened it. Add the class `.top`, `.right`, or `.bottom` to the dropdown to change this.

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/YVvjvz?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <button class="button" type="button" data-toggle="example-dropdown2">Top Aligned</button>

    <div class="dropdown-pane top" id="example-dropdown2" data-dropdown>
      Just some junk that needs to be said. Or not. Your choice.
    </div>
    ```

    <button class="button" type="button" data-toggle="example-dropdown3" style="float: right;">Left Aligned</button>
    <div class="dropdown-pane left" id="example-dropdown3" data-dropdown>
      Just some junk that needs to be said. Or not. Your choice.
    </div>

    <button class="button" type="button" data-toggle="example-dropdown4">Right Aligned</button>
    <div class="dropdown-pane right" id="example-dropdown4" data-dropdown>
      Just some junk that needs to be said. Or not. Your choice.
    </div>


    Adding `.float-right` or `.float-left` to the anchor will change the direction of the dropdown as well.

    <button class="button float-right" type="button" data-toggle="example-dropdown5">Bottom-right Aligned</button>
    <div class="dropdown-pane bottom" id="example-dropdown5" data-dropdown>
      Just some junk that needs to be said. Or not. Your choice.
    </div>

    <button class="button float-left" type="button" data-toggle="example-dropdown6">Bottom-left Aligned</button>
    <div class="dropdown-pane bottom" id="example-dropdown6" data-dropdown>
      Just some junk that needs to be said. Or not. Your choice.
    </div>

    ---

    ## Explicit Positioning

    <div class="callout primary">
      <p><strong>New in v6.4:</strong> Heads up! This explicit positioning model is a new feature in v6.4.</p>
    </div>

    Wouldn't it be great if you can define both positions at the dropdown element. Dropdown has a fully explicit positioning model through which you can use both `data-position` and `data-alignment` to define both positions of the box.

    These dropdowns test various positioning and alignments. Valid positions are left/right/top/bottom. Valid alignments are left/right/top/bottom/center. Left align means left sides should line up. Right align means right sides should line up. Center align means centers should line up.

    #### Top and Bottom positioned

    ```html
    <!-- Bottom Left -->
    <button class="button" type="button" data-toggle="example-dropdown-bottom-left">Toggle Dropdown</button>
    <div class="dropdown-pane" data-position="bottom" data-alignment="left" id="example-dropdown-bottom-left" data-dropdown data-auto-focus="true">
      <!-- My dropdown content in here -->
    </div>

    <!-- Bottom Center -->
    <button class="button" type="button" data-toggle="example-dropdown-bottom-center">Toggle Dropdown</button>
    <div class="dropdown-pane" data-position="bottom" data-alignment="center" id="example-dropdown-bottom-center" data-dropdown data-auto-focus="true">
      <!-- My dropdown content in here -->
    </div>

    <!-- Bottom Right -->
    <button class="button" type="button" data-toggle="example-dropdown-bottom-right">Toggle Dropdown</button>
    <div class="dropdown-pane" data-position="bottom" data-alignment="right" id="example-dropdown-bottom-right" data-dropdown data-auto-focus="true">
      <!-- My dropdown content in here -->
    </div>

    <!-- Top Left -->
    <button class="button" type="button" data-toggle="example-dropdown-top-left">Toggle Dropdown</button>
    <div class="dropdown-pane" data-position="top" data-alignment="left" id="example-dropdown-top-left" data-dropdown data-auto-focus="true">
      <!-- My dropdown content in here -->
    </div>

    <!-- Top Center -->
    <button class="button" type="button" data-toggle="example-dropdown-top-center">Toggle Dropdown</button>
    <div class="dropdown-pane" data-position="top" data-alignment="center" id="example-dropdown-top-center" data-dropdown data-auto-focus="true">
      <!-- My dropdown content in here -->
    </div>

    <!-- Top Right -->
    <button class="button" type="button" data-toggle="example-dropdown-top-right">Toggle Dropdown</button>
    <div class="dropdown-pane" data-position="top" data-alignment="right" id="example-dropdown-top-right" data-dropdown data-auto-focus="true">
      <!-- My dropdown content in here -->
    </div>
    ```

    <div class="grid-container">
      <div class="grid-x grid-margin-x small-up-1 medium-up-3">
        <div class="cell">
          <p>Bottom Left</p>
          <button class="button" type="button" data-toggle="example-dropdown-bottom-left">Toggle Dropdown</button>
          <div class="dropdown-pane" data-position="bottom" data-alignment="left" id="example-dropdown-bottom-left" data-dropdown data-auto-focus="true">
            <p>This dropdown has position bottom and alignment left should align with its top left corner at the bottom left of the button</p>
          </div>
        </div>
        <div class="cell">
          <p>Bottom Center</p>
          <button class="button" type="button" data-toggle="example-dropdown-bottom-center">Toggle Dropdown</button>
          <div class="dropdown-pane" data-position="bottom" data-alignment="center" id="example-dropdown-bottom-center" data-dropdown data-auto-focus="true">
            <p>This dropdown has position bottom and alignment center should align below the button with its center aligned with the center of the button</p>
          </div>
        </div>
        <div class="cell">
          <p>Bottom Right</p>
          <button class="button" type="button" data-toggle="example-dropdown-bottom-right">Toggle Dropdown</button>
          <div class="dropdown-pane" data-position="bottom" data-alignment="right" id="example-dropdown-bottom-right" data-dropdown data-auto-focus="true">
            <p>This dropdown has position bottom and alignment right should align with its top right corner at the bottom right of the button</p>
          </div>
        </div>
        <div class="cell">
          <p>Top Left</p>
          <button class="button" type="button" data-toggle="example-dropdown-top-left">Toggle Dropdown</button>
          <div class="dropdown-pane" data-position="top" data-alignment="left" id="example-dropdown-top-left" data-dropdown data-auto-focus="true">
            <p>This dropdown has position top and alignment left should align with its bottom left corner at the top left of the button</p>
          </div>
        </div>
        <div class="cell">
          <p>Top Center</p>
          <button class="button" type="button" data-toggle="example-dropdown-top-center">Toggle Dropdown</button>
          <div class="dropdown-pane" data-position="top" data-alignment="center" id="example-dropdown-top-center" data-dropdown data-auto-focus="true">
            <p>This dropdown has position top and alignment center should align above with its center aligned with the center of the button</p>
          </div>
        </div>
        <div class="cell">
          <p>Top Right</p>
          <button class="button" type="button" data-toggle="example-dropdown-top-right">Toggle Dropdown</button>
          <div class="dropdown-pane" data-position="top" data-alignment="right" id="example-dropdown-top-right" data-dropdown data-auto-focus="true">
            <p>This dropdown has position top and alignment right should align with its bottom right corner at the top right of the button</p>
          </div>
        </div>
      </div>
    </div>

    <br>

    #### Left and Right Positioned

    ```html
    <!-- Right Top -->
    <button class="button" type="button" data-toggle="example-dropdown-right-top">Toggle Dropdown</button>
    <div class="dropdown-pane" data-position="right" data-alignment="top" id="example-dropdown-right-top" data-dropdown data-auto-focus="true">
    </div>

    <!-- Left Top -->
    <button class="button" type="button" data-toggle="example-dropdown-left-top">Toggle Dropdown</button>
    <div class="dropdown-pane" data-position="left" data-alignment="top" id="example-dropdown-left-top" data-dropdown data-auto-focus="true">
    </div>

    <!-- Right Center -->
    <button class="button" type="button" data-toggle="example-dropdown-right-center">Toggle Dropdown</button>
    <div class="dropdown-pane" data-position="right" data-alignment="center" id="example-dropdown-right-center" data-dropdown data-auto-focus="true">
    </div>

    <!-- Left Center -->
    <button class="button" type="button" data-toggle="example-dropdown-left-center">Toggle Dropdown</button>
    <div class="dropdown-pane" data-position="left" data-alignment="center" id="example-dropdown-left-center" data-dropdown data-auto-focus="true">
    </div>

    <!-- Right Bottom -->
    <button class="button" type="button" data-toggle="example-dropdown-right-bottom">Toggle Dropdown</button>
    <div class="dropdown-pane" data-position="right" data-alignment="bottom" id="example-dropdown-right-bottom" data-dropdown data-auto-focus="true">
    </div>

    <!-- Left Bottom -->
    <button class="button" type="button" data-toggle="example-dropdown-left-bottom">Toggle Dropdown</button>
    <div class="dropdown-pane" data-position="left" data-alignment="bottom" id="example-dropdown-left-bottom" data-dropdown data-auto-focus="true">
    </div>
    ```

    <div class="grid-container">
      <div class="grid-x grid-margin-x small-up-1 medium-up-2">
        <div class="cell">
          <p>Right Top</p>
          <button class="button" type="button" data-toggle="example-dropdown-right-top">Toggle Dropdown</button>
          <div class="dropdown-pane" data-position="right" data-alignment="top" id="example-dropdown-right-top" data-dropdown data-auto-focus="true">
            <p>This dropdown has position right and alignment top should align with its top left corner at the top right of the button</p>
          </div>
        </div>
        <div class="cell">
          <p>Left Top</p>
          <button class="button" type="button" data-toggle="example-dropdown-left-top">Toggle Dropdown</button>
          <div class="dropdown-pane" data-position="left" data-alignment="top" id="example-dropdown-left-top" data-dropdown data-auto-focus="true">
            <p>This dropdown has position left and alignment top should align with its top right corner at the top left of the button</p>
          </div>
        </div>
        <div class="cell">
          <p>Right Center</p>
          <button class="button" type="button" data-toggle="example-dropdown-right-center">Toggle Dropdown</button>
          <div class="dropdown-pane" data-position="right" data-alignment="center" id="example-dropdown-right-center" data-dropdown data-auto-focus="true">
            <p>This dropdown has position right and alignment center should align to the right of the button with the center of the dropdown vertically aligned with the center of the button</p>
          </div>
        </div>
        <div class="cell">
          <p>Left Center</p>
          <button class="button" type="button" data-toggle="example-dropdown-left-center">Toggle Dropdown</button>
          <div class="dropdown-pane" data-position="left" data-alignment="center" id="example-dropdown-left-center" data-dropdown data-auto-focus="true">
            <p>This dropdown has position left and alignment center should align to the left of the button with the center of the dropdown vertically aligned with the center of the button</p>
          </div>
        </div>
        <div class="cell">
          <p>Right Bottom</p>
          <button class="button" type="button" data-toggle="example-dropdown-right-bottom">Toggle Dropdown</button>
          <div class="dropdown-pane" data-position="right" data-alignment="bottom" id="example-dropdown-right-bottom" data-dropdown data-auto-focus="true">
            <p>This dropdown has position right and alignment bottom should align with its bottom left corner at the bottom right of the button</p>
          </div>
        </div>
        <div class="cell">
          <p>Left Bottom</p>
          <button class="button" type="button" data-toggle="example-dropdown-left-bottom">Toggle Dropdown</button>
          <div class="dropdown-pane" data-position="left" data-alignment="bottom" id="example-dropdown-left-bottom" data-dropdown data-auto-focus="true">
            <p>This dropdown has position left and alignment bottom should align with its bottom right corner at the bottom left of the button</p>
          </div>
        </div>
      </div>
    </div>"""

    pass


class EQUALIZER:
    """---
    title: Equalizer
    description: Equalizer makes it dead simple to give multiple items equal height.
    video: KbruAemirVQ
    js: js/foundation.equalizer.js
    ---

    ## Basics

    To set up an Equalizer group, you need a container, which gets the attribute `data-equalizer`, and then a series of child elements, which get the attribute `data-equalizer-watch`. The child elements will all be resized to have the same height.

    <p>
      <a class="" data-open-video="0:47"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/colin-marshall/pen/BryEYL?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-margin-x" data-equalizer data-equalize-on="medium" id="test-eq">
      <div class="cell medium-4">
        <div class="callout" data-equalizer-watch>
          <img src= "assets/img/generic/square-1.jpg">
        </div>
      </div>
      <div class="cell medium-4">
        <div class="callout" data-equalizer-watch>
          <p>Pellentesque habitant morbi tristique senectus et netus et, ante.</p>
        </div>
      </div>
      <div class="cell medium-4">
        <div class="callout" data-equalizer-watch>
          <img src= "assets/img/generic/rectangle-1.jpg">
        </div>
      </div>
    </div>
    ```

    ---

    ## Nesting

    To use one Equalizer inside another, each container needs a unique ID, assigned with the `data-equalizer` attribute. Each `data-equalizer-watch` element should then have a value that matches its parent.

    In the below example, the first set of Equalizer elements have the value `foo`, while the inside elements have the value `bar`. In the live example, we've also set the `equalizeOn` option to 'medium' for the parent elements, and the child Equalizer contained in the first div equalizes on stack, and maintains equal height.

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/colin-marshall/pen/oqgOoR?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x" data-equalizer="foo">
      <div class="cell medium-4" data-equalizer-watch="foo">
        <div class="callout" data-equalizer-watch="foo" data-equalizer="bar">
          <h3>Parent panel</h3>
          <div class="callout" data-equalizer-watch="bar"></div>
          <div class="callout" data-equalizer-watch="bar"></div>
          <div class="callout" data-equalizer-watch="bar"></div>
        </div>
      </div>
      <div class="cell medium-4">
        <div class="callout panel" data-equalizer-watch="foo"></div>
      </div>
      <div class="cell medium-4">
        <div class="callout" data-equalizer-watch="foo"></div>
      </div>
    </div>
    ```

    <div class="grid-x grid-margin-x"  data-equalize-on="medium" data-equalizer="foo">
      <div class="cell medium-4" >
        <div class="callout" data-equalizer-watch="foo" data-equalizer="bar" data-equalize-on-stack="true">
          <h3>Parent panel</h3>
          <div class="callout" data-equalizer-watch="bar">
            <p>The three callouts in this panel will equalize, even when stacked.</p>
          </div>
          <div class="callout" data-equalizer-watch="bar">
            <p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante.</p>
          </div>
          <div class="callout" data-equalizer-watch="bar">
            <p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante.</p>
          </div>
        </div>
      </div>
      <div class="cell medium-4">
        <div class="callout panel" data-equalizer-watch="foo">
          <p>Where these panels will not equalize on stack, and instead equalize on medium up.</p>
        </div>
      </div>
      <div class="cell medium-4">
        <div class="callout" data-equalizer-watch="foo">
          <p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante.</p>
        </div>
      </div>
    </div>

    ---

    ## Equalize By Row

    If you have a gallery of items that wrap multiple times, Equalizer can be configured to match each row's items in height. Works great with the block grid!

    <a class="" data-open-video="4:24"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>

    <div class="callout primary">
      <p><strong>Under the Hood:</strong></p>
      <p>Equalizer splits the `data-equalizer-watch` elements into groups by checking their vertical offsets, and grouping ones with the same offset into a "row".</p>
      <p>Be aware on what you set `data-equalizer-watch`, if the top position is different, Equalizer will interpret that as a new "row" and equalize accordingly.</p>
    </div>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/colin-marshall/pen/MVYRBG?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-padding-x small-up-1 medium-up-2 large-up-4" data-equalizer data-equalize-by-row="true">
      <div class="cell" data-equalizer-watch></div>
      <div class="cell" data-equalizer-watch></div>
      <div class="cell" data-equalizer-watch></div>
      <!-- ... -->
    </div>
    ```

    <div class="grid-x grid-padding-x small-up-1 medium-up-2 large-up-4" data-equalizer data-equalize-by-row="true">
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <img src="https://placehold.it/180x200" class="thumbnail" alt="">
          <p>Lorem ipsum dolor sit amet<p>
        </div>
      </div>
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <p>Lorem ipsum dolor sit amet<p>
        </div>
      </div>
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <p>Lorem ipsum dolor sit amet<p>
        </div>
      </div>
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <img src="https://placehold.it/180x180" class="thumbnail" alt="">
        </div>
      </div>
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <p>Lorem ipsum dolor sit amet<p>
        </div>
      </div>
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <p>Lorem ipsum dolor sit amet<p>
        </div>
      </div>
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <img src="https://placehold.it/180x400" class="thumbnail" alt="">
        </div>
      </div>
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <img src="https://placehold.it/180x200" class="thumbnail" alt="">
          <p>Lorem ipsum dolor sit amet<p>
        </div>
      </div>
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <p>Lorem ipsum dolor sit amet<p>
        </div>
      </div>
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <p>Lorem ipsum dolor sit amet<p>
        </div>
      </div>
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <img src="https://placehold.it/180x180" class="thumbnail" alt="">
        </div>
      </div>
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <p>Lorem ipsum dolor sit amet<p>
        </div>
      </div>
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <p>Lorem ipsum dolor sit amet<p>
        </div>
      </div>
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <p>Lorem ipsum dolor sit amet<p>
        </div>
      </div>
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <p>Lorem ipsum dolor sit amet<p>
        </div>
      </div>
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <p>Lorem ipsum dolor sit amet<p>
        </div>
      </div>
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <p>Lorem ipsum dolor sit amet<p>
        </div>
      </div>
      <div class="cell">
        <div class="callout" data-equalizer-watch>
          <img src="https://placehold.it/180x400" class="thumbnail" alt="">
        </div>
      </div>
    </div>"""

    pass


class FLEX_GRID:
    """---
    title: Flex Grid
    description: New in Foundation 6 is a Flexbox-powered grid, which you can use instead of the traditional float grid.
    sass: scss/grid/_flex-grid.scss
    video: tpmQcZSPw4Q
    ---

    <!-- <div class="callout training-callout">
      <p>Become a master of the Foundation Grids to create complex layouts faster and with less code. The new XY Grid is the newest and most powerful version. Stay up-to-date with all the new features in Foundation 6.4 and learn how to migrate to the XY Grid with our online webinar training. You’ll also learn all the useful UI components and Foundation JavaScript to really crush your projects.</p>
      <a href="https://zurb.com/university/foundation-intro" target="_blank">Get registered for an upcoming Foundation training →</a>
    </div> -->

    The flex grid works very similarly to the standard float grid, but includes a number of useful features only possible with flexbox, like horizontal and vertical alignment, automatic sizing, and easier source ordering.

    ---

    ## Browser support

    The flex grid is only supported in Chrome, Firefox, Safari 6+, IE10+, iOS 7+, and Android 4.4+. Flexbox is supported in Android 2, but not reliably enough for use with this grid. ([View flexbox browser support.](https://caniuse.com/#feat=flexbox)) We recommend only using the flex grid on projects that can live with purely cutting-edge browser support.

    <div class="callout warning">
      <p>In Firefox 43+, images in flex columns may overflow their container. To fix this, add a defined <code>width</code> to any images inside a flex column, or use <code>width: 100%</code> for full-bleed images.</p>
    </div>

    ---

    ## Importing

    <div class="docs-video-codepen-container">
      <a class="" data-open-video="2:45"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </div>

    <div class="callout alert">
      **From Foundation v6.4, the Flex Grid is disabled by default**, replaced by the new [XY Grid](xy-grid.html). Unless you need to support IE 10, it is recommended to use the XY Grid.
    </div>

    To use the Flex Grid in Foundation v6.4+, you need to:
    * In CDN link or package managers: import `foundation-flex.css` in place of `foundation.css`.
    * In Sass: set `$xy-grid` to `false`.

    If you're using the Sass version of Foundation, you can enable a framework-wide flexbox mode, and add exports for the flex grid and flexbox helper classes. [Learn more about enabling flexbox mode.](flexbox.html#enabling-flexbox-mode)

    You can manually generate the Flex Grid with:
    ```scss
    @import 'foundation';

    // @include foundation-grid;
    @include foundation-flex-classes;
    @include foundation-flex-grid;
    ```

    <div class="callout primary">
      <p>The flex grid uses the same settings variables as the float grid to adjust gutter size, column count, and so on. Refer to the <a href="grid.html#sass-variables">Sass variable reference</a> for the default grid to see how the flex grid can be customized.</p>
    </div>

    <div class="callout warning">
      <p>The standard grid and flex grid use some of the same classes, namely <code>.row</code> and <code>.column</code>, and don't play nice together. If you want to use both in the same project, we recommend using the Sass mixins for each grid, instead of the default CSS.</p>
    </div>

    ---

    ## Basics

    The structure of the flex grid is identical to that of the float grid. Rows use the class `.row`, and columns use the class `.column` (or `.columns`). Basic percentage-based sizing can also be done using the same grid classes you're used to: `.small-6`, `.medium-12`, and so on.

    <p>
      <a class="" data-open-video="6:09"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/dWmVax?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="columns small-6">6 columns</div>
      <div class="columns small-6">6 columns</div>
    </div>
    <div class="row">
      <div class="columns medium-6 large-4">12/6/4 columns</div>
      <div class="columns medium-6 large-8">12/6/8 columns</div>
    </div>
    ```

    ---

    ## Advanced Sizing

    If no sizing class is added to the column, it will simply expand to fill the leftover space. We call this an *expand behavior*.

    <p>
      <a class="" data-open-video="10:29"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/XREzBv?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="columns small-4">4 columns</div>
      <div class="columns">Whatever's left!</div>
    </div>
    ```

    ---

    Multiple expanding columns will share the leftover space equally.

    <p>
      <a class="" data-open-video="11:04"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/pPLdYY?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="columns small-4">4 columns</div>
      <div class="columns">Whatever's left!</div>
      <div class="columns">Whatever's left!</div>
    </div>
    ```

    ---

    A column can also be made to *shrink*, by adding the `.shrink` class. This means it will only take up the horizontal space its contents need.

    <p>
      <a class="" data-open-video="13:34"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/aWYVgd?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="columns shrink">Shrink!</div>
      <div class="columns">Expand!</div>
    </div>
    ```

    ---

    ## Responsive Adjustments

    Columns in a flex grid will not wrap if not given an explicit size&mdash;this is what allows the magical auto-sizing to work. To make columns stack on smaller screens, add the class `.small-12` manually.

    To switch back to the expand behavior from a percentage or shrink behavior, use the classes `.medium-expand` or `.large-expand`. In the below example, the columns stack on small screens, and become even-width on large screens.

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/vmRpBJ?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="columns small-12 large-expand">One</div>
      <div class="columns small-12 large-expand">Two</div>
      <div class="columns small-12 large-expand">Three</div>
      <div class="columns small-12 large-expand">Four</div>
      <div class="columns small-12 large-expand">Five</div>
      <div class="columns small-12 large-expand">Six</div>
    </div>
    ```

    ---

    ### Automatic Stacking

    We have a few shorthand classes for the above behavior. Use the `.[size]-unstack` classes to stack all columns in the row by default, and then unstack them on a larger screen size, making each one equal-width.

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/xdWpER?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row medium-unstack">
      <div class="columns">One</div>
      <div class="columns">Two</div>
      <div class="columns">Three</div>
      <div class="columns">Four</div>
      <div class="columns">Five</div>
      <div class="columns">Six</div>
    </div>
    ```

    ---

    ## Column Alignment

    Columns in a flex grid can be aligned across the horizontal or vertical axis of their parent row.

    ### Horizontal Alignment

    Columns can be aligned the same way you would align text in a paragraph. By default, all columns align to the left (or the right in RTL), but this can be overridden with by adding the `.align-[dir]` class to the flex row.

    <p>
      <a class="" data-open-video="13:32"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">

      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/mmxpGz?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="column small-4">Aligned to</div>
      <div class="column small-4">the left</div>
    </div>
    <div class="row align-right">
      <div class="column small-4">Aligned to</div>
      <div class="column small-4">the right</div>
    </div>
    <div class="row align-center">
      <div class="column small-4">Aligned to</div>
      <div class="column small-4">the middle</div>
    </div>
    <div class="row align-justify">
      <div class="column small-4">Aligned to</div>
      <div class="column small-4">the edges</div>
    </div>
    <div class="row align-spaced">
      <div class="column small-4">Aligned to</div>
      <div class="column small-4">the space around</div>
    </div>
    ```

    <div class="docs-code-live">
      <div class="text-center">
        <div class="row">
          <div class="column small-4">Aligned to</div>
          <div class="column small-4">the left</div>
        </div>
        <div class="row align-right">
          <div class="column small-4">Aligned to</div>
          <div class="column small-4">the right</div>
        </div>
        <div class="row align-center">
          <div class="column small-4">Aligned to</div>
          <div class="column small-4">the middle</div>
        </div>
        <div class="row align-justify">
          <div class="column small-4">Aligned to</div>
          <div class="column small-4">the edges</div>
        </div>
        <div class="row align-spaced">
          <div class="column small-4">Aligned to</div>
          <div class="column small-4">the space around</div>
        </div>
      </div>
    </div>

    You might be wondering what the difference between `.align-justify` and `.align-spaced` is. A justified grid (`justify-content: space-between`) evenly distributes the space *between* each column. The first and last columns pin to the edge of the grid.

    A spaced grid (`justify-content: space-around`) evenly distributes the space *around* each column. This means there will always be space to the left of the first column, and to the right of the last column.

    The horizontal alignment classes are shorthands for the `justify-content` CSS property. [Learn more about `justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content).

    ---

    ### Vertical Alignment

    By default, all columns in a flex grid stretch to be equal height. This behavior can be changed with another set of alignment classes. That's right, *middle alignment in CSS*!

    Your options for vertical alignment are `top`, `middle`, `bottom`, and `stretch`. Note that we use the word *middle* for vertical alignment, and *center* for horizontal alignment.

    Applying a vertical alignment class to the flex row will affect every column directly inside it.

    <p>
      <a class="" data-open-video="13:32"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/BRrYQy?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row align-middle">
      <div class="columns">I'm in the middle!</div>
      <div class="columns">I am as well, but I have so much text I take up more space! Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quis facere ducimus earum minus, inventore, ratione doloremque deserunt neque perspiciatis accusamus explicabo soluta, quod provident distinctio aliquam omnis? Labore, ullam possimus.</div>
    </div>
    ```

    ```html
    <div class="row align-top">
      <div class="columns">These columns align to the top.</div>
      <div class="columns">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatum, tempora. Impedit eius officia possimus laudantium? Molestiae eaque, sapiente atque doloremque placeat! In sint, fugiat saepe sunt dolore tempore amet cupiditate.</div>
    </div>
    ```

    ---

    ### Vertical Alignment of child columns (individually)

    Similar alignment classes can also be applied to individual columns, which use the format `.align-self-*` instead of `.align-*`.

    <a class="" data-open-video="13:32"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>

    <div class="callout warning">
      <p>In Foundation 6.2, we introduced the <code>.align-self-&ast;</code> classes, which replace the old method of using <code>.align-&ast;</code> classes on columns. The old classes have been removed completely in Foundation 6.3.</p>
    </div>


    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/pPLaPe?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="column align-self-bottom">Align bottom</div>
      <div class="column align-self-middle">Align middle</div>
      <div class="column align-self-top">Align top</div>
      <div class="column">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Non harum laborum cum voluptate vel, eius adipisci similique dignissimos nobis at excepturi incidunt fugit molestiae quaerat, consequuntur porro temporibus. Nisi, ex?</div>
    </div>
    ```

    ---

    ## Collapse/Uncollapse Rows

    The `.collapse` class lets you remove column gutters (padding).

    There are times when you won't want each media query to be collapsed or uncollapsed. In this case, use the media query size you want and collapse or uncollapse and add that to your row element. Example shows gutters at small and medium and no gutters on large and up.

    The `.is-collapse-child` class removes negative margins from nested row under collapsed parent.

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/pPLaWP?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row small-collapse medium-uncollapse">
      <div class="columns small-6">
        Removes gutter at small media query and adds at medium.
      </div>
      <div class="columns small-6">
        Removes gutter at small media query and adds at medium.
      </div>
    </div>
    ```

    <p class="lead">Scale the browser down to a medium size to see the difference.</p>

    <div class="row medium-uncollapse large-collapse">
      <div class="columns small-6">
        <div class="callout secondary">
          <p class="show-for-small-only">On a small screen, I have gutters!</p>
          <p class="show-for-medium-only">On a medium screen, I have gutters!</p>
          <p class="show-for-large">On a large screen, I have no gutters!</p>
        </div>
      </div>
      <div class="columns small-6">
        <div class="callout secondary">
          <p class="show-for-small-only">On a small screen, I have gutters!</p>
          <p class="show-for-medium-only">On a medium screen, I have gutters!</p>
          <p class="show-for-large">On a large screen, I have no gutters!</p>
        </div>
      </div>
    </div>

    ---

    ## Offsets

    Offsets work identically to the float grid, by applying `margin-left` to a column.

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/mmxXpb?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="columns small-4 large-offset-2">Offset 2 on large</div>
      <div class="columns small-4">4 columns</div>
    </div>
    ```

    ---

    ## Block Grids

    To define column widths at the row-level, instead of the individual column level, add the class `.[size]-up-[n]` to a row, where `[n]` is the number of columns to display per row, and `[size]` is the breakpoint at which to apply the effect.

    <a class="" data-open-video="27:19"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>

    <div class="callout primary">
      <p>A block grid row has the property <code>align-items: stretch</code> by default, meaning the columns in each row are equal height. To change this, change the <code>align-items</code> property of the row, or use one of the <a href="flexbox.html#vertical-alignment">vertical alignment flexbox classes</a>.</p>
    </div>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/PmRdOy?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row small-up-1 medium-up-2 large-up-3">
      <div class="column">1 per row on small</div>
      <div class="column">2 per row on medium</div>
      <div class="column">3 per row on large</div>
    </div>
    ```"""

    pass


class FLEXBOX_MODE:
    """---
    title: Flexbox Mode
    description: For browsers with cutting-edge support, some of Foundation's key components can be converted to flexbox.
    video: 'KxafSdyTCIg'
    sass:
      - scss/components/_flex.scss
      - scss/util/_flex.scss
    ---

    ## Flexbox Mode

    Foundation components use a combination of floats, vertical alignment, table cells, and various other CSS hacks to get layouts looking right. These days though, there's a better way... if you are happy with the below browser support!

    Enabling **flexbox mode** replaces those hacks with flexbox properties, streamlining how layouts are made, and making sizing and alignment of elements much easier.

    Flexbox mode is only supported in these browsers:

    - The latest Chrome and Firefox
    - Safari 6+
    - IE/Edge 10+
    - iOS 7+
    - Android 4.4+

    ---

    ## Enabling Flexbox Mode

    Using the Sass version of Foundation, you can enable flexbox mode two ways:

    If you use the `foundation-everything()` mixin in your main Sass file, pass in the parameter `true` to enable flexbox mode.

    ```scss
    @include foundation-everything(true);
    ```

    If you included each component manually (like our starter projects do), open your settings file (basic template: scss/_settings.scss, ZURB template: src/assets/scss/_settings.scss) and set `$global-flexbox` to `true`, and remove the `@include` for the float grid and replace it with the one for the flex grid, along with the helper classes (basic template: scss/app.scss, ZURB template: src/assets/scss/app.scss):

    ```scss
    $global-flexbox: true;

    // @include foundation-grid;
    @include foundation-flex-grid;
    @include foundation-flex-classes;
    ```

    ---

    ## Supported Components

    Besides the flex grid, these components have flexbox modes:

    - [Button group](button-group.html)
    - [Input group - (Forms)](forms.html#inline-labels-and-buttons)
    - [Menu](menu.html)
    - [Top bar](top-bar.html)
    - [Media object](media-object.html)
    - [Title bar](off-canvas.html#combining-with-title-bar)
    - [Card](card.html)

    In general, all of the components work exactly the same. However, a few of them require slight changes to CSS classes used to work properly. Refer to the documentation for each to find out what's different.
    """

    pass


class FLEXBOX_UTILITIES:
    """---
    title: Flexbox Utilities
    description: Flexbox utility classes and mixins to make working with flexbox easier.
    video: 'KxafSdyTCIg'
    sass:
      - scss/xy-grid/*.scss
      - scss/components/_flex.scss
      - scss/util/_flex.scss
    ---

    ## Flexbox Utilities

    Flexbox makes horizontal and vertical alignment painless, through the CSS properties [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items), [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/align-self), and [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content). Foundation includes a handful of classes for these properties, which work with any flexbox-enabled component.

    To understand how these classes work, you need to understand the parent-child relationship created with flexbox. An element with `display: flex` is a *flex parent*, and can horizontally or vertically align its children. All immediate children of the flex parent are *flex children*. A flex child can vertically align itself.

    <div class="alert callout">
      <p>In the below examples we are using [XY Grid](xy-grid.html) classes instead of [Legacy Flex Grid's](flex-grid.html) <code>row</code> and <code>column</code>. These examples will work for <code>row</code> and <code>column</code> but then again the Legacy Flex Grid will be deprecated from Foundation 7 so we recommend to use XY Grid.</p>
    </div>

    Here's a basic example: when using the grid, a `grid-x` or `grid-y` is a flex parent, and a `cell` is a flex child. Use `grid-margin-x` or `grid-padding-x` for adding [gutters](xy-grid.html#gutters)

    ```html
    <div class="grid-x grid-padding-x">
      <div class="cell small-4">Cell 1</div>
      <div class="cell small-4">Cell 2</div>
      <div class="cell small-4">Cell 3</div>
    </div>
    ```

    ---

    ### Horizontal Alignment

    Horizontal alignment classes are applied to flex parents. Left alignment is the default, but you can use one of these classes to change this:

    - `.align-right`
    - `.align-center`
    - `.align-justify`
    - `.align-spaced`

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/mwqGLm?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-padding-x"> <!-- Aligned to the left -->
      <div class="cell small-4">Aligned to</div>
      <div class="cell small-4">the left</div>
    </div>
    <div class="grid-x grid-padding-x align-right"> <!-- Aligned to the right -->
      <div class="cell small-4">Aligned to</div>
      <div class="cell small-4">the right</div>
    </div>
    <div class="grid-x grid-padding-x align-center"> <!-- Aligned to the center -->
      <div class="cell small-4">Aligned to</div>
      <div class="cell small-4">the center</div>
    </div>
    <div class="grid-x grid-padding-x align-justify"> <!-- Aligned to the edges -->
      <div class="cell small-4">Aligned to</div>
      <div class="cell small-4">the edges</div>
    </div>
    <div class="grid-x grid-padding-x align-spaced"> <!-- Aligned to the space around -->
      <div class="cell small-4">Aligned to</div>
      <div class="cell small-4">the space around</div>
    </div>
    ```

    You might be wondering what the difference between `.align-justify` and `.align-spaced` is. A justified grid (`justify-content: space-between`) evenly distributes the space *between* each column. The first and last columns pin to the edge of the grid.

    A spaced grid (`justify-content: space-around`) evenly distributes the space *around* each column. This means there will always be space to the left of the first column, and to the right of the last column.

    The horizontal alignment classes are shorthands for the `justify-content` CSS property. [Learn more about `justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content).

    ---

    ### Vertical Alignment

    Vertical alignment can be applied to a flex parent&mdash;which will align all the children automatically&mdash;or to a flex child, which will align only that element.

    Stretch alignment is the default. To set parent alignment, use these classes:

    - `.align-top`
    - `.align-middle`
    - `.align-bottom`
    - `.align-stretch`

    <div class="primary callout">
      <p>Note that with vertical alignment, we use the term "middle" for the midpoint, while with horizontal alignment, we use the term "center". As we can't have two CSS classes with the same name, thus we are using different terms.</p>
    </div>

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/LLOgYx?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-padding-x align-top">
      <div class="cell small-4">I'm at the top (default)</div>
      <div class="cell small-4">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatum, tempora. Impedit eius officia possimus laudantium? Molestiae eaque, sapiente atque doloremque placeat! In sint, fugiat saepe sunt dolore tempore amet cupiditate.</div>
    </div>
    ```

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/vZWVOW?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-padding-x align-middle">
      <div class="cell small-4">I'm in the middle</div>
      <div class="cell small-4">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatum, tempora. Impedit eius officia possimus laudantium? Molestiae eaque, sapiente atque doloremque placeat! In sint, fugiat saepe sunt dolore tempore amet cupiditate.</div>
    </div>
    ```

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/awVRvZ?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-padding-x align-bottom">
      <div class="cell small-4">I'm at the bottom</div>
      <div class="cell small-4">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatum, tempora. Impedit eius officia possimus laudantium? Molestiae eaque, sapiente atque doloremque placeat! In sint, fugiat saepe sunt dolore tempore amet cupiditate.</div>
    </div>
    ```

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/wePYKY?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-padding-x align-stretch">
      <div class="cell small-4">These cells have the same height</div>
      <div class="cell small-4">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatum, tempora. Impedit eius officia possimus laudantium? Molestiae eaque, sapiente atque doloremque placeat! In sint, fugiat saepe sunt dolore tempore amet cupiditate.</div>
    </div>
    ```

    ---

    To align an individual child, use the below classes. They use the same alignment terms as the parent-level classes, but the classes start with `.align-self-` instead of `.align-`.

    - `.align-self-top`
    - `.align-self-middle`
    - `.align-self-bottom`
    - `.align-self-stretch`

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/NgwOxe?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-padding-x">
        <div class="cell small-3 align-self-bottom"><div class="demo">Align bottom</div></div>
        <div class="cell small-3 align-self-middle"><div class="demo">Align middle</div></div>
        <div class="cell small-3 align-self-stretch"><div class="demo">Align stretch</div></div>
        <div class="cell small-3 align-self-top"><div class="demo">Align top. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Non harum laborum cum voluptate vel, eius adipisci similique dignissimos nobis at excepturi incidunt fugit molestiae quaerat, consequuntur porro temporibus. Nisi, ex?</div></div>
      </div>
    ```

    ---

    ### Central Alignment

    Central alignment can be applied to a flex parent, which will centrally align all children horizontally and vertically automatically. To set this to your layout, simply use the class: `.align-center-middle`.

    <div class="primary callout">
      <p>We are using `.text-center` class just for demo purposes here.</p>
    </div>

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/vZWVXp?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-padding-x align-center-middle text-center" style="height: 200px;">
      <div class="cell small-4">I am in the center-middle</div>
      <div class="cell small-4">I am also centrally located</div>
    </div>
    ```

    ---

    ## Vanilla Flexbox Helper Classes

    Foundation also includes some helper classes for quickly applying flex
    container & direction attributes to elements.

    To make something a flex container, simply apply
    - `.flex-container`

    And to change its flex direction from row to column you can use the helper classes:

    - `.flex-dir-row` (default)
    - `.flex-dir-row-reverse`
    - `.flex-dir-column`
    - `.flex-dir-column-reverse`

    For children, there are 3 quick helper classes to apply the flex property. These control how the containers take up space relative to their siblings:

    - `.flex-child-auto` (auto size flex child)
    - `.flex-child-grow` (flex child that will grow to take up all possible space)
    - `.flex-child-shrink` (flex child that will shrink to minimum possible space)

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/bRYmRZ?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-padding-x">
      <div class="cell small-4 flex-container flex-dir-column">
        <div class="callout primary flex-child-auto">Auto</div>
        <div class="callout primary flex-child-auto">Auto</div>
        <div class="callout primary flex-child-shrink">Shrink</div>
      </div>
      <div class="cell small-4">
      </div>
      <div class="cell small-4 align-self-top">Align top. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Non harum laborum cum voluptate vel, eius adipisci similique dignissimos nobis at excepturi incidunt fugit molestiae quaerat, consequuntur porro temporibus. Nisi, ex?Align top. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Non harum laborum cum voluptate vel, eius adipisci similique dignissimos nobis at excepturi incidunt fugit molestiae quaerat, consequuntur porro temporibus. Nisi, ex?Align top. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Non harum laborum cum voluptate vel, eius adipisci similique dignissimos nobis at excepturi incidunt fugit molestiae quaerat, consequuntur porro temporibus. Nisi, ex?</div>
    </div>
    ```

    ### Responsive Classes

    All of these helper classes come in responsive varieties, prefixed with all of your named breakpoints.

    These vanilla flexbox helper classes also have an optional mobile first responsive classes so that setting a class will apply to the small breakpoint and large unless overridden by a class for a larger breakpoint.. Example: `class="flex-child-shrink large-flex-child-auto"` will be shrink on the small and medium breakpoints and then auto on large.

    These optional responsive classes can be disabled by setting `$flexbox-responsive-breakpoints` to `false`. See [here](#sass-variables)

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/yXPRjY?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-padding-x">
      <div class="cell small-12 flex-container flex-dir-column large-flex-dir-row">
        <div class="callout primary flex-child-auto">Auto</div>
        <div class="callout primary flex-child-auto">Auto</div>
        <div class="callout primary flex-child-shrink large-flex-child-auto">Auto on Large</div>
      </div>
      <div class="cell small-12 align-self-top">Align top. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Non harum laborum cum voluptate vel, eius adipisci similique dignissimos nobis at excepturi incidunt fugit molestiae quaerat, consequuntur porro temporibus. Nisi, ex?Align top. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Non harum laborum cum voluptate vel, eius adipisci similique dignissimos nobis at excepturi incidunt fugit molestiae quaerat, consequuntur porro temporibus. Nisi, ex?Align top. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Non harum laborum cum voluptate vel, eius adipisci similique dignissimos nobis at excepturi incidunt fugit molestiae quaerat, consequuntur porro temporibus. Nisi, ex?</div>
    </div>
    ```

    ---

    ## Source Ordering

    Flexbox supports source ordering, making it easy to rearrange columns on different screen sizes without weird relative positioning tricks.

    The CSS property is easy enough to remember.

    ```scss
    .element {
      order: 1;
    }
    ```

    Columns within a row will be sorted by their `order` property. Lower numbers are placed first. If multiple columns have the same number, they're sorted in the order they appear in the HTML.

    We have a set of classes that make it easy to setup source ordering in your HTML. They also come in responsive flavors, allowing you to reorder a grid on different screen sizes.

    <p>
      <a class="" data-open-video="27:19"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/ZyaqNL?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-padding-x">
      <div class="cell small-6 small-order-2 medium-order-1">
        This column will come second on small, and first on medium and larger.
      </div>
      <div class="cell small-6 small-order-1 medium-order-2">
        This column will come first on small, and second on medium and larger.
      </div>
    </div>
    ```

    ---

    ## Helper Mixins

    If you're using the Sass version of Foundation, you can access the above helpers as mixins as well.

    For parent-level alignment, use `flex-align()`. You can pass in a horizontal alignment (`$x`), vertical alignment (`$y`), or both.

    ```scss
    .container {
      @include flex-align($x: center, $y: stretch);
    }
    ```

    For child-level alignment, use `flex-align-self()`. You can pass in any vertical alignment.

    ```scss
    .sidebar {
      @include flex-align-self(bottom);
    }
    ```

    Interested in building your own flexbox-ey component? Use the `flex()` mixin to get started.

    ```scss
    .flexish-thang {
      @include flex;
      @include flex-align(center, middle);
    }
    ```"""

    pass


class FLOAT_CLASSES:
    """---
    title: Float Classes
    description: Foundation includes a handful of helpful float classes to add common positioning behaviors to elements.
    video: 'VEzXdMmqhAY'
    ---

    ## Float Left/Right

    You can change the float behavior of an element by adding the `.float-left` or `.float-right` classes to an element. To clear floats, add the class `.clearfix` to the parent element.

    <div class="callout primary">
      <p>Float Left/Right classes use `!important` to ensure they aren't overridden by more specific selectors. This framework conscientiously avoids using `!important` declarations. This is one of the few components that does.</p>
    </div>

    <div class="callout warning">
      <p>Float classes don't flip direction in a <a href="rtl.html">right-to-left</a> environment&mdash;<code>left</code> always means left, and <code>right</code> always means right.</p>
    </div>

    ```html
    <div class="callout clearfix">
      <a class="button float-left">Left</a>
      <a class="button float-right">Right</a>
    </div>
    ```

    ---

    ## Float Center

    Okay, it's not *really* a float, but you can add the `.float-center` class to an element to engage the automatic margin centering trick. Note that this will only work on elements with an absolute width, which means not a percentage or `auto` width.

    ```html
    <img src="assets/img/generic/voyager.jpg" class="float-center">
    ```"""

    pass


class FORMS:
    """---
    title: Forms
    description: We set out to create an easy, powerful and versatile form layout system. A combination of form styles and the Foundation grid means you can do almost anything.
    video: 'pJDXFNJ2jkA'
    sass:
      - scss/forms/*.scss
      - '!scss/forms/_error.scss'
    tags:
      - input
      - select
      - radio
      - checkbox
    flex: true
    ---

    <!-- <div class="callout training-callout">
      <p>Learn the right way to tackle your project and at same time saving time and money. We offer in depth online webinars for you to gain the skills to become a Foundation front-end master.</p>
      <a href="https://zurb.com/university/foundation-intro" target="_blank">Check out our upcoming training opportunities →</a>
    </div> -->

    ## Form Basics

    Creating a form in Foundation is designed to be easy but extremely flexible. Forms are built with a combination of standard form elements, as well as grid rows and columns or cells.

    ---

    #### Text Inputs

    These input types create a text field: `text`, `date`, `datetime`, `datetime-local`, `email`, `month`, `number`, `password`, `search`, `tel`, `time`, `url`, and `week`.

    <p>
      <a class="" data-open-video="0:38"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/wdmQrr?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html

    <form>
      <div class="grid-container">
        <div class="grid-x grid-padding-x">
          <div class="medium-6 cell">
            <label>Input Label
              <input type="text" placeholder=".medium-6.cell">
            </label>
          </div>
          <div class="medium-6 cell">
            <label>Input Label
              <input type="text" placeholder=".medium-6.cell">
            </label>
          </div>
        </div>
      </div>
    </form>
    ```

    ---

    #### Number Inputs

    In most desktop browsers, `<input type="number">` elements will have up/down controls inside them, which increment and decrement the number inside the field. These are called *spin buttons*. You can disable them by setting the `$input-number-spinners` Sass variable to `false`.

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/WjzYJJ?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <label>
      How many puppies?
      <input type="number" value="100">
    </label>
    ```

    ---

    #### Text Areas

    The `<textarea>` element creates a multi-line text input.

    <p>
      <a class="" data-open-video="5:20"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/rmdQrg?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <label>
      What books did you read over summer break?
      <textarea placeholder="None"></textarea>
    </label>
    ```

    ---

    #### Select Menus

    Use select menus to combine many choices into one menu.

    <p>
      <a class="" data-open-video="7:27"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/XREyxv?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <label>Select Menu
      <select>
        <option value="husker">Husker</option>
        <option value="starbuck">Starbuck</option>
        <option value="hotdog">Hot Dog</option>
        <option value="apollo">Apollo</option>
      </select>
    </label>
    ```

    Add the `multiple` attribute to allow more than one option to be selected. Hold down the Ctrl (windows) / Command (Mac) button to select multiple options.

    ```html
    <label>Multiple Select Menu
      <select multiple>
        <option value="showboat">Showboat</option>
        <option value="redwing">Redwing</option>
        <option value="narcho">Narcho</option>
        <option value="hardball">Hardball</option>
      </select>
    </label>
    ```

    ---

    #### Checkboxes and Radio Buttons

    Use groups of checkboxes when the user may select multiple choices from a list, and use radio buttons when the user must select just one choice.

    Wrap a group of checkboxes or radio buttons in a `<fieldset>` element, and give them a common label using the `<legend>` element. Each individual control should also have its own label, created using a typical `<label>`.

    <p>
      <a class="" data-open-video="9:03"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/Omvadz?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-padding-x">
      <fieldset class="large-5 cell">
        <legend>Choose Your Favorite</legend>
        <input type="radio" name="pokemon" value="Red" id="pokemonRed" required><label for="pokemonRed">Red</label>
        <input type="radio" name="pokemon" value="Blue" id="pokemonBlue"><label for="pokemonBlue">Blue</label>
        <input type="radio" name="pokemon" value="Yellow" id="pokemonYellow"><label for="pokemonYellow">Yellow</label>
      </fieldset>
      <fieldset class="large-7 cell">
        <legend>Check these out</legend>
        <input id="checkbox1" type="checkbox"><label for="checkbox1">Checkbox 1</label>
        <input id="checkbox2" type="checkbox"><label for="checkbox2">Checkbox 2</label>
        <input id="checkbox3" type="checkbox"><label for="checkbox3">Checkbox 3</label>
      </fieldset>
    </div>
    ```

    ---

    #### Fieldset Styles

    To encourage their use as an accessibility tool, the `<fieldset>` element is no longer styled by default. Those styles are now contained in the `.fieldset` class.

    <p>
      <a class="" data-open-video="9:03"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/XREyxv?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <fieldset class="fieldset">
      <legend>Check these out</legend>
      <input id="checkbox12" type="checkbox"><label for="checkbox12">Checkbox 1</label>
      <input id="checkbox22" type="checkbox"><label for="checkbox22">Checkbox 2</label>
      <input id="checkbox32" type="checkbox"><label for="checkbox32">Checkbox 3</label>
    </fieldset>
    ```

    ---

    ## Help Text (Accessibility)

    Place help text below a field to clarify its purpose. Whenever you use help text, give the text a unique ID, and add the attribute `aria-describedby` to the input. Doing so associates the helper text to the input. A screen reader then can read the helper text when the user focusses on the input.

    <p>
      <a class="" data-open-video="11:19"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/wdmOqr?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <label>Password
      <input type="password" aria-describedby="passwordHelpText">
    </label>
    <p class="help-text" id="passwordHelpText">Your password must have at least 10 characters, a number, and an Emoji.</p>
    ```

    ---

    ## Label Positioning

    Sometimes you want a form with labels to the left of your inputs. Piece of cake! You can put the label inside a different cell or column to the left of the input. Then use the class `.text-right` or `.float-right` (or add `text-align: right` yourself) to realign the label.

    <a class="" data-open-video="12:00"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    <div class="warning callout">
      <p>In a <a href="rtl.html">right-to-left</a> environment, use <code>.float-left</code> instead.</p>
    </div>

    <div class="docs-video-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/eWMXex?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <form>
      <div class="grid-x grid-padding-x">
        <div class="small-3 cell">
          <label for="right-label" class="text-right">Label</label>
        </div>
        <div class="small-9 cell">
          <input type="text" id="right-label" placeholder="Right-aligned text input">
        </div>
      </div>
    </form>
    ```

    <div class="medium-8 grid-x grid-padding-x cell align-center">
      <div class="grid-x grid-padding-x">
        <div class="small-3 cell">
          <label for="right-label" class="text-right">Label</label>
        </div>
        <div class="small-9 cell">
          <input type="text" id="right-label" placeholder="Right-aligned text input">
        </div>
      </div>
    </div>

    ---

    Add the `.middle` class to vertically align the label with its input.

    ```html
    <form>
      <div class="grid-x grid-padding-x">
        <div class="small-3 cell">
          <label for="middle-label" class="text-right middle">Label</label>
        </div>
        <div class="small-9 cell">
          <input type="text" id="middle-label" placeholder="Right- and middle-aligned text input">
        </div>
      </div>
    </form>
    ```

    <div class="medium-8 grid-x grid-padding-x cell align-center">
      <div class="grid-x grid-padding-x">
        <div class="small-3 cell">
          <label for="middle-label" class="text-right middle">Label</label>
        </div>
        <div class="small-9 cell">
          <input type="text" id="middle-label" placeholder="Right- and middle-aligned text input">
        </div>
      </div>
    </div>

    ---

    ## Inline Labels and Buttons

    To attach extra text or controls to the left or right of an input field, wrap the elements in an `.input-group` container, then add these classes to the elements inside:

    - `.input-group-field` on the text field.
    - `.input-group-label` on a text label.
    - `.input-group-button` on a button. **Place the button inside this wrapper.**

    <a class="" data-open-video="14:53"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    <div class="primary callout">
      <p>This component supports flexbox mode. <a href="flexbox.html">Learn how to enable flexbox mode</a>.</p>
    </div>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/rmdRqg?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="input-group">
      <span class="input-group-label">$</span>
      <input class="input-group-field" type="number">
      <div class="input-group-button">
        <input type="submit" class="button" value="Submit">
      </div>
    </div>
    ```

    ---

    ## File Upload Button

    Use `<input type="file">` to create a file upload button. For security reasons, most browsers don't let you style file inputs. To work around that, we can style a form label as a button, and point it to the `<input>`. To properly mask the input, the `.show-for-sr` class is added.

    <p>
      <a class="" data-open-video="17:45"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/NjYJZB?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <label for="exampleFileUpload" class="button">Upload File</label>
    <input type="file" id="exampleFileUpload" class="show-for-sr">
    ```

    ---

    ## Custom Controls (Accessibility)

    Custom form controls, like date pickers, range sliders, or switches need some extra attention to be made accessible. Our custom inputs, such as the range slider and switch, do most of this work for you.

    Custom inputs with labels or help text need the attributes `aria-labelledby` and `aria-describedby` added to them, so screen readers know how to describe the control.

    ```html
    <label id="ageLabel">Age</label>
    <div class="slider" aria-labelledby="ageLabel" aria-describedby="ageHelpText" data-slider data-initial-start="50" data-end="200">
      <span class="slider-handle"  data-slider-handle role="slider" tabindex="1"></span>
      <span class="slider-fill" data-slider-fill></span>
      <input type="hidden">
    </div>
    <p id="ageHelpText">How old are you?</p>
    ```"""

    pass


class GLOBAL:
    """---
    title: Global Styles
    description: Our global CSS includes helpful resets to ensure consistent styling across browsers.
    video: 'nEgHk2wmMjU'
    sass: scss/_global.scss
    ---

    ## Font Sizing

    The default font size is set to 100% of the browser style sheet, usually 16 pixels. This ensures compatibility with browser-based text zoom or user-set defaults. If you're using the Sass version of Foundation, edit the `$global-font-size` variable to change the base font size. This can be a percentage value, or a pixel value.

    ---

    ## Colors

    Foundation has an accessible default color palette. The primary color is used for interactive elements, such as links and buttons. The secondary, success, warning, and alert colors are used to give more context to UI elements and actions.

    <div class="grid-x grid-margin-x small-up-1 medium-up-3 large-up-5">
      <div class="cell">
        <div class="docs-color-block">
          <div class="docs-color-block-primary"></div>
          <p>Primary</p>
        </div>
      </div>
      <div class="cell">
        <div class="docs-color-block">
          <div class="docs-color-block-secondary"></div>
          <p>Secondary</p>
        </div>
      </div>
      <div class="cell">
        <div class="docs-color-block">
          <div class="docs-color-block-success"></div>
          <p>Success</p>
        </div>
      </div>
      <div class="cell">
        <div class="docs-color-block">
          <div class="docs-color-block-warning"></div>
          <p>Warning</p>
        </div>
      </div>
      <div class="cell">
        <div class="docs-color-block">
          <div class="docs-color-block-alert"></div>
          <p>Alert</p>
        </div>
      </div>
      <div class="cell">
        <div class="docs-color-block">
          <div class="docs-color-block-white"></div>
          <p>White</p>
        </div>
      </div>
      <div class="cell">
        <div class="docs-color-block">
          <div class="docs-color-block-light-gray"></div>
          <p>Light Gray</p>
        </div>
      </div>
      <div class="cell">
        <div class="docs-color-block">
          <div class="docs-color-block-medium-gray"></div>
          <p>Medium Gray</p>
        </div>
      </div>
      <div class="cell">
        <div class="docs-color-block">
          <div class="docs-color-block-dark-gray"></div>
          <p>Dark Gray</p>
        </div>
      </div>
      <div class="cell">
        <div class="docs-color-block">
          <div class="docs-color-block-black"></div>
          <p>Black</p>
        </div>
      </div>
    </div>

    ---

    ### Changing the Color Palette

    If you're using the Sass version of Foundation, you can easily change the color palette by editing the variables in your settings file.

    The semantic colors (primary, secondary, success, warning, and alert) can be changed in the `$foundation-palette` map. The keys in this map are referenced by various settings to style components and output alternate class names.

    ```scss
    $foundation-palette: (
      "primary": #1779ba,
      "secondary": #767676,
      "success": #3adb76,
      "warning": #ffae00,
      "alert": #cc4b37,
    );
    ```

    <div class="warning callout">
      <p>If you remove a default key from `$foundation-palette`, be sure to edit any variables in your settings file that reference that color.</p>
    </div>

    The named colors (white, light gray, medium gray, dark gray, and black) can be changed in their respective variables

    ```scss
    $light-gray: #e6e6e6;
    $medium-gray: #cacaca;
    $dark-gray: #8a8a8a;
    $black: #0a0a0a;
    $white: #fefefe;
    ```

    The line `@include add-foundation-colors;` in your settings file allows you to use the following Sass variables to reference *default colors* from the palette:

    - `$primary-color`
    - `$secondary-color`
    - `$success-color`
    - `$warning-color`
    - `$alert-color`

    You can also use Foundation's `get-color()` function to reference *any color* from the palette. This function gives you access to custom colors you've added to the palette.

    ```scss
    // Create a variable for my custom color.
    $custom-color: get-color(custom);
    ```"""

    pass


class GRID:
    """---
    title: The Grid
    description: Create powerful multi-device layouts quickly and easily with the default 12-column, nestable Foundation grid. If you're familiar with grid systems, you'll feel right at home. If not, you'll learn quickly.
    video: k1zizfK2xbQ
    sass:
      - scss/grid/*.scss
      - '!scss/grid/_flex-grid.scss'
    tags:
      - block grid
    ---

    <!-- <div class="callout training-callout">
      <p>Become a master of the Foundation Grids to create complex layouts faster and with less code. The new XY Grid is the newest and most powerful version. Stay up-to-date with all the new features in Foundation 6.4 and learn how to migrate to the XY Grid with our online webinar training. You’ll also learn all the useful UI components and Foundation JavaScript to really crush your projects.</p>
      <a href="https://zurb.com/university/foundation-intro" target="_blank">Get registered for an upcoming Foundation training →</a>
    </div> -->


    ## Importing

    <div class="callout alert">
      **From Foundation v6.4, the Float Grid is disabled by default**, replaced by the new [XY Grid](xy-grid.html). Unless you need to support IE 10, it is recommended to use the XY Grid.
    </div>

    To use the Float Grid in Foundation v6.4+, you need to:
    * In CDN link or package managers: import `foundation-float.css` in place of `foundation.css`.
    * In Sass: set both `$xy-grid` and `$global-flexbox` to `false`.


    ## Basics

    Start by adding an element with a class of `.row`. This will create a horizontal block to contain vertical columns. Then add elements with a `.column` class within that row. Specify the widths of each column with the `.small-#`, `.medium-#`, and `.large-#` classes.

    **Foundation is mobile-first.** Code for small screens first, and larger devices will inherit those styles. Customize for larger screens as necessary.

    <p>
      <a class="" data-open-video="1:07"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="callout primary">
      <p>By default `.column` has an alias `.columns` (see the <a href="#sass-reference">`$grid-column-alias` option</a>) &mdash;the only difference is grammar.</p>
      <p>Disabling the alias can reduce the Foundation CSS file size from 3 to 5%. It is recommended if the alias is not used.</p>
    </div>

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/ZKrdZz?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="columns small-2 large-4"><!-- ... --></div>
      <div class="columns small-4 large-4"><!-- ... --></div>
      <div class="columns small-6 large-4"><!-- ... --></div>
    </div>
    <div class="row">
      <div class="columns large-3"><!-- ... --></div>
      <div class="columns large-6"><!-- ... --></div>
      <div class="columns large-3"><!-- ... --></div>
    </div>
    <div class="row">
      <div class="columns small-6 large-2"><!-- ... --></div>
      <div class="columns small-6 large-8"><!-- ... --></div>
      <div class="columns small-12 large-2"><!-- ... --></div>
    </div>
    <div class="row">
      <div class="columns small-3"><!-- ... --></div>
      <div class="columns small-9"><!-- ... --></div>
    </div>
    <div class="row">
      <div class="columns large-4"><!-- ... --></div>
      <div class="columns large-8"><!-- ... --></div>
    </div>
    <div class="row">
      <div class="columns small-6 large-5"><!-- ... --></div>
      <div class="columns small-6 large-7"><!-- ... --></div>
    </div>
    <div class="row">
      <div class="columns large-6"><!-- ... --></div>
      <div class="columns large-6"><!-- ... --></div>
    </div>
    ```

    <div class="row display">
      <div class="columns small-2 large-4"><span class="hide-for-large">2</span><span class="show-for-large">4</span></div>
      <div class="columns small-4 large-4">4</div>
      <div class="columns small-6 large-4"><span class="hide-for-large">6</span><span class="show-for-large">4</span></div>
    </div>
    <div class="row display">
      <div class="columns large-3"><span class="hide-for-large">full</span><span class="show-for-large">3</span></div>
      <div class="columns large-6"><span class="hide-for-large">full</span><span class="show-for-large">6</span></div>
      <div class="columns large-3"><span class="hide-for-large">full</span><span class="show-for-large">3</span></div>
    </div>
    <div class="row display">
      <div class="columns small-6 large-2"><span class="hide-for-large">6</span><span class="show-for-large">2</span></div>
      <div class="columns small-6 large-8"><span class="hide-for-large">6</span><span class="show-for-large">8</span></div>
      <div class="columns small-12 large-2"><span class="hide-for-large">full</span><span class="show-for-large">2</span></div>
    </div>
    <div class="row display">
      <div class="columns small-3">3</div>
      <div class="columns small-9">9</div>
    </div>
    <div class="row display">
      <div class="columns large-4"><span class="hide-for-large">full</span><span class="show-for-large">4</span></div>
      <div class="columns large-8"><span class="hide-for-large">full</span><span class="show-for-large">8</span></div>
    </div>
    <div class="row display">
      <div class="columns small-6 large-5"><span class="hide-for-large">6</span><span class="show-for-large">5</span></div>
      <div class="columns small-6 large-7"><span class="hide-for-large">6</span><span class="show-for-large">7</span></div>
    </div>
    <div class="row display">
      <div class="columns large-6"><span class="hide-for-large">full</span><span class="show-for-large">6</span></div>
      <div class="columns large-6"><span class="hide-for-large">full</span><span class="show-for-large">6</span></div>
    </div>

    ---

    ### Small Grids

    Small grids expand to large screens easier than large grids cram into small screens.

    <p>
    <a class="" data-open-video="9:14"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/oWEKXw?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="columns small-2">2</div>
      <div class="columns small-10">10</div>
    </div>
    <div class="row">
      <div class="columns small-3">3</div>
      <div class="columns small-9">9</div>
    </div>
    ```

    <div class="row display">
      <div class="columns small-2">2</div>
      <div class="columns small-10">10</div>
    </div>
    <div class="row display">
      <div class="columns small-3">3</div>
      <div class="columns small-9">9</div>
    </div>

    ---

    ### Medium Grid

    Medium sized screens will inherit styles from small, unless you specify a different layout using the medium grid classes.

    <p>
      <a class="" data-open-video="11:44"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/vmdoxj?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="columns medium-2">2</div>
      <div class="columns medium-10">10</div>
    </div>
    <div class="row">
      <div class="columns medium-3">3</div>
      <div class="columns medium-9">9</div>
    </div>
    ```

    <div class="row display">
      <div class="columns medium-2">2</div>
      <div class="columns medium-10">10</div>
    </div>
    <div class="row display">
      <div class="columns medium-3">3</div>
      <div class="columns medium-9">9</div>
    </div>

    ---

    ## Advanced

    ### Combined Column/Row

    If you have just a single column, you can save some markup by combining the `.row` and `.column` classes together on the same element. You can still nest more grids inside this container like usual.

    <div class="callout warning">
      <p>Column rows can use sizing classes like <code>.small-8</code>, but only when used as a top-level container&mdash;not when nested inside another row.</p>
    </div>

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/ZKrgop?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="column row">
      Row column
    </div>
    ```

    <div class="column row display">
      Row column
    </div>

    ---

    ### Fluid Row

    Normally, a row is always 1200 pixels wide. Make a row completely fluid by adding the `.expanded` class.

    <p>
      <a class="" data-open-video="14:51"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/rmJXZy?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="expanded row">
    </div>
    ```

    ---

    ### Nesting

    You can nest the grids indefinitely, though at a certain point it will get absurd.

    <p>
      <a class="" data-open-video="26:29"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/zwRgbE?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="columns small-8">8
        <div class="row">
          <div class="columns small-8">8 Nested
            <div class="row">
              <div class="columns small-8">8 Nested Again</div>
              <div class="columns small-4">4</div>
            </div>
          </div>
          <div class="columns small-4">4</div>
        </div>
      </div>
      <div class="columns small-4">4</div>
    </div>
    ```

    <div class="row display">
      <div class="columns small-8">8
        <div class="row">
          <div class="columns small-8">8 Nested
            <div class="row">
              <div class="columns small-8">8 Nested Again</div>
              <div class="columns small-4">4</div>
            </div>
          </div>
          <div class="columns small-4">4</div>
        </div>
      </div>
      <div class="columns small-4">4</div>
    </div>

    ---

    ### Offsets

    Move blocks up to 11 columns to the right by using classes like `.large-offset-1` and `.small-offset-3`.

    <p>
      <a class="" data-open-video="16:12"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs--codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/YVaKyg?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="columns large-1">1</div>
      <div class="columns large-11">11</div>
    </div>
    <div class="row">
      <div class="columns large-1">1</div>
      <div class="columns large-10 large-offset-1">10, offset 1</div>
    </div>
    <div class="row">
      <div class="columns large-1">1</div>
      <div class="columns large-9 large-offset-2">9, offset 2</div>
    </div>
    <div class="row">
      <div class="columns large-1">1</div>
      <div class="columns large-8 large-offset-3">8, offset 3</div>
    </div>
    ```

    <div class="row display">
      <div class="columns large-1">1</div>
      <div class="columns large-11">11</div>
    </div>
    <div class="row display">
      <div class="columns large-1">1</div>
      <div class="columns large-10 large-offset-1">10, offset 1</div>
    </div>
    <div class="row display">
      <div class="columns large-1">1</div>
      <div class="columns large-9 large-offset-2">9, offset 2</div>
    </div>
    <div class="row display">
      <div class="columns large-1">1</div>
      <div class="columns large-8 large-offset-3">8, offset 3</div>
    </div>

    ---

    ### Incomplete Rows

    In order to work around browsers' different rounding behaviors, Foundation will float the last column in a row to the right so the edge aligns. If your row doesn't have a count that adds up to 12 columns, you can tag the last column with a class of `.end` in order to override that behavior. Alternatively, you can set the `$grid-column-align-edge` variable to `false` to turn off this behavior entirely.

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/dWmbpa?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="columns medium-3">3</div>
      <div class="columns medium-3">3</div>
      <div class="columns medium-3">3</div>
    </div>
    <div class="row">
      <div class="columns medium-3">3</div>
      <div class="columns medium-3">3</div>
      <div class="columns medium-3 end">3 end</div>
    </div>
    ```

    <div class="row display-end">
      <div class="columns medium-3">3</div>
      <div class="columns medium-3">3</div>
      <div class="columns medium-3">3</div>
    </div>
    <div class="row display-end">
      <div class="columns medium-3">3</div>
      <div class="columns medium-3">3</div>
      <div class="columns medium-3 end">3 end</div>
    </div>

    ---

    ### Gutters

    #### Responsive Gutters

    The grid *gutter*&mdash;the space between two columns in a row, and the space between the edge of a grid and the edge of the page&mdash;is responsive, and becomes larger on larger screens.

    Breakpoint | Gutter Size
    -----------|------------
    `small`    | 20px
    `medium`   | 30px

    If you're using the Sass version of Foundation, you can change these defaults by editing the `$grid-column-gutter` variable map:

    ```scss
    $grid-column-gutter: (
      small: 20px,
      medium: 30px,
    );
    ```

    To add more gutter definitions, add new lines to the map. The breakpoint names used here must match a breakpoint name in your project's `$breakpoints` map.

    #### Static Gutters

    If you prefer using one gutter size for every breakpoint, just use a single number for the `$grid-column-gutter` variable:

    ```scss
    $grid-column-gutter: 30px;
    ```

    You can also explicitly set the gutter size for a particular grid row by adding the `.gutter-[size]` class. This is useful when your using responsive gutters but specific components need static gutters.

    ```html
    <div class="row gutter-small">
      <div class="columns">This grid always has small gutters</div>
    </div>
    ```

    ---

    ### Collapse/Uncollapse Rows

    The `.collapse` class lets you remove column gutters (padding).

    There are times when you won't want each media query to be collapsed or uncollapsed. In this case, use the media query size you want and collapse or uncollapse and add that to your row element. Example shows gutters at small and medium and no gutters on large and up.

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/xdWKqa?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row medium-uncollapse large-collapse">
      <div class="columns small-6">
        Removes gutter at large media query
      </div>
      <div class="columns small-6">
        Removes gutter at large media query
      </div>
    </div>
    ```

    <p class="lead">Scale the browser down to a medium size to see the difference.</p>

    <div class="row medium-uncollapse large-collapse">
      <div class="columns small-6">
        <div class="callout secondary">
          <p class="show-for-small-only">On a small screen, I have gutters!</p>
          <p class="show-for-medium-only">On a medium screen, I have gutters!</p>
          <p class="show-for-large">On a large screen, I have no gutters!</p>
        </div>
      </div>
      <div class="columns small-6">
        <div class="callout secondary">
          <p class="show-for-small-only">On a small screen, I have gutters!</p>
          <p class="show-for-medium-only">On a medium screen, I have gutters!</p>
          <p class="show-for-large">On a large screen, I have no gutters!</p>
        </div>
      </div>
    </div>

    ---

    ### Centered Columns

    Center your columns by adding a class of `.small-centered` to your column. Large will inherit small centering by default, but you can also center solely on large by applying a `.large-centered` class. To uncenter on large screens, use `.large-uncentered`.

    <p>
      <a class="" data-open-video="23:16"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/zwWOpL?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="columns small-3 small-centered">3 centered</div>
    </div>
    <div class="row">
      <div class="columns small-6 large-centered">6 centered</div>
    </div>
    <div class="row">
      <div class="columns small-9 small-centered large-uncentered">9 centered</div>
    </div>
    <div class="row">
      <div class="columns small-11 small-centered">11 centered</div>
    </div>
    ```

    <div class="row display">
      <div class="columns small-3 small-centered">3 centered</div>
    </div>
    <div class="row display">
      <div class="columns small-6 large-centered">6 centered, large</div>
    </div>
    <div class="row display">
      <div class="columns small-9 small-centered large-uncentered">9 centered small</div>
    </div>
    <div class="row display">
      <div class="columns small-11 small-centered">11 centered</div>
    </div>

    ---

    ### Source Ordering

    Using these source ordering classes, you can shift columns around between our breakpoints. This means if you place sub-navigation below main content on small displays, you have the option to position the sub-navigation on either the left or right of the page for large displays. Prefix push/pull with the size of the device you want to apply the styles to. `.medium-push-#`, `.large-push-#` is the syntax you'll use. Use the number 0 instead to reset a push/pull, such as `.medium-push-0` or `.large-pull-0`.

    <p>
      <a class="" data-open-video="19:28"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/QvmLmv?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="columns small-10 small-push-2">10</div>
      <div class="columns small-2 small-pull-10">2, last</div>
    </div>
    <div class="row">
      <div class="columns large-9 large-push-3">9</div>
      <div class="columns large-3 large-pull-9">3, last</div>
    </div>
    <div class="row">
      <div class="columns large-8 large-push-4">8</div>
      <div class="columns large-4 large-pull-8">4, last</div>
    </div>
    <div class="row">
      <div class="columns small-5 small-push-7 medium-7 medium-push-5">7</div>
      <div class="columns small-7 small-pull-5 medium-5 medium-pull-7">5, last</div>
    </div>
    <div class="row">
      <div class="columns medium-6 medium-push-6">6</div>
      <div class="columns medium-6 medium-pull-6">6, last</div>
    </div>
    ```

    <div class="row display">
      <div class="columns small-10 small-push-2">10</div>
      <div class="columns small-2 small-pull-10">2, last</div>
    </div>
    <div class="row display">
      <div class="columns large-9 large-push-3">9</div>
      <div class="columns large-3 large-pull-9">3, last</div>
    </div>
    <div class="row display">
      <div class="columns large-8 large-push-4">8</div>
      <div class="columns large-4 large-pull-8">4, last</div>
    </div>
    <div class="row display">
      <div class="columns small-5 small-push-7 medium-7 medium-push-5">7</div>
      <div class="columns small-7 small-pull-5 medium-5 medium-pull-7">5, last</div>
    </div>
    <div class="row display">
      <div class="columns medium-6 medium-push-6">6</div>
      <div class="columns medium-6 medium-pull-6">6, last</div>
    </div>

    ---

    ### Block Grids

    Block grids are a shorthand way to create equally-sized columns. Add a class of the format `.[size]-up-[n]` to change the number of columns within the row. By default, the max number of columns you can use with block grid are 8. Adding the `.column-block` class to columns will apply a bottom margin equal to the width of gutters.

    <p>
      <a class="" data-open-video="30:07"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/eWMOjK?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row small-up-2 medium-up-3 large-up-4">
      <div class="column column-block">
        <img src="https://placehold.it/600x600" class="thumbnail" alt="">
      </div>
      <div class="column column-block">
        <img src="https://placehold.it/600x600" class="thumbnail" alt="">
      </div>
      <div class="column column-block">
        <img src="https://placehold.it/600x600" class="thumbnail" alt="">
      </div>
      <div class="column column-block">
        <img src="https://placehold.it/600x600" class="thumbnail" alt="">
      </div>
      <div class="column column-block">
        <img src="https://placehold.it/600x600" class="thumbnail" alt="">
      </div>
      <div class="column column-block">
        <img src="https://placehold.it/600x600" class="thumbnail" alt="">
      </div>
    </div>
    ```

    ---

    ## Building Semantically

    Our grid CSS is generated with a powerful set of Sass mixins, which you can use in your own code to build a semantic grid.

    ### Rows

    Use the `grid-row()` mixin to create a row.

    ```scss
    .container {
      @include grid-row;
    }
    ```

    ---

    ### Columns

    Use the `grid-column()` mixin to create a column. There are a number of ways to define the width of the column.

    ```scss
    .main-content {
      // Use the full column count (100%)
      @include grid-column;

      // Use a column count (33%);
      @include grid-column(4);

      // Use a percentage (15%)
      @include grid-column(15%);

      // Use a custom fraction (20%)
      @include grid-column(1 of 5);
    }
    ```

    The grid column calculator can also be accessed as a function. This gives you the percentage value, without any of the grid column CSS.

    ```scss
    .main-content {
      width: grid-column(1 of 7);
    }
    ```

    To center a column semantically. Use ´grid-column-position(center);´.

    ```scss
    .centered-column {
      @include grid-column-position(center);
    }
    ```

    ---

    ### Multiple Grids

    By default, all grids use the number of columns set by the `$grid-column-count` variable. However, this can be selectively overridden within an instance of a row.

    In this example, the grid is 16 columns instead of the normal 12. Any references to column math inside the mixin will use the new column count.

    ```scss
    .container {
      @include grid-row(16) {
        .main-content {
          // 11/16 = 68.75%
          @include grid-column(11);
        }

        .sidebar {
          // 5/16 = 31.25%
          @include grid-column(5);
        }
      }
    }
    ```

    You can also temporarily change the grid context without outputting any row CSS, by using the `grid-context()` mixin.

    ```scss
    @include grid-context(7) {
      .sidebar {
        @include grid-column(4);
      }
    }
    ```

    Every other grid feature, from sizing to offsets to source ordering, can also be accessed with a mixin. Pair them with the `breakpoint()` mixin to make your grid responsive.

    Refer to the Sass documentation below to learn how each mixin works.

    ```scss
    .main-content {
      // The mixins have shorthands, too!
      @include grid-col;

      @include breakpoint(medium) {
        // Changes size only
        @include grid-col-size(8);

        // Changes position only
        @include grid-col-pos(4);
      }
    }
    ```

    ### Custom Block Grid

    Use the `grid-layout()` mixin to create your own block grid.
    By default the mixin takes 3 parameters:
    - Number of columns
    - The child element selector
      - An optional padding value

    The padding value can be set to `$grid-column-gutter` to use the values from that map.
    This will then generate different paddings at different breakpoints. Alternatively supply a numeric value (without a unit type) to output a static rem value.

    Here's an example:

    ```scss
    .gallery {
      @include grid-layout(3, '.gallery-item', $grid-column-gutter);
    }
    ```
    That outputs this CSS:

    ```
    .gallery > .gallery-item {
      width: 33.33333%;
      float: left;
      padding-left: 0.625rem;
      padding-right: 0.625rem;
    }

    @media screen and (min-width: 40em) {
      .gallery > .gallery-item {
        padding-left: 0.9375rem;
        padding-right: 0.9375rem;
      }
    }

    .gallery > .gallery-item:nth-of-type(1n) {
      clear: none;
    }

    .gallery > .gallery-item:nth-of-type(3n+1) {
      clear: both;
    }

    .gallery > .gallery-item:last-child {
      float: left;
    }
    ```

    ---"""

    pass


class INDEX:
    """---
    title: Welcome to Foundation 6
    description: We built Foundation for Sites to be the most advanced responsive front-end framework in the world.
    tags:
      - index
      - home

    video-hero: true

    ---

    ## Installing Foundation

    There are a number of ways to install Foundation for Sites. Our installation page will help you find the best option for you.

    <a href="installation.html" class="large button">Install Foundation for Sites</a>

    ---

    ## New to Foundation for Sites?

    With an easy to understand syntax and consistent structure, you'll learn your way around Foundation in no time!

    <ul class="accordion welcome-accordion" data-accordion data-allow-all-closed="true">
      <li class="accordion-item welcome-accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Getting Started</a>
        <div class="accordion-content" data-tab-content>
          <a href="{{root}}starter-projects.html?video=lFrpnk0Oo_8" target="_blank">
            <div class="grid-x grid-margin-x accordion-content-item">
              <div class="cell medium-4 accordion-content-item-thumbnail">
                <img src="https://i3.ytimg.com/vi/lFrpnk0Oo_8/maxresdefault.jpg" class="" height="" width="" alt="">
              </div>
              <div class="cell medium-8">
                <h5>Foundation Starter Projects - CSS Download</h5>
                <p>This video will take you through downloading and getting started with the Foundation CSS project.</p>
                <span class="accordion-content-item-cta"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="" height="" width="" alt=""> Watch Video</span>
              </div>
            </div>
          </a>
          <a href="{{root}}starter-projects.html?video=3Uj74uJ3GSQ" target="_blank">
            <div class="grid-x grid-margin-x accordion-content-item">
              <div class="cell medium-4 accordion-content-item-thumbnail">
                <img src="https://i3.ytimg.com/vi/3Uj74uJ3GSQ/maxresdefault.jpg" class="" height="" width="" alt="">
              </div>
              <div class="cell medium-8">
                <h5>Foundation Starter Projects</h5>
                <p>This video will take you through downloading and getting started with the Foundation stack.</p>
                <span class="accordion-content-item-cta"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="" height="" width="" alt=""> Watch Video</span>
              </div>
            </div>
          </a>
        </div>
      </li>

      <li class="accordion-item welcome-accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Why Foundation</a>
        <div class="accordion-content" data-tab-content>
          <a target="_blank" href="https://get.foundation/learn/get-your-team-on-a-solid-foundation.html">
            <div class="grid-x grid-margin-x accordion-content-item">
              <div class="cell medium-4 accordion-content-item-thumbnail">
                <img src="https://i.ytimg.com/vi/kLgRITKjcWw/mqdefault.jpg" class="" height="" width="" alt="">
              </div>
              <div class="cell medium-8">
                <h5>The World’s Most Advanced Front-end Framework</h5>
                <p>Coming from another framework? It’s the perfect time to make the switch and learn Foundation. Download our free e-book that will help you convince your team that Foundation is better, easier to learn, and more flexible than anything else out there.
                </p>
                <span class="accordion-content-item-cta">Learn More</span>
              </div>
            </div>
          </a>
          <a target="_blank" href="https://get.foundation/learn/build-your-career-on-a-solid-foundation.html">
            <div class="grid-x grid-margin-x accordion-content-item">
              <div class="cell medium-4 accordion-content-item-thumbnail">
                <img src="https://i.ytimg.com/vi/dZZk9Kz5j_0/mqdefault.jpg" class="" height="" width="" alt="">
              </div>
              <div class="cell medium-8">
                <h5>Build Your Career on a Solid Foundation</h5>
                <p>Web technologies are rapidly changing, but time and resources are finite. Find out why Learning Foundation places you at the cutting edge of the website development.
                </p>
                <span class="accordion-content-item-cta">Learn More</span>
              </div>
            </div>
          </a>
        </div>
      </li>

      <li class="accordion-item welcome-accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Templates and Code Snippets</a>
        <div class="accordion-content " data-tab-content>
          <a target="_blank" href="https://get.foundation/templates.html">
            <div class="grid-x grid-margin-x accordion-content-item">
              <div class="cell medium-4 accordion-content-item-thumbnail">
                <img src="https://get.foundation/assets/img/sites-templates/foundation6-templates-07.svg">
              </div>
              <div class="cell medium-8">
                <h5>Foundation Templates</h5>
                <p>Get eight responsive templates to kick off your projects built with the same techniques we teach in our Introduction to Foundation 6 Course to build your business upon.</p>
                <span class="accordion-content-item-cta">View Templates</span>
              </div>
            </div>
          </a>
          <a target="_blank" href="https://get.foundation/building-blocks/how-to.html">
            <div class="grid-x grid-margin-x accordion-content-item">
              <div class="cell medium-4 accordion-content-item-thumbnail">
                <img src="https://i3.ytimg.com/vi/SmhGUT_N-jw/maxresdefault.jpg" class="" height="" width="" alt="" style="height: 142px;">
              </div>
              <div class="cell medium-8">
                <h5>Foundation Building Blocks</h5>
                <p>Building Blocks are coded UI components you can drop into any standard Foundation project. Building Blocks will help you rapidly accelerate your development time.</p>
                <span class="accordion-content-item-cta">Learn More</span>
              </div>
            </div>
          </a>
          <a target="_blank" href="https://get.foundation/building-blocks/kits.html">
            <div class="grid-x grid-margin-x accordion-content-item">
              <div class="cell medium-4 accordion-content-item-thumbnail">
                <img src="https://get.foundation/building-blocks/assets/img/kits/dashboard/dashboard-kit.jpg" style="height: 142px; width: 100%;">
              </div>
              <div class="cell medium-8">
                <h5>Foundation Kits</h5>
                <p>Foundation Kits are curated bundles of Building Blocks designed for building specific types of websites and apps. Download from 7 powerful Kits to jumpstart your next project.</p>
                <span class="accordion-content-item-cta">View Kits</span>
              </div>
            </div>
          </a>
        </div>
      </li>

      <li class="accordion-item welcome-accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Additional Resources</a>
        <div class="accordion-content" data-tab-content>
          <a target="_blank" href="https://get.foundation/learn/zero-to-website-in-no-time-flat.html">
            <div class="grid-x grid-margin-x accordion-content-item">
              <div class="cell medium-4 accordion-content-item-thumbnail">
                <img src="https://i.ytimg.com/vi/KHMXOTbLAGE/mqdefault.jpg" class="" height="" width="" alt="">
              </div>
              <div class="cell medium-8">
                <h5>Zero to Website Guide</h5>
                <p>Learning a framework for the first time can be overwhelming, so we’ve put together “Zero to Website,” a 60-page guide that will walk you through coding a real, live, responsive website from scratch with Foundation.</p>
                <span class="accordion-content-item-cta">Get The Guide</span>
              </div>
            </div>
          </a>
        </div>
      </li>

    </ul>

    ---

    ## Experienced with Foundation for Sites?

    With an easy to understand syntax and consistent structure, you'll learn your way around Foundation in no time!

    <ul class="accordion welcome-accordion" data-accordion data-allow-all-closed="true">
      <li class="accordion-item welcome-accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Latest Foundation Updates</a>
        <div class="accordion-content" data-tab-content>
          <a target="_blank" href="https://github.com/foundation/foundation-sites/releases/tag/6.3.1">
            <div class="grid-x grid-margin-x accordion-content-item">
              <div class="cell medium-4 accordion-content-item-thumbnail">
                <img src="{{root}}assets/img/docs-631.png" class="" height="" width="" alt="">
              </div>
              <div class="cell medium-8">
                <h5>Foundation 6.3.1 Update: Sass mixins and bug fixes</h5>
                <p>Foundation 6.3.1 contains plenty of bug fixes underlying reworks to old features. Along with bug fixes, Foundation gets some some new Sass mixins and optimizations that make it work in more scenarios and the docs got a lot of love. Enjoy it!</p>
                <span class="accordion-content-item-cta">Learn More</span>
              </div>
            </div>
          </a>
        </div>
      </li>
      <li class="accordion-item welcome-accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Building Blocks</a>
        <div class="accordion-content" data-tab-content>
          <a target="_blank" href="https://get.foundation/building-blocks/how-to.html">
            <div class="grid-x grid-margin-x accordion-content-item">
              <div class="cell medium-4 accordion-content-item-thumbnail">
                <img src="https://i3.ytimg.com/vi/adLpmsU9v2g/maxresdefault.jpg" class="" height="" width="" alt="">
              </div>
              <div class="cell medium-8">
                <h5>How to Use Foundation's Building Blocks</h5>
                <p>The Foundation team has cut your development time in half again with Foundation Building Blocks. In this tutorial we'll show you how to find the right building block and the way to install it that works best for you.</p>
                <span class="accordion-content-item-cta">Learn More</span>
              </div>
            </div>
          </a>
        </div>
      </li>
      <li class="accordion-item welcome-accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Foundation Integrations</a>
        <div class="accordion-content" data-tab-content>
          <a target="_blank" href="https://circlingthesun.github.io/angular-foundation-6/">
            <div class="grid-x grid-margin-x accordion-content-item">
              <div class="cell medium-3 accordion-content-item-thumbnail">
                <img src="https://circlingthesun.github.io/angular-foundation-6/assets/logo.png" class="" height="147" width="147" alt="" style="border: 0;">
              </div>
              <div class="cell medium-9">
                <h5>Angular Foundation 6</h5>
                <p>The awesome folks at Pinecone created an Angular port for Foundation. Angular.js assists with creating single-page applications, one-page web applications that only require HTML, CSS, and JavaScript on the client side.</p>
                <span class="accordion-content-item-cta">Learn More</span>
              </div>
            </div>
          </a>
          <a target="_blank" href="https://react.foundation/">
            <div class="grid-x grid-margin-x accordion-content-item">
              <div class="cell medium-3 accordion-content-item-thumbnail">
                <img src="https://cdn.worldvectorlogo.com/logos/react.svg" class="" height="" width="" alt="" style="border: 0;">
              </div>
              <div class="cell medium-9">
                <h5>React + Foundation 6</h5>
                <p>React is a JavaScript library for building user interfaces. Now you can use Foundation for Sites 6 components implemented in React with CSS Modules!</p>
                <span class="accordion-content-item-cta">Learn More</span>
              </div>
            </div>
          </a>
          <a target="_blank" href="https://jointswp.com/">
            <div class="grid-x grid-margin-x accordion-content-item">
              <div class="cell medium-3 accordion-content-item-thumbnail">
                <img src="https://s.w.org/about/images/logos/wordpress-logo-simplified-rgb.png" class="" height="147" width="147" alt="" style="border: 0;">
              </div>
              <div class="cell medium-9">
                <h5>JointsWP: Foundation 6 meets WordPress</h5>
                <p>JointsWP is a blank WordPress theme built with Foundation 6, giving you all the power and flexibility you need to build complex, mobile friendly websites without starting from scratch.</p>
                <span class="accordion-content-item-cta">Learn More</span>
              </div>
            </div>
          </a>
          <a target="_blank" href="https://medium.com/@tommaso.marcelli/setting-up-vue-2-and-foundation-6-3f858b4ad20">
            <div class="grid-x grid-margin-x accordion-content-item">
              <div class="cell medium-3 accordion-content-item-thumbnail">
                <img src="{{root}}assets/img/docs-vue.jpeg" class="" height="147" width="147" alt="" style="border: 0;">
              </div>
              <div class="cell medium-9">
                <h5>Setting up Vue 2 and Foundation 6</h5>
                <p>This is a demo integration of Foundation for Sites 6.3 in a VueJS 2.1 single-page application.</p>
                <span class="accordion-content-item-cta">Learn More</span>
              </div>
            </div>
          </a>
        </div>
      </li>
      <li class="accordion-item welcome-accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Foundation Showcase</a>
        <div class="accordion-content" data-tab-content>
          <a target="_blank" href="https://get.foundation/foundationturns5">
            <div class="grid-x grid-margin-x accordion-content-item">
              <div class="cell medium-4 accordion-content-item-thumbnail">
                <img src="{{root}}assets/img/foundation-turns-5.png" class="" height="" width="" alt="">
              </div>
              <div class="cell medium-8">
                <h5>5 Years of Shaping the Web</h5>
                <p>This year Foundation turned five years old. It was the first to be responsive, the first to be semantic, the first to be mobile first, the first to be built with Sass, and the first to have accessibility built in. Learn more about the framework and where it's going next.</p>
                <span class="accordion-content-item-cta">Learn More</span>
              </div>
            </div>
          </a>
          <a target="_blank" href="https://get.foundation/showcase/brands.html">
            <div class="grid-x grid-margin-x accordion-content-item">
              <div class="cell medium-4 accordion-content-item-thumbnail">
                <img src="{{root}}assets/img/foundation-brands.png" class="" height="" width="" alt="">
              </div>
              <div class="cell medium-8">
                <h5>Foundation Brands</h5>
                <p>Big brands are relying more and more on the world's most advanced, responsive front-end framework. Their sites are now built so that customers can connect with them on any device.</p>
                <span class="accordion-content-item-cta">Learn More</span>
              </div>
            </div>
          </a>
          <a target="_blank" href="https://get.foundation/showcase/case-studies.html">
            <div class="grid-x grid-margin-x accordion-content-item">
              <div class="cell medium-4 accordion-content-item-thumbnail">
                <img src="https://get.foundation/assets/img/learn/case-studies/meundies-mockup1.jpg" class="" height="" width="" alt="">
              </div>
              <div class="cell medium-8">
                <h5>Foundation Case Studies</h5>
                <p>Foundation in the wild. See how people are using Foundation to build responsive, future-friendly sites. We learn what went into their designs, decisions, and how Foundation helped them get to their goals.</p>
              </div>
            </div>
          </a>
        </div>
      </li>
    </ul>"""

    pass


class INSTALLATION:
    """---
    title: Installation
    description: There are many ways to install Foundation, but if you're just getting started, we have a few suggestions.
    video: '6KwsGcEHVTE'
    ---

    ## Install with Package Managers

    Foundation is available on npm. The package includes all of the source Sass and JavaScript files, as well as compiled CSS and JavaScript, in uncompressed and compressed flavors.

    <div class="grid-x grid-margin-x">
      <div class="cell small-2 text-right">
        <a href="https://www.npmjs.com/package/foundation-sites">
          <img class="docs-install-vendor-icon" src="{{root}}assets/img/icons/logo-npm.svg" alt="NPM">
        </a>
      </div>
      <div class="cell small-10">
        <div class="docs-code">
          <code class="bash">
            npm install foundation-sites
          </code>
        </div>
      </div>

      <div class="cell small-2 text-right">
        <a href="https://yarnpkg.com/en/package/foundation-sites">
          <img class="docs-install-vendor-icon" src="{{root}}assets/img/icons/logo-yarn.svg" alt="Yarn">
        </a>
      </div>
      <div class="cell small-10">
        <div class="docs-code">
          <code class="bash">
            yarn add foundation-sites
          </code>
        </div>
      </div>

    </div>

    Here's what comes in the package.

    ```
    ├─ scss       Source Sass files. Use this folder as a load path in Sass.
    ├─ js         Source JavaScript files. If you're using a build system, make sure `foundation.core.js` is loaded first.
    └─ dist       Compiled files:
       ├─ css        * Compiled CSS files. Includes minified and unminified files.
       ├─ js         * Concatenated JavaScript files. Includes minified and unminified files.
       └─ plugins    * Standalone JavaScript plugins.
    ```

    ---

    ## Install with Foundation via CLI

    Not a fan of GUIs? Foundation can easily be installed via the CLI. It can install the same template projects for you.


    <!-- Install Foundation CLI:

    ```bash
    npm install --global foundation-cli
    # or sudo npm install --global foundation-cli
    ```

    <div class="callout info">
      Depending on how your machine is configured, the command may fail with an `EACCESS` error. To get around this, run the commands with `sudo` at the beginning.
    </div>

    Then use to create a new Foundation project:

    ```bash
    foundation new
    ```

    After you selected "Foundation for Sites", Foundation CLI will ask you which template you want to use. You can choose between: -->

    ### Basics Template Installation

    ```bash
    git clone https://github.com/foundation/foundation-sites-template basic-project
    cd basic-project
    yarn install
    yarn start
    ```

    ### Experienced Template Installation

    ```bash
    git clone https://github.com/foundation/foundation-zurb-template f6-project
    cd f6-project
    yarn install
    yarn start
    ```

    <div class="grid-x grid-margin-x">
      <div class="cell small-6">
        <h3>Basic template</h3>
        <p>
          <b>Recommended for beginners</b><br>
          A basic template to begin to use Foundation. It includes:
          <ul>
            <li>
              Foundation for Sites pre-configured.
            </li>
            <li>
              Sass compilation<br>
              A tool to convert your SASS/SCSS files to CSS.
            </li>
            <li>
              Starter HTML file<br>
              A basic file to help you to use basic Foundation component (including the new XY grid !)
            </li>
          </ul>
        </p>
      </div>

      <div class="cell small-6">
        <h3>Experienced template</h3>
        <p>
          <b>Recommended for experienced (or curious) users</b><br>
          A more advanced project including Foundation and a build process with:
          <ul>
            <li>Handlebars HTML templates with Panini</li>
            <li>Sass compilation and prefixing</li>
            <li>JavaScript module bundling with webpack</li>
            <li>Built-in BrowserSync</li>
            <li>Production build with CSS, Javascript and Image compression</li>
          </ul>
        </p>
      </div>
    </div>

    <p class="text-center">
      <a href="starter-projects.html" class="button">See advanced Template installations</a>
    </p>

    <div class="callout info">
      <p><strong>Foundation 5 users</strong>: if you already have the Foundation 5 CLI on your machine, you will only be able to access one of the commands, depending on how your command line environment is configured.</p>

      <p>To remove the Foundation 5 CLI, run <code>gem uninstall foundation</code>. After testing the Foundation 6 CLI, if you want to remove it to go back to the old CLI, run <code>npm uninstall foundation-cli --global</code>.</p>
    </div>

    <div class="callout info">
      <p><strong>Windows users</strong>: make sure you've python v2.7 available in your node environment since it's required by the node-gyp tool. There are two way to achieve this</p>

      <ol>
        <li>Install the <a href="https://github.com/felixrieseberg/windows-build-tools">windows-build-tools</a> (recommended) and make python afterwards accessible via <code>npm config set python "%USERPROFILE%\.windows-build-tools\python27\python.exe"</code></li>
        <li>Install <a href="https://www.python.org/downloads/">python</a> (not recommended) and add it to your system environment variables</li>
      </ol>

      <p>The first way is recommended if you've not installed python v2.7 yet as it doesn't affect your machine outside the node environment. In case you've already installed python v2.7 you may of course skip both ways and start using foundationc-cli immediately.</p>
    </div>

    ---

    ## Download

    <div class="grid-x grid-margin-x">
      <div class="cell small-6">
        <div class="responsive-embed widescreen mb1">
          <iframe width="560" height="315" src="https://www.youtube.com/embed/lFrpnk0Oo_8" frameborder="0" allowfullscreen></iframe>
          <a id="docs-mobile-video-link" class="docs-mobile-video" target="_blank" href="https://youtu.be/lFrpnk0Oo_8"></a>
        </div>
      </div>

      <div class="cell small-6">
        <p>
          If you aren't into Sass, we have a starter template with compiled CSS and JavaScript, as well as a starting `index.html` file for you to hack on. Just unzip and get coding!
        </p>
        <p class="text-center">
          <a href="https://static.foundationcss.com/sites-css-latest" class="button">Download Foundation</a>
        </p>
      </div>
    </div>

    ---

    ## CDN Links

    The folks at [jsDelivr](https://www.jsdelivr.com) host the compressed Foundation CSS and JavaScript for us. Just drop one of these `<script>` tags into your HTML and you're set:

    ```html
    <!-- Compressed CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/foundation-sites@6.8.1/dist/css/foundation.min.css" crossorigin="anonymous">

    <!-- Compressed JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/foundation-sites@6.8.1/dist/js/foundation.min.js" crossorigin="anonymous"></script>
    ```

    From Foundation 6.4, flex is enabled by default and **only the new XY Grid is available**. However, others CSS versions are available for backward compatibility and the most common usage cases. For others uses and advanced customization, we recommand to build Foundation with custom settings (see others installation methods).

    ```html
    <!-- foundation-float.min.css: Compressed CSS with legacy Float Grid -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/foundation-sites@6.8.1/dist/css/foundation-float.min.css" crossorigin="anonymous">

    <!-- foundation-prototype.min.css: Compressed CSS with prototyping classes -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/foundation-sites@6.8.1/dist/css/foundation-prototype.min.css" crossorigin="anonymous">

    <!-- foundation-rtl.min.css: Compressed CSS with right-to-left reading direction -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/foundation-sites@6.8.1/dist/css/foundation-rtl.min.css" crossorigin="anonymous">
    ```

    <div class="text-center">
      <a href="https://www.jsdelivr.com/package/npm/foundation-sites?path=dist" class="button" target="_blank">See all CDN files and versions</a>
    </div>

    ---

    ## HTML Starter Template
    Start with this HTML template and adapt it to your needs. Be sure to include the `.no-js` class on the `html` tag of your template.  Adding this class prevents [flash of unstyled content](https://en.wikipedia.org/wiki/Flash_of_unstyled_content) for a number of foundation components.

    ```html
    <!doctype html>
    <html class="no-js" lang="en">
      <head>
        <meta charset="utf-8" />
        <meta http-equiv="x-ua-compatible" content="ie=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Foundation Starter Template</title>
        <link rel="stylesheet" href="css/foundation.css" />
      </head>
      <body>
        <h1>Hello, world!</h1>

        <script src="js/vendor/jquery.js"></script>
        <script src="js/vendor/what-input.js"></script>
        <script src="js/vendor/foundation.min.js"></script>
        <script>
          $(document).foundation();
        </script>

      </body>
    </html>

    ```

    ---

    ## Other Integrations

    The Foundation community has helped us integrate the framework into Rails, WordPress, Django, and more. Head to our [resources page](https://get.foundation/sites/resources) to find even more ways to use Foundation.
    """

    pass


class INTERCHANGE:
    """---
    title: Interchange
    description: Interchange uses media queries to dynamically load responsive content that is appropriate for the user's device.
    js: js/foundation.interchange.js
    video: '1Nr12_1rUpo'

    ---

    ## Use with Images

    Bandwidth is precious on mobile networks, so it helps to serve users on smaller screens a smaller image. Using Interchange, you can serve up specific images for users depending on their screen size. CSS media queries are used to determine what size the user's device is, and which image should be served.

    In the below example, we have three different sizes of image: one for small screens, one for medium, and one for large. Use the below format to set up a responsive image. The image will change automatically as the browser resizes.

    <p>
      <a class="" data-open-video="0:50"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/JNZQGB?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <img data-interchange="[assets/img/interchange/small.jpg, small], [assets/img/interchange/medium.jpg, medium], [assets/img/interchange/large.jpg, large]">
    ```

    <img data-interchange="[assets/img/interchange/small.jpg, small], [assets/img/interchange/medium.jpg, medium], [assets/img/interchange/large.jpg, large]">

    The image set is a comma-separated list of items with this format:

    ```
    [image_path, media_query]
    ```

    `image_path` can be a relative or absolute path. `media_query` can be any CSS media query, or a Foundation breakpoint&mdash;see [Named Media Queries](#named-media-queries) below.

    <div class="callout primary">
      <p>Interchange evaluates rules in order, and the last rule to match will be used. For this reason, you should order your rules from smallest screen to largest screen.</p>
    </div>

    ---

    ## Use with HTML

    Interchange can also swap in and out entire chunks of HTML. This allows you to load in mobile-friendly components on small screens, or more advanced versions on large screens.

    In the below example, we've applied `data-interchange` to a `<div>` instead of an `<img>` element, and the paths are to HTML files instead of images.

    ```html
    <div data-interchange="[assets/partials/interchange-default.html, small], [assets/partials/interchange-medium.html, medium], [assets/partials/interchange-large.html, large]"></div>
    ```

    <div id="docs-example-interchange" data-interchange="[assets/partials/interchange-default.html, small], [assets/partials/interchange-medium.html, medium], [assets/partials/interchange-large.html, large]"></div>

    ---

    ## Use with Background Images

    When using Interchange on a non-`<img>` element, you can pass in an image path instead of an HTML path, and the element's `background-image` property will be set to the path of the matching rule.

    ```html
    <div data-interchange="[assets/img/interchange/small.jpg, small], [assets/img/interchange/medium.jpg, medium], [assets/img/interchange/large.jpg, large]"></div>
    ```

    ---

    ## Named Media Queries

    Interchange supports named queries as shorthands for full CSS media queries. Any breakpoint defined in the `$breakpoints` variable in your Sass will work, along with a few other keywords. [Learn more about changing the default breakpoints.](media-queries.html)

    Query Name | Media Query
    -----------|------------
    small      | `screen and (min-width: 0em)`
    medium     | `only screen and (min-width: 40em)`
    large      | `only screen and (min-width: 64em)`
    xlarge     | `only screen and (min-width: 75em)`
    xxlarge    | `only screen and (min-width: 90em)`
    portrait   | `screen and (orientation: portrait)`
    landscape  | `screen and (orientation: landscape)`
    retina     | `only screen and (-webkit-min-device-pixel-ratio: 2), only screen and (min--moz-device-pixel-ratio: 2), only screen and (-o-min-device-pixel-ratio: 2/1), only screen and (min-device-pixel-ratio: 2), only screen and (min-resolution: 192dpi), only screen and (min-resolution: 2dppx)`

    To add your own named media queries, add them as properties to `Foundation.Interchange.SPECIAL_QUERIES`.

    ```js
    Foundation.Interchange.SPECIAL_QUERIES['square'] = 'screen and (aspect-ratio: 1/1)';
    ```

    ---

    ## Programmatic Use

    When using Interchange programmatically, you need to pass in your ruleset in the `options` object, as well as the *container* element, *not* the content elements, like so:

    ```js
    var $photoFrame = $('#some-container');
    var interchange = new Foundation.Interchange($photoFrame, {
      rules: [
        "[path/to/default.jpg, small]",
        "[path/to/medium.jpg, medium]",
        "[path/to/large.jpg, large]"
      ]
     });
    ```"""

    pass


class JAVASCRIPT_UTILITIES:
    """---
    title: JavaScript Utilities
    description: Our JavaScript Utility Libraries are easy to use and super helpful.
    video: 'h83jR82cjWM'
    ---

    ## Installing

    See our [JavaScript](javascript.html) and [Installation](installation.html) pages on how to install our files in your project.

    ## Box
    `js/foundation.util.box.js`

    One of the useful libraries is `Foundation.Box`, and it has a couple methods designed to make your life easier. You can pass either jQuery objects or plain JavaScript elements to both.

    ```js

    var dims = Foundation.Box.GetDimensions(element);
    ```
    Will return an object that contains the dimensions of `element`. The object return looks like:

    ```js

    {
      height: 54,
      width: 521,
      offset: {
        left: 198,
        top: 1047
      },
      parentDims: {
        height: ... // parentDims and windowDims share the same format as the element dimensions.
      },
      windowDims: {
        height: ...
      }
    }
    ```

    Also included is the `ImNotTouchingYou` function. It returns a boolean based on whether the passed `element` is colliding with the edge of the window (default), or a parent element. The remaining two options are booleans for limiting collision detection to only one axis.
    ```js

    var clear = Foundation.Box.ImNotTouchingYou(element [, parent, leftAndRightOnly, topAndBottomOnly]);
    ```

    ## Keyboard
    `js/foundation.util.keyboard.js`

    Another quite useful library, `Foundation.Keyboard` has several methods to make keyboard event interaction easier for all. Shout out to Marius Olbertz of Germany who conceived and coded this library.

    Ever wanted a handy list of common keycodes and the keys they represent? Use `Foundation.Keyboard.keys`. This is an object containing key/value pairs of the most frequently used keys in our framework.

    Want to manage your own keyboard inputs? No problem! Within your `.on('key**')` callback, call `Foundation.Keyboard.parseKey(event)` to get a string of what key was pressed, e.g. `'TAB'` or `'ALT_X'`.
    (You can also use this function outside of the Foundation components, in your own JavaScript code!)

    What if you want to know if there's focusable elements somewhere on a page? Instead of writing your own function and selector from scratch, just use:
    ```js
    var focusable = Foundation.Keyboard.findFocusable($('#content'));
    ```

    The Keyboard utility also provides functions to trap the keyboard focus inside a given element. This is quite useful for modals in terms of accessibility. When the focus is trapped, pressing tab while the last focusable element inside the given container is selected will focus the first element and vice versa.
    ```js
    // Trap focus to given element
    Foundation.Keyboard.trapFocus($('#content'));

    // Release focus from given element
    Foundation.Keyboard.releaseFocus($('#content'));
    ```


    The real gem of this library, however, is the `handleKey` function. Any plugin that is registered with the utility can call on this method to manage keyboard inputs.
    ```js
    Foundation.Keyboard.register('pluginName', {
      'TAB': 'next'
    });
    ...//in event callback
    Foundation.Keyboard.handleKey(event, 'pluginName', {
      next: function(){
        //do stuff
      }
    });
    ```
    There are also the functions `handled` and `unhandled`, where you can place any code that shall always be executed after the key event has been handled (or not).

    If you want to use your own key bindings, simply call the `Foundation.Keyboard.register` function. It even works after Foundation has already initialized.

    ## MediaQuery
    `js/foundation.util.mediaQuery.js`

    The media query library used by Foundation has two publicly accessible functions and two properties:
    ```js

    Foundation.MediaQuery.get('medium');
    // returns the minimum pixel value for the `medium` breakpoint.
    Foundation.MediaQuery.atLeast('large');
    // returns a boolean if the current screen size is, you guessed it, at least `large`.
    Foundation.MediaQuery.queries;
    // an array of media queries Foundation uses for breakpoints.
    Foundation.MediaQuery.current;
    // a string of the current breakpoint size.
    ```

    Also included is an event emitter for breakpoint changes. You can hook into this event with:
    ```js

    $(window).on('changed.zf.mediaquery', function(event, newSize, oldSize){});
    ```

    ## Motion & Move
    `js/foundation.util.motion.js`

    Two handy utilities, one little file.

    `Foundation.Motion` is the same JavaScript used by the [Motion-UI](https://github.com/foundation/motion-ui/) library, and is included in Foundation 6. See the GitHub page for more details.

    `Foundation.Move` is a simple helper function for utilizing browsers' `requestAnimationFrame` method for hardware acceleration. Invoke like so:
    ```js
    Foundation.Move(durationInMS, $element, function(){
      //animation logic
    });
    ```
    When the animation is complete, your jQuery element will fire `finished.zf.animate`.

    ## Timer
    `js/foundation.util.timer.js`

    ```js

    var timer = new Foundation.Timer($element, {duration: ms, infinite: bool}, callback);
    // includes: timer.start(), timer.pause(), timer.restart()
    ```
    Similar to `setInterval`, except you can pause and resume where you left off.

    ## ImageLoader
    `js/foundation.util.imageLoader.js`

    ```js
    Foundation.onImagesLoaded($images, callback);
    ```
    This will execute your callback function after all the images in your jQuery collection have loaded.

    ## Touch
    `js/foundation.util.touch.js`

    Allows you to add `swipe*` and pseudo-drag events to elements.

    ```js
    $('selector').addTouch().on('mousemove', handleDrag);
    // Binds elements to touch events. Used in the Slider plugin for mobile devices.
    $('selector').on('swipeleft', handleLeftSwipe);
    // Binds elements to swipe events. Used in the Orbit plugin for mobile devices.
    ```

    ## Triggers
    `js/foundation.util.triggers.js`

    Provides a number of event listeners and triggers your script can hook into. Most are self-explanatory, and used in many Foundation plugins.
    ```html
    <button data-open="someId">I open something!</button>
    <button data-close="someId">I close something!</button>
    <button data-toggle="someId">I toggle something!</button>
    ```
    ```js
    // Add the data-open/close/toggle="idOfElement" tag to your markup.
    // When a click event is triggered on that element, these are the non-bubbling events directed at your element.
    // If you don't use an `id` selector, an event will be triggered that bubbles up to window.
    $('selector').on('open.zf.trigger', handleOpen);
    $('selector').on('close.zf.trigger', handleClose);
    $('selector').on('toggle.zf.trigger', handleToggle);
    ```
    Besides these useful click triggers, there are also other listeners for you to tap into. Need to know when the window has been resized, but only when it's done resizing? How about a debounced scroll event? Add this markup and JavaScript and you're good to go!

    ```html
    <div data-scroll="someId">...</div>
    <div data-resize="someId">...</div>
    ```
    ```js
    $('#someId').on('scrollme.zf.trigger', handleScroll);
    $('#someId').on('resizeme.zf.trigger', handleResize);
    ```

    ## Throttle
    `js/foundation.core.js`

    Many times when you create a callback, it's advantageous to add a delay in order to prevent it from being triggered multiple times. Foundation includes one type of callback delay: `throttle`.

    `Throttle` prevents a function from being executed more than once every n milliseconds. Throttling is often used in cases where it's disadvantageous to trigger a callback every time an event is triggered (during a continuous action), but you still want to trigger a reaction while the event is occurring. Examples of this would be reacting to the browser window being resized, or animating an element.

    ### Without Delay
    ```js
    // Button click handler
    $('.button').on('click', function(e){
      // Handle Click
    });

    // Resize function
    $(window).on('resize', function(e){
      // Do responsive stuff
    });
    ```

    ### With Delay
    ```js
    // Throttled resize function
    $(window).on('resize', Foundation.util.throttle(function(e){
      // Do responsive stuff
    }, 300));
    ```

    ### Method Signature
    ```js
    // Arguments:
    //    Func (Function): Function to be throttled.
    //
    //    Delay (Integer): Function execution threshold in milliseconds.
    //
    // Returns:
    //    Lazy_function (Function): Function with throttling applied.

    throttle(func, delay) { ... }
    ```

    ## Miscellaneous

    Foundation includes a couple useful features in the core library that are used in many places, that you can tap into.

    `Foundation.GetYoDigits([number, namespace])` returns a base-36, pseudo-random string with a hyphenated namespace (if you include one). Both arguments are optional; by default, it will return a string six characters long.

    `Foundation.getFnName(fn)` returns a string representation of a named function. Seems small, but believe us—it's useful.

    `Foundation.transitionend()` is a function<span data-tooltip title="Goodbye ZURB, I'll miss you"> </span> that returns the string of the properly vendor-prefixed version of `transitionend` events. Most browsers don't require a prefix these days, but for those that do, we've got you covered. But IE 9 doesn't support transitions?? Quite right you are! In that case, our plugins that use transitions will simply snap to whatever location or visibility state they were headed to, and this function will fire a `transitionend` event manually on the element you passed. It still gives the desired results, and allows Motion-UI to work in IE 9.
    """

    pass


class JAVASCRIPT:
    """---
    title: JavaScript
    description: Our JavaScript is easy to set up and only requires jQuery to get going.
    video: 'Mf5ZZfKTe-I'
    ---

    ## Installing

    You can get the Foundation JavaScript files from a ZIP download, package manager, or CDN. Check out the [Installation](installation.html) page to learn more.

    Once you have the files, add links to jQuery and Foundation as `<script>` tags at the bottom of your page, just before the closing `<body>` tag.

    ```html
    <!-- jQuery must be imported before Foundation -->
    <script src="js/jquery.min.js"></script>
    <!-- this will include every plugin and utility required by Foundation -->
    <script src="js/foundation.min.js"></script>
    ```


    ### Import in HTML

    You can import in your HTML the complete Foundation library `foundation.min.js` like above, but also each plugin individually.

    ```html
    <!-- Example of selectively including files -->
    <script src="js/jquery.min.js"></script> <!-- Required -->
    <script src="js/foundation.core.min.js"></script>  <!-- Required -->
    <script src="js/foundation.util.mediaQuery.min.js"></script>
    <script src="js/foundation.tabs.min.js"></script>
    <script src="js/foundation.accordion.min.js"></script>
    ```

    Know that they all require `foundation.core.js` to be loaded *first*. Some plugins also require specific utility libraries that ship with Foundation&mdash;refer to a plugin's documentation to find out which plugins require what, and see the [JavaScript Utilities](javascript-utilities.html) page for more information.

    <div class="callout warning">
      <p>Loading many individual files like this creates a lot of network overhead, especially for users on mobile networks. To keep your pages loading quick, we recommend using a tool like <a href="https://gruntjs.com">Grunt</a> or <a href="https://gulpjs.com">Gulp</a> to combine all of your JavaScript files into one.</p>
    </div>

    ### Import in JavaScript

    By default, Foundation is exported as [UMD modules](http://bob.yexley.net/umd-javascript-that-runs-anywhere/). This means that Foundation and its plugins can be imported and used in any JavaScript environment.

    For example with [ES6](https://github.com/lukehoban/es6features#readme) (the ESM format):
    ```js
    import Foundation from 'foundation-sites';
    const $dropdown = new Foundation.Dropdown($('#mydropdown'));
    // Or
    import { Dropdown } from 'foundation-sites';
    const $dropdown = new Dropdown($('#mydropdown'));
    ```

    With [RequireJs](https://requirejs.org/) (the AMD format):
    ```js
    define(['foundation'], function(Foundation) {
      var $dropdown = new Foundation.Dropdown($('#mydropdown'));
    });
    ```

    With [Node.js](https://www.safaribooksonline.com/library/view/learning-javascript-design/9781449334840/ch11s03.html) (the CommonJs format):
    ```js
    var Foundation = require('foundation-sites');
    var $dropdown = new Dropdown($('#mydropdown'));
    ```

    #### Available formats

    Foundation is provided in bundles of various module formats so you can pick the one that matches the best your needs. If you don't know these terms yet, take a look at this [10-minute introduction to module formats in JavaScript](https://www.jvandemo.com/a-10-minute-primer-to-javascript-modules-module-formats-module-loaders-and-module-bundlers/). You will find in the `dist/js` folder the following bundles:

    * `foundation.js` <span class="label secondary">UMD</span> <span class="label">Default</span><br>
      Compatible with most environments and tools (AMD, CJS, ESM...). It works almost everywhere by checking the module format of your environments and then using it, which makes the bundle a little heavier.

    * `foundation.cjs.js` <span class="label secondary">CommonJS</span><br>
      Dedicated to Node.js and older bundlers like Browserify or Webpack v1.

    * `foundation.esm.js` <span class="label secondary">ES6 Modules</span>  (`module` in `package.json`)<br>
      Everything is transpiled to ES5 but the modules. Dedicated to modern bundlers, like Webpack 2+ or Rollup. They will automatically use this bundle and parse the ES6 modules to remove the unused code (see [tree shaking](#tree-shaking) below).

    * `foundation.es6.js` <span class="label secondary">ES6</span> (`esnext` in `package.json`)<br>
      Unlike the other bundles, this bundle is not transpiled. It contains all the Foundation sources in ES6 in a single file. Use it if you want to manually transpile it for your own targets.

    #### Tree Shaking

    Many bundlers like Webpack, Rollup or Parcel support tree shaking. It consists of the removing the unused code parts from your codebase or your dependencies. Take a look at these articles to know how it works and how to enable it: [How To Clean Up Your JavaScript Build With Tree Shaking](https://www.engineyard.com/blog/tree-shaking), [Why Webpack 2's Tree Shaking is not as effective as you think](https://advancedweb.hu/2017/02/07/treeshaking/) and [Reduce JavaScript Payloads with Tree Shaking](https://developers.google.com/web/fundamentals/performance/optimizing-javascript/tree-shaking/).

    As tree shaking is only available in ES6, we recommend to import plugins like the following:

    ```js
    // Only Dropdown and DropdownMenu will be included in your application.
    import { Dropdown, DropdownMenu } from 'foundation-sites';
    ```

    Sadly, the "static analysis" promised by these bundlers to detect unused code in dependencies does not always work. Depending on your build environment, you may have to manually import the Foundation plugins to make it work correctly:

    ```js
    // /!\ Don't use this if tree shaking works with standard named imports.
    // Only Dropdown and DropdownMenu will be included in your application.
    import { Dropdown } from 'foundation-sites/js/foundation.dropdown';
    import { DropdownMenu } from 'foundation-sites/js/foundation.dropdownMenu';
    ```

    ---

    ## Initializing

    The `.foundation()` function on the jQuery object will kick off every Foundation plugin at once.

    ```js
    $(document).foundation();
    ```

    You can also selectively initialize plugins by calling the `.foundation();` method on one or more elements with a plugin.

    ```js
    $('#foo').foundation(); // initialize all plugins within the element `#foo`
    $('.has-tip').foundation(); // initialize all tooltips on the page.
    ```

    ---

    ## Using Plugins

    Plugins are attached to HTML elements using data attributes. The data attribute will match the name of the plugin. For example, adding `data-accordion` to an element creates an accordion, while adding `data-tooltip` creates a tooltip link.

    ```html
    <p><span data-tooltip aria-haspopup="true" class="has-tip" tabindex="1" title="Fancy word for a beetle.">Scarabaeus</span></p>
    ```

    <div class="callout warning">
      <p>A single element can only have one Foundation plugin on it at a time. However, most plugins can be nested inside other ones.</p>
    </div>

    ---

    ## Configuring Plugins

    Each plugin has a set of configuration settings that customize how it works. For example, you change how fast an [accordion](accordion.html) slides up and down, or if [tooltips](tooltip.html) should appear on touch devices.

    Plugin settings can be changed globally by changing the `DEFAULTS` property on the plugin.

    ```js
    Foundation.Accordion.defaults.slideSpeed = 500;
    Foundation.Accordion.defaults.multiExpand = true;
    ```

    An individual instance of a plugin can also have different settings. These can be set in the HTML or in JavaScript.
    <div class="callout warning">
      <p>In the HTML, each setting can be defined as an individual data attribute. Note that camelCased options are converted to hyphenated words. In the below example, `multiExpand` becomes `data-multi-expand`.</p>
    </div>

    ```html
    <div data-accordion data-slide-speed="500" data-multi-expand="true"></div>
    ```

    Data options can also be set in bulk on one attribute, `data-options`. Options are written with the format `key: value;`, with a semicolon separating each option. The above example can be written using `data-options` like so:

    ```html
    <div data-accordion data-options="slideSpeed: 500; multiExpand: true;"></div>
    ```
    There is one exception to this rule above, in the [Sticky](sticky.html) plugin. Because of the way you pass top and bottom anchors to that plugin, you can't include them in your `data-options` attribute. If you are using a single anchor or no declared anchor at all, you can still use `data-options`, and you can use it for all other options available.

    <hr>
    Setting options with JavaScript involves passing an object into the constructor function, like this:

    ```js
    var options = {multiExpand: true, allowAllClosed: false};
    var accordion = new Foundation.Accordion($('#some-accordion'), options);
    ```

    It's worth noting that options passed to plugins via JavaScript take the highest precedence, and will overwrite any default values or options applied via the `data-some-option` tag. This is also how the `data-options="someOption:true; someOtherOption:false"` options are passed into constructor functions. So, if you were to say:
    ```html
    <div data-accordion data-slide-speed="500" data-options="slideSpeed:250;">...</div>
    ```
    your accordion element would have a slide speed of 250 milliseconds.

    ---

    ## Adding Plugins After Page Load

    If you add new HTML to the DOM, any plugins on those elements won't be initialized by default. Re-call the `.foundation()` function to check for new plugins.

    ```js
    $.ajax('assets/partials/kitten-carousel.html', function(data) {
      $('#kitten-carousel').html(data).foundation();
    });
    ```

    Plugins that are already initialized will be ignored. However for performance reasons, we recommend calling `.foundation()` only on the DOM nodes that changed.

    ---

    ## Adding Content to Plugins

    In previous versions of Foundation, there was a method for plugins called `reflow`, though it's inclusion on plugins wasn't universal. For Foundation 6 we've added a global `reInit` method that will remove and reapply event listeners, update the plugin's instance data for relevant information, like a new tab or content pane being added, and reset any cached data the plugin may rely on.

    This method can be called on a plugin class:
    ```js
    Foundation.reInit('tooltip');
    ```
    an array of plugin classes:
    ```js
    Foundation.reInit(['tooltip', 'accordion', 'reveal']);
    ```
    or an individual element or collection of elements selected with jQuery:
    ```js
    Foundation.reInit($('#some-plugin'));
    Foundation.reInit($('.some-plugin-class'));
    ```

    If passing strings, it is required to pass proper <strong>camelCased</strong> or <strong>kebab-cased</strong> plugin names. Passing `DropdownMenu` or `dropdown-menu` are equivalent.

    ---

    ## Programmatic Use

    Plugins can be created programmatically in JavaScript. Every plugin is a class on the global `Foundation` object, with a constructor that accepts two parameters: an element to attach to, and an object of options.

    ```js
    var $accordion = new Foundation.Accordion($('#accordion'), {
      slideSpeed: 500,
      multiExpand: true
    });
    ```

    Most plugins have a public API that allows you to manipulate it through JavaScript. Refer to a plugin's documentation to learn what functions are available. Invoking methods is easy as pie:

    ```js
    $('#reveal').foundation('open'); //will open a Reveal modal with id `reveal`.

    $('[data-tabs]').eq(0).foundation('selectTab', $('#example')); //will change the first Tabs on the page to whatever panel you choose.

    $('.tooltip').foundation('_destroy'); //will destroy all Tooltips on the page.

    ```
    You can use any jQuery selector you like, and if the selector encompasses multiple plugins, they will all have the same the chosen method invoked. You pass arguments just like you would any in other JavaScript `function(comma, delimited, so, easy)`. We did make an effort to reduce the number of public methods that require arguments, but check the plugin's page to see if it requires additional information.

    If you are creating your plugins programmatically, you can, of course, invoke methods directly:

    ```js
    var $modal = new Foundation.Reveal($('#some-modal'), options);
    $modal.open();
    ```

    <div class="callout warning">
      <p>Plugin methods prefixed with an underscore are considered part of the internal API, which means they could change, break, or disappear without warning. We recommend sticking to only the public API, which is documented on each plugin's page.</p>
    </div>

    ---

    ## Events

    Every plugin fires DOM events when certain functions finish. For example, you can listen for when tabs change, or an off-canvas menu opens, and create a callback to respond to it.

    ```js
    $('[data-tabs]').on('change.zf.tabs', function() {
      console.log('Those tabs sure did change!');
    });
    ```

    Refer to each plugin's documentation to see a list of events it fires, and when they fire.

    <div class="callout warning">
      <p>Starting with Foundation 6, we removed callbacks as plugin settings. All use of callbacks with plugins should be done as event listeners.</p>
    </div>"""

    pass


class KITCHEN_SINK:
    """---
    title: Kitchen Sink
    description: Everything but.
    ---

    ## Abide


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/qmoKbK?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <form data-abide novalidate>
      <div class="grid-x grid-margin-x">
        <div class="cell">
          <div data-abide-error class="alert callout" style="display: none;">
            <p><i class="fi-alert"></i> There are some errors in your form.</p>
          </div>
        </div>
      </div>
      <div class="grid-x grid-margin-x">
        <div class="cell small-12">
          <label>Number Required
            <input type="text" placeholder="1234" aria-describedby="exampleHelpTextNumber" required pattern="number">
            <span class="form-error">
              Yo, you had better fill this out, it's required.
            </span>
          </label>
          <p class="help-text" id="exampleHelpTextNumber">Here's how you use this input field!</p>
        </div>
        <div class="cell small-12">
          <label>Nothing Required!
            <input type="text" placeholder="Use me, or don't" aria-describedby="exampleHelpTextNothing" data-abide-ignore>
          </label>
          <p class="help-text" id="exampleHelpTextNothing">This input is ignored by Abide using `data-abide-ignore`</p>
        </div>
        <div class="cell small-12">
          <label>Password Required
            <input type="password" id="password" placeholder="yeti4preZ" aria-describedby="exampleHelpTextPassword" required >
            <span class="form-error">
              I'm required!
            </span>
          <p class="help-text" id="exampleHelpTextPassword">Enter a password please.</p>
          </label>
        </div>
        <div class="cell small-12">
          <label>Re-enter Password
            <input type="password" placeholder="yeti4preZ" aria-describedby="exampleHelpText2" required pattern="alpha_numeric" data-equalto="password">
            <span class="form-error">
              Hey, passwords are supposed to match!
            </span>
          </label>
          <p class="help-text" id="exampleHelpText2">This field is using the `data-equalto="password"` attribute, causing it to match the password field above.</p>
        </div>
      </div>
      <div class="grid-x grid-margin-x">
        <div class="cell medium-6">
          <label>URL Pattern, not required, but throws error if it doesn't match the Regular Expression for a valid URL.
            <input type="text" placeholder="https://get.foundation" pattern="url">
          </label>
        </div>
        <div class="cell medium-6">
          <label>European Cars, Choose One, it can't be the blank option.
            <select id="select" required>
              <option value=""></option>
              <option value="volvo">Volvo</option>
              <option value="saab">Saab</option>
              <option value="mercedes">Mercedes</option>
              <option value="audi">Audi</option>
            </select>
          </label>
        </div>
      </div>
      <div class="grid-x grid-margin-x">
        <fieldset class="cell medium-6">
          <legend>Choose Your Favorite, and this is required, so you have to pick one.</legend>
          <input type="radio" name="pokemon" value="Red" id="pokemonRed"><label for="pokemonRed">Red</label>
          <input type="radio" name="pokemon" value="Blue" id="pokemonBlue" required><label for="pokemonBlue">Blue</label>
          <input type="radio" name="pokemon" value="Yellow" id="pokemonYellow"><label for="pokemonYellow">Yellow</label>
        </fieldset>
        <fieldset class="cell medium-6">
          <legend>Choose Your Favorite - not required, you can leave this one blank.</legend>
          <input type="radio" name="pockets" value="Red" id="pocketsRed"><label for="pocketsRed">Red</label>
          <input type="radio" name="pockets" value="Blue" id="pocketsBlue"><label for="pocketsBlue">Blue</label>
          <input type="radio" name="pockets" value="Yellow" id="pocketsYellow"><label for="pocketsYellow">Yellow</label>
        </fieldset>
        <fieldset class="cell medium-6">
          <legend>Check these out</legend>
          <input id="checkbox1" type="checkbox"><label for="checkbox1">Checkbox 1</label>
          <input id="checkbox2" type="checkbox" required><label for="checkbox2">Checkbox 2</label>
          <input id="checkbox3" type="checkbox"><label for="checkbox3">Checkbox 3</label>
        </fieldset>
      </div>
      <div class="grid-x grid-margin-x">
        <fieldset class="cell medium-6">
          <button class="button" type="submit" value="Submit">Submit</button>
        </fieldset>
        <fieldset class="cell medium-6">
          <button class="button" type="reset" value="Reset">Reset</button>
        </fieldset>
      </div>
    </form>
    ```

    ---

    ## Accordion


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/WjzKqa?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="accordion" data-accordion>
      <li class="accordion-item is-active" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 1</a>
        <div class="accordion-content" data-tab-content >
          <p>Panel 1. Lorem ipsum dolor</p>
          <a href="#">Nowhere to Go</a>
        </div>
      </li>
      <li class="accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 2</a>
        <div class="accordion-content" data-tab-content>
          <textarea></textarea>
          <button class="button">I do nothing!</button>
        </div>
      </li>
      <li class="accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 3</a>
        <div class="accordion-content" data-tab-content>
          Type your name!
          <input type="text">
        </div>
      </li>
    </ul>
    ```


    ---

    ## Accordion Menu


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/XREPVK?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="vertical menu" data-accordion-menu>
      <li>
        <a href="#0">Item 1</a>
        <ul class="menu vertical nested is-active">
          <li>
            <a href="#0">Item 1A</a>
            <ul class="menu vertical nested">
              <li><a href="#0">Item 1Ai</a></li>
              <li><a href="#0">Item 1Aii</a></li>
              <li><a href="#0">Item 1Aiii</a></li>
            </ul>
          </li>
          <li><a href="#0">Item 1B</a></li>
          <li><a href="#0">Item 1C</a></li>
        </ul>
      </li>
      <li>
        <a href="#0">Item 2</a>
        <ul class="menu vertical nested">
          <li><a href="#0">Item 2A</a></li>
          <li><a href="#0">Item 2B</a></li>
        </ul>
      </li>
      <li><a href="#0">Item 3</a></li>
    </ul>
    ```

    ---

    ## Badge


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/JNvKZj?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <span class="primary badge">1</span>
    <span class="secondary badge">2</span>
    <span class="success badge">3</span>
    <span class="alert badge">A</span>
    <span class="warning badge">B</span>
    ```

    ---

    ## Breadcrumbs


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/MmGeMx?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <nav aria-label="You are here:" role="navigation">
      <ul class="breadcrumbs">
        <li><a href="#0">Home</a></li>
        <li><a href="#0">Features</a></li>
        <li class="disabled">Gene Splicing</li>
        <li>
          <span class="show-for-sr">Current: </span> Cloning
        </li>
      </ul>
    </nav>
    ```

    ---

    ## Button


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/ybjagd?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <!-- Anchors (links) -->
    <a href="#0" class="button">Learn More</a>
    <a href="#features" class="button">View All Features</a>

    <!-- Buttons (actions) -->
    <button type="button" class="success button">Save</button>
    <button type="button" class="alert button">Delete</button>

    <a class="tiny button" href="#0">So Tiny</a>
    <a class="small button" href="#0">So Small</a>
    <a class="large button" href="#0">So Large</a>
    <a class="expanded button" href="#0">Such Expand</a>

    <div class="button-group">
      <a class="button">One</a>
      <a class="button">Two</a>
      <a class="button">Three</a>
    </div>
    ```

    ---

    ## Callout


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/XRqjxj?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="callout">
      <h5>This is a callout.</h5>
      <p>It has an easy to override visual style, and is appropriately subdued.</p>
      <a href="#0">It's dangerous to go alone, take this.</a>
    </div>

    <div class="callout primary">
      <h5>This is a primary callout.</h5>
      <p>It has an easy to override visual style, and is appropriately subdued.</p>
      <a href="#0">It's dangerous to go alone, take this.</a>
    </div>

    <div class="callout secondary">
      <h5>This is a secondary callout</h5>
      <p>It has an easy to override visual style, and is appropriately subdued.</p>
      <a href="#0">It's dangerous to go alone, take this.</a>
    </div>

    <div class="callout success">
      <h5>This is a success callout</h5>
      <p>It has an easy to override visual style, and is appropriately subdued.</p>
      <a href="#0">It's dangerous to go alone, take this.</a>
    </div>

    <div class="callout warning">
      <h5>This is a warning callout</h5>
      <p>It has an easy to override visual style, and is appropriately subdued.</p>
      <a href="#0">It's dangerous to go alone, take this.</a>
    </div>

    <div class="callout alert">
      <h5>This is an alert callout</h5>
      <p>It has an easy to override visual style, and is appropriately subdued.</p>
      <a href="#0">It's dangerous to go alone, take this.</a>
    </div>
    ```

    ---

    ## Close Button


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/dWepJz?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="callout" data-closable>
      <button class="close-button" aria-label="Close alert" type="button" data-close>
        <span aria-hidden="true">&times;</span>
      </button>
      <p>This is a close button example.</p>
    </div>
    ```

    ---

    ## Drilldown Menu


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/mmLrZz?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="vertical menu" data-drilldown style="width: 200px" id="m1">
      <li>
        <a href="#0">Item 1</a>
        <ul class="vertical menu" id="m2">
          <li>
            <a href="#0">Item 1A</a>
            <ul class="vertical menu" id="m3">
              <li><a href="#0">Item 1Aa</a></li>
              <li><a href="#0">Item 1Ba</a></li>
              <li><a href="#0">Item 1Ca</a></li>
              <li><a href="#0">Item 1Da</a></li>
              <li><a href="#0">Item 1Ea</a></li>
            </ul>
          </li>
          <li><a href="#0">Item 1B</a></li>
          <li><a href="#0">Item 1C</a></li>
          <li><a href="#0">Item 1D</a></li>
          <li><a href="#0">Item 1E</a></li>
        </ul>
      </li>
      <li>
        <a href="#0">Item 2</a>
        <ul class="vertical menu">
          <li><a href="#0">Item 2A</a></li>
          <li><a href="#0">Item 2B</a></li>
          <li><a href="#0">Item 2C</a></li>
          <li><a href="#0">Item 2D</a></li>
          <li><a href="#0">Item 2E</a></li>
        </ul>
      </li>
      <li>
        <a href="#0">Item 3</a>
        <ul class="vertical menu">
          <li><a href="#0">Item 3A</a></li>
          <li><a href="#0">Item 3B</a></li>
          <li><a href="#0">Item 3C</a></li>
          <li><a href="#0">Item 3D</a></li>
          <li><a href="#0">Item 3E</a></li>
        </ul>
      </li>
      <li><a href='#0'> Item 4</a></li>
    </ul>
    ```

    ---

    ## Dropdown Menu


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/jmxVPP?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="dropdown menu" data-dropdown-menu>
      <li>
        <a>Item 1</a>
        <ul class="menu">
          <li><a href="#0">Item 1A Loooong</a></li>
          <li>
            <a href='#0'> Item 1 sub</a>
            <ul class="menu">
              <li><a href='#0'>Item 1 subA</a></li>
              <li><a href='#0'>Item 1 subB</a></li>
              <li>
                <a href='#0'> Item 1 sub</a>
                <ul class="menu">
                  <li><a href='#0'>Item 1 subA</a></li>
                  <li><a href='#0'>Item 1 subB</a></li>
                </ul>
              </li>
              <li>
                <a href='#0'> Item 1 sub</a>
                <ul class="menu">
                  <li><a href='#0'>Item 1 subA</a></li>
                </ul>
              </li>
            </ul>
          </li>
          <li><a href="#0">Item 1B</a></li>
        </ul>
      </li>
      <li>
        <a href="#0">Item 2</a>
        <ul class="menu">
          <li><a href="#0">Item 2A</a></li>
          <li><a href="#0">Item 2B</a></li>
        </ul>
      </li>
      <li><a href="#0">Item 3</a></li>
      <li><a href='#0'>Item 4</a></li>
    </ul>
    ```

    ---

    ## Dropdown Pane


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/QvrGGj?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <button class="button" type="button" data-toggle="example-dropdown">Toggle Dropdown</button>
    <div class="dropdown-pane" id="example-dropdown" data-dropdown>
      Just some junk that needs to be said. Or not. Your choice.
    </div>
    ```

    ---

    ## Equalizer


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/mmLBEa?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-margin-x" data-equalizer data-equalize-on="medium" id="test-eq">
      <div class="cell medium-4">
        <div class="callout" data-equalizer-watch>
          <img src= "assets/img/generic/square-1.jpg" alt="">
        </div>
      </div>
      <div class="cell medium-4">
        <div class="callout" data-equalizer-watch>
          <p>Pellentesque habitant morbi tristique senectus et netus et, ante.</p>
        </div>
      </div>
      <div class="cell medium-4">
        <div class="callout" data-equalizer-watch>
          <img src= "assets/img/generic/rectangle-1.jpg" alt="">
        </div>
      </div>
    </div>
    ```

    ---

    ## Flex Grid


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/dWmVax?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="small-6 columns">6 columns</div>
      <div class="small-6 columns">6 columns</div>
    </div>
    <div class="row">
      <div class="medium-6 large-4 columns">12/6/4 columns</div>
      <div class="medium-6 large-8 columns">12/6/8 columns</div>
    </div>
    ```

    <div class="row display">
      <div class="small-6 columns">6 columns</div>
      <div class="small-6 columns">6 columns</div>
    </div>
    <div class="row display">
      <div class="medium-6 large-4 columns">12/6/4 columns</div>
      <div class="medium-6 large-8 columns">12/6/8 columns</div>
    </div>

    ---

    ## Responsive Embed


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/MmGEbb?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="responsive-embed">
      <iframe width="420" height="315" src="https://www.youtube.com/embed/mM5_T-F1Yn4" frameborder="0" allowfullscreen></iframe>
    </div>
    ```

    ---

    ## Float Classes


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/zwjEPP?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="callout clearfix">
      <a class="button float-left">Left</a>
      <a class="button float-right">Right</a>
    </div>
    ```

    ---

    ## Forms


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/jmxGGr?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <form>
      <label>Input Label
        <input type="text" placeholder=".small-12.columns" aria-describedby="exampleHelpText">
      </label>
      <p class="help-text" id="exampleHelpText">Here's how you use this input field!</p>
      <label>
        How many puppies?
        <input type="number" value="100">
      </label>
      <label>
        What books did you read over summer break?
        <textarea placeholder="None"></textarea>
      </label>
      <label>Select Menu
        <select>
          <option value="husker">Husker</option>
          <option value="starbuck">Starbuck</option>
          <option value="hotdog">Hot Dog</option>
          <option value="apollo">Apollo</option>
        </select>
      </label>
      <div class="grid-x grid-margin-x">
        <fieldset class="cell large-6">
          <legend>Choose Your Favorite</legend>
          <input type="radio" name="pokemon" value="Red" id="formRed" required><label for="formRed">Red</label>
          <input type="radio" name="pokemon" value="Blue" id="formBlue"><label for="formBlue">Blue</label>
          <input type="radio" name="pokemon" value="Yellow" id="formYellow"><label for="formYellow">Yellow</label>
        </fieldset>
        <fieldset class="cell large-6">
          <legend>Check these out</legend>
          <input id="formCheckbox1" type="checkbox"><label for="formCheckbox1">Checkbox 1</label>
          <input id="formCheckbox2" type="checkbox"><label for="formCheckbox2">Checkbox 2</label>
          <input id="formCheckbox3" type="checkbox"><label for="formCheckbox3">Checkbox 3</label>
        </fieldset>
      </div>
      <div class="grid-x grid-margin-x">
        <div class="cell small-3">
          <label for="middle-label" class="text-right middle">Label</label>
        </div>
        <div class="cell small-9">
          <input type="text" id="middle-label" placeholder="Right- and middle-aligned text input">
        </div>
      </div>
      <div class="input-group">
        <span class="input-group-label">$</span>
        <input class="input-group-field" type="url">
        <div class="input-group-button">
          <input type="submit" class="button" value="Submit">
        </div>
      </div>
    </form>
    ```

    ---

    ## Grid


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/rmvEBJ?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="small-2 medium-3 large-4 columns">2/3/4 columns</div>
      <div class="small-4 medium-3 large-4 columns">4/3/4 columns</div>
      <div class="small-6 large-4 columns">6/6/4 columns</div>
    </div>
    <div class="row">
      <div class="large-3 columns">12/12/3 columns</div>
      <div class="large-6 columns">12/12/6 columns</div>
      <div class="large-3 columns">12/12/3 columns</div>
    </div>
    <div class="row">
      <div class="small-6 large-2 columns">6/6/2 columns</div>
      <div class="small-6 large-8 columns">6/6/8 columns</div>
      <div class="small-12 large-2 columns">12/12/2 columns</div>
    </div>
    <div class="row">
      <div class="small-3 columns">3 columns</div>
      <div class="small-9 columns">9 columns</div>
    </div>
    <div class="row">
      <div class="medium-8 large-4 columns">12/8/4 columns</div>
      <div class="medium-4 large-8 columns">12/4/8 columns</div>
    </div>
    ```

    <div class="row display">
      <div class="small-2 medium-3 large-4 columns">2/3/4 columns</div>
      <div class="small-4 medium-3 large-4 columns">4/3/4 columns</div>
      <div class="small-6 large-4 columns">6/6/4 columns</div>
    </div>
    <div class="row display">
      <div class="large-3 columns">12/12/3 columns</div>
      <div class="large-6 columns">12/12/6 columns</div>
      <div class="large-3 columns">12/12/3 columns</div>
    </div>
    <div class="row display">
      <div class="small-6 large-2 columns">6/6/2 columns</div>
      <div class="small-6 large-8 columns">6/6/8 columns</div>
      <div class="small-12 large-2 columns">12/12/2 columns</div>
    </div>
    <div class="row display">
      <div class="small-3 columns">3 columns</div>
      <div class="small-9 columns">9 columns</div>
    </div>
    <div class="row display">
      <div class="medium-8 large-4 columns">12/8/4 columns</div>
      <div class="medium-4 large-8 columns">12/4/8 columns</div>
    </div>

    ---

    ## Interchange


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/xdjXYj?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <img data-interchange="[assets/img/interchange/small.jpg, small], [assets/img/interchange/medium.jpg, medium], [assets/img/interchange/large.jpg, large]" src="#" alt="">
    ```

    ---

    ## Label


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/VbxMXq?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <span class="primary label">Primary Label</span>
    <span class="secondary label">Secondary Label</span>
    <span class="success label">Success Label</span>
    <span class="alert label">Alert Label</span>
    <span class="warning label">Warning Label</span>
    ```

    ---

    ## Magellan


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/MmGEXo?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="horizontal menu" data-magellan>
      <li><a href="#first">First Arrival</a></li>
      <li><a href="#second">Second Arrival</a></li>
      <li><a href="#third">Third Arrival</a></li>
    </ul>
    <div class="sections">
      <section id="first" data-magellan-target="first">
        <h4>First section</h4>
        <p>Duis scelerisque ligula ut metus rhoncus scelerisque. Integer ut egestas metus. Nulla facilisi. Aenean luctus magna lobortis ligula rhoncus, sit amet lacinia lorem sagittis. Sed ultrices at metus id aliquet. Vestibulum in condimentum quam, id ornare erat. Vivamus nec justo quis ex fringilla condimentum ac non quam.</p>
      </section>
      <section id="second" data-magellan-target="second">
        <h4>Second section</h4>
        <p>Sed vulputate, felis interdum molestie viverra, neque urna placerat dui, ac efficitur est magna eu tellus. Nunc sodales consequat eros at bibendum. Vestibulum hendrerit gravida elit non eleifend. Nunc at vehicula ipsum. Vestibulum eu suscipit felis. Proin ipsum felis, consequat congue quam ac, efficitur tincidunt ex. Morbi accumsan sem iaculis nunc malesuada tincidunt.</p>
      </section>
      <section id="third" data-magellan-target="third">
        <h4>Third section</h4>
        <p>Aliquam orci orci, maximus a pulvinar id, tincidunt a neque. Suspendisse eros diam, finibus et faucibus ac, suscipit feugiat orci. Morbi scelerisque sem id blandit malesuada. Donec suscipit tincidunt dolor in blandit. Nam rhoncus risus vitae lacinia dictum. Cras lobortis, nulla non faucibus mattis, tellus nibh condimentum eros, posuere volutpat arcu risus vel ante. In ut ullamcorper eros, et vestibulum risus. Fusce auctor risus vitae diam viverra tincidunt.</p>
      </section>
    </div>
    ```

    <ul class="horizontal menu" data-magellan>
      <li><a href="#first">First Arrival</a></li>
      <li><a href="#second">Second Arrival</a></li>
      <li><a href="#third">Third Arrival</a></li>
    </ul>

    ---

    ## Media Object


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/NjMaEr?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="media-object">
      <div class="media-object-section">
        <img src= "https://placeimg.com/200/200/people" alt="">
      </div>
      <div class="media-object-section">
        <h4>Dreams feel real while we're in them.</h4>
        <p>I'm going to improvise. Listen, there's something you should know about me... about inception. An idea is like a virus, resilient, highly contagious. The smallest seed of an idea can grow. It can grow to define or destroy you.</p>
      </div>
    </div>
    ```

    ---

    ## Menu


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/bWMMzZ?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="menu">
      <li><a href="#0"><i class="fi-list"></i> <span>One</span></a></li>
      <li><a href="#0"><i class="fi-list"></i> <span>Two</span></a></li>
      <li><a href="#0"><i class="fi-list"></i> <span>Three</span></a></li>
      <li><a href="#0"><i class="fi-list"></i> <span>Four</span></a></li>
    </ul>
    ```

    ---

    ## Off-canvas


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/oWdrLR?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <!-- Set up Off-canvas -->
    <body>
      <div class="off-canvas-wrapper">
        <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>
          <div class="off-canvas position-left" id="offCanvasLeft" data-off-canvas>
            <!-- left off-canvas markup -->
          </div>
          <div class="off-canvas position-right" id="offCanvasRight" data-off-canvas data-position="right">
            <!-- right off-canvas markup -->
          </div>
          <div class="off-canvas-content" data-off-canvas-content>
            <!-- page content -->
          </div>
        </div>
      </div>
    </body>

    <!-- Fire Off-canvas -->
    <button type="button" class="button" data-toggle="offCanvasLeft">Open Menu</button>
    ```

    ---

    ## Orbit


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/zwjjgN?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="orbit" role="region" aria-label="Favorite Text Ever" data-orbit>
      <ul class="orbit-container">
        <button class="orbit-previous" aria-label="previous"><span class="show-for-sr">Previous Slide</span>&#9664;</button>
        <button class="orbit-next" aria-label="next"><span class="show-for-sr">Next Slide</span>&#9654;</button>
        <li class="is-active orbit-slide">
          <div class="docs-example-orbit-slide">
            <p><strong>This is dodgerblue.</strong> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
          </div>
        </li>
        <li class="orbit-slide">
          <div class="docs-example-orbit-slide">
            <p><strong>This is rebeccapurple.</strong> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
          </div>
        </li>
        <li class="orbit-slide">
          <div class="docs-example-orbit-slide">
            <p><strong>This is darkgoldenrod.</strong> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
          </div>
        </li>
        <li class="orbit-slide">
          <div class="docs-example-orbit-slide">
            <p><strong>This is lightseagreen.</strong> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
          </div>
        </li>
      </ul>
      <nav class="orbit-bullets">
        <button class="is-active" data-slide="0">
          <span class="show-for-sr">First slide details.</span>
          <span class="show-for-sr" data-slide-active-label>Current Slide</span>
        </button>
        <button data-slide="1"><span class="show-for-sr">Second slide details.</span></button>
        <button data-slide="2"><span class="show-for-sr">Third slide details.</span></button>
        <button data-slide="3"><span class="show-for-sr">Fourth slide details.</span></button>
      </nav>
    </div>
    ```

    ---

    ## Pagination


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/BRxVmB?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="pagination" role="navigation" aria-label="Pagination">
      <li class="disabled">Previous <span class="show-for-sr">page</span></li>
      <li class="current"><span class="show-for-sr">You're on page</span> 1</li>
      <li><a href="#0" aria-label="Page 2">2</a></li>
      <li><a href="#0" aria-label="Page 3">3</a></li>
      <li><a href="#0" aria-label="Page 4">4</a></li>
      <li class="ellipsis" aria-hidden="true"></li>
      <li><a href="#0" aria-label="Page 12">12</a></li>
      <li><a href="#0" aria-label="Page 13">13</a></li>
      <li><a href="#0" aria-label="Next page">Next <span class="show-for-sr">page</span></a></li>
    </ul>
    ```

    ---

    ## Progress Bar


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/YVLvvB?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="primary progress" role="progressbar" tabindex="0" aria-valuenow="25" aria-valuemin="0" aria-valuetext="25 percent" aria-valuemax="100">
      <div class="progress-meter" style="width: 25%">
        <p class="progress-meter-text">25%</p>
      </div>
    </div>

    <div class="warning progress">
      <div class="progress-meter" style="width: 50%">
        <p class="progress-meter-text">50%</p>
      </div>
    </div>

    <div class="alert progress">
      <div class="progress-meter" style="width: 75%">
        <p class="progress-meter-text">75%</p>
      </div>
    </div>

    <div class="success progress" role="progressbar" tabindex="0" aria-valuenow="100" aria-valuemin="0" aria-valuetext="100 percent" aria-valuemax="100">
      <div class="progress-meter" style="width: 100%">
        <p class="progress-meter-text">100%</p>
      </div>
    </div>
    ```

    ---

    ## Responsive Menu


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/qmYKgJ?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="vertical medium-horizontal menu">
      <li><a href="#0"><i class="fi-list"></i> <span>One</span></a></li>
      <li><a href="#0"><i class="fi-list"></i> <span>Two</span></a></li>
      <li><a href="#0"><i class="fi-list"></i> <span>Three</span></a></li>
      <li><a href="#0"><i class="fi-list"></i> <span>Four</span></a></li>
    </ul>
    ```

    ---

    ## Responsive Toggle


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/LymroM?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="title-bar" data-responsive-toggle="example-menu" data-hide-for="medium">
      <button class="menu-icon" type="button" data-toggle></button>
      <div class="title-bar-title">Menu</div>
    </div>

    <div class="top-bar" id="example-menu">
      <div class="top-bar-left">
        <ul class="dropdown menu" data-dropdown-menu>
          <li class="menu-text">Site Title</li>
          <li class="has-submenu">
            <a href="#0">One</a>
            <ul class="submenu menu vertical" data-submenu>
              <li><a href="#0">One</a></li>
              <li><a href="#0">Two</a></li>
              <li><a href="#0">Three</a></li>
            </ul>
          </li>
          <li><a href="#0">Two</a></li>
          <li><a href="#0">Three</a></li>
        </ul>
      </div>
      <div class="top-bar-right">
        <ul class="menu">
          <li><input type="search" placeholder="Search"></li>
          <li><button type="button" class="button">Search</button></li>
        </ul>
      </div>
    </div>
    ```

    ---

    ## Reveal


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/RVyBPw?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <p><a data-open="exampleModal1">Click me for a modal</a></p>

    <div class="reveal" id="exampleModal1" data-reveal>
      <h1>Awesome. I Have It.</h1>
      <p class="lead">Your couch. It is mine.</p>
      <p>I'm a cool paragraph that lives inside of an even cooler modal. Wins!</p>
      <button class="close-button" data-close aria-label="Close reveal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    ```

    ---

    ## Slider


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/xdjJVm?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="slider" data-slider data-initial-start="50" data-end="200">
      <span class="slider-handle"  data-slider-handle role="slider" tabindex="1"></span>
      <span class="slider-fill" data-slider-fill></span>
      <input type="hidden">
    </div>

    <div class="slider vertical" data-slider data-initial-start="25" data-end="200" data-vertical="true">
      <span class="slider-handle" data-slider-handle role="slider" tabindex="1"></span>
      <span class="slider-fill" data-slider-fill></span>
      <input type="hidden">
    </div>

    <div class="slider" data-slider data-initial-start="25" data-initial-end="75">
      <span class="slider-handle" data-slider-handle role="slider" tabindex="1"></span>
      <span class="slider-fill" data-slider-fill></span>
      <span class="slider-handle" data-slider-handle role="slider" tabindex="1"></span>
      <input type="hidden">
      <input type="hidden">
    </div>
    ```

    ---

    ## Sticky


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/ZKodJR?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="row">
      <div class="columns small-6" id="example1" data-something>
        <p id="doodle">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
      </div>
      <div class="columns small-6 right" data-sticky-container>
        <div class="sticky" data-sticky data-margin-top="6" data-anchor="example1">
          <img class="thumbnail" src="assets/img/generic/rectangle-3.jpg" alt="">
        </div>
      </div>
    </div>
    ```

    ---

    ## Switch


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/dWejpx?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="switch tiny">
      <input class="switch-input" id="tinySwitch" type="checkbox" name="exampleSwitch">
      <label class="switch-paddle" for="tinySwitch">
        <span class="show-for-sr">Tiny Sandwiches Enabled</span>
      </label>
    </div>

    <div class="switch small">
      <input class="switch-input" id="smallSwitch" type="checkbox" name="exampleSwitch">
      <label class="switch-paddle" for="smallSwitch">
        <span class="show-for-sr">Small Portions Only</span>
      </label>
    </div>

    <div class="switch large">
      <input class="switch-input" id="largeSwitch" type="checkbox" name="exampleSwitch">
      <label class="switch-paddle" for="largeSwitch">
        <span class="show-for-sr">Show Large Elephants</span>
      </label>
    </div>
    ```

    ---

    ## Table


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/eWrjQx?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <table>
      <thead>
        <tr>
          <th>Table Header</th>
          <th>Table Header</th>
          <th>Table Header</th>
          <th>Table Header</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Content Goes Here</td>
          <td>This is longer content Donec id elit non mi porta gravida at eget metus.</td>
          <td>Content Goes Here</td>
          <td>Content Goes Here</td>
        </tr>
        <tr>
          <td>Content Goes Here</td>
          <td>This is longer Content Goes Here Donec id elit non mi porta gravida at eget metus.</td>
          <td>Content Goes Here</td>
          <td>Content Goes Here</td>
        </tr>
        <tr>
          <td>Content Goes Here</td>
          <td>This is longer Content Goes Here Donec id elit non mi porta gravida at eget metus.</td>
          <td>Content Goes Here</td>
          <td>Content Goes Here</td>
        </tr>
      </tbody>
    </table>
    ```

    ---

    ## Tabs


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/qmYygE?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="tabs" data-tabs id="example-tabs">
      <li class="tabs-title is-active"><a href="#panel1" aria-selected="true">Tab 1</a></li>
      <li class="tabs-title"><a href="#panel2">Tab 2</a></li>
      <li class="tabs-title"><a href="#panel3">Tab 3</a></li>
      <li class="tabs-title"><a href="#panel4">Tab 4</a></li>
      <li class="tabs-title"><a href="#panel5">Tab 5</a></li>
      <li class="tabs-title"><a href="#panel6">Tab 6</a></li>
    </ul>

    <div class="tabs-content" data-tabs-content="example-tabs">
      <div class="tabs-panel is-active" id="panel1">
        <p>One</p>
        <p>Check me out! I'm a super cool Tab panel with text content!</p>
      </div>
      <div class="tabs-panel" id="panel2">
        <p>Two</p>
        <img class="thumbnail" src="assets/img/generic/rectangle-7.jpg" alt="">
      </div>
      <div class="tabs-panel" id="panel3">
        <p>Three</p>
        <p>Check me out! I'm a super cool Tab panel with text content!</p>
      </div>
      <div class="tabs-panel" id="panel4">
        <p>Four</p>
        <img class="thumbnail" src="assets/img/generic/rectangle-2.jpg" alt="">
      </div>
      <div class="tabs-panel" id="panel5">
        <p>Five</p>
        <p>Check me out! I'm a super cool Tab panel with text content!</p>
      </div>
      <div class="tabs-panel" id="panel6">
        <p>Six</p>
        <img class="thumbnail" src="assets/img/generic/rectangle-8.jpg" alt="">
      </div>
    </div>
    ```

    ---

    ## Thumbnail


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/EmLexY?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-margin-x">
      <div class="cell small-4">
        <img class="thumbnail" src="assets/img/thumbnail/01.jpg" alt="Photo of Uranus.">
      </div>
      <div class="cell small-4">
        <img class="thumbnail" src="assets/img/thumbnail/02.jpg" alt="Photo of Neptune.">
      </div>
      <div class="cell small-4">
        <img class="thumbnail" src="assets/img/thumbnail/03.jpg" alt="Photo of Pluto.">
      </div>
    </div>
    ```

    ---

    ## Title Bar


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/qmYMZZ?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="title-bar">
      <div class="title-bar-left">
        <button class="menu-icon" type="button"></button>
        <span class="title-bar-title">Foundation</span>
      </div>
      <div class="title-bar-right">
        <button class="menu-icon" type="button"></button>
      </div>
    </div>
    ```

    ---

    ## Toggler


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/LymJLb?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <p><a data-toggle="menuBar">Expand!</a></p>

    <ul class="menu" id="menuBar" data-toggler=".expanded">
      <li><a href="#0"><i class="fi-list"></i> <span>One</span></a></li>
      <li><a href="#0"><i class="fi-list"></i> <span>Two</span></a></li>
      <li><a href="#0"><i class="fi-list"></i> <span>Three</span></a></li>
      <li><a href="#0"><i class="fi-list"></i> <span>Four</span></a></li>
    </ul>
    ```

    ---

    ## Tooltip


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/pPVOdm?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <p>The <span data-tooltip aria-haspopup="true" class="has-tip" data-disable-hover="false" tabindex=1 title="Fancy word for a beetle.">scarabaeus</span> hung quite clear of any branches, and, if allowed to fall, would have fallen at our feet. Legrand immediately took the scythe, and cleared with it a circular space, three or four yards in diameter, just beneath the insect, and, having accomplished this, ordered Jupiter to let go the string and come down from the tree.</p>
    ```

    ---

    ## Top Bar


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/eWrwKP?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="top-bar">
      <div class="top-bar-left">
        <ul class="dropdown menu" data-dropdown-menu>
          <li class="menu-text">Site Title</li>
          <li class="has-submenu">
            <a href="#0">One</a>
            <ul class="submenu menu vertical" data-submenu>
              <li><a href="#0">One</a></li>
              <li><a href="#0">Two</a></li>
              <li><a href="#0">Three</a></li>
            </ul>
          </li>
          <li><a href="#0">Two</a></li>
          <li><a href="#0">Three</a></li>
        </ul>
      </div>
      <div class="top-bar-right">
        <ul class="menu">
          <li><input type="search" placeholder="Search"></li>
          <li><button type="button" class="button">Search</button></li>
        </ul>
      </div>
    </div>
    ```

    ---

    ## Visibility Classes


    <div class="docs-codepen-container" data-ks-codepen>
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/vmjqVG?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg"  alt="edit on codepen button"></a>
    </div>

    ```html
    <p>You are on a small screen or larger.</p>
    <p class="show-for-medium">You are on a medium screen or larger.</p>
    <p class="show-for-large">You are on a large screen or larger.</p>
    <p class="show-for-small-only">You are <em>definitely</em> on a small screen.</p>
    <p class="show-for-medium-only">You are <em>definitely</em> on a medium screen.</p>
    <p class="show-for-large-only">You are <em>definitely</em> on a large screen.</p>

    <p class="hide-for-medium">You are <em>not</em> on a medium screen or larger.</p>
    <p class="hide-for-large">You are <em>not</em> on a large screen or larger.</p>
    <p class="hide-for-small-only">You are <em>definitely not</em> on a small screen.</p>
    <p class="hide-for-medium-only">You are <em>definitely not</em> on a medium screen.</p>
    <p class="hide-for-large-only">You are <em>definitely not</em> on a large screen.</p>
    <p class="hide">Can't touch this.</p>

    <p class="invisible">Can sort of touch this.</p>

    <p class="show-for-landscape">You are in landscape orientation.</p>
    <p class="show-for-portrait">You are in portrait orientation.</p>

    <p class="show-for-sr">This text can only be read by a screen reader.</p>
    <p>There's a line of text above this one, you just can't see it.</p>

    <p aria-hidden="true">This text can be seen, but won't be read by a screen reader.</p>

    <p><a class="show-on-focus" href="#mainContent">Skip to Content</a></p>
    <header id="header" role="banner">
    </header>
    <main id="mainContent" role="main" tabindex="0">
    </main>
    ```"""

    pass


class LABEL:
    """---
    title: Label
    description: Labels are useful inline styles that can be dropped into body copy to call out certain sections or to attach metadata. For example, you can attach a label that notes when something was updated.
    sass: scss/components/_label.scss
    video: '_S_OO9NiWQ8'
    ---

    ## Basics

    Add the `.label` class to an element to create a label. In the below example, we're using `<span>`, but any tag will work fine.

    <p>
      <a class="" data-open-video="3:52"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/pPKYVd?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <span class="label">Default Label</span>
    ```

    <br>

    A label will typically be describing another element on the page. To bind the two elements together, give the label a unique ID, and reference that ID in an `aria-describedby` attribute on the main element.

    ```html
    <p aria-describedby="emailLabel">Re: re: re: you won't believe what's in this email!</p>
    <span class="label" id="emailLabel">High Priority</span>
    ```

    If an element is described by multiple labels, place multiple IDs inside of `aria-describedby`.

    ```html
    <p aria-describedby="emailLabel1 emailLabel2">Re: re: re: you won't believe what's in this email!</p>
    <span class="label" id="emailLabel1">High Priority</span>
    <span class="label" id="emailLabel2">Unread</span>
    ```

    ---

    ## Coloring

    Add color classes to give labels additional meaning.

    <p>
      <a class="" data-open-video="4:04"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/rmKRJK?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <span class="label primary">Primary Label</span>
    <span class="label secondary">Secondary Label</span>
    <span class="label success">Success Label</span>
    <span class="label alert">Alert Label</span>
    <span class="label warning">Warning Label</span>
    ```

    ---

    ### Custom Colors

    If you're using the Sass version of Foundation, you can customize the label classes by editing the `$label-palette` map in your settings file. The label palette defaults to `$foundation-palette`.

    If you don't need certain colors from the default palette, simply remove them from the list.

    ```scss
    $label-palette: map-remove($foundation-palette, (
        primary,
        secondary
    )) !default;
    ```

    Or you can add more colors to the default palette.

    ```scss
    $label-palette: map-merge($foundation-palette, (
        purple: #bb00ff
    )) !default;
    ```

    Or you can define your own custom label palette.

    ```scss
    $label-palette: (
        black: #000000,
        red: #ff0000,
        purple: #bb00ff
    ) !default;
    ```

    ---

    ### Text Colors

    The text color for each label class is determined by either `$label-color` or `$label-color-alt`, whichever settings variable has more contrast.

    <div class="primary callout">
      <p>The default settings meet WCAG 2.0 level AA contrast requirements. Be sure to [check the contrast](https://webaim.org/resources/contrastchecker/) when changing color variables. To give all labels the same color text, set `$label-color` and `$label-color-alt` to the same value &mdash; but know that doing so may decrease accessibility.</p>
    </div>

    ---

    ## Icons

    An icon can be dropped into a label just fine. We're using the [Foundation icon font](https://zurb.com/playground/foundation-icon-fonts-3) here, but any icon fonts or image-based icons will work fine.

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/dWKrgb?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <span class="label alert"><i class="fi-x-circle"></i> Alert Label</span>
    <span class="label warning"><i class="fi-x"></i> Warning Label</span>
    <span class="label"><i class="fi-widget"></i> Default Label</span>
    ```"""

    pass


class MAGELLAN:
    """---
    title: Magellan
    description: Magellan allows you to create navigation that tracks the active section of a page your user is in. Pair it with our Sticky plugin to create a fixed navigation element.
    video: 'eT-WWX74SY0'
    js: js/foundation.magellan.js
    tags:
      - navigation
    ---

    ## Setup

    You can use Magellan with any navigation element, like our [Menu](menu.html) or your own custom component. Just add the attribute `data-magellan` to the container, and links to specific sections of your page. Each section needs a unique ID.

    <p>
      <a class="" data-open-video="0:42"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/MmGEXo?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <!-- Add a Menu -->
    <ul class="menu expanded" data-magellan>
      <li><a href="#first">First Arrival</a></li>
      <li><a href="#second">Second Arrival</a></li>
      <li><a href="#third">Third Arrival</a></li>
    </ul>

    <!-- Add content where magellan will be linked -->
    <div class="sections">
      <section id="first" data-magellan-target="first">First Section</section>
      <section id="second" data-magellan-target="second">Second Section</section>
      <section id="third" data-magellan-target="third">Third Section</section>
    </div>
    ```

    ---

    ## Sticky Navigation

    You can use Magellan with our [Sticky plugin](sticky.html) to create a persistent navigation header or sidebar.

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/gWKLqV?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <!-- Add a Sticky Menu -->
    <div data-sticky-container>
      <div class="top-bar" data-sticky data-margin-top="0" id="example-menu">
        <div class="top-bar-left">
          <ul class="menu">
            <li class="menu-text">Site Title</li>
          </ul>
        </div>
        <div class="top-bar-right">
          <ul class="menu" data-magellan>
            <li><a href="#first">One</a></li>
            <li><a href="#second">Two</a></li>
            <li><a href="#third">Three</a></li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Add content where magellan will be linked -->
    <div class="sections">
      <section id="first" data-magellan-target="first">First Section</section>
      <section id="second" data-magellan-target="second">Second Section</section>
      <section id="third" data-magellan-target="third">Third Section</section>
    </div>
    ```

    This below example is a simplified version of the table of contents on the right side of this page.

    ```html
    <div class="cell large-3">
      <nav class="sticky-container" data-sticky-container>
        <div class="sticky" data-sticky data-anchor="exampleId" data-sticky-on="large">
          <ul class="vertical menu" data-magellan>
            <li><a href="#first">First Arrival</a></li>
            <li><a href="#second">Second Arrival</a></li>
            <li><a href="#third">Third Arrival</a></li>
          </ul>
        </div>
      </nav>
    </div>
    ```

    ---

    ## Browser History

    When the `data-deep-link` option is set to `true`, the active section of Magellan is recorded by adding a hash with the active Magellan section ID to the browser URL. By default, Magellan *replaces* the browser history (using `history.replaceState()`).

    Modify this behavior by using the attribute `data-update-history="true"` to *append* to the browser history (using `history.pushState()`). In the latter case, the browser's back button will track each section Magellan has gone through (in most case, this is not recommended).
    """

    pass


class MEDIA_OBJECT:
    """---
    title: Media Object
    description: Media objects are super useful components for displaying an item, usually an image, alongside some content, usually text. You could put lists, grids, or even other media objects inside.
    video: 'H74_A6eI-wY'
    sass: scss/components/_media-object.scss
    flex: true
    ---

    ## Basics

    Foundation's Media Object will help you create this common repeatable pattern and can be used several different ways. A media object is a container with the class `.media-object`, and two or three sections with the class `.media-object-section`.

    <p>
      <a class="" data-open-video="1:58"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/NjzbEG?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="media-object">
      <div class="media-object-section">
        <div class="thumbnail">
          <img src="assets/img/media-object/avatar-1.jpg">
        </div>
      </div>
      <div class="media-object-section">
        <h4>Dreams feel real while we're in them.</h4>
        <p>I'm going to improvise. Listen, there's something you should know about me... about inception. An idea is like a virus, resilient, highly contagious. The smallest seed of an idea can grow. It can grow to define or destroy you.</p>
      </div>
    </div>
    ```

    <div class="primary callout">
      <p>In flexbox mode, the class `.main-section` must be added to your center section in order to properly size it.</p>
    </div>

    ```html
    <div class="media-object">
      <div class="media-object-section">
        <div class="thumbnail">
          <img src= "assets/img/media-object/avatar-1.jpg">
        </div>
      </div>
      <div class="media-object-section main-section">
        <h4>Dreams feel real while we're in them.</h4>
        <p>I'm going to improvise. Listen, there's something you should know about me... about inception. An idea is like a virus, resilient, highly contagious. The smallest seed of an idea can grow. It can grow to define or destroy you.</p>
      </div>
    </div>
    ```

    ---

    ## Section Alignment

    Each section aligns to the top by default, but individual sections can also be middle- or bottom-aligned with the `.middle` and `.bottom` classes.

    <p>
      <a class="" data-open-video="3:33"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/aWKpOj" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="media-object">
      <div class="media-object-section middle">
        <div class="thumbnail">
          <img src= "assets/img/media-object/avatar-2.jpg">
        </div>
      </div>
      <div class="media-object-section">
        <h4>Why is it so important to dream?</h4>
        <p>So, once we've made the plant, how do we go out? Hope you have something more elegant in mind than shooting me in the head? A kick. What's a kick? This, Ariadne, would be a kick.</p>
        <p>What is the most resilient parasite? Bacteria? A virus? An intestinal worm? An idea. Resilient... highly contagious. Once an idea has taken hold of the brain it's almost impossible to eradicate. An idea that is fully formed - fully understood - that sticks; right in there somewhere.</p>
      </div>
      <div class="media-object-section bottom">
        <div class="thumbnail">
          <img src= "assets/img/media-object/avatar-3.jpg">
        </div>
      </div>
    </div>
    ```

    In flexbox mode, you can use the <a href="flexbox.html#helper-classes">flexbox helper classes</a> instead to get the same result. The `.align-*` classes can be used on the container to align every child section at once, or individual child sections can be aligned with `.align-self-*` classes.

    ```html
    <div class="media-object">
      <div class="media-object-section align-self-middle">
        <div class="thumbnail">
          <img src= "assets/img/media-object/avatar-2.jpg">
        </div>
      </div>
      <div class="media-object-section main-section">
        <h4>Why is it so important to dream?</h4>
        <p>So, once we've made the plant, how do we go out? Hope you have something more elegant in mind than shooting me in the head? A kick. What's a kick? This, Ariadne, would be a kick.</p>
        <p>What is the most resilient parasite? Bacteria? A virus? An intestinal worm? An idea. Resilient... highly contagious. Once an idea has taken hold of the brain it's almost impossible to eradicate. An idea that is fully formed - fully understood - that sticks; right in there somewhere.</p>
      </div>
      <div class="media-object-section align-self-bottom">
        <div class="thumbnail">
          <img src= "assets/img/media-object/avatar-3.jpg">
        </div>
      </div>
    </div>
    ```

    ---

    ### Stack on Small

    By adding the `.stack-for-small` class, you can make your media object responsive. Images will get a width of 100%, but this can be changed.

    <p>
      <a class="" data-open-video="5:45"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/JNZEKe?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="media-object stack-for-small">
      <div class="media-object-section">
        <div class="thumbnail">
          <img src= "assets/img/generic/rectangle-1.jpg">
        </div>
      </div>
      <div class="media-object-section">
        <h4>I Can Stack.</h4>
        <p>Shrink the browser width to see me stack. I do tricks for dog treats, but I'm not a dog.</p>
      </div>
    </div>
    ```

    ---

    ### Nesting Media Objects

    By nesting a media object into the media-object-section section, you can easily indent it. This is great for comment strings.

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/aWKpOj" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="media-object">
      <div class="media-object-section">
        <div class="thumbnail">
          <img src= "assets/img/media-object/avatar-1.jpg">
        </div>
      </div>
      <div class="media-object-section">
        <h4>I'm First!</h4>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Porro at, tenetur cum beatae excepturi id ipsa? Esse dolor laboriosam itaque ea nesciunt, earum, ipsum commodi beatae velit id enim repellat.</p>
        <!-- Nested media object starts here -->
        <div class="media-object">
          <div class="media-object-section">
            <div class="thumbnail">
              <img src= "assets/img/media-object/avatar-2.jpg">
            </div>
          </div>
          <div class="media-object-section">
            <h4>I'm Second!</h4>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptas magni, quam mollitia voluptatum in, animi suscipit tempora ea consequuntur non nulla vitae doloremque. Eius rerum, cum earum quae eveniet odio.</p>
          </div>
        </div>
        <!-- And ends here -->
      </div>
    </div>
    ```"""

    pass


class MEDIA_QUERIES:
    """---
    title: Media Queries
    description: CSS media queries allow us to adjust the display and orientation of content at different screen sizes.
    video: gqqi2cqlST8
    sass: scss/util/_breakpoint.scss
    js: js/foundation.util.mediaQuery.js
    tags:
      - breakpoints
    ---

    <!-- <div class="callout training-callout">
      <p>Build better websites and apps, code cleaner, and become a better front-end developer with Foundation training. We're running two online webinar training sessions this month where we break down how to get the most out of Foundation and leap ahead skillwise.</p>
      <a href="https://zurb.com/university/courses" target="_blank"> Get registered →</a>
    </div> -->

    ## Default Media Queries

    Foundation for Sites has three core breakpoints:

    - **Small:** any screen.
    - **Medium:** any screen 640 pixels or larger.
    - **Large:** any screen 1024 pixels or larger.

    Many components can be modified at different screen sizes using special *breakpoint classes*. The grid is the most obvious example. In the code below, the left-hand column is six columns wide on small screens, hence `.small-6`. On medium-sized screens, the class `.medium-4` overrides the small style, changing the column to be four wide.

    ```html
    <div class="grid-x grid-margin-x">
      <div class="cell small-6 medium-4"></div>
      <div class="cell small-6 medium-8"></div>
    </div>
    ```

    If you're using the CSS version of Foundation, use these media queries to imitate the three core breakpoints:

    ```css
    /* Small only */
    @media screen and (max-width: 39.9375em) {}

    /* Medium and up */
    @media screen and (min-width: 40em) {}

    /* Medium only */
    @media screen and (min-width: 40em) and (max-width: 63.9375em) {}

    /* Large and up */
    @media screen and (min-width: 64em) {}

    /* Large only */
    @media screen and (min-width: 64em) and (max-width: 74.9375em) {}
    ```

    ---

    ## Upgrading from Foundation 5

    In Foundation 5, breakpoints were accessed using a series of Sass variables named `$small-up`, `$small-only`, `$medium-only`, and so on. In Foundation 6, this method of writing media queries has been replaced with a dedicated [breakpoint mixin](#the-breakpoint-mixin), described below. **The legacy variables will be removed in Foundation 6.3.**

    To upgrade your existing media queries, replace rulesets like this:

    ```scss
    @media #{$medium-only} {
    }
    ```

    With this:

    ```scss
    @include breakpoint(medium only) {
    }
    ```

    ---

    ## Changing the Breakpoints

    If you're using the Sass version of Foundation, the default breakpoints can be changed. The names of the breakpoints, and their widths, are stored in a `$breakpoints` variable in the settings file.

    ```scss
    $breakpoints: (
      small: 0px,
      medium: 640px,
      large: 1024px,
      xlarge: 1200px,
      xxlarge: 1440px,
    );
    ```

    <div class="primary callout">
      <p>Even though the above values are in pixels, they're converted to ems at the end for use in media queries.</p>
    </div>

    Changing the widths of any of the breakpoints is as easy as changing the pixel values in this map. Note that here there are two extra breakpoints: `xlarge` and `xxlarge`. We don't use these for any components, and also don't output any CSS classes that use them by default.

    Please note that the order of breakpoints must be in ascending order so that keywords like `down` in the `breakpoint` function below will work as expected e.g.


    You can change that by modifying the `$breakpoint-classes` variable in your settings file. This is a list of breakpoint names. Adding or removing names from the list will change the CSS class output. It looks like this by default:

    ```scss
    $breakpoint-classes: (small medium large);
    ```

    For example, to get `.xlarge` classes in your CSS, for use in the grid, Menu, and more, just add it to the end of the list:

    ```scss
    $breakpoint-classes: (small medium large xlarge);
    ```

    ---

    ## Sass

    ### The Breakpoint Mixin

    Our `breakpoint()` mixin makes it easy to write media queries. You can use the named breakpoints, or a custom pixel, rem, or em value.

    To use the mixin, call it with `@include`, and then include the CSS content you want inside the curly braces.

    ```scss
    .element {
      // Only affects medium screens and larger
      @include breakpoint(medium) {
        // All CSS in here goes inside the media query
      }
    }
    ```

    The behavior of the media query can be changed by adding the keyword `down` or `only` after the breakpoint value, separated by a space.

    ```scss
    .element {
      // Only affects medium screens and smaller
      @include breakpoint(medium down) { }
      // Only affects medium screens, not small or large
      @include breakpoint(medium only) { }
    }
    ```

    It's also possible to pass in custom values. You can enter a pixel, rem, or em value&mdash;all values are converted to em at the end.

    ```scss
    .element {
      // Converted to 20em
      @include breakpoint(320px) { }
      // Unitless values are assumed to be pixels
      @include breakpoint(320) { }
      // Converted to 40em
      @include breakpoint(40rem) { }
    }
    ```

    Lastly, there are three special media queries that are not width-based: `portrait`, `landscape`, and `retina`. Using these keywords with the `breakpoint()` mixin will output a media query for device orientation or pixel density, rather than screen width.

    ```scss
    .element {
      @include breakpoint(landscape) {
        // CSS for landscape-oriented devices only
      }
      @include breakpoint(retina) {
        // CSS for high-resolution displays only
      }
    }
    ```

    ---

    ### Breakpoint Function

    The functionality of the `breakpoint()` mixin comes from an internal function, also called `breakpoint()`. If you want to write your own media queries, you can use the `breakpoint()` function to access the logic of the mixin directly.

    ```scss
    @media screen and #{breakpoint(medium)} {
      // Medium and up styles
    }
    ```

    This can be used to combine multiple media queries together.

    ```scss
    @media screen and #{breakpoint(medium)} and #{breakpoint(xlarge down)} {
      // Medium to extra large styles
    }
    ```

    ---

    ## JavaScript

    ### Working with Media Queries

    The Foundation JavaScript includes a set of helper functions for working with media queries. They're all on the `Foundation.MediaQuery` object.

    <div class="callout warning">
      The MediaQuery utility uses the Sass breakpoint settings and requires the Foundation CSS to be imported. For Sass users, you need to include either `foundation-everything()` or `foundation-global-styles()`.
    </div>

    Get the name of the current breakpoint with `MediaQuery.current`.

    ```js
    Foundation.MediaQuery.current // => 'small', 'medium', etc.
    ```

    You can use `MediaQuery.is()` to check the breakpoint the screen is at.
    ```js
    Foundation.MediaQuery.is('medium') // => True for "medium" or larger
    ```

    You can also use the `up` (default), `only` and `down` modifiers like in Sass, or use the equivalent `MediaQuery.atLeast()`, `MediaQuery.only()` and `MediaQuery.upTo()`.
    ```js
    // ↑ True for "medium" or larger (by default)
    Foundation.MediaQuery.is('medium up');
    Foundation.MediaQuery.atLeast('medium');

    // → True for "medium" only
    Foundation.MediaQuery.is('medium only');
    Foundation.MediaQuery.only('medium');

    // ↓ True for "medium" or smaller
    Foundation.MediaQuery.is('medium down');
    Foundation.MediaQuery.upTo('medium');
    ```

    To get the media query of a breakpoint, use `MediaQuery.get`.

    ```js
    Foundation.MediaQuery.get('medium') // => only screen and (min-width: 640px)
    ```

    ---

    ### Watching for Breakpoint Changes

    The media query helper broadcasts an event on the window every time the breakpoint changes. We use this internally with plugins like Interchange to detect a shift in breakpoint. You can also subscribe to the event yourself.

    ```js
    $(window).on('changed.zf.mediaquery', function(event, newSize, oldSize) {
      // newSize is the name of the now-current breakpoint, oldSize is the previous breakpoint
    });
    ```"""

    pass


class MENU:
    """---
    title: Menu
    description: Our flexible menu component makes it easy to build many common navigation patterns, all with the same markup.
    video: 'CmMGPCd-fYc'
    sass: scss/components/_menu.scss
    tags:
      - navigation
      - side nav
      - sub nav
      - icon bar
      - top bar
    flex: true
    ---

    <!-- <div class="callout training-callout">
      <p>Navigation is one the most crucial part of your site. Be a navigation guru with our Foundation online webinar training. You’ll learn techniques for creating responsive navigations that work with any type of site. In addition to that you can learn tips and tricks and best practices for all of Foundation’s components.</p>
      <a href="https://zurb.com/university/foundation-intro" target="_blank">Find out more about Foundation training classes →</a>
    </div> -->

    The menu is a flexible, all-purpose component for navigation. It replaces Foundation 5's inline list, side nav, sub nav, and icon bar, unifying them into one component.

    ---

    ## Basic Menu

    All versions of the menu are a `<ul>` filled with `<li>` elements containing links. By default, a Menu is horizontally oriented.

    <p>
      <a class="" data-open-video="00:36"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/rmvXMX?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="menu">
      <li><a href="#">One</a></li>
      <li><a href="#">Two</a></li>
      <li><a href="#">Three</a></li>
      <li><a href="#">Four</a></li>
    </ul>
    ```

    ---

    ## Item Alignment

    By default, each item in the menu aligns to the left. They can also be aligned to the right with the `.align-right` class.

    <a class="" data-open-video="2:02"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    <div class="warning callout">
      <p>In a <a href="rtl.html">right-to-left</a> environment, items align to the right by default, and the class <code>.align-left</code> can be used to reverse direction.</p>
    </div>


    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/zwjgWv?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="menu align-right">
      <li><a href="#">One</a></li>
      <li><a href="#">Two</a></li>
      <li><a href="#">Three</a></li>
      <li><a href="#">Four</a></li>
    </ul>
    ```

    <br>

    To align items in the middle, add `.align-center` to the `.menu` class.

    <a class="" data-open-video="2:46"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/VbOypm?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="menu align-center">
      <li><a href="#">One</a></li>
      <li><a href="#">Two</a></li>
      <li><a href="#">Three</a></li>
      <li><a href="#">Four</a></li>
    </ul>
    ```

    <br>

    Items can also be set to expand out and take up an even amount of space, with the `.expanded` class. Thanks to the magic of CSS, the items will automatically size themselves equally depending on how many are inside the menu.

    <p>
      <a class="" data-open-video="3:34"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/bWMXQO?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="menu expanded">
      <li><a href="#">One</a></li>
      <li><a href="#">Two</a></li>
    </ul>
    ```

    <ul class="menu expanded">
      <li><a href="#0">One</a></li>
      <li><a href="#0">Two</a></li>
      <li><a href="#0">Three</a></li>
    </ul>

    <ul class="menu expanded">
      <li><a href="#0">One</a></li>
      <li><a href="#0">Two</a></li>
      <li><a href="#0">Three</a></li>
      <li><a href="#0">Four</a></li>
    </ul>

    ---

    ## Vertical Menu

    Add the `.vertical` class to a Menu to switch its orientation.

    <p>
      <a class="" data-open-video="4:53"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/YVLmBY?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="vertical menu">
      <li><a href="#">One</a></li>
      <li><a href="#">Two</a></li>
      <li><a href="#">Three</a></li>
      <li><a href="#">Four</a></li>
    </ul>
    ```

    <br>

    Add `align-right` class for making the vertical menu aligned to the right.

    ```html
    <ul class="vertical menu align-right">
      <li><a href="#">One</a></li>
      <li><a href="#">Two</a></li>
      <li><a href="#">Three</a></li>
      <li><a href="#">Four</a></li>
    </ul>
    ```

    <br>

    Add `align-center` class for making the vertical menu aligned to the center.

    <div class="warning callout">
      <p>
        The above vertically left &amp; right aligned menu are supported in all types of menu's. <br>
        But `align-center` for vertical menu&rsquo;s is only available for basic menu and is not available for dropdown, accordion or a drilldown menu.
      </p>
    </div>

    ```html
    <ul class="vertical menu align-center">
      <li><a href="#">One</a></li>
      <li><a href="#">Two</a></li>
      <li><a href="#">Three</a></li>
      <li><a href="#">Four</a></li>
    </ul>
    ```

    ---

    ## Simple Style

    Add the `.simple` class to a Menu to remove the padding and color change. This style imitates the inline list from Foundation 5.

    <p>
      <a class="" data-open-video="6:06"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/ZKogNb?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="menu simple">
      <li>One</li>
      <li><a href="#">Two</a></li>
      <li><a href="#">Three</a></li>
      <li><a href="#">Four</a></li>
    </ul>
    ```

    ---

    ## Nested Style

    Add a new menu inside the `<li>` of a Menu and add the class `.nested` to create a nested menu. The nested Menu has extra padding on the inside.

    <p>
      <a class="" data-open-video="7:17"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/vmrBOr?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="vertical menu">
      <li>
        <a href="#">One</a>
        <ul class="nested vertical menu">
          <li><a href="#">One</a></li>
          <li><a href="#">Two</a></li>
          <li><a href="#">Three</a></li>
          <li><a href="#">Four</a></li>
        </ul>
      </li>
      <li><a href="#">Two</a></li>
      <li><a href="#">Three</a></li>
      <li><a href="#">Four</a></li>
    </ul>
    ```

    ---

    ## Active State

    Add the class `.is-active` to any `<li>` to create an active state. You could apply this server-side to mark the active page, or dynamically with JavaScript.

    <p>
      <a class="" data-open-video="8:18"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/XRYrKp?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="menu">
      <li class="is-active"><a>Home</a></li>
      <li><a>About</a></li>
      <li><a>Nachos</a></li>
    </ul>
    ```

    ---

    ## Text

    Because the padding of the menu item is applied to the `<a>`, if you try to add an item that's text only, it will be misaligned. To get around this, add the class `.menu-text` to any `<li>` that doesn't have a link inside of it.

    <p>
      <a class="" data-open-video="9:11"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/GmGRWp?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="menu">
      <li class="menu-text">Site Title</li>
      <li><a href="#">One</a></li>
      <li><a href="#">Two</a></li>
      <li><a href="#">Three</a></li>
    </ul>
    ```

    ---

    ## Icons

    Menu items can have icons. Wrap the text of the item in a `<span>`, and then add an `<img>` element before the `<span>`. If you're using the Foundation icon font, the `<img>` will be an `<i>` instead.

    <p>
      <a class="" data-open-video="9:52"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/OmEJQW?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>


    ```html
    <ul class="menu">
      <li><a href="#"><i class="fi-list"></i> <span>One</span></a></li>
      <li><a href="#"><i class="fi-list"></i> <span>Two</span></a></li>
      <li><a href="#"><i class="fi-list"></i> <span>Three</span></a></li>
      <li><a href="#"><i class="fi-list"></i> <span>Four</span></a></li>
    </ul>
    ```

    ---

    Add the class `.icons` to the parent menu container to specify that the menu contains icons. Along with this, add your choice of layout class, such as `.icon-top`.

    When using any of the menu icon layout classes, ensure that the icon and the text are in the correct order. For `.icon-right` and `.icon-bottom`, the icon must come AFTER the text.

    <p>
      <a class="" data-open-video="10:42"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <br>

    ### Icon Top
    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/EXLmxO?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="menu icons icon-top">
      <li><a href="#"><i class="fi-list"></i> <span>One</span></a></li>
      <li><a href="#"><i class="fi-list"></i> <span>Two</span></a></li>
      <li><a href="#"><i class="fi-list"></i> <span>Three</span></a></li>
      <li><a href="#"><i class="fi-list"></i> <span>Four</span></a></li>
    </ul>
    ```

    <br>

    ### Icon Right
    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/vZjmEE?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="menu icons icon-right">
      <li><a href="#"><span>One</span> <i class="fi-list"></i></a></li>
      <li><a href="#"><span>Two</span> <i class="fi-list"></i></a></li>
      <li><a href="#"><span>Three</span> <i class="fi-list"></i></a></li>
      <li><a href="#"><span>Four</span> <i class="fi-list"></i></a></li>
    </ul>
    ```

    <br>

    ### Icon Bottom
    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/vZjmOE?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="menu icons icon-bottom">
      <li><a href="#"><span>One</span> <i class="fi-list"></i></a></li>
      <li><a href="#"><span>Two</span> <i class="fi-list"></i></a></li>
      <li><a href="#"><span>Three</span> <i class="fi-list"></i></a></li>
      <li><a href="#"><span>Four</span> <i class="fi-list"></i></a></li>
    </ul>
    ```

    <br>

    ### Icon Left
    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/qjYmdG?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="menu icons icon-left">
      <li><a href="#"><i class="fi-list"></i> <span>One</span></a></li>
      <li><a href="#"><i class="fi-list"></i> <span>Two</span></a></li>
      <li><a href="#"><i class="fi-list"></i> <span>Three</span></a></li>
      <li><a href="#"><i class="fi-list"></i> <span>Four</span></a></li>
    </ul>
    ```

    <br>

    ### Icon Position with Nested Styles
    Nested lists can have icons positioned differently based on the menu layer. Add the class `.nested` to the nested list and your desired icon position: `.icon-top`, `.icon-right`, `.icon-bottom`, `.icon-left`.

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/qjYmdG?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="vertical menu icons icon-top">
      <li>
        <a href="#"><i class="fi-list"></i> One</a>
        <ul class="nested vertical menu icons icon-left">
          <li><a href="#"><i class="fi-list"></i> One</a></li>
          <li><a href="#"><i class="fi-list"></i> Two</a></li>
        </ul>
      </li>
      <li><a href="#"><i class="fi-list"></i> Two</a></li>
      <li><a href="#"><i class="fi-list"></i> Three</a></li>
    </ul>
    ```
    ---

    ## Sticky Navigation

    See the documentation for the [Sticky](sticky.html#sticky-navigation) plugin to see how to easily make a sticky nav bar.
    """

    pass


class MOTION_UI:
    """---
    title: Motion UI
    description: A Sass library for creating flexible UI transitions and animations.
    library:
      github: https://github.com/foundation/motion-ui
      docs: https://github.com/foundation/motion-ui/tree/master/docs
    ---

    Motion UI is a standalone library that powers the transition effects used in a number of Foundation components, including [Toggler](toggler.html), [Reveal](reveal.html), and [Orbit](orbit.html).

    <div class="text-center">
      <button type="button" class="button" data-toggle="motion-header-example">Animate!</button>
      <div data-toggler data-animate="fade-in fade-out" id="motion-header-example" style="display: none;">
        <img src="/assets/img/generic/rectangle-7.jpg" style="width: 100%;">
      </div>
    </div>


    ---

    ## Installing

    **Motion UI is already included in both [starter projects](starter-projects.html).** If you want to add it to an existing project, follow these steps.

    First, install the library with npm or yarn.

    ```bash
    npm install motion-ui --save-dev
    yarn add motion-ui
    ```

    Next, add the path `[modules_folder]/motion-ui/src` to your Sass compiler's import path list. Here's what you would add in Compass, via `config.rb`:

    ```ruby
    add_import_path 'node_modules/motion-ui/src'
    ```

    Here's how it works using gulp-sass:

    ```js
    gulp.src('./src/scss/app.scss')
      .pipe(sass({
        includePaths: ['node_modules/motion-ui/src']
      }));
    ```

    Finally, import the library into your Sass file and include the mixins.

    ```scss
    @import 'motion-ui'
    @include motion-ui-transitions;
    @include motion-ui-animations;
    ```

    Or, another way to start using Motion UI is through a CDN.

    ```html
    <!-- Insert this within your head tag and after foundation.css -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/motion-ui@1.2.3/dist/motion-ui.min.css" />

    ```

    ---

    ## Usage in Components

    Various Foundation components provide options for to use Motion UI animations when changing state. Here are the options for each plugin that support Motion UI:
    - [Orbit](orbit.html): `data-animate`
    - [Reveal](reveal.html): `data-animation-in`, `data-animation-out`
    - [Toggler](toggler.html): `data-animate`
    - [Responsive Toggler](responsive-navigation.html): `data-animate`

    For example, here are two instances of Toggler&mdash;one using fade classes (`.fade-in` and `.fade-out`), and one using slide classes (`.slide-in-down` and `.slide-out-up`). See all available classes in [build-in transitions](#built-in-transitions) below.

    ```html
    <div data-toggler data-animate="fade-in fade-out" class="callout secondary">
      <p>This panel fades.</p>
    </div>

    <div data-toggler data-animate="slide-in-down slide-out-up" class="callout secondary">
      <p>This panel slides.</p>
    </div>
    ```

    <button type="button" class="button" data-toggle="motion-example-1">Fade</button><button type="button" class="button" data-toggle="motion-example-2">Slide</button>
    <div class="grid-x grid-margin-x">
      <div class="cell small-6">
        <div data-toggler data-animate="fade-in fade-out" class="callout secondary ease" id="motion-example-1">
          <p>This panel <strong>fades</strong>.</p>
        </div>
      </div>
      <div class="cell small-6">
        <div data-toggler data-animate="slide-in-down slide-out-up" class="callout secondary ease" id="motion-example-2">
          <p>This panel <strong>slides</strong>.</p>
        </div>
      </div>
    </div>

    ---

    ## Built-in Transitions

    Motion UI includes more than two dozen built-in transition classes. They can be enabled by adding this line to your Sass file, after you've imported the library:

    ```scss
    @include motion-ui-transitions;
    ```

    <div>
      <select name="docs-transitions" class="docs-transitions">
        <optgroup label="Slide">
          <option value="slide-in-down">slide-in-down</option>
          <option value="slide-in-left">slide-in-left</option>
          <option value="slide-in-up">slide-in-up</option>
          <option value="slide-in-right">slide-in-right</option>
          <option value="slide-out-down">slide-out-down</option>
          <option value="slide-out-left">slide-out-left</option>
          <option value="slide-out-up">slide-out-up</option>
          <option value="slide-out-right">slide-out-right</option>
        </optgroup>
        <optgroup label="Fade">
          <option value="fade-in">fade-in</option>
          <option value="fade-out">fade-out</option>
        </optgroup>
        <optgroup label="Hinge">
          <option value="hinge-in-from-top">hinge-in-from-top</option>
          <option value="hinge-in-from-right">hinge-in-from-right</option>
          <option value="hinge-in-from-bottom">hinge-in-from-bottom</option>
          <option value="hinge-in-from-left">hinge-in-from-left</option>
          <option value="hinge-in-from-middle-x">hinge-in-from-middle-x</option>
          <option value="hinge-in-from-middle-y">hinge-in-from-middle-y</option>
          <option value="hinge-out-from-top">hinge-out-from-top</option>
          <option value="hinge-out-from-right">hinge-out-from-right</option>
          <option value="hinge-out-from-bottom">hinge-out-from-bottom</option>
          <option value="hinge-out-from-left">hinge-out-from-left</option>
          <option value="hinge-out-from-middle-x">hinge-out-from-middle-x</option>
          <option value="hinge-out-from-middle-y">hinge-out-from-middle-y</option>
        </optgroup>
        <optgroup label="Scale">
          <option value="scale-in-up">scale-in-up</option>
          <option value="scale-in-down">scale-in-down</option>
          <option value="scale-out-up">scale-out-up</option>
          <option value="scale-out-down">scale-out-down</option>
        </optgroup>
        <optgroup label="Spin">
          <option value="spin-in">spin-in</option>
          <option value="spin-out">spin-out</option>
          <option value="spin-in-ccw">spin-in-ccw</option>
          <option value="spin-out-ccw">spin-out-ccw</option>
        </optgroup>
      </select>
      <img src="assets/img/generic/voyager.jpg" class="docs-transition-demo">
    </div>

    ---

    ## Custom Transitions

    Custom transition classes can be made using Motion UI's mixin library. Here's an example of a custom hinge. **Refer to [Motion UI's transition documentation](https://github.com/foundation/motion-ui/blob/master/docs/transitions.md) to learn more.**

    ```scss
    @include mui-hinge(
      $state: in,
      $from: top,
      $turn-origin: from-back,
      $duration: 0.5s,
      $timing: easeInOut
    );
    ```

    ---

    ## Animation

    You can use the same five transition effects to create CSS animations as well. The library also allows you to create series effects, with animations on multiple elements happening in a queue. **Refer to [Motion UI's animation documentation](https://github.com/foundation/motion-ui/blob/master/docs/animations.md) to learn more.**

    <button type="button" class="button" data-docs-example-series>Play Animation</button>
    <div class="grid-x grid-margin-x" id="series-example">
      <div class="cell small-4">
        <img class="thumbnail" src= "assets/img/generic/square-1.jpg" id="series-example-1">
      </div>
      <div class="cell small-4">
        <img class="thumbnail" src= "assets/img/generic/square-2.jpg" id="series-example-2">
      </div>
      <div class="cell small-4">
        <img class="thumbnail" src= "assets/img/generic/square-3.jpg" id="series-example-3">
      </div>
    </div>

    ---

    ## JavaScript Reference

    Motion UI includes a tiny JavaScript utility that will work anywhere as long as jQuery is loaded. However, Foundation 6 includes a customized version of this code that is included in `js/foundation.util.motion.js`. If you are using the Foundation version of this utility, and you wish to animate your own elements, trigger it this way:

    ```js
    var elem = $('#elem-to-animate');

    Foundation.Motion.animateIn(elem, animationClass [, callback]);
    Foundation.Motion.animateOut(elem, animationClass [, callback]);
    ```

    The callback is optional in this case, and will fire when the animation is complete.
    <div class="callout primary">
      <p>Please note that the duration/animation speed for Motion UI animations are controlled via Sass mixin variables. The JavaScript handles the addition and removal of classes and event listener/callback firing only.
      <br>
      If you are individually including your <code>&lt;script&gt;</code> tags, make sure you are including the <code>js/foundation.util.motion.js</code> path.
      </p>
    </div>"""

    pass


class NAVIGATION:
    """---
    title: Navigation
    description: Foundation is bundled with many simple navigation patterns, which can be combined to form more complex, robust responsive navigation solutions.
    ---

    ## Basics: Menu

    The Menu is an all-purpose navigation component. It can be aligned horizontally or vertically, can be nested, and supports icons. [Learn more about the Menu.](menu.html)

    All menus use the `ul > li > a` pattern. The markup is a little strict, but this makes it easy to attach a navigation plugin to any menu, as you'll see below.

    Here's a basic Menu.

    ```html
    <ul class="menu">
      <li><a href="#">Item One</a></li>
      <li><a href="#">Item Two</a></li>
      <li><a href="#">Item Three</a></li>
    </ul>
    ```

    ---

    To nest menus, add a new `<ul>` inside of an `<li>`, *after* the `<a>` inside.

    ```html
    <ul class="menu">
      <li>
        <a href="#">Item One</a>
        <ul class="menu">
          <li><a href="#">Item One-one</a></li>
        </ul>
      </li>
      <li><a href="#">Item Two</a></li>
      <li><a href="#">Item Three</a></li>
    </ul>
    ```

    ---

    ## Top Bar

    Top bar is a simple wrapper around these menu patterns. It supports a left-hand and right-hand section, which collapse on top of each other on small screens. [Learn more about the top bar.](top-bar.html)

    <div class="top-bar">
      <div class="top-bar-left">
        <ul class="dropdown menu" data-dropdown-menu>
          <li class="menu-text">Site Title</li>
          <li><a href="#0">One</a></li>
          <li><a href="#0">Two</a></li>
          <li><a href="#0">Three</a></li>
        </ul>
      </div>
      <div class="top-bar-right">
        <ul class="menu">
          <li><input type="search" placeholder="Search"></li>
          <li><button type="button" class="button">Search</button></li>
        </ul>
      </div>
    </div>

    ---

    ## Menu Plugins

    The basic Menu can be enhanced with one of three **Menu plugins**. All three use the exact same markup to create a different style of multi-tier navigation.

    ### Dropdown Menu

    The dropdown menu plugin (`data-dropdown-menu`) converts a nested menu into a series of dropdown menus. The nested menus can be opened through hover, click, or keyboard. [Learn more about the dropdown menu.](dropdown-menu.html)

    <ul class="dropdown menu" data-dropdown-menu>
      <li class="has-submenu">
        <a>Item 1</a>
        <ul class="submenu menu" data-submenu>
          <li><a href="#0">Item 1A Loooong</a></li>
          <li class="has-submenu">
            <a href="#0"> Item 1 sub</a>
            <ul class="submenu menu" data-submenu>
              <li><a href="#0">Item 1 subA</a></li>
              <li><a href="#0">Item 1 subB</a></li>
              <li class="has-submenu">
                <a href="#"> Item 1 sub</a>
                <ul class="submenu menu" data-submenu>
                  <li><a href="#0">Item 1 subA</a></li>
                  <li><a href="#0">Item 1 subB</a></li>
                </ul>
              </li>
              <li class="has-submenu">
                <a href="#0">Item 1 sub</a>
                <ul class="submenu menu" data-submenu>
                  <li><a href="#0">Item 1 subA</a></li>
                  <li><a href="#0">Item 1 subB</a></li>
                </ul>
              </li>

            </ul>
          </li>
          <li><a href="#0">Item 1B</a></li>
        </ul>
      </li>
      <li class="has-submenu">
        <a href="#0">Item 2</a>
        <ul class="submenu menu" data-submenu>
          <li><a href="#0">Item 2A</a></li>
          <li><a href="#0">Item 2B</a></li>
        </ul>
      </li>
      <li class="has-submenu">
        <a href="#0">Item 3</a>
        <ul class="submenu menu" data-submenu>
          <li><a href="#0">Item 3A</a></li>
          <li><a href="#0">Item 3B</a></li>
        </ul>
      </li>
      <li><a href="#0">Item 4</a></li>
    </ul>

    ---

    ### Drilldown Menu

    The drilldown menu plugin (`data-drilldown`) converts a nested menu into a series of sliding menus. Clicking an item slides the next level menu into view. [Learn more about the drilldown menu.](drilldown-menu.html)

    <ul class="vertical menu" data-drilldown style="width: 300px;" id="m1">
      <li class="has-submenu">
        <a href="#">Item 1</a>
        <ul class="vertical menu" data-submenu id="m2">
          <li class="has-submenu">
            <a href="#">Item 1A</a>
            <ul class="vertical menu" data-submenu id="m3">
              <li><a href="#0">Item 1Aa</a></li>
              <li><a href="#0">Item 1Ba</a></li>
              <li><a href="#0">Item 1Ca</a></li>
              <li><a href="#0">Item 1Da</a></li>
              <li><a href="#0">Item 1Ea</a></li>
            </ul>
          </li>
          <li><a href="#0">Item 1B</a></li>
          <li><a href="#0">Item 1C</a></li>
          <li><a href="#0">Item 1D</a></li>
          <li><a href="#0">Item 1E</a></li>
        </ul>
      </li>
      <li class="has-submenu">
        <a href="#">Item 2</a>
        <ul class="vertical menu" data-submenu>
          <li><a href="#0">Item 2A</a></li>
          <li><a href="#0">Item 2B</a></li>
          <li><a href="#0">Item 2C</a></li>
          <li><a href="#0">Item 2D</a></li>
          <li><a href="#0">Item 2E</a></li>
        </ul>
      </li>
      <li class="has-submenu">
        <a href="#">Item 3</a>
        <ul class="vertical menu" data-submenu>
          <li><a href="#0">Item 3A</a></li>
          <li><a href="#0">Item 3B</a></li>
          <li><a href="#0">Item 3C</a></li>
          <li><a href="#0">Item 3D</a></li>
          <li><a href="#0">Item 3E</a></li>
        </ul>
      </li>
      <li><a href="#"> Item 4</a></li>
    </ul>

    ---

    ### Accordion Menu

    The accordion menu plugin (`data-accordion-menu`) converts a nested menu into a series of collapsed accordions. Clicking an item slides down the nested menu. [Learn more about the accordion menu.](accordion-menu.html)

    <div class="vertical menu" data-accordion-menu>
      <li class="has-submenu">
        <a href="#">Item 1</a>
        <ul class="menu vertical nested is-active" data-submenu>
          <li class="has-submenu">
            <a href="#">Item 1A</a>
            <ul class="menu vertical nested" data-submenu>
              <li><a href="#0">Item 1Ai</a></li>
              <li><a href="#0">Item 1Aii</a></li>
              <li><a href="#0">Item 1Aiii</a></li>
            </ul>
          </li>
          <li><a href="#0">Item 1B</a></li>
          <li><a href="#0">Item 1C</a></li>
        </ul>
      </li>
      <li class="has-submenu">
        <a href="#">Item 2</a>
        <ul class="menu vertical nested" data-submenu>
          <li><a href="#0">Item 2A</a></li>
          <li><a href="#0">Item 2B</a></li>
        </ul>
      </li>
      <li><a href="#0">Item 3</a></li>
    </div>

    ---

    ## Responsive Navigation

    Each of the above three patterns has a use in a specific context. But some patterns only work at certain screen sizes. For example, dropdown menus don't work as well on smaller screens, but the same navigation items might work better as a drilldown or an accordion menu at that screen size.

    Our responsive menu plugin (`data-responsive-menu`) allows you to take a Menu, and assign different navigation patterns to it at different screen sizes. In the below example, a drilldown menu changes to a dropdown menu at larger screen sizes. [Learn more about the responsive Menu plugin.](responsive-navigation.html#responsive-menu)

    <ul class="vertical menu" data-responsive-menu="drilldown medium-dropdown" style="width: 300px;">
      <li class="has-submenu">
        <a href="#0">Item 1</a>
        <ul class="vertical submenu menu" data-submenu id="m2">
          <li class="has-submenu">
            <a href="#0">Item 1A</a>
            <ul class="vertical submenu menu" data-submenu id="m3">
              <li><a href="#0">Item 1A</a></li>
              <li><a href="#0">Item 1B</a></li>
              <li><a href="#0">Item 1C</a></li>
              <li><a href="#0">Item 1D</a></li>
              <li><a href="#0">Item 1E</a></li>
            </ul>
          </li>
          <li><a href="#0">Item 1B</a></li>
        </ul>
      </li>
      <li class="has-submenu">
        <a href="#0">Item 2</a>
        <ul class="vertical submenu menu" data-submenu>
          <li><a href="#0">Item 2A</a></li>
          <li><a href="#0">Item 2B</a></li>
        </ul>
      </li>
      <li class="has-submenu">
        <a href="#0">Item 3</a>
        <ul class="vertical submenu menu" data-submenu>
          <li><a href="#0">Item 3A</a></li>
          <li><a href="#0">Item 3B</a></li>
        </ul>
      </li>
    </ul>

    ---

    In other situations, you may wish to always display a menu on a larger screen, but hide that same menu behind a click toggle on smaller screens. You can do this with the responsive toggle plugin (`data-responsive-toggle`). This plugin works with any container, not just a menu. [Learn more about the responsive toggle plugin.](responsive-navigation.html#responsive-toggle)

    To see the below example in action, scale your browser down. The top bar will be replaced by a smaller title bar. Clicking the icon inside the title bar reveals the top bar.

    <div class="title-bar" data-responsive-toggle="example-menu" data-hide-for="medium">
      <button class="menu-icon" type="button" data-toggle></button>
      <div class="title-bar-title">Menu</div>
    </div>

    <div class="top-bar" id="example-menu">
      <div class="top-bar-left">
        <ul class="dropdown menu" data-dropdown-menu>
          <li class="menu-text">Site Title</li>
          <li class="has-submenu">
            <a href="#0">One</a>
            <ul class="submenu menu vertical" data-submenu>
              <li><a href="#0">One</a></li>
              <li><a href="#0">Two</a></li>
              <li><a href="#0">Three</a></li>
            </ul>
          </li>
          <li><a href="#0">Two</a></li>
          <li><a href="#0">Three</a></li>
        </ul>
      </div>
      <div class="top-bar-right">
        <ul class="menu">
          <li><input type="search" placeholder="Search"></li>
          <li><button type="button" class="button">Search</button></li>
        </ul>
      </div>
    </div>

    ---

    ## Sticky Navigation

    See the documentation for the [Sticky](sticky.html#sticky-navigation) plugin to see how to easily make a sticky nav bar.
    """

    pass


class OFF_CANVAS:
    """---
    title: Off-canvas
    description: Off-canvas panels are positioned outside of the viewport and slide in when activated. Setting up an off-canvas layout in Foundation is super easy.
    video: 'RK_k__4Y4TU'
    sass:
      - scss/components/_off-canvas.scss
      - scss/components/_title-bar.scss
    js: js/foundation.offcanvas.js
    tags:
      - navigation
      - offcanvas
      - off-canvas
      - nav
      - title bar
    flex: true
    ---

    <!-- <div class="callout training-callout">
      <p>Off-canvas layouts are common and useful for mobile and desktop layouts. Be a navigation guru with our Foundation online webinar training. You’ll learn techniques for creating responsive navigations that work with any type of site. In addition to that you can learn tips and tricks and best practices for all of Foundation’s components.</p>
      <a href="https://zurb.com/university/foundation-intro" target="_blank">Find out more about Foundation training classes →</a>
    </div> -->

    <div class="primary callout">
      <p>Good news! We've updated Off-canvas to offer more and better functionality. Another bonus is the markup is simplified. This new version applies to version 6.3+. We work hard to avoid breaking changes, so any markup updates are listed in the <a href="#migrating-from-versions-prior-to-v6-3">migration section</a> of this page.</p>
    </div>

    <button class="button" type="button" data-toggle="offCanvasLeft">Toggle Off-canvas</button>

    Foundation's Off-canvas is a well established mobile pattern for navigation that can also be used to create a responsive sidebar. It can open from any direction, left, right, top, and bottom. There are options to allow the Off-canvas to push your page over or to overlap your page plus a few other neat tricks.

    ## Setup

    Setting up the Off-canvas only requires two elements! To setup the Off-canvas create an off-canvas container with the class `.off-canvas` and the attribute `data-off-canvas`. This is the container that holds your Off-canvas content.

    The Off-canvas container also needs a positioning class to determine which side of the viewport it opens from:

    - `.position-left`
    - `.position-right`
    - `.position-top`
    - `.position-bottom`

    <p>
      <a class="" data-open-video="2:00"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    Also be sure the off-canvas panel has a unique ID so it can be targeted by the click trigger.

    Example:

    ```html
    <div class="off-canvas position-left" id="offCanvas" data-off-canvas>
      <!-- Your menu or Off-canvas content goes here -->
    </div>
    ```

    Along with the Off-canvas container, the main content of your page will be housed in its own container with the class `.off-canvas-content` and attribute `data-off-canvas-content`. This is where your page content lives.

    ```html
    <div class="off-canvas-content" data-off-canvas-content>
      <!-- Your page content lives here -->
    </div>
    ```

    So putting it all together:

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/ZKjXvQ?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <body>
      <div class="off-canvas position-left" id="offCanvas" data-off-canvas>
        <!-- Your menu or Off-canvas content goes here -->
      </div>
      <div class="off-canvas-content" data-off-canvas-content>
        <!-- Your page content lives here -->
      </div>
    </body>
    ```

    ### Wrapper

    You can add an optional wrapper around off-canvas and the content. This hides the vertical (on top/bottom off-canvas) or horizontal (on left/right off-canvas) scrollbars the body will have.
    Simply add a container with the class `.off-canvas-wrapper`.

    ```html
    <body>
      <div class="off-canvas-wrapper">
        <div class="off-canvas position-left" id="offCanvas" data-off-canvas>
          <!-- Your menu or Off-canvas content goes here -->
        </div>
        <div class="off-canvas-content" data-off-canvas-content>
          <!-- Your page content lives here -->
        </div>
      </div>
    </body>
    ```

    ### Click Triggers

    To create a click trigger that opens the panel, add the attribute `data-open` or `data-toggle` to any element. That element will then open or toggle the panel when clicked on. The value of the data attribute should be the ID of the off-canvas.

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/ZKjXvQ?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <button type="button" class="button" data-toggle="offCanvas">Open Menu</button>
    ```

    ### Close Button

    Foundation's Close component can be used inside the off-canvas to close it.

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/QvBQjo?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <button class="close-button" aria-label="Close menu" type="button" data-close>
      <span aria-hidden="true">&times;</span>
    </button>
    ```

    ### Complete Example

    Here's a complete example that can be pasted into the `<body>` tag of your page. It includes a close button and basic menu styles.

    ```html
    <body>
      <div class="off-canvas position-left" id="offCanvas" data-off-canvas>

        <!-- Close button -->
        <button class="close-button" aria-label="Close menu" type="button" data-close>
          <span aria-hidden="true">&times;</span>
        </button>

        <!-- Menu -->
        <ul class="vertical menu">
          <li><a href="#">Foundation</a></li>
          <li><a href="#">Dot</a></li>
          <li><a href="#">ZURB</a></li>
          <li><a href="#">Com</a></li>
          <li><a href="#">Slash</a></li>
          <li><a href="#">Sites</a></li>
        </ul>

      </div>

      <div class="off-canvas-content" data-off-canvas-content>
        <!-- Your page content lives here -->
      </div>
    </body>
    ```
    ---

    ## Off-canvas Position

    Foundation's Off-canvas is set to `position: fixed` by default using the `.off-canvas` class. This makes the off-canvas panel sit in relation to the viewport, and is the desired behavior for most users. However you can also set an off-canvas container to `position: absolute` by using the alternative class `.off-canvas-absolute`. Also be sure to use the `.off-canvas-wrapper` when using this method.

    ```html
    <button type="button" class="button" data-toggle="offCanvasLeftSplit1">Open Left</button>
    <button type="button" class="button" data-toggle="offCanvasRightSplit2">Open Right</button>

    <div class="grid-x grid-margin-x">
      <div class="cell small-6">
        <div class="off-canvas-wrapper">
          <div class="off-canvas-absolute position-left" id="offCanvasLeftSplit1" data-off-canvas>
            <!-- Your menu or Off-canvas content goes here -->
          </div>
          <div class="off-canvas-content" style="min-height: 300px;" data-off-canvas-content>
            <p>I have nothing to do with the off-canvas on the right!</p>
          </div>
        </div>
      </div>
      <div class="cell small-6">
        <div class="off-canvas-wrapper">
          <div class="off-canvas-absolute position-right" id="offCanvasRightSplit2" data-off-canvas>
            <!-- Your menu or Off-canvas content goes here -->
          </div>
          <div class="off-canvas-content" style="min-height: 300px;" data-off-canvas-content>
            <p>Im a unique off-canvas container all on my own!</p>
          </div>
        </div>
      </div>
    </div>
    ```

    ---

    ## Off-canvas Directions

    Foundation's Off-canvas can open from any direction, left, right, top, and bottom.

    The Off-canvas container requires a positioning class to determine which side of the viewport it opens from:

    - `.position-left`
    - `.position-right`
    - `.position-top`
    - `.position-bottom`

    ```html
    <button type="button" class="button" data-toggle="offCanvasLeft1">Open Left</button>
    <button type="button" class="button" data-toggle="offCanvasRight1">Open Right</button>
    <button type="button" class="button" data-toggle="offCanvasTop1">Open Top</button>
    <button type="button" class="button" data-toggle="offCanvasBottom1">Open Bottom</button>

    <div class="cell">
      <div class="off-canvas-wrapper">
        <div class="off-canvas position-left" id="offCanvasLeft1" data-off-canvas>
          <!-- Your menu or Off-canvas content goes here -->
        </div>
        <div class="off-canvas position-right" id="offCanvasRight1" data-off-canvas>
          <!-- Your menu or Off-canvas content goes here -->
        </div>
        <div class="off-canvas position-top" id="offCanvasTop1" data-off-canvas>
          <!-- Your menu or Off-canvas content goes here -->
        </div>
        <div class="off-canvas position-bottom" id="offCanvasBottom1" data-off-canvas>
          <!-- Your menu or Off-canvas content goes here -->
        </div>
        <div class="off-canvas-content" data-off-canvas-content>
          <img src="https://placehold.it/300x300" class="" height="" width="" alt="">
        </div>
      </div>
    </div>
    ```

    ---

    ## Multiple Panels

    A design can have multiple panels. Be sure that all panels come *before* the `.off-canvas-content` wrapper&mdash;this is required for the CSS to apply correctly.

    <div class="primary callout">
      <p>When using Foundation in <a href="rtl.html">right-to-left</a> mode, "right" still means right, and "left" still means left.</p>
    </div>

    ```html
    <body>
      <div class="off-canvas position-left" id="offCanvasLeft" data-off-canvas></div>
      <div class="off-canvas position-right" id="offCanvasRight" data-off-canvas></div>
      <div class="off-canvas-content" data-off-canvas-content></div>
    </body>
    ```

    <button class="button" type="button" data-toggle="offCanvasLeft">Open Left Menu</button>
    <button class="button" type="button" data-toggle="offCanvasRight">Open Right Menu</button>

    ---

    ## Off-canvas Transitions

    You can switch the default transition of the off-canvas from pushing the page over as it open to overlapping the page by adding the `data-transition="overlap"` to the `.off-canvas`.
    There are 2 available transitions: push (`data-transition="push"`) which is the default, and overlap (`data-transition="overlap"`).

    <div class="primary callout">
      <p>When placing the off-canvas within the off-canvas-content container as <a href="#nested-off-canvas">Nested Off-Canvas</a>, only overlap transition is possible. If you've explicitely defined push transition it will be replaced with overlap automatically.</p>
    </div>

    ```html
    <div class="off-canvas position-left" id="offCanvasLeftOverlap" data-off-canvas data-transition="overlap">
      <!-- Your menu or Off-canvas content goes here -->
    </div>
    <div class="off-canvas position-right" id="offCanvasRightPush" data-off-canvas data-transition="push">
      <!-- Your menu or Off-canvas content goes here -->
    </div>
    ```

    <button type="button" class="button" data-toggle="offCanvasOverlap">Open Left with Overlap</button>
    <button class="button" type="button" data-toggle="offCanvasRight">Open Right with Push</button>

    <div class="off-canvas position-left is-closed" id="offCanvasOverlap" data-off-canvas data-transition="overlap">
      <ul class="vertical menu">
        <li><a href="#">Foundation</a></li>
        <li><a href="#">Dot</a></li>
        <li><a href="#">ZURB</a></li>
        <li><a href="#">Com</a></li>
        <li><a href="#">Slash</a></li>
        <li><a href="#">Sites</a></li>
      </ul>
    </div>

    ---

    ## Reveal on Larger Screens

    The left- and right-hand off-canvas panes can be set to be persistent on larger screens like a sidebar. Add the class `.reveal-for-medium` or `.reveal-for-large` to the off-canvas menu. These classes determine what breakpoint the off-canvas will default open.

    The main content area (`.off-canvas-content`) will be padded to the left or right equal to the width of the container.

    <div class="callout">
      <p>The menu will be fixed-position by default, meaning it follows you as you scroll up and down. The menu also gets its own scroll bar if it's taller than the window. To disable these features, set the <code>$offcanvas-fixed-reveal</code> variable to <code>false</code>.</p>
    </div>

    <div class="warning callout">
      <p>The slide in/out of the plugin still works when these classes are active. If you use this feature on a larger screen, be sure to hide any click triggers on those larger breakpoints as well. Foundation's <a href="visibility.html">visibility classes</a> can help you with that.</p>
    </div>

    ```html
    <div class="off-canvas position-left reveal-for-large" data-off-canvas>
      <!-- ... -->
    </div>
    ```

    <button type="button" class="button" data-docs-example-ofc>Toggle Reveal Class</button>

    ---

    ## Combining with Title Bar

    If you need a simple bar to contain your hamburger icon/s and toggle the off-canvas, `.title-bar` is here to help. It supports left- and right-aligned sections. You can add your off-canvas toggle triggers here:

    ```html
    <div class="title-bar">
      <div class="title-bar-left">
        <button class="menu-icon" type="button" data-open="offCanvasLeft"></button>
        <span class="title-bar-title">Foundation</span>
      </div>
      <div class="title-bar-right">
        <button class="menu-icon" type="button" data-open="offCanvasRight"></button>
      </div>
    </div>
    ```
    <br>

    <div class="primary callout">
      <p>When using the `title-bar` with a vertical off-canvas, the title-bar icons are still either `title-bar-left` or `title-bar-right`.</p>
    </div>

    ```html
    <div class="title-bar">
      <div class="title-bar-left">
        <button class="menu-icon" type="button" data-open="offCanvasTop"></button>
        <span class="title-bar-title">Foundation title bar with top off-canvas</span>
      </div>
      <div class="title-bar-right">
        <button class="menu-icon" type="button" data-open="offCanvasTop"></button>
      </div>
    </div>
    ```

    ---

    #### Off-Canvas (Putting it all together)

    For an example of off-canvas, checkout this top bar with off-canvas navigation and dropdowns for submenus building block: <https://get.foundation/building-blocks/blocks/multilevel-offcanvas-menu.html>

    ---

    ## In-Canvas to Off-Canvas

    With this feature you can have a standard page element move off-canvas at a particular breakpoint. Use the <code>inCanvasOn</code> option for this. In-Canvas differs from the <a href="#reveal-on-larger-screens">Reveal on Larger Screens</a> feature as it doesn't actually open the off-canvas for specific screen sizes but overrides the off-canvas styles so it behaves as a regular page element. This way you can place an element anywhere on the page and move it into off-canvas for e.g. small screens only.

    <div class="primary callout">
      <p>The <code>inCanvasOn</code> option will automatically add the <code>.in-canvas-for-[BREAKPOINT]</code> class since most of the work is done via CSS only. However you may also add this class yourself which will override the option.</p>
    </div>

    ```html
    <button type="button" class="button hide-for-large" data-toggle="inCanvasExample">
      Open in-canvas that is off-canvas now
    </button>
    <div class="off-canvas position-right" id="inCanvasExample" data-off-canvas data-options="inCanvasOn:large;">
      <div class="callout">I'm in-canvas for medium screen size and move off-canvas for medium down.</div>
    </div>
    ```

    ---

    ## Nested Off-Canvas

    In v6.4 the off-canvas component has been heavily extended. Apart from the <a href="#in-canvas">In-Canvas</a> feature it is now possible to nest the element in the content instead of using it only as a sibling. This is handy if you want to use the same element e.g. for small screens as off-canvas and for large screens as usual page element without duplicate content.

    Another improvement is the support of several off-canvas elements that share the same position e.g. two elements with `position-left`.

    Advanced off-canvas users may use the new `contentId` option to bind an element to a content. This lets you place the element much more flexibly as it may be a sibling of the content, a child or none of it.<br>
    <strong>Important:</strong> when using the `contentId` on a nested element you must also use the new `nested` option and tell the JavaScript it's nested!

    <div class="callout warning">
      <p>Please note that it's not possible to use the push transition for a nested off-canvas element.</p>
    </div>

    ```html
    <button type="button" class="button" data-toggle="offCanvasNestedPush">
      Open Nested Off-Canvas Push
    </button>
    <button type="button" class="button" data-toggle="offCanvasNestedOverlap">
      Open Nested Off-Canvas Overlap
    </button>

    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>

    <div class="off-canvas position-left is-closed" id="offCanvasNestedPush" data-off-canvas>
      <div class="callout">
        <p>I'm a nested off-canvas that mustn't be a sibling of the off-canvas content anymore.</p>
        <p>Since push transition is currently not possible for nested elements, I'm forced to use overlayp transition.</p>
      </div>
    </div>
    <div class="off-canvas position-left is-closed" data-transition="overlap" id="offCanvasNestedOverlap" data-off-canvas>
      <div class="callout">I'm a nested off-canvas that uses overlap transition and the same position as the other nested off-canvas.</div>
    </div>

    <p>Enim, repudiandae officia dolores temporibus soluta, ipsa saepe tempora ipsum laudantium in mollitia quidem, nisi magni provident hic architecto rem culpa beatae.</p>
    ```

    ---

    ## Off-canvas Scrollbox

    Placing scrollable elements within an off-canvas if `contentScroll: false` is tricky because on touch devices it may become difficult to scroll those elements due to stopped event propagation. There's no continous touch move possible.

    However you can still achieve this when you add `data-off-canvas-scrollbox` to the scrollable elements.
    Once you've reached the start/end of a scrollbox (while touch moving) the off-canvas will continue scrolling the off-cannvas element. You can optionally use a wrapper with `data-off-canvas-scrollbox-outer` which gets scrolled instead of the off-canvas element. This is useful when you nest your scrollable elements into other scrollable elements or work with fix heights.

    ```html
    <div class="off-canvas-wrapper">
      <div class="off-canvas-content" data-off-canvas-content style="min-height: 300px;">
        <div class="grid-x">
          <div class="cell">
            <div class="primary callout">
              You have to view this example on a touch device or use e.g. the chrome dev tools with touch emulation.
            </div>
            <button type="button" class="button" data-toggle="offCanvasScrollbox">
              Open Scrollbox Off-canvas
            </button>
          </div>
        </div>
        <div class="off-canvas-absolute position-left" id="offCanvasScrollbox" data-off-canvas data-content-scroll="false">
          <div style="padding: 0 1rem;">
            <article data-off-canvas-scrollbox style="max-height: 290px; overflow: auto; padding: 0.5rem 0; margin-bottom: 1rem; box-shadow: inset 0 -10px 10px -10px rgba(0,0,0,0.65);">
              <p>The 1st list supports continuous touchmove</p>
              <ul>
                <li>bullet 01</li>
                <li>bullet 02</li>
                <li>bullet 03</li>
                <li>bullet 04</li>
                <li>bullet 05</li>
                <li>bullet 06</li>
                <li>bullet 07</li>
                <li>bullet 08</li>
                <li>bullet 09</li>
                <li>bullet 10</li>
              </ul>
            </article>
            <article style="max-height: 290px; overflow: auto; padding: 0.5rem 0; margin-bottom: 1rem; box-shadow: inset 0 -10px 10px -10px rgba(0,0,0,0.65);">
              <p>The 2nd list doesn't support continuous touchmove</p>
              <ul>
                <li>bullet 01</li>
                <li>bullet 02</li>
                <li>bullet 03</li>
                <li>bullet 04</li>
                <li>bullet 05</li>
                <li>bullet 06</li>
                <li>bullet 07</li>
                <li>bullet 08</li>
                <li>bullet 09</li>
                <li>bullet 10</li>
              </ul>
            </article>
            <article style="padding: 0.5rem 0;">
              <p>The 3rd list is regular content</p>
              <ul>
                <li>bullet 01</li>
                <li>bullet 02</li>
                <li>bullet 03</li>
                <li>bullet 04</li>
                <li>bullet 05</li>
                <li>bullet 06</li>
                <li>bullet 07</li>
                <li>bullet 08</li>
                <li>bullet 09</li>
                <li>bullet 10</li>
              </ul>
            </article>
          </div>
        </div>
      </div>
    </div>
    ```

    ---

    ## Sticky

    By default an element with `position: fixed` disappears when opening an off-canvas with push transition. The reason for this is the transform property of the off-canvas content container what causes a `position: absolute` behavior for the fixed element.

    The good news: we've added the possibility to preserve the fixed appearance!
    You only have to add the attribute `data-off-canvas-sticky` to every sticky / fixed element that is supposed to remain fixed after opening the off-canvas.

    <div class="callout warning">
      Please note that using this attribute will force the option `contentScroll: false`
    </div>

    ```html
    <div class="top-bar sticky" data-sticky data-off-canvas-sticky>
      Sticky top bar that will remain sticky after having opened an off-canvas
    </div>
    ```

    ---

    ## Off-canvas Sizes

    In v6.4.2 the type of the off-canvas size variables has changed from number to map. This lets you define breakpoint specific sizes instead of one value for all.
    The map may contain every key that is defined in `$breakpoint-classes`.

    <div class="warning callout">
      Please note the sizes maps do currently not work perfectly for the reveal classes. If sizes are defined for medium and large, `.reveal-for-medium` will only consider the medium value. This is going to get fixed in a future release.
    </div>

    ```scss
    $offcanvas-sizes: (
      small: 250px,
      medium: 350px,
    );
    $offcanvas-vertical-sizes: (
      small: 250px,
      medium: 350px,
    );
    ```

    ---

    ## Migrating from versions prior to v6.4

    If you're upgrading from v6.3 there's nothing to do unless you haven't changed the default value of `$offcanvas-shadow`. Prior to v6.4 this variable was used for both, overlap and push off-canvas elements. Now it's only used for the overlap element whereas the push element uses two new variables:

    - `$offcanvas-inner-shadow-size` which is a number (mostly px)
    - `$offcanvas-inner-shadow-color` which is a color (mostly rgba)

    So if you have changed the default off-canvas shadow you have to adjust the value of these variables in your settings.

    ---

    ## Migrating from versions prior to v6.3

    <div class="primary callout">
      <p>`off-canvas-wrapper` and `off-canvas-wrapper-inner` are no longer needed on the new off-canvas. If you leave them in with 6.3+ off-canvas will work as expected.</p>
    </div>

    The default off-canvas position has changed from absolute to fixed. This will likely be the position you want since the menu is in view when opened regardless of the scroll position. You can choose the off-canvas position back to absolute using the built in classes:

    - `.is-overlay-absolute`
    - `.is-overlay-fixed`

    Or in globally in the _settings.scss, set the <code>$offcanvas-fixed-reveal</code> variable to <code>false</code>.</p>

    ```html
    <div class="off-canvas position-left reveal-for-large" data-off-canvas>
      <!-- ... -->
    </div>
    ```

    ### Pre 6.3 Off-canvas Setup

    To start, create two wrappers to house the page. These are necessary to prevent the off-canvas panels from being visible when they're not open. They also smooth out cross-browser bugs.
    - The outer wrapper has the class `.off-canvas-wrapper`.
    - The inner wrapper has the class `.off-canvas-wrapper-inner` and the attribute `data-off-canvas-wrapper`.

    ```html
    <body>
      <div class="off-canvas-wrapper">
        <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper></div>
      </div>
    </body>
    ```

    Inside these wrappers, create an off-canvas panel with the class `.off-canvas` and the attribute `data-off-canvas`. The panel also needs a positioning class, which can be `.position-left` or `.position-right`, and an attribute set for the position, `data-position="left"` or `data-position="right"`. Last, make sure the off-canvas panel has a unique ID so it can be targeted.

    Along with the panel, the main content of your page will be housed in its own container with the class `.off-canvas-content` and attribute `data-off-canvas-content`. You will be putting your actual page content inside a class of `.off-canvas-content`.)

    ```html
    <body>
      <div class="off-canvas-wrapper">
        <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>
          <div class="off-canvas position-left" id="offCanvas" data-off-canvas></div>
          <div class="off-canvas-content" data-off-canvas-content></div>
        </div>
      </div>
    </body>
    ```"""

    pass


class ORBIT:
    """---
    title: Orbit
    description: An image and content carousel with animation support and many customizable options.
    sass: scss/components/_orbit.scss
    js: js/foundation.orbit.js
    mui: true
    video: l0bdHvBuylA
    tags:
      - slider
      - carousel
    ---

    ## Basics

    Orbit doesn't automatically generate any HTML for you, giving you the flexibility to move around the various pieces of the plugin. Here's a complete example&mdash;we'll break down the individual pieces farther down.

    <div class="callout alert">
      <p>Please note that apart from Javascript, <a href="https://get.foundation/sites/docs/motion-ui.html">Motion UI</a> is a dependency for Orbit to work properly. If in case, you don't want any animations within your Carousel, you can always <a href="#disabling-animation">disable</a> the animation.</p>
    </div>

    <p>
      <a class="" data-open-video="0:48"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/GmGzWY?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="orbit" role="region" aria-label="Favorite Space Pictures" data-orbit>
      <div class="orbit-wrapper">
        <div class="orbit-controls">
          <button class="orbit-previous"><span class="show-for-sr">Previous Slide</span>&#9664;&#xFE0E;</button>
          <button class="orbit-next"><span class="show-for-sr">Next Slide</span>&#9654;&#xFE0E;</button>
        </div>
        <ul class="orbit-container">
          <li class="is-active orbit-slide">
            <figure class="orbit-figure">
              <img class="orbit-image" src="https://placehold.it/1200x600/999?text=Slide-1" alt="Space">
              <figcaption class="orbit-caption">Space, the final frontier.</figcaption>
            </figure>
          </li>
          <li class="orbit-slide">
            <figure class="orbit-figure">
              <img class="orbit-image" src="https://placehold.it/1200x600/888?text=Slide-2" alt="Space">
              <figcaption class="orbit-caption">Lets Rocket!</figcaption>
            </figure>
          </li>
          <li class="orbit-slide">
            <figure class="orbit-figure">
              <img class="orbit-image" src="https://placehold.it/1200x600/777?text=Slide-3" alt="Space">
              <figcaption class="orbit-caption">Encapsulating</figcaption>
            </figure>
          </li>
          <li class="orbit-slide">
            <figure class="orbit-figure">
              <img class="orbit-image" src="https://placehold.it/1200x600/666&text=Slide-4" alt="Space">
              <figcaption class="orbit-caption">Outta This World</figcaption>
            </figure>
          </li>
        </ul>
      </div>
      <nav class="orbit-bullets">
        <button class="is-active" data-slide="0">
          <span class="show-for-sr">First slide details.</span>
          <span class="show-for-sr" data-slide-active-label>Current Slide</span>
        </button>
        <button data-slide="1"><span class="show-for-sr">Second slide details.</span></button>
        <button data-slide="2"><span class="show-for-sr">Third slide details.</span></button>
        <button data-slide="3"><span class="show-for-sr">Fourth slide details.</span></button>
      </nav>
    </div>
    ```

    <div class="orbit" role="region" aria-label="Favorite Space Pictures" data-orbit>
      <div class="orbit-wrapper">
        <div class="orbit-controls">
          <button class="orbit-previous"><span class="show-for-sr">Previous Slide</span>&#9664;&#xFE0E;</button>
          <button class="orbit-next"><span class="show-for-sr">Next Slide</span>&#9654;&#xFE0E;</button>
        </div>
        <ul class="orbit-container">
          <li class="is-active orbit-slide">
            <figure class="orbit-figure">
              <img class="orbit-image" src="assets/img/orbit/01.jpg" alt="Space">
              <figcaption class="orbit-caption">Space, the final frontier.</figcaption>
            </figure>
          </li>
          <li class="orbit-slide">
            <figure class="orbit-figure">
              <img class="orbit-image" src="assets/img/orbit/02.jpg" alt="Space">
              <figcaption class="orbit-caption">Lets Rocket!</figcaption>
            </figure>
          </li>
          <li class="orbit-slide">
            <figure class="orbit-figure">
              <img class="orbit-image" src="assets/img/orbit/03.jpg" alt="Space">
              <figcaption class="orbit-caption">Encapsulating</figcaption>
            </figure>
          </li>
          <li class="orbit-slide">
            <figure class="orbit-figure">
              <img class="orbit-image" src="assets/img/orbit/04.jpg" alt="Space">
              <figcaption class="orbit-caption">Outta This World</figcaption>
            </figure>
          </li>
        </ul>
      </div>
      <nav class="orbit-bullets">
        <button class="is-active" data-slide="0">
          <span class="show-for-sr">First slide details.</span>
          <span class="show-for-sr" data-slide-active-label>Current Slide</span>
        </button>
        <button data-slide="1"><span class="show-for-sr">Second slide details.</span></button>
        <button data-slide="2"><span class="show-for-sr">Third slide details.</span></button>
        <button data-slide="3"><span class="show-for-sr">Fourth slide details.</span></button>
      </nav>
    </div>

    ---

    ### Wrapper

    The wrapper houses the entire carousel. We use the `aria-label` attribute to label what the carousel is, for assistive technology.

    ```html
    <div class="orbit" role="region" aria-label="Favorite Space Pictures" data-orbit>
    </div>
    ```

    ### Slide Container

    The slide container houses each individual slide. In our above markup example, we also placed the buttons in here, so we can anchor them to the center edge of the slide container. However, they can be moved anywhere within the `data-orbit` wrapper.

    Each slide is an `<li>` with the class `.orbit-slide`. The first slide is marked with the `.is-active` class to indicate it's the default. You can place any HTML you want inside of the slide, but we have some premade styles for image-based slides with a caption.

    ```html
    <ul class="orbit-container">
      <li class="orbit-slide is-active">
        <figure class="orbit-figure">
          <img class="orbit-image" src="assets/img/orbit/01.jpg" alt="Space">
          <figcaption class="orbit-caption">Space, the final frontier.</figcaption>
        </figure>
      </li>
      <!-- More slides... -->
    </ul>
    ```

    ### Next/Previous Arrows

    Orbit controls use the class `.orbit-previous` and `.orbit-next`. The below example has an important accessibility hook: since we're using ASCII arrows for the carousel controls, we add screen reader-only text (wrapped in the class `.show-for-sr`) that explain what the controls do.

    ```html
    <button class="orbit-previous"><span class="show-for-sr">Previous Slide</span> &#9664;&#xFE0E;</button>
    <button class="orbit-next"><span class="show-for-sr">Next Slide</span> &#9654;&#xFE0E;</button>
    ```

    ### Bullets

    The bullets serve two purposes: they mark the current slide, and can be clicked on to navigate to another slide. Like with the controls, the bullets can also have screen reader-friendly labels.

    ```html
    <nav class="orbit-bullets">
      <button class="is-active" data-slide="0">
        <span class="show-for-sr">First slide details.</span>
        <span class="show-for-sr" data-slide-active-label>Current Slide</span>
      </button>
      <button data-slide="1"><span class="show-for-sr">Second slide details.</span></button>
      <button data-slide="2"><span class="show-for-sr">Third slide details.</span></button>
      <button data-slide="3"><span class="show-for-sr">Fourth slide details.</span></button>
    </nav>
    ```

    ---

    ## Slide Contents

    A carousel slide can contain images or HTML&mdash;you can even mix between slides in one carousel!

    <p>
      <a class="" data-open-video="5:20"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/vmrbrV?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <li class="orbit-slide">
      <div>
        <h3 class="text-center">2: You can also throw some text in here!</h3>
        <p class="text-center">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde harum rem, beatae ipsa consectetur quisquam. Rerum ratione, delectus atque tempore sed, suscipit ullam, beatae distinctio cupiditate ipsam eligendi tempora expedita.</p>
        <h3 class="text-center">This Orbit slider does not use animations.</h3>
      </div>
    </li>
    ```

    <div class="orbit" role="region" aria-label="Favorite Text Ever" data-orbit>
      <div class="orbit-wrapper">
        <div class="orbit-controls">
          <button class="orbit-previous" aria-label="previous"><span class="show-for-sr">Previous Slide</span>&#9664;</button>
          <button class="orbit-next" aria-label="next"><span class="show-for-sr">Next Slide</span>&#9654;</button>
        </div>
        <ul class="orbit-container">
          <li class="is-active orbit-slide">
            <div class="docs-example-orbit-slide">
              <p><strong>This is dodgerblue.</strong> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            </div>
          </li>
          <li class="orbit-slide">
            <div class="docs-example-orbit-slide">
              <p><strong>This is rebeccapurple.</strong> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            </div>
          </li>
          <li class="orbit-slide">
            <div class="docs-example-orbit-slide">
              <p><strong>This is darkgoldenrod.</strong> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            </div>
          </li>
          <li class="orbit-slide">
            <div class="docs-example-orbit-slide">
              <p><strong>This is lightseagreen.</strong> Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            </div>
          </li>
        </ul>
      </div>
      <nav class="orbit-bullets">
        <button class="is-active" data-slide="0">
          <span class="show-for-sr">First slide details.</span>
          <span class="show-for-sr" data-slide-active-label>Current Slide</span>
        </button>
        <button data-slide="1"><span class="show-for-sr">Second slide details.</span></button>
        <button data-slide="2"><span class="show-for-sr">Third slide details.</span></button>
        <button data-slide="3"><span class="show-for-sr">Fourth slide details.</span></button>
      </nav>
    </div>

    ---

    ## Using Animation

    Orbit uses [Motion UI](motion-ui.html) CSS classes to animate slides around.

    <div class="callout warning">
      <p>Without the inclusion of the `motion-ui` [Motion UI](motion-ui.html) CSS file in your template, Orbit slider fails to work properly. </p>
    </div>

    There are four plugin options you can set to change the default effects:

    - `data-anim-in-from-left`: transition to play when a slide comes *in from the left*.
    - `data-anim-in-from-right`: transition to play when a slide comes *in from the right*.
    - `data-anim-out-to-left`: transition to play when a slide comes *out to the left*.
    - `data-anim-out-to-right`: transition to play when a slide comes *out to the right*.

    Since those option names are pretty *long*, you can also set them all in one HTML attribute, using `data-options`:


    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/oWymQy?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="orbit" role="region" aria-label="Favorite Space Pictures" data-orbit data-options="animInFromLeft:fade-in; animInFromRight:fade-in; animOutToLeft:fade-out; animOutToRight:fade-out;">
    </div>
    ```

    <div class="orbit" role="region" aria-label="Favorite Space Pictures" data-orbit data-options="animInFromLeft:fade-in; animInFromRight:fade-in; animOutToLeft:fade-out; animOutToRight:fade-out;">
      <div class="orbit-wrapper">
        <div class="orbit-controls">
          <button class="orbit-previous" aria-label="previous"><span class="show-for-sr">Previous Slide</span>&#9664;</button>
          <button class="orbit-next" aria-label="next"><span class="show-for-sr">Next Slide</span>&#9654;</button>
        </div>
        <ul class="orbit-container">
          <li class="is-active orbit-slide">
            <figure class="orbit-figure">
              <img class="orbit-image" src="assets/img/orbit/01.jpg" alt="Space">
              <figcaption class="orbit-caption">Space, the final frontier.</figcaption>
            </figure>
          </li>
          <li class="orbit-slide">
            <figure class="orbit-figure">
              <img class="orbit-image" src="assets/img/orbit/02.jpg" alt="Space">
              <figcaption class="orbit-caption">Lets Rocket!</figcaption>
            </figure>
          </li>
          <li class="orbit-slide">
            <figure class="orbit-figure">
              <img class="orbit-image" src="assets/img/orbit/03.jpg" alt="Space">
              <figcaption class="orbit-caption">Encapsulating</figcaption>
            </figure>
          </li>
          <li class="orbit-slide">
            <figure class="orbit-figure">
              <img class="orbit-image" src="assets/img/orbit/04.jpg" alt="Space">
              <figcaption class="orbit-caption">Outta This World</figcaption>
            </figure>
          </li>
        </ul>
      </div>
      <nav class="orbit-bullets">
        <button class="is-active" data-slide="0">
          <span class="show-for-sr">First slide details.</span>
          <span class="show-for-sr" data-slide-active-label>Current Slide</span>
        </button>
        <button data-slide="1"><span class="show-for-sr">Second slide details.</span></button>
        <button data-slide="2"><span class="show-for-sr">Third slide details.</span></button>
        <button data-slide="3"><span class="show-for-sr">Fourth slide details.</span></button>
      </nav>
    </div>

    ---

    ### Disabling Animation

    To disable Motion UI, set the plugin option `useMUI` to `false`. Written as an HTML attribute, that's `data-use-m-u-i="false"`.

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/VbdgNV?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="orbit" role="region" aria-label="Favorite Space Pictures" data-orbit data-use-m-u-i="false">
    </div>
    ```

    <div class="orbit" role="region" aria-label="Favorite Space Pictures" data-orbit data-use-m-u-i="false">
      <div class="orbit-wrapper">
        <div class="orbit-controls">
          <button class="orbit-previous" aria-label="previous"><span class="show-for-sr">Previous Slide</span>&#9664;</button>
          <button class="orbit-next" aria-label="next"><span class="show-for-sr">Next Slide</span>&#9654;</button>
        </div>
        <ul class="orbit-container">
          <li class="is-active orbit-slide">
            <figure class="orbit-figure">
              <img class="orbit-image" src="assets/img/orbit/01.jpg" alt="Space">
              <figcaption class="orbit-caption">Space, the final frontier.</figcaption>
            </figure>
          </li>
          <li class="orbit-slide">
            <figure class="orbit-figure">
              <img class="orbit-image" src="assets/img/orbit/02.jpg" alt="Space">
              <figcaption class="orbit-caption">Lets Rocket!</figcaption>
              </figure>
          </li>
          <li class="orbit-slide">
            <figure class="orbit-figure">
              <img class="orbit-image" src="assets/img/orbit/03.jpg" alt="Space">
              <figcaption class="orbit-caption">Encapsulating</figcaption>
              </figure>
          </li>
          <li class="orbit-slide">
            <figure class="orbit-figure">
              <img class="orbit-image" src="assets/img/orbit/04.jpg" alt="Space">
              <figcaption class="orbit-caption">Outta This World</figcaption>
              </figure>
          </li>
        </ul>
      </div>
      <nav class="orbit-bullets">
        <button class="is-active" data-slide="0">
          <span class="show-for-sr">First slide details.</span>
          <span class="show-for-sr" data-slide-active-label>Current Slide</span>
        </button>
        <button data-slide="1"><span class="show-for-sr">Second slide details.</span></button>
        <button data-slide="2"><span class="show-for-sr">Third slide details.</span></button>
        <button data-slide="3"><span class="show-for-sr">Fourth slide details.</span></button>
     </nav>
    </div>"""

    pass


class PAGINATION:
    """---
    title: Pagination
    description: Pagination is a type of navigation that lets users click through pages of search results, products, or other related items.
    video: '9gcGADHzz9o'
    sass: scss/components/_pagination.scss
    ---

    ## Basics

    A pagination list is just a `<ul>` with the class `.pagination`, and a series of `<li>`/`<a>` pairs. Add the class `.current` to an `<li>` to mark the current page, or `.disabled` to add disabled styles to a link.

    Note that the list is nested inside a `<nav>` with the attributes `aria-label="Pagination"`. This explains the purpose of the component to assistive technologies.

    Extra screen reader-only text should also be added to a pagination element. In the below example, users reading the page will just see "Next" and "Previous", but screen readers will read it as "Next page" and "Previous page". Additionally, the text for the current page will read as "You're on page one".

    <p>
      <a class="" data-open-video="0:47"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/BRxVmB?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <nav aria-label="Pagination">
      <ul class="pagination">
        <li class="pagination-previous disabled">Previous <span class="show-for-sr">page</span></li>
        <li class="current"><span class="show-for-sr">You're on page</span> 1</li>
        <li><a href="#" aria-label="Page 2">2</a></li>
        <li><a href="#" aria-label="Page 3">3</a></li>
        <li><a href="#" aria-label="Page 4">4</a></li>
        <li class="ellipsis" aria-hidden="true"></li>
        <li><a href="#" aria-label="Page 12">12</a></li>
        <li><a href="#" aria-label="Page 13">13</a></li>
        <li class="pagination-next"><a href="#" aria-label="Next page">Next <span class="show-for-sr">page</span></a></li>
      </ul>
    </nav>
    ```

    ---

    ## Centered

    The items in a pagination list are `display: inline-block`, which makes centering them easy. Use our built-in `.text-center` class, or add `text-align: center` in your CSS.

    <p>
      <a class="" data-open-video="7:20"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/dWKYZb?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <nav aria-label="Pagination">
      <ul class="pagination text-center">
        <li class="pagination-previous disabled">Previous</li>
        <li class="current"><span class="show-for-sr">You're on page</span> 1</li>
        <li><a href="#" aria-label="Page 2">2</a></li>
        <li><a href="#" aria-label="Page 3">3</a></li>
        <li><a href="#" aria-label="Page 4">4</a></li>
        <li class="ellipsis"></li>
        <li><a href="#" aria-label="Page 12">12</a></li>
        <li><a href="#" aria-label="Page 13">13</a></li>
        <li class="pagination-next"><a href="#" aria-label="Next page">Next</a></li>
      </ul>
    </nav>
    ```"""

    pass


class PANINI:
    """---
    title: Panini
    description: A flat file compiler that powers our prototyping template. Create pages with consistent layouts and reusable partials with ease.
    video: 't_ekdBMj4cc'
    library:
      github: https://github.com/foundation/panini
      docs: https://github.com/foundation/panini
    ---

    {{{{raw}}}}

    If you've ever created a static site, maybe you had five pages that all shared the same header and footer. You create your first page, and then copy and paste the common elements to the next page. But now if you need to make a change to the header, the change has to be made across multiple files.

    Panini is a flat file compiler that uses the concepts of templates, pages, and partials&mdash;powered by the [Handlebars](https://handlebarsjs.com/) templating language&mdash;to streamline the process of creating static prototypes.

    Our [prototyping template](starter-projects.html) uses Panini, along with a host of other tools for processing Sass, JavaScript, and images, to make creating static prototypes easy. It's already been configured to utilize all of the features below, but if you want to learn the specifics of how to configure the library, head over to the [Panini GitHub page](https://github.com/foundation/panini).

    ---

    ## Basics: Templates & Pages

    A **template** is a common layout that every page in your design shares. It's possible to have multiple templates, but generally you'll only need one, and a page can only use one template. In the prototyping template, the default layout is found under `src/layouts/default.html`.

    Here's what a basic template might look like:

    ```handlebars
    <html>
      <head>
        <title>Definitely a Website!</title>
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

    In the prototyping template, these finished files are compiled into a standalone folder called `dist` (short for "distribution"), which also includes your processed CSS, JavaScript, and images. This folder can easily be uploaded to any web server, or Notable's Hosted Prototypes service.

    ---

    ## Partials

    Partials are a feature of Handlebars which allow you to inject HTML anywhere in a page or layout. They're really useful when you need to repeat certain chunks of code throughout your pages, or to keep individual files from getting too cluttered with HTML.

    Here's an example of a layout file that divides its key sections into partials:

    ```handlebars
    <html>
      <head>
        <title>Definitely STILL a Website!</title>
      </head>
      <body>
        {{> header}}
        {{> navigation}}
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

    Helpers are special functions that manipulate content on the page. In addition to [Handlebars's built-in helpers](https://handlebarsjs.com/builtin_helpers.html), Panini includes a few custom helpers and you can add your own.

    ### ifequal
    Displays the HTML inside the helper if the two values are equal.
    ```handlebars
    {{#ifequal foo bar}}
      <p>foo and bar are equal</p>
    {{else}}
      <p>foo and bar are not equal</p>
    {{/ifequal}}
    ```

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
    Lorem ipsum [dolor sit amet](https://example.com), consectetur adipisicing elit. Nam dolor, perferendis. Mollitia aut dolorum, est amet libero eos ad facere pariatur, ullam dolorem similique fugit, debitis impedit, eligendi officiis dolores.
    {{/markdown}}
    ```

    ### Custom Helpers

    If you don't see the right helper, you can write your own. Add a javascript file to 'src/helpers', add `helpers: 'src/helpers'` to the Panini process in your gulpfile.babel.js, restart npm, then call it in your templates.

    ```
    // Example file src/helpers/bold.js
    module.exports = function(options) {
      // options.fn(this) = Handelbars content between {{#bold}} HERE {{/bold}}
      var bolder = '<strong>' + options.fn(this) + '</strong>';
      return bolder;
    }
    ```

    ```
    // Example  gulpfile.babel.js
    function pages() {
      return gulp.src('src/pages/**/*.html')
        .pipe(panini({
          root: 'src/pages',
          layouts: 'src/layouts',
          partials: 'src/partials',
          helpers: 'src/helpers'
        }))
        .pipe(inky())
        .pipe(gulp.dest('dist'));
    }
    ```

    Then in your projects call your custom `{{#bold}}` helper

    ```
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

    ```
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

    {{{{/raw}}}}"""

    pass


class PROGRESS_BAR:
    """---
    title: Progress Bar
    description: Show your progress. A simple way to add progress bars to your layouts. You only need two HTML elements to make them and they're easy to customize.
    video: gMLSHzlshpM
    sass:
      - scss/components/_progress-bar.scss
      - scss/forms/_progress.scss
      - scss/forms/_meter.scss
    ---

    ## Basics

    A progress bar has two elements: the container `.progress`, and the meter `.progress-meter`. The `role` and `aria-` attributes in the code example clarify the status of the bar:

    - `aria-valuemin`: Minimum value.
    - `aria-valuemax`: Maximum value.
    - `aria-valuenow`: Current value.

    If the value of the progress bar is not numeric, also add the attribute `aria-valuetext`, which should include a human-readable version of the bar's value.

    <p>
      <a class="" data-open-video="0:39"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/PmBqPB?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="progress" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
      <div class="progress-meter"></div>
    </div>
    ```

    Add a `width` CSS property to the inner meter to fill the progress bar.

    ```html
    <div class="progress" role="progressbar" aria-valuenow="50" aria-valuemin="0" aria-valuetext="50 percent" aria-valuemax="100">
      <div class="progress-meter" style="width: 50%"></div>
    </div>
    ```

    ---

    ## Colors

    A progress bar can be styled with the `.secondary`, `.success`, `.warning`, and `.alert` colors.

    <p>
      <a class="" data-open-video="3:22"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/mmjJPL?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="secondary progress" role="progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuetext="25 percent" aria-valuemax="100">
      <div class="progress-meter" style="width: 25%"></div>
    </div>

    <div class="success progress">
      <div class="progress-meter" style="width: 50%"></div>
    </div>

    <div class="warning progress">
      <div class="progress-meter" style="width: 50%"></div>
    </div>

    <div class="alert progress">
      <div class="progress-meter" style="width: 75%"></div>
    </div>
    ```

    ---

    ## With Text

    You can add text inside the meter of a progress bar. Make sure the text you use in the meter is also used in the `aria-valuetext` attribute.

    <p>
      <a class="" data-open-video="5:00"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/NjBqRm?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="progress" role="progressbar" aria-valuenow="25" aria-valuemin="0" aria-valuetext="25 percent" aria-valuemax="100">
      <span class="progress-meter" style="width: 25%">
        <span class="progress-meter-text">25%</span>
      </span>
    </div>
    ```

    ---

    ## Native Progress

    As an alternative to our custom progress bar style, you can also opt to use the native `<progress>` element. It provides a more succinct way to create progress bars, but it's not supported in IE9, and some other older browsers. [View `<progress>` element support.](https://caniuse.com/#feat=progress)

    ```html
    <progress max="100" value="75"></progress>
    ```

    If you're using the Sass version of Foundation, add this line to your main Sass file to export the `<progress>` CSS:

    ```scss
    @include foundation-progress-element;
    ```

    The `<progress>` element can be styled with the same coloring classes: `.secondary`, `.success`, `.warning`, and `.alert`.

    ```html
    <progress class="secondary" max="100" value="75"></progress>
    <progress class="success" max="100" value="75"></progress>
    <progress class="warning" max="100" value="75"></progress>
    <progress class="alert" max="100" value="75"></progress>
    ```

    ---

    ## Native Meter

    For the *extra* adventurous developers out there, we also provide styles for the `<meter>` element. What's the difference? `<progress>` represents a value that changes over time, like storage capacity. `<meter>` represents a value that fluctuates around some optimum value. It also has *no* support in Internet Explorer, Mobile Safari, or Android 2. [View `<meter>` element support.](https://caniuse.com/#search=meter)

    If you're using the Sass version of Foundation, add this line to your main Sass file to export the `<meter>` CSS:

    ```scss
    @include foundation-meter-element;
    ```

    The meter automatically colors itself based on the current values, and the defined low, medium, and high ranges. [Learn more about the mechanics of `<meter>` values.](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms/The_native_form_widgets#Meters_and_progress_bars)

    ```html
    <meter value="30" min="0" low="33" high="66" optimum="100" max="100"></meter>
    <meter value="50" min="0" low="33" high="66" optimum="100" max="100"></meter>
    <meter value="100" min="0" low="33" high="66" optimum="100" max="100"></meter>
    ```

    ---

    ## Screen Readers

    Test the progress bar with different `aria-valuenow` values in a couple of screen readers. The screen reader behavior may not be always obvious.

    If the value of the progress bar is numeric, make sure the range is defined correctly (extracting `aria-valuemin` from `aria-valuemax` defines the full range). For percentage progress bars (0-100%) the value range is typically 100 (`aria-valuemin="0"` and `aria-valuemax="100"`). Most screen readers will calculate the announced percentage based on these numbers with the following formula:

    ```
    aria-valuenow / (aria-valuemax - aria-valuemin) = announced percentage
    ```"""

    pass


class PROTOTYPING_UTILITIES:
    """---
    title: Prototyping Utilities
    description: Quickly prototype layouts and UI with Foundation's Prototyping Utilities. These optional classes and mixins are great for quickly turning sketches and mockups into coded prototypes.
    video: Xhc_KUJMEuk
    sass:
      - scss/prototype/*.scss
    ---

    <h4><strong>Prototype to Production</strong></h4>

    Prototyping allows us to see problems more clearly—and often earlier—in the development process. Designs in sketches or wireframes only get us so far in understanding the behavior, feasibility, and cost (time or resources) of implementation. Prototyping processes foster collaboration where designers and developers work closely together find better solutions.

    Sometimes prototype code is meant to be thrown away, and that's ok. While in early stage development it's extremely valuable to get ideas and interactions up and shared with stakeholders for scrutiny. This is how ideas get fleshed out and improved. It's not code we're delivering, it's a solution to a problem. Get the idea out, get feedback, iterate, repeat. Then when all parties are satisfied the right approach is being taken, go back to clean it up and refactor.

    Foundation's Prototyping Utilities help you build coded prototypes from scratch ultra-fast. This allows you to get to right answer faster through feedback and experimentation. From positioning to visual styles, there are a range of utilities to choose from. Every Utility has a mixin, so you can use your own custom classes or swap classes for mixins in production for cleaner markup.

    #### Prototype mode is **disabled by default!**

    Not all projects require Prototyping Utilities and adding utility classes like these increase your CSS file size especially if you're not using all of them. For these reasons Prototype mode is *disabled by default*.

    <div class="primary callout">
            <p>
                    Many Prototype classes use `!important` to ensure that these they aren't overridden by more specific selectors. This framework conscientiously avoids using `!important` declarations. Please note that we have only inserted `!important` on those specific **CSS** properties which in no case should be overridden.
            </p>
    </div>

    ---

    ## Enabling Prototype Mode

    <div class="warning callout">
            <p>
                    Prototyping classes like these below should only be used for prototyping tasks. Also if you are using **Sass**, we encourage you to use **[Prototyping Mixins](#sass-mixins)** instead.
            </p>
    </div>

    Using the Sass version of Foundation, you can enable prototype mode in two ways:

    If you use the `foundation-everything()` mixin in your main Sass file, just pass in `$prototype: true` to enable the prototype mode.

    ```scss
    @include foundation-everything($prototype: true);
    ```

    If you included each component manually (like our starter projects do), open up your `app.scss` file and simply comment in:

    ```scss
    // @include foundation-prototype-classes;
    ```

    So it will look like:

    ```scss
    @include foundation-prototype-classes;
    ```

    You can instead import only the specific utility classes that you need. To make it easy, the full list is included below:

    ```scss
    @include foundation-prototype-typescale;
    @include foundation-prototype-text-utilities;
    @include foundation-prototype-text-transformation;
    @include foundation-prototype-text-decoration;
    @include foundation-prototype-font-styling;
    @include foundation-prototype-list-style-type;
    @include foundation-prototype-rounded;
    @include foundation-prototype-bordered;
    @include foundation-prototype-shadow;
    @include foundation-prototype-arrow;
    @include foundation-prototype-separator;
    @include foundation-prototype-overflow;
    @include foundation-prototype-display;
    @include foundation-prototype-position;
    @include foundation-prototype-border-box;
    @include foundation-prototype-border-none;
    @include foundation-prototype-sizing;
    @include foundation-prototype-spacing;
    ```

    Looking for more customization? Click here for the [Sass Reference](#sass-reference)

    ---

    ## Responsive breakpoints

    <div class="alert callout">
      <p>Responsive breakpoints is disabled by default.</p>
    </div>

    These prototype classes also have an optional mobile first responsive classes  so that setting a class will apply to the small breakpoint and large unless overridden by a class for a larger breakpoint. <br>
    You can easily enable these classes by setting `$global-prototype-breakpoints` to `true`.

    ```html
    <p class="medium-text-uppercase">This text will be uppercase for medium and up.</p>
    <p class="large-text-lowercase">This text will be lowercase for large breakpoint.</p>
    ```

    You can also customise things by choosing to add responsive breakpoints only for specific prototype helpers that you would need as responsive classes. <br>
    For example, text transformation classes have a breakpoint variable `$prototype-transformation-breakpoints` which is set to `$global-prototype-breakpoints` which is set to `false` by default. For enabling responsive breakpoints for text transformation classes, simply set:

    ```scss
    $prototype-transformation-breakpoints: true;
    ```

    ---

    ## Component Styling

    These `.radius`, `.rounded`, `.bordered` & `.shadow` classes can be used independently or together to style the component by rounding its corners, giving light borders, and creating shadow to it respectively. Mostly used in buttons, cards, tables, images and many more.

    <div class="primary callout">
            **Sass Tip**: You can use [Shadow](#shadow) mixin to create something like `shadow-hover-focus`. [Codepen example](https://codepen.io/IamManchanda/pen/XMRMwo)
    </div>

    <p>
      <a class="" data-open-video="1:06"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    #### Buttons

    ```html
    <button type="button" class="button radius bordered shadow primary">Primary</button>
    <button type="button" class="button rounded bordered shadow secondary">Secondary</button>
    <button type="button" class="button radius bordered shadow success">Success</button>
    <button type="button" class="button rounded bordered shadow alert">Alert</button>
    <button type="button" class="button radius bordered shadow warning">Warning</button>
    ```

    #### Switches

    Add the `.rounded` class to `.switch` to make it rounded.

    ```html
    <div class="switch rounded">
      <input class="switch-input" id="exampleSwitch" type="checkbox" name="exampleSwitch">
      <label class="switch-paddle" for="exampleSwitch">
        <span class="show-for-sr">Download Kittens</span>
      </label>
    </div>
    ```

    #### Cards

    ```html
    <div class="radius bordered shadow card">
      <img src="https://placehold.it/500x250">
      <div class="card-divider">
        Styled Card
      </div>
      <div class="card-section">
        <h4>This is a card.</h4>
        <p>It has an easy to override visual style, and is appropriately subdued.</p>
      </div>
    </div>
    ```

    <div class="docs-code-live">
            <div class="grid-x grid-margin-x">
                    <div class="cell medium-4">
                            <div class="radius bordered shadow card">
                              <img src="assets/img/generic/rectangle-1.jpg">
                              <div class="card-divider">
                                Styled Card
                              </div>
                              <div class="card-section">
                                <h4>This is a card.</h4>
                                <p>It has an easy to override visual style, and is appropriately subdued.</p>
                              </div>
                            </div>
                    </div>
                    <div class="cell medium-4">
                            <div class="radius bordered shadow card">
                              <img src="assets/img/generic/rectangle-1.jpg">
                              <div class="card-divider">
                                Styled Card
                              </div>
                              <div class="card-section">
                                <h4>This is a card.</h4>
                                <p>It has an easy to override visual style, and is appropriately subdued.</p>
                              </div>
                            </div>
                    </div>
                    <div class="cell medium-4">
                            <div class="radius bordered shadow card">
                              <img src="assets/img/generic/rectangle-1.jpg">
                              <div class="card-divider">
                                Styled Card
                              </div>
                              <div class="card-section">
                                <h4>This is a card.</h4>
                                <p>It has an easy to override visual style, and is appropriately subdued.</p>
                              </div>
                            </div>
                    </div>
            </div>
    </div>

    #### Tables

    ```html
    <table class="radius bordered shadow">
            <!-- My Table goes here -->
    </table>
    ```

    <div class="docs-code-live">
            <table class="radius bordered shadow">
              <thead>
                <tr>
                  <th width="200">Table Header</th>
                  <th>Table Header</th>
                  <th width="150">Table Header</th>
                  <th width="150">Table Header</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Content Goes Here</td>
                  <td>This is longer content Donec id elit non mi porta gravida at eget metus.</td>
                  <td>Content Goes Here</td>
                  <td>Content Goes Here</td>
                </tr>
                <tr>
                  <td>Content Goes Here</td>
                  <td>This is longer Content Goes Here Donec id elit non mi porta gravida at eget metus.</td>
                  <td>Content Goes Here</td>
                  <td>Content Goes Here</td>
                </tr>
                <tr>
                  <td>Content Goes Here</td>
                  <td>This is longer content Donec id elit non mi porta gravida at eget metus.</td>
                  <td>Content Goes Here</td>
                  <td>Content Goes Here</td>
                </tr>
                <tr>
                  <td>Content Goes Here</td>
                  <td>This is longer Content Goes Here Donec id elit non mi porta gravida at eget metus.</td>
                  <td>Content Goes Here</td>
                  <td>Content Goes Here</td>
                </tr>
              </tbody>
            </table>
    </div>

    #### Images

    ```html
    <img src="https://placehold.it/150x150" class="radius">
    ```

    <div class="docs-code-live margin-bottom-1">
            <img src="https://placehold.it/150x150" class="radius">
    </div>

    ---

    ## Arrow Utility

    Mostly used as dropdown arrows for navigation.

    ```html
    <div class="arrow-down"></div>
    <div class="arrow-up"></div>
    <div class="arrow-right"></div>
    <div class="arrow-left"></div>
    ```

    <div class="arrow-down display-inline-block margin-right-1"></div>
    <div class="arrow-up display-inline-block margin-right-1"></div>
    <div class="arrow-right display-inline-block margin-right-1"></div>
    <div class="arrow-left display-inline-block"></div>

    ---

    ## Separator

    This creates a tiny separator below the heading of an element and is usually used within the heading of a section.

    <div class="primary callout">
            You don't need to use [Text alignment classes](typography-helpers.html#text-alignment) as this separator utility deals with the alignment of the text itself.
    </div>

    ```html
    <h3 class="separator-left">Lorem</h3>
    <h3 class="separator-center">Ipsum Dolor</h3>
    <h3 class="separator-right">Tempor</h3>
    ```

    <div class="docs-code-live">
            <div class="grid-x grid-margin-x">
                    <div class="cell small-12 medium-4">
                            <h3 class="separator-left">Lorem</h3>
                    </div>
                    <div class="cell small-12 medium-4">
                            <h3 class="separator-center">Ipsum Dolor</h3>
                    </div>
                    <div class="cell small-12 medium-4">
                            <h3 class="separator-right">Tempor</h3>
                    </div>
            </div>
    </div>

    ---

    ## Font Styling

    You can use font styling to style your text. You can change the font styling by adding `font-normal`, `font-bold`, `font-italic` to an element. You can also larger the text of an element with `font-wide`.

    ```html
    <p class="font-wide">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
    <p class="font-normal">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    <p class="font-bold">Perspiciatis tempore cumque, magni aspernatur, quidem. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse</p>
    <p class="font-italic">Lorem minus, placeat, cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.iure voluptas aliquam tempora neque?</p>
    ```

    ---

    ## List Styling

    <div class="primary callout">
            Please note that [Unbulleted lists](typography-helpers.html#un-bulleted-list), `.no-bullet` is enabled by default for both ordered and unordered lists.
    </div>

    #### Unordered Lists

    ```html
    <ul class="no-bullet"></ul>
    <ul class="list-disc"></ul>
    <ul class="list-circle"></ul>
    <ul class="list-square"></ul>
    ```

    #### Ordered Lists

    ```html
    <ol class="no-bullet"></ol>
    <ol class="list-decimal"></ol>
    <ol class="list-lower-alpha"></ol>
    <ol class="list-lower-latin"></ol>
    <ol class="list-lower-roman"></ol>
    <ol class="list-upper-alpha"></ol>
    <ol class="list-upper-latin"></ol>
    <ol class="list-upper-roman"></ol>
    ```

    ---

    ## Text Helpers

    ### Image Replacement (Text Hide)

    You can include an image with visually hidden helper text for the sake of accessibility and improving SEO. The `.text-hide` class will visually hide an element’s text within the context of an image.

    ```html
    <a href="#" class="text-hide">
      <img src="https://placehold.it/100x30" alt="zurb logo">
      Zurb <!-- Logo Text  -->
    </a>
    ```
    <a href="#" class="text-hide">
      <img src="assets/img/logos/zurb-logo.svg" alt="zurb logo">
      Zurb <!-- Logo Text  -->
    </a>

    ---

    ### Text Transformation

    Text transformation lets you control the capitalization of text. You can change the text transformation by adding `.text-uppercase`, `text-lowercase`, `text-capitalize` to an element.

    ```html
    <p class="text-uppercase"><!-- Text here --></p>
    <p class="text-lowercase"><!-- Text here --></p>
    <p class="text-capitalize"><!-- Text here --></p>
    ```

    <p class="text-uppercase"><strong>This is a upper-cased text.</strong> Set in the year 0 F.E. ("Foundation Era"), The Psychohistorians opens on Trantor, the capital of the 12,000-year-old Galactic Empire. Though the empire appears stable and powerful, it is slowly decaying in ways that parallel the decline of the Western Roman Empire.</p>

    <p class="text-lowercase"><strong>This is a lower-cased text.</strong> Set in the year 0 F.E. ("Foundation Era"), The Psychohistorians opens on Trantor, the capital of the 12,000-year-old Galactic Empire. Though the empire appears stable and powerful, it is slowly decaying in ways that parallel the decline of the Western Roman Empire.</p>

    <p class="text-capitalize"><strong>This is a caPitAlized teXt.</strong> Set in the yEar 0 F.E. ("Foundation Era"), The PsychohisTorians opens on Trantor, the capital of the 12,000-year-old Galactic Empire. Though the empire appears stable and powerful, it is slowly decaying in ways that parallel the decline of the Western Roman Empire.</p>

    <div class="callout primary">
      <strong>Note:</strong> `.text-capitalize` changes the first letter of every single word, leaving the case of other letters unaffected.
    </div>

    ---

    ### Text Decoration

    Text Decoration can be used to underline, overline, or line-through a text. You can change the text decoration by adding `.text-underline`, `.text-overline`, or `.text-line-through` to an element.

    ```html
    <p class="text-underline">Lorem ipsum dolor sit amet, consectetur adipisicing elit. </p>
    <p class="text-overline">Perspiciatis tempore cumque, magni aspernatur, quidem</p>
    <p class="text-line-through">Lorem minus, placeat, iure voluptas aliquam tempora neque?</p>
    ```

    ---

    ### Text Truncate

    The `.text-truncate` class will truncate your text and display an elipsis. This class works for a single line of text.

    ```html
    <p class="text-truncate">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aperiam voluptatem similique officiis recusandae esse cum in totam quisquam perspiciatis quod! Magnam culpa vitae, tempore eos explicabo cupiditate. Deserunt, quisquam, quos!</p>
    ```

    ---

    ### Text No-wrap

    If you would like to prevent the text wrapping into the next line you can utilize `.text-nowrap`. Please note that the text will continue to be in same line unless the `<br>` tag is used.

    ```html
    <p class="text-nowrap">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aperiam voluptatem similique officiis recusandae esse cum in totam quisquam perspiciatis quod! Magnam culpa vitae, tempore eos explicabo cupiditate. Deserunt, quisquam, quos!</p>
    ```

    ### Text Wrap

    To force text to wrap to the next line, you can use `.text-wrap`.

    ```html
    <p class="text-wrap">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aperiam voluptatem similique officiis recusandae esse cum in totam quisquam perspiciatis quod! Magnam culpa vitae, tempore eos explicabo cupiditate. Deserunt, quisquam, quos!</p>
    ```

    ---

    ## Margin Helpers

    Generate spacing around elements with these easy to use margin classes.

    <div class="primary callout">
            Please note that here below, `1 = 1 * $global-margin` and so on. By default `$global-margin` is equal to `1rem` which you can easily customize through [Sass Variables](#sass-variables).
    </div>

    <p>
      <a class="" data-open-video="1:28"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    #### Margin (All Sides)

    ```html
    <div class="margin-0"></div>
    <div class="margin-1"></div>
    <div class="margin-2"></div>
    <div class="margin-3"></div>
    ```

    #### Margin Top

    ```html
    <div class="margin-top-0"></div>
    <div class="margin-top-1"></div>
    <div class="margin-top-2"></div>
    <div class="margin-top-3"></div>
    ```

    #### Margin Bottom

    ```html
    <div class="margin-bottom-0"></div>
    <div class="margin-bottom-1"></div>
    <div class="margin-bottom-2"></div>
    <div class="margin-bottom-3"></div>
    ```

    #### Margin Left

    ```html
    <div class="margin-left-0"></div>
    <div class="margin-left-1"></div>
    <div class="margin-left-2"></div>
    <div class="margin-left-3"></div>
    ```

    #### Margin Right

    ```html
    <div class="margin-right-0"></div>
    <div class="margin-right-1"></div>
    <div class="margin-right-2"></div>
    <div class="margin-right-3"></div>
    ```

    #### Margin Left Right (Horizontal Axis)

    ```html
    <div class="margin-horizontal-0"></div>
    <div class="margin-horizontal-1"></div>
    <div class="margin-horizontal-2"></div>
    <div class="margin-horizontal-3"></div>
    ```

    #### Margin Top Bottom (Vertical Axis)

    ```html
    <div class="margin-vertical-0"></div>
    <div class="margin-vertical-1"></div>
    <div class="margin-vertical-2"></div>
    <div class="margin-vertical-3"></div>
    ```

    #### Margin: Usage as a Mixin

    ```scss
    .foo {
      @include margin(1, 0, 2, null);
    }
    ```

    This above code will generate the below output

    ```scss
    .foo {
      margin-top: 1rem !important;
      margin-right: 0 !important;
      margin-bottom: 2rem !important;
    }
    ```

    Note: The `margin-left` property wasn't printed as this mixin also accept `null` as a value to reduce CSS output. [See Sass Reference here](#margin)

    ---

    ## Padding Helpers

    Generate spaces around the content with these easy to use padding classes.

    <div class="primary callout">
            Please note that here below, `1 = 1 * $global-padding` and so on. By default `$global-padding` is equal to `1rem` which you can easily customize through [Sass Variables](#sass-variables).
    </div>

    #### Padding (All Sides)

    ```html
    <div class="padding-0"></div>
    <div class="padding-1"></div>
    <div class="padding-2"></div>
    <div class="padding-3"></div>
    ```

    #### Padding Top

    ```html
    <div class="padding-top-0"></div>
    <div class="padding-top-1"></div>
    <div class="padding-top-2"></div>
    <div class="padding-top-3"></div>
    ```

    #### Padding Bottom

    ```html
    <div class="padding-bottom-0"></div>
    <div class="padding-bottom-1"></div>
    <div class="padding-bottom-2"></div>
    <div class="padding-bottom-3"></div>
    ```

    #### Padding Left

    ```html
    <div class="padding-left-0"></div>
    <div class="padding-left-1"></div>
    <div class="padding-left-2"></div>
    <div class="padding-left-3"></div>
    ```

    #### Padding Right

    ```html
    <div class="padding-right-0"></div>
    <div class="padding-right-1"></div>
    <div class="padding-right-2"></div>
    <div class="padding-right-3"></div>
    ```

    #### Padding Left Right (Horizontal Axis)

    ```html
    <div class="padding-horizontal-0"></div>
    <div class="padding-horizontal-1"></div>
    <div class="padding-horizontal-2"></div>
    <div class="padding-horizontal-3"></div>
    ```

    #### Padding Top Bottom (Vertical Axis)

    ```html
    <div class="padding-vertical-0"></div>
    <div class="padding-vertical-1"></div>
    <div class="padding-vertical-2"></div>
    <div class="padding-vertical-3"></div>
    ```

    #### Padding: Usage as a Mixin

    ```scss
    .bar {
      @include padding(1, 0, 2, null);
    }
    ```

    This above code will generate the below output

    ```scss
    .bar {
      padding-top: 1rem !important;
      padding-right: 0 !important;
      padding-bottom: 2rem !important;
    }
    ```

    Note: The `padding-left` property wasn't printed as this mixin also accept `null` as a value to reduce CSS output. [See Sass Reference here](#padding)

    ---

    ## Sizing

    These width and height classes help you to easily make an element as wide or as tall as needed relative to its parent. By default it supports `25%`, `50%`, `75%` and `100%`. You can add more sizes though, through Sass map variable.

    #### Width

    ```html
    <div class="width-25"></div>
    <div class="width-50"></div>
    <div class="width-75"></div>
    <div class="width-100"></div>

    <div class="max-width-100"></div>
    ```

    #### Height

    ```html
    <div class="height-25"></div>
    <div class="height-50"></div>
    <div class="height-75"></div>
    <div class="height-100"></div>

    <div class="max-height-100"></div>
    ```

    ---

    ## Border box

    Border box lets you only add the content, padding and border, but not the margin within the width and height CSS properties.

    ```html
    <div class="border-box"></div>
    ```

    ---

    ## Border none

    Border none lets you quickly resets border to `none` for any element.

    ```html
    <div class="callout primary border-none">
      Hi! I am a callout with no Borders
    </div>
    ```

    ---

    ## Display Classes

    Display classes allow you to change the display property of any element.

    ```html
    <div class="display-inline"></div>
    <div class="display-inline-block"></div>
    <div class="display-block"></div>
    <div class="display-table"></div>
    <div class="display-table-cell"></div>
    ```

    These cover some of the most used display types. There are many other display values as specified by MDN [here](https://developer.mozilla.org/en-US/docs/Web/CSS/display). If you need some of those classes, then you can add them easily through Sass variables with `$prototype-display`. Sass Reference [here](#sass-reference)

    <div class="primary callout">
      <ul>
            <li>For `display: flex` use `.flex-container`. See [Flexbox Reference](flexbox.html)</li>
            <li>For `display: none` use `.hide`. or Foundation's [Visibility Classes](visibility.html)</li>
      </ul>
    </div>

    ---

    ## Positioning

    Positioning classes help you change an element's position value. By default, an element's postion value is `static`.

    ```html
    <div class="position-relative"></div>
    <div class="position-absolute"></div>
    <div class="position-fixed"></div>
    <div class="position-fixed-top"></div>
    <div class="position-fixed-bottom"></div>
    <div class="position-static"></div>
    ```

    #### Positioning: Usage as a Mixin

    The position mixin can be used to set a position and to set the `top` `right` `bottom` and/or `left` property all in one.

    ```scss
    .foo {
      @include position(fixed, 1, 2, 0, null);
    }
    ```

    This above code will generate the below output

    ```scss
    .foo {
      position: fixed !important;
      top: 1rem !important;
      right: 2rem !important;
      bottom: 0 !important;
    }
    ```

    See how the `left` offset wasn't printed as this mixin also accepts `null` as a value. Sass Reference [here](#position)

    ---

    ## Overflow

    These overflow classes helps you to clip content, render scrollbars or simply just display the content when it overflows its block level container.

    #### All sides

    ```html
    <div class="overflow-visible"></div>
    <div class="overflow-hidden"></div>
    <div class="overflow-scroll"></div>
    ```

    #### Horizontal Axis

    ```html
    <div class="overflow-x-visible"></div>
    <div class="overflow-x-hidden"></div>
    <div class="overflow-x-scroll"></div>
    ```

    #### Vertical Axis

    ```html
    <div class="overflow-y-visible"></div>
    <div class="overflow-y-hidden"></div>
    <div class="overflow-y-scroll"></div>
    ```

    Note: Combining `overflow: hidden` in either the X or Y direction with the `overflow: visible` in the opposite direction does not work as expected in CSS spec. [More info](https://stackoverflow.com/questions/6421966/css-overflow-x-visible-and-overflow-y-hidden-causing-scrollbar-issue#answer-6433475)

    ---

    ## Sass Mixin Helpers

    We also provides some extra utility mixins that you can use for your next prototype project.

    ### Box Mixin

    This mixin helps you to easily create a square, rectangle or a circle. Sass Reference [here](#box)

    ```scss
    .foo {
            @include box(1rem, 2rem); // Rectangle
    }

    .bar {
            @include box(1rem); // Square
    }

    .baz {
            @include box(1rem, $circle: true); // Circle
    }
    ```

    ### Rotate Mixin
    These Rotate mixins lets you rotate an element to a certain degree. Clockwise is the default direction but adding a `-` in front of the degrees will make it counter-clockwise.

    ```scss
    .foo {
            @include rotate(30); // 30 Degree
    }

    .bar {
            @include rotateX(60); // 60 Degree on X axis
    }

    .baz {
            @include rotateY(90); // 90 Degree on Y axis
    }

    .shaz {
            @include rotateZ(120); // 120 Degree on Z axis
    }
    ```

    ### Relational Mixins (AKA: nth:child mixins)

    These relational mixins helps you to manage styling of :nth-child’ified elements through easy Sass mixins.

    ```scss
    @include first($num) {} // applies style to first n children
    @include first-child {} // applies style to first child only
    @include last($num) {}  // applies style to last n children
    @include last-child {}  // applies style to first child only
    @include every($num) {} // applies style to every n children
    @include first-last {}  // applies style to first and last child only
    @include after-first($num) {} // applies style to all after nth child
    @include from-last($num) {} // applies style to all after and including nth child
    @include from-first-last($num) {} // applies style to nth child from first child and last child
    @include all-but($num) {} // applies style to all except nth child
    @include all-but-first-last($num) {} // applies style all except first and last child
    @include unique {} // applies style to a child who has no siblings
    @include not-unique {} // applies style to all children except a child who has no siblings
    @include between($first, $last) {} // applies style to all except first and last child
    @include even {} // applies style to all even children
    @include even-between($first, $last) {} // applies style to all even children except first and last
    @include odd {} // applies style to all odd children
    @include odd-between($first, $last) {} // applies style to all odd children except first and last
    @include number-between($num, $first, $last) {} // applies style to every n children from first child and last child
    ```"""

    pass


class RESPONSIVE_ACCORDION_TABS:
    """---
    title: Responsive Accordion Tabs
    description: Added in 6.3.0, use the Markup of the Accordion or Tabs components to create Responsive Accordion Tabs.
    video: 'FKzzaWR6j2M'
    sass:
      - scss/components/_accordion.scss
      - scss/components/_tabs.scss
    js: js/foundation.responsiveAccordionTabs.js
    tags:
      - tabcordion
    ---

    ## Basics

    Either the <a href="accordion.html">Accordion Markup</a> or the <a href="tabs.html">Tabs Markup</a> can be used to responsively switch between the two components at different breakpoints.

    The Accordion should have an id specified, but the plugin will automatically generate one if the id is omitted.

    Accordion content should also have an ID, or the # of the href should be specified, otherwise a random id will be generated

    <div class="secondary callout">
      <p>The accordion/tabs values can be in any order.</p>
    </div>

    #### Accordion HTML Markup

    <p>
      <a class="" data-open-video="0:35"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/eWKPqE?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="accordion" data-responsive-accordion-tabs="accordion medium-tabs large-accordion">
      <li class="accordion-item is-active" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 1</a>
        <div class="accordion-content" data-tab-content>
          I would start in the open state, due to using the `is-active` state class.
        </div>
      </li>
      <!-- ... -->
    </ul>
    ```
    <div class="secondary callout">
      <p>Once you put it all together, here's what you get!<br>Scale your browser down to see the toggle happen.<br>I am an `Accordion on small and large` but I am `Tabs on medium`</p>
    </div>

    <ul class="accordion" data-responsive-accordion-tabs="accordion medium-tabs large-accordion">
      <li class="accordion-item is-active" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 1</a>
        <div class="accordion-content" data-tab-content >
          <p>Panel 1. Lorem ipsum dolor</p>
          <a href="#">Nowhere to Go</a>
        </div>
      </li>
      <li class="accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 2</a>
        <div class="accordion-content" data-tab-content>
          <textarea></textarea>
          <button class="button">I do nothing!</button>
        </div>
      </li>
      <li class="accordion-item" data-accordion-item>
        <a href="#" class="accordion-title">Accordion 3</a>
        <div class="accordion-content" data-tab-content>
          Pick a date!
          <input type="date"></input>
        </div>
      </li>
    </ul>

    #### Tabs HTML Markup

    <p>
      <a class="" data-open-video="2:39"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/mmKQVN?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="tabs" data-responsive-accordion-tabs="tabs medium-accordion large-tabs" id="example-tabs">
      <li class="tabs-title is-active"><a href="#panel1" aria-selected="true">Tab 1</a></li>
      <li class="tabs-title"><a href="#panel2">Tab 2</a></li>
      <li class="tabs-title"><a href="#panel3">Tab 3</a></li>
      <li class="tabs-title"><a href="#panel4">Tab 4</a></li>
      <li class="tabs-title"><a href="#panel5">Tab 5</a></li>
      <li class="tabs-title"><a href="#panel6">Tab 6</a></li>
    </ul>

    <div class="tabs-content" data-tabs-content="example-tabs">
      <div class="tabs-panel is-active" id="panel1">
        <p>one</p>
        <p>Check me out! I'm a super cool Tab panel with text content!</p>
      </div>
      <div class="tabs-panel" id="panel2">
        <p>two</p>
        <img class="thumbnail" src="assets/img/generic/rectangle-7.jpg">
      </div>
      <div class="tabs-panel" id="panel3">
        <p>three</p>
        <p>Check me out! I'm a super cool Tab panel with text content!</p>
      </div>
      <div class="tabs-panel" id="panel4">
        <p>four</p>
        <img class="thumbnail" src="assets/img/generic/rectangle-2.jpg">
      </div>
      <div class="tabs-panel" id="panel5">
        <p>five</p>
        <p>Check me out! I'm a super cool Tab panel with text content!</p>
      </div>
      <div class="tabs-panel" id="panel6">
        <p>six</p>
        <img class="thumbnail" src="assets/img/generic/rectangle-8.jpg">
      </div>
    </div>
    ```
    <div class="secondary callout">
      <p>Once you put it all together, here's what you get!<br>Scale your browser down to see the toggle happen.<br>I am `Tabs on small and large` and `Accordion on medium`</p>
    </div>

    <ul class="tabs" data-responsive-accordion-tabs="tabs medium-accordion large-tabs" id="example-tabs">
      <li class="tabs-title is-active"><a href="#panel1" aria-selected="true">Tab 1</a></li>
      <li class="tabs-title"><a href="#panel2">Tab 2</a></li>
      <li class="tabs-title"><a href="#panel3">Tab 3</a></li>
      <li class="tabs-title"><a href="#panel4">Tab 4</a></li>
      <li class="tabs-title"><a href="#panel5">Tab 5</a></li>
      <li class="tabs-title"><a href="#panel6">Tab 6</a></li>
    </ul>

    <div class="tabs-content" data-tabs-content="example-tabs">
      <div class="tabs-panel is-active" id="panel1">
        <p>one</p>
        <p>Check me out! I'm a super cool Tab panel with text content!</p>
      </div>
      <div class="tabs-panel" id="panel2">
        <p>two</p>
        <img class="thumbnail" src="assets/img/generic/rectangle-7.jpg">
      </div>
      <div class="tabs-panel" id="panel3">
        <p>three</p>
        <p>Check me out! I'm a super cool Tab panel with text content!</p>
      </div>
      <div class="tabs-panel" id="panel4">
        <p>four</p>
        <img class="thumbnail" src="assets/img/generic/rectangle-2.jpg">
      </div>
      <div class="tabs-panel" id="panel5">
        <p>five</p>
        <p>Check me out! I'm a super cool Tab panel with text content!</p>
      </div>
      <div class="tabs-panel" id="panel6">
        <p>six</p>
        <img class="thumbnail" src="assets/img/generic/rectangle-8.jpg">
      </div>
    </div>

    <br>
    <div class="success callout">The responsive behavior  can be set through the `data-responsive-accordion-tabs` option.<br> `tabs|accordion` , `medium-tabs|accordion` , `large-tabs|accordion` sets the behavior</div>

    ---

    ## Plugin Options

    Plugin options can be set as individual data attributes, one combined data-options attribute, or as an object passed to the plugin's constructor. <a href="javascript.html#initializing">Learn more about how JavaScript plugins are initialized.</a><br>
    <div class="primary callout">All `data-options` from <a href="accordion.html#js-options">Accordion</a> or <a href="tabs.html#js-options">Tabs</a> can be passed through.</div>
    """

    pass


class RESPONSIVE_EMBED:
    """---
    title: Responsive Embed
    description: Wrap embedded content like videos, maps, and calendars in a responsive embed container to maintain the correct aspect ratio regardless of screen size.
    sass: scss/components/_responsive-embed.scss
    tags: flex video 'flex video'
    video: GxUsloI_qnQ
    ---

    To make sure embedded content maintains its aspect ratio as the width of the screen changes, wrap the `iframe`, `object`, `embed`, or `video` in a container with the `.responsive-embed` class.

    <p>
      <a class="" data-open-video="0:56"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/MmGEbb?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="responsive-embed">
      <iframe width="420" height="315" src="https://www.youtube.com/embed/mM5_T-F1Yn4" frameborder="0" allowfullscreen></iframe>
    </div>
    ```

    ---

    ## Aspect Ratios

    Add ratio classes to change the aspect ratio of responsive embeds. The default ratio is 4:3. The `.widescreen` class will change the container's aspect ratio to 16:9.

    <p>
      <a class="" data-open-video="2:17"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/MmXxpO?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="responsive-embed widescreen">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/WUgvvPRH7Oc" frameborder="0" allowfullscreen></iframe>
    </div>
    ```

    The ratio classes are generated by the keys in the `$responsive-embed-ratios` map in your settings file. Only the `default` key is required. You can, for example, make your default ratio 16:9, remove widescreen, and add other aspect ratios.

    ```scss
    $responsive-embed-ratios: (
      default: 16 by 9,
      vertical: 9 by 16,
      panorama: 256 by 81,
      square: 1 by 1,
    );
    ```

    <p>
      <a class="" data-open-video="3:18"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/OmEqgM?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="responsive-embed panorama">
      <iframe width="1024" height="315" src="https://www.youtube.com/embed/bnD9I24EL_4" frameborder="0" allowfullscreen></iframe>
    </div>
    ```"""

    pass


class RESPONSIVE_NAVIGATION:
    """---
    title: Responsive Navigation
    description: Our three Menu patterns form like Voltron into one responsive Menu plugin, which allows you to switch between patterns at different screen sizes.
    video: 'dmKun75_9oc'
    js:
      - js/foundation.responsiveMenu.js
      - js/foundation.responsiveToggle.js
    ---

    ## Responsive Menu

    The Menu has some responsive CSS classes built in, which allow you to re-orient a menu on different screen sizes.

    <p>
      <a class="" data-open-video="0:58"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/qmYKgJ?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="vertical medium-horizontal menu">
      <li><a href="#0"><i class="fi-list"></i> <span>One</span></a></li>
      <li><a href="#0"><i class="fi-list"></i> <span>Two</span></a></li>
      <li><a href="#0"><i class="fi-list"></i> <span>Three</span></a></li>
      <li><a href="#0"><i class="fi-list"></i> <span>Four</span></a></li>
    </ul>
    ```

    ---

    The Menu can be augmented with one of three different plugins&mdash;dropdown menu, drilldown menu, or accordion menu. However, these patterns tend to work best on specific screen sizes.

    With our responsive Menu plugin, you can apply a default pattern to a Menu, and then change that pattern on other screen sizes.

    Some Menu Combination (but not limited) to are

    - [Drilldown Dropdown Menu](#drilldown-dropdown-menu)
    - [Accordion Dropdown Menu](#accordion-dropdown-menu)
    - [Drilldown Accordion Menu](#drilldown-accordion-menu)

    #### Drilldown Dropdown Menu

    A drilldown menu works well on mobile, but on larger screens, you may want to convert that same menu into a dropdown. Here's an example that does just that:

    <p>
      <a class="" data-open-video="2:35"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/jmKPdM?editors=1010" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="vertical medium-horizontal menu" data-responsive-menu="drilldown medium-dropdown">
      <li>
        <a href="#">Item 1</a>
        <ul class="vertical menu">
          <li>
            <a href="#">Item 1A</a>
            <ul class="vertical menu">
              <li><a href="#">Item 1A</a></li>
              <li><a href="#">Item 1B</a></li>
              <li><a href="#">Item 1C</a></li>
              <li><a href="#">Item 1D</a></li>
              <li><a href="#">Item 1E</a></li>
            </ul>
          </li>
          <li><a href="#">Item 1B</a></li>
        </ul>
      </li>
      <li>
        <a href="#">Item 2</a>
        <ul class="vertical menu">
          <li><a href="#">Item 2A</a></li>
          <li><a href="#">Item 2B</a></li>
        </ul>
      </li>
      <li>
        <a href="#">Item 3</a>
        <ul class="vertical menu">
          <li><a href="#">Item 3A</a></li>
          <li><a href="#">Item 3B</a></li>
        </ul>
      </li>
    </ul>
    ```

    <br>
    <div class="alert callout">
      <p>
        <strong>Bug(v6.3.1):</strong> There is a bug within <strong>drilldown-dropdown menu</strong> combo. If you set up a responsive menu with drilldown on small, then dropdown for medium up, and resize to small and then back to medium the dropdowns will not work. The bug can be reproduced <a href="https://codepen.io/IamManchanda/pen/mmGOgG?editors=1000">here</a> <br>
        <strong>Good News:</strong> The Bug will be fixed with the upcoming foundation release. If you are specifically using <strong>v6.3.1</strong>, we recommend to use this below patch to fix this.
      </p>
    </div>

    ```javascript
    // Patch for a Bug in v6.3.1
    $(window).on('changed.zf.mediaquery', function() {
      $('.is-dropdown-submenu.invisible').removeClass('invisible');
    });
    ```

    #### Accordion Dropdown Menu

    Same like drilldowns, an accordion menu works well on mobile, but on larger screens, you may want to convert that same menu into a dropdown. Here's an example for the same:

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/LyXBQz?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="vertical medium-horizontal menu" data-responsive-menu="accordion medium-dropdown">
      <li>
        <a href="#">Item 1</a>
        <ul class="vertical menu">
          <li>
            <a href="#">Item 1A</a>
            <ul class="vertical menu">
              <li><a href="#">Item 1A</a></li>
              <li><a href="#">Item 1B</a></li>
              <li><a href="#">Item 1C</a></li>
              <li><a href="#">Item 1D</a></li>
              <li><a href="#">Item 1E</a></li>
            </ul>
          </li>
          <li><a href="#">Item 1B</a></li>
        </ul>
      </li>
      <li>
        <a href="#">Item 2</a>
        <ul class="vertical menu">
          <li><a href="#">Item 2A</a></li>
          <li><a href="#">Item 2B</a></li>
        </ul>
      </li>
      <li>
        <a href="#">Item 3</a>
        <ul class="vertical menu">
          <li><a href="#">Item 3A</a></li>
          <li><a href="#">Item 3B</a></li>
        </ul>
      </li>
    </ul>
    ```

    <br>

    #### Drilldown Accordion Menu

    Just like foundation docs itself (see left sidenav), an accordion menu is great for a sidenav of a website on desktop, but for mobile, You might need Drilldown menu.

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/bWQjQP?editors=1010" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="vertical menu" data-responsive-menu="drilldown medium-accordion" style="max-width: 250px;">
      <li>
        <a href="#">Item 1</a>
        <ul class="vertical menu">
          <li>
            <a href="#">Item 1A</a>
            <ul class="vertical menu">
              <li><a href="#">Item 1A</a></li>
              <li><a href="#">Item 1B</a></li>
              <li><a href="#">Item 1C</a></li>
              <li><a href="#">Item 1D</a></li>
              <li><a href="#">Item 1E</a></li>
            </ul>
          </li>
          <li><a href="#">Item 1B</a></li>
        </ul>
      </li>
      <li>
        <a href="#">Item 2</a>
        <ul class="vertical menu">
          <li><a href="#">Item 2A</a></li>
          <li><a href="#">Item 2B</a></li>
        </ul>
      </li>
      <li>
        <a href="#">Item 3</a>
        <ul class="vertical menu">
          <li><a href="#">Item 3A</a></li>
          <li><a href="#">Item 3B</a></li>
        </ul>
      </li>
    </ul>
    ```

    ---

    ## Responsive Toggle

    In Foundation 5, the top bar combined this menu toggling concept into one plugin. We now have a separate, optional component you can use in tandem with the responsive plugin. It's called the title bar, and it allows you to quickly setup a menu toggle on mobile. The title bar hides itself on larger screens.

    To set it up, first give your menu a unique ID. (You don't even need to use Menu! Any element will work.) Next, add a title bar with the class `.title-bar` and the attribute `data-responsive-toggle`. The value of `data-responsive-toggle` should be the ID of the menu you're toggling. Lastly, add `data-toggle` to the element that will trigger the toggle. The value of `data-toggle` should also be the ID of the menu you're toggling.

    By default, the title bar will be visible on small screens, and the Menu hides. At the medium breakpoint, the title bar disappears, and the menu is always visible. This breakpoint can be changed with the `data-hide-for` attribute in HTML, or the `hideFor` setting in JavaScript.

    <a class="" data-open-video="5:05"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>

    <div class="primary callout show-for-medium">
      <p>Scale your browser down to see the toggle happen.</p>
    </div>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/LymroM?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="title-bar" data-responsive-toggle="example-menu" data-hide-for="medium">
      <button class="menu-icon" type="button" data-toggle="example-menu"></button>
      <div class="title-bar-title">Menu</div>
    </div>

    <div class="top-bar" id="example-menu">
      <div class="top-bar-left">
        <ul class="dropdown menu" data-dropdown-menu>
          <li class="menu-text">Site Title</li>
          <li>
            <a href="#">One</a>
            <ul class="menu vertical">
              <li><a href="#">One</a></li>
              <li><a href="#">Two</a></li>
              <li><a href="#">Three</a></li>
            </ul>
          </li>
          <li><a href="#">Two</a></li>
          <li><a href="#">Three</a></li>
        </ul>
      </div>
      <div class="top-bar-right">
        <ul class="menu">
          <li><input type="search" placeholder="Search"></li>
          <li><button type="button" class="button">Search</button></li>
        </ul>
      </div>
    </div>
    ```

    ---

    ## Responsive Toggle with animation

    To use animations from the Motion UI library, include the <code>data-animate="someAnimationIn someAnimationOut"</code> attribute.


    <div class="primary callout show-for-medium">
      <p>Scale your browser down to see the toggle happen.</p>
    </div>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/KmepBg?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="title-bar" data-responsive-toggle="example-animated-menu" data-hide-for="medium">
      <button class="menu-icon" type="button" data-toggle></button>
      <div class="title-bar-title">Menu</div>
    </div>

    <div class="top-bar" id="example-animated-menu" data-animate="hinge-in-from-top spin-out">
      <div class="top-bar-left">
        <ul class="dropdown menu" data-dropdown-menu>
          <li class="menu-text">Site Title</li>
          <li>
            <a href="#">One</a>
            <ul class="menu vertical">
              <li><a href="#">One</a></li>
              <li><a href="#">Two</a></li>
              <li><a href="#">Three</a></li>
            </ul>
          </li>
          <li><a href="#">Two</a></li>
          <li><a href="#">Three</a></li>
        </ul>
      </div>
    </div>
    ```

    ---

    ### Preventing FOUC

    Before the JavaScript on your page loads, you'll be able to see both the mobile and desktop element at once for a brief second. This is known as a [flash of unstyled content](https://en.wikipedia.org/wiki/Flash_of_unstyled_content). There's not an easy way for the framework to handle this for you, but you can add some extra CSS to account for it.

    If we reference the above example, `.title-bar` is our mobile element and `.top-bar` is our desktop element. So before the JavaScript loads, we want only the right element for that screen size to be visible.

    ```css
    .no-js .top-bar {
      display: none;
    }

    @media screen and (min-width: 40em) {
      .no-js .top-bar {
        display: block;
      }

      .no-js .title-bar {
        display: none;
      }
    }
    ```

    If you're using Sass, you can write it like this:

    ```scss
    .no-js {
      @include breakpoint(small only) {
        .top-bar {
          display: none;
        }
      }

      @include breakpoint(medium) {
        .title-bar {
          display: none;
        }
      }
    }
    ```"""

    pass


class REVEAL:
    """---
    title: Reveal
    description: Modal dialogs, or pop-up windows, are handy for prototyping and production. Foundation includes Reveal, our jQuery modal plugin, to make this easy for you.
    sass: scss/components/_reveal.scss
    js: js/foundation.reveal.js
    video: vnT3bp07iHI
    mui: true
    tags:
      - modal
    ---


    <!-- <div class="callout training-callout">
      <p>We hope you’re loving these free documentation videos! If you’d like to really accelerate your learning and master the world of front-end development, our Foundation online webinar training is the answer.</p>
      <a href="https://zurb.com/university/courses" target="_blank">See the upcoming Foundation trainings →</a>
    </div> -->

    ## Basics

    A modal is just an empty container, so you can put any kind of content inside it, from text to forms to video to an entire grid.

    <div class="callout primary">
      <p>Please note that we removed the option for AJAX loaded modals in Foundation 6. We did make it very easy to implement on your own though, check out a sample in the <span><a href="#advanced-options">Advanced</a></span> section.</p>
    </div>

    To create a modal, add the class `.reveal`, the attribute `data-reveal`, and a unique ID to a container.

    <p>
      <a class="" data-open-video="0:36"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/RVyBPw?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="reveal" id="exampleModal1" data-reveal>
      <h1>Awesome. I Have It.</h1>
      <p class="lead">Your couch. It is mine.</p>
      <p>I'm a cool paragraph that lives inside of an even cooler modal. Wins!</p>
      <button class="close-button" data-close aria-label="Close modal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    ```

    You'll also need a way to open the modal. Add the attribute `data-open` to any element. The value of `data-open` should be the ID of the modal.

    ```html
    <p><button class="button" data-open="exampleModal1">Click me for a modal</button></p>
    ```

    You'll also need a way to *close* the modal from inside. By default, modals will close if clicked outside of, or if the <kbd>esc</kbd> key is pressed. However, you'll generally also want to add your own click trigger. Add the attribute `data-close` to any element within the modal to add one.

    You can use our handy [close button](close-button.html) styles to do this:

    ```html
    <button class="close-button" data-close aria-label="Close modal" type="button">
      <span aria-hidden="true">&times;</span>
    </button>
    ```

    ---

    ## Sizing

    On small screens, a modal is always 100% of the width of the screen. On medium-sized screens and larger, the width changes to 600px (see the `$reveal-width` setting).

    The size of a modal can be changed with these sizing classes, which are added to the modal container:

    - `.tiny`: 30% wide
    - `.small`: 50% wide
    - `.large`: 90% wide
    - `.full`: 100% width *and* height, defaults the `escClose` option to true, as well as creates a close button.

    <p>
      <a class="" data-open-video="3:38"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/eWKQer?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="tiny reveal" id="exampleModal" data-reveal>
      <!-- ... -->
    </div>
    ```

    <p><button class="button" data-toggle="exampleModal5" aria-controls="exampleModal5">Click me for a tiny modal</button></p>

    <div class="tiny reveal" id="exampleModal5" data-reveal>
      <p>OH I'M SO TIIINY</p>
      <button class="close-button" data-close aria-label="Close reveal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>

    <p><button class="button" data-toggle="exampleModal6">Click me for a small modal</button></p>

    <div class="small reveal" id="exampleModal6" data-reveal>
      <p>I may be small, but I've got a big heart!</p>
      <button class="close-button" data-close aria-label="Close reveal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>

    <p><button class="button" data-toggle="exampleModal7">Click me for a large modal</button></p>

    <div class="large reveal" id="exampleModal7" data-reveal>
      <p>I'm big, like bear!</p>
      <button class="close-button" data-close aria-label="Close reveal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>

    ---

    ## Nested Modal

    It's possible for modals to open other modals. Create a second modal with a unique ID, and then add a click trigger with `data-open` inside the first modal.

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/PmaxBz?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <p><button class="button" data-open="exampleModal2">Click me for a modal</button></p>

    <!-- This is the first modal -->
    <div class="reveal" id="exampleModal2" data-reveal>
      <h1>Awesome!</h1>
      <p class="lead">I have another modal inside of me!</p>
      <button class="button" data-open="exampleModal3">Click me for another modal!</button>
      <button class="close-button" data-close aria-label="Close reveal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>

    <!-- This is the nested modal -->
    <div class="reveal" id="exampleModal3" data-reveal>
      <h2>ANOTHER MODAL!!!</h2>
      <button class="close-button" data-close aria-label="Close reveal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    ```

    ---

    ## Full-screen

    A full-screen modal is 100% of the width *and* height of the window. Add the `.full` class to make it go.

    <p>
      <a class="" data-open-video="4:58"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/mmKQQV?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <p><button class="button" data-toggle="exampleModal8">Click me for a full-screen modal</button></p>

    <div class="full reveal" id="exampleModal8" data-reveal>
      <p>OH I'M SO FUUUUL</p>
      <img src="https://placekitten.com/1920/1280" alt="Introspective Cage">
      <button class="close-button" data-close aria-label="Close reveal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    ```

    ## Advanced Options

    ### No Overlay

    To remove the overlay, add the attribute `data-overlay="false"` to the modal.

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/vmrQwL?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <p><button class="button" data-toggle="exampleModal9">Click me for an overlay-lacking modal</button></p>

    <div class="reveal" id="exampleModal9" data-reveal data-overlay="false">
      <p>I feel so free!</p>
      <button class="close-button" data-close aria-label="Close reveal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    ```

    ---

    ### Animations

    To use animations from the Motion UI library, include the <code>data-animation-in="someAnimationIn"</code> and <code>data-animation-out="someAnimationOut"</code> attributes. If you want to adjust the speed or timing, include it the attributes like <code>data-animation-in="someAnimationIn fast"</code>.

    <p>
      <a class="" data-open-video="5:40"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/ZKRVeP?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <p><button class="button" data-toggle="animatedModal10">Click me for a modal</button></p>

    <div class="reveal" id="animatedModal10" data-reveal data-close-on-click="true" data-animation-in="spin-in" data-animation-out="spin-out">
      <h1>Whoa, I'm dizzy!</h1>
      <p class="lead">There are many options for animating modals, check out the Motion UI library to see them all</p>
      <button class="close-button" data-close aria-label="Close reveal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    ```

    ---

    ### AJAX

    To use AJAX to load your modal content, use the code snippet below.

    ```js
    var $modal = $('#modal');

    $.ajax('/url')
      .done(function(resp){
        $modal.html(resp).foundation('open');
    });
    ```


    ---

    ## Accessibility

    Modals by default are accessible through the use of various ARIA attributes.  To make a modal even more accessible, designate a label to the modal by adding `aria-labelledby="exampleModalHeader11"` to the container and `id="exampleModalHeader11"` to the element you want to designate as the label.

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/RVJEBZ?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <p><button class="button" data-open="exampleModal11">Click me for a modal</button></p>

    <div class="reveal" id="exampleModal11" aria-labelledby="exampleModalHeader11" data-reveal>
      <h1 id="exampleModalHeader11">Label for the Modal!</h1>
      <p class="lead">I am even more accessible than the other modals.</p>
      <button class="close-button" data-close aria-label="Close Accessible Modal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    ```"""

    pass


class RTL:
    """---
    title: Right-to-Left Support
    description: Foundation can easily adapt its components to work with languages that read from right to left.
    video: 'TPz2Uzr4urE'
    ---

    ## HTML

    You'll need to make a few changes to your markup to get the Javascript components working nice and smooth. In the `<html>` tag, you'll need to add a `dir` attribute with a value of `rtl`. Here's what your `<html>` tag should look like:

    ```html
    <!-- This example is for a right-to-left Arabic layout -->
    <html class="no-js" lang="ar" dir="rtl">
    ```

    ### Language Code

    You'll need to change your lang attribute value to match your language. Here's a handy list of common right-to-left languages and their html codes.

    - **Arabic:** `ar`
    - **Farsi:** `fa`
    - **Hebrew:** `he`, `iw`
    - **Urdu:** `ur`
    - **Yiddish:** `yi`, `ji`

    View of a [full list of language codes](https://www.loc.gov/standards/iso639-2/php/code_list.php) on the website of the Library of Congress.

    ---

    ## CSS Download

    If you use a CSS version of Foundation, you'll need to create a custom download that includes RTL CSS instead of LTR. Just select "Right-to-left" under the Text Direction section of the customizer.

    ---

    ## Sass Configuration

    If you're using the Sass version of Foundation, open your project's [settings file](sass.html#the-settings-file) (`settings.scss`) and change this variable in the Global section:

    ```scss
    $global-text-direction: rtl;
    ```

    This will convert the framework's components to RTL format."""

    pass


class SASS_FUNCTIONS:
    """---
    title: Sass Functions
    description: Behind the scenes, Foundation is powered by a set of utility Sass functions that help us work with colors, units, selectors, and more.
    sass:
      - scss/util/*.scss
      - '!scss/util/_breakpoint.scss'
      - '!scss/util/_mixins.scss'
    ---

    ## Importing

    All of Foundation's Sass utilities are in the folder `scss/util`, and broken up into multiple files by category. You can import every utility file at once using this line of code:

    ```scss
    @import 'util/util';
    ```

    Or, utilities can be imported individually.

    ```scss
    // Color manipulation
    @import 'util/color';

    // Selector generation
    @import 'util/selector';

    // Unit manipulation and conversion
    @import 'util/unit';

    // Value checking and extraction
    @import 'util/value';
    ```

    <div class="callout warning">
      <p>Variables, functions, or mixins prefixed with <code>-zf-</code> are considered part of the internal API, which means they could change, break, or disappear without warning. We recommend sticking to only the public API, which is documented below.</p>
    </div>"""

    pass


class SASS_MIXINS:
    """---
    title: Sass Mixins
    description: Mixins allow us to reuse code in various parts of the framework. Foundation includes mixins for clearfixes, visibility, icons, shapes, and more.
    sass:
      - scss/util/_mixins.scss
      - scss/prototype/*.scss
    video: 'aiO5nFepdcw'
    ---

    ## Importing

    Foundation's Sass mixins are all kept in one file: `scss/util/_mixins.scss`. To import it in Sass, use this line of code:

    ```scss
    @import 'util/mixins';
    ```

    Note: These mixins are included by default when using the [ZURB Stack](starter-projects.html#zurb-template) and [Basic Template](starter-projects.html#basic-template) Starter Projects.

    ## General Mixins

    Foundation includes some handy Sass mixins to quickly create styles or to extend and truly customize an existing component. Here is a list of available mixins:

    - [CSS Triangle mixin](#css-triangle)
    - [Hamburger Icon mixin](#hamburger)
    - [Background triangle](#background-triangle)
    - [Clearfix](#clearfix)
    - [Auto width children](#auto-width)
    - [Disable Mouse Outline](#disable-mouse-outline)
    - [Element Invisible](#element-invisible)
    - [Element Invisible Off](#element-invisible-off)
    - [Vertical Center](#vertical-center)
    - [Horizontal Center](#horizontal-center)
    - [Absolute Center](#absolute-center)

    ## Prototyping Utility Mixins

    Quickly prototype layouts and UI with Foundation's Prototyping Utility mixins. These mixins are great realizing your sketches and mockups into hi-fi coded prototype's ultra fast. [Learn more about Prototyping Utilities](prototyping-utilities.html)

    Here is a list of available mixins:

    - [Border Box](#border-box)
    - [Border None](#border-none)
    - [Bordered](#bordered)
    - [Box](#box)
    - [Display](#display)
    - [Font Wide](#font-wide)
    - [Font Normal](#font-normal)
    - [Font Bold](#font-bold)
    - [Font Italic](#font-italic)
    - [Style Type Unordered](#style-type-unordered)
    - [Style Type Ordered](#style-type-ordered)
    - [Overflow](#overflow)
    - [Overflow-x](#overflow-x)
    - [Overflow-y](#overflow-y)
    - [Position](#position)
    - [Position Fixed Top](#position-fixed-top)
    - [Position Fixed Bottom](#position-fixed-bottom)
    - [Rotate](#rotate)
    - [RotateX](#rotatex)
    - [RotateY](#rotatey)
    - [RotateZ](#rotateZ)
    - [Border Radius](#border-radius)
    - [Border Rounded](#border-rounded)
    - [Separator](#separator)
    - [Shadow](#shadow)
    - [Max Width 100%](#max-width-100)
    - [Margin](#margin)
    - [Padding](#padding)
    - [Text Decoration](#text-decoration)
    - [Text Transform](#text-transform)
    - [Text Hide](#text-hide)
    - [Text Truncate](#text-truncate)
    - [Text Nowrap](#text-nowrap)
    - [Nth Child](#first)"""

    pass


class SASS:
    """---
    title: Sass
    description: Foundation is written in Sass, which allows us to make the codebase customizable and flexible.
    video: mYiyunVQdMY
    ---

    <!-- <div class="callout training-callout">
      <p>Get trained up on Foundation's Sass with our online webinar training. Sass allows you to write dramatically more efficient code. We'll go over things like how to install and start compiling Sass, nesting mixins and functions, and writing fully semantic CSS using Foundation mixins for insanely maintainable code.</p>
      <a href="https://zurb.com/university/advanced-foundation-training" target="_blank">Reserve your spot →</a>
    </div> -->

    <div class="primary callout">
      <p>Not familiar with Sass? The [official tutorial](https://sass-lang.com/guide) on sass-lang.com is a great place to start.</p>
    </div>

    ## Compatibility

    <img src="assets/img/logos/sass-logo.svg" alt="Sass logo" class="float-right" style="width: 150px; height: 150px; margin-left: 1rem;">

    **Foundation for Sites can be compiled with Ruby Sass and libsass.** We tend to stick to the latest versions of both compilers when possible. Our documentation and starter project are compiled with [node-sass](https://github.com/sass/node-sass), a Node port of libsass. We recommend these versions of either compiler:

    - Ruby Sass **3.4+**
    - node-sass **3.4.2+** (libsass **3.3.2**)

    ### Autoprefixer Required

    We don't include vendor prefixes in our Sass files&mdash;instead, we let [Autoprefixer](https://github.com/postcss/autoprefixer) handle it for us. Our build process uses [gulp-autoprefixer](https://github.com/sindresorhus/gulp-autoprefixer), but there are [other versions](https://github.com/postcss/autoprefixer#usage) that work with Grunt, Rails, Brunch, and more.

    To get the proper browser support, use these Autoprefixer settings:

    ```js
    autoprefixer({
      browsers: ['last 2 versions', 'ie >= 9', 'android >= 4.4', 'ios >= 7']
    });
    ```

    ---

    ## Loading the Framework

    If you're using the CLI to create a project, the Sass compilation process is already set up for you. If not, you can compile our Sass files yourself, or drop in a pre-built CSS file.

    To get started, first install the framework files using favorite package manager like npm or yarn.

    ```bash
    npm install foundation-sites --save
    ```

    ### Compiling Manually

    Next, add the framework files as an import path. How you do this depends on your build process, but the path is the same regardless: `packages_folder/foundation-sites/scss`

    Here's an example using grunt-contrib-sass:

    ```js
    grunt.initConfig({
      sass: {
        dist: {
          options: {
            loadPath: ['node_modules/foundation-sites/scss']
          }
        }
      }
    });
    ```

    If you're using Compass, open your project's `config.rb` and add the import path there:

    ```ruby
    add_import_path "node_modules/foundation-sites/scss"
    ```

    Finally, add an `@import` statement to the top of your primary Sass file. Refer to [Adjusting CSS Output](#adjusting-css-output) below to learn how to control the CSS output of the framework.

    ```scss
    @import 'foundation';
    ```

    You're also going to want a settings file for your project, which will allow you to modify the default styles of Foundation. **[Download the latest settings file here](https://raw.githubusercontent.com/foundation/foundation-sites/master/scss/settings/_settings.scss)**, add it to your project as `_settings.scss`, then import it *before* Foundation itself.

    <div class="callout">
    The settings file needs to import `util/util` from Foundation. Please ensure that the Foundation folder is included in Sass or change `@import util/util` for it to points to the full path of the file. For example, NPM users may need to change the import to `node_modules/foundation-sites/scss/util/util`.
    </div>

    ```scss
    @import 'settings';
    @import 'foundation';
    ```

    ### Using Compiled CSS

    The Foundation for Sites npm package includes pre-compiled CSS files, in minified (compressed) and unminified flavors. If you're interested in editing the framework CSS directly, use the unminified file. For production, use the minified version.

    ```html
    <link rel="stylesheet" href="node_modules/foundation-sites/dist/css/foundation-sites.css">

    <link rel="stylesheet" href="node_modules/foundation-sites/dist/css/foundation-sites.min.css">
    ```

    ---

    ## Adjusting CSS Output

    Foundation outputs many classes for its various components. These help developers get up and running quickly. However, when you move to production, you may wish to build your grid semantically, replace our pre-built classes with your own, or remove components entirely.

    Each component has an **export mixin** which prints out the CSS for that component. If you're cool with having everything, you just need one line of code:

    ```scss
    @include foundation-everything;
    ```

    Our [starter projects](starter-projects.html) include the full list of imports, making it easy to comment out the components you don't need. A full list is also included below.

    ```scss
    @import 'foundation';

    // Global styles
    @include foundation-global-styles;
    @include foundation-forms;
    @include foundation-typography;

    // Grids (choose one)
    @include foundation-xy-grid-classes;
    // @include foundation-grid;
    // @include foundation-flex-grid;

    // Generic components
    @include foundation-button;
    @include foundation-button-group;
    @include foundation-close-button;
    @include foundation-label;
    @include foundation-progress-bar;
    @include foundation-slider;
    @include foundation-switch;
    @include foundation-table;
    // Basic components
    @include foundation-badge;
    @include foundation-breadcrumbs;
    @include foundation-callout;
    @include foundation-card;
    @include foundation-dropdown;
    @include foundation-pagination;
    @include foundation-tooltip;

    // Containers
    @include foundation-accordion;
    @include foundation-media-object;
    @include foundation-orbit;
    @include foundation-responsive-embed;
    @include foundation-tabs;
    @include foundation-thumbnail;
    // Menu-based containers
    @include foundation-menu;
    @include foundation-menu-icon;
    @include foundation-accordion-menu;
    @include foundation-drilldown-menu;
    @include foundation-dropdown-menu;

    // Layout components
    @include foundation-off-canvas;
    @include foundation-reveal;
    @include foundation-sticky;
    @include foundation-title-bar;
    @include foundation-top-bar;

    // Helpers
    @include foundation-float-classes;
    // @include foundation-flex-classes;
    @include foundation-visibility-classes;
    // @include foundation-prototype-classes;
    ```

    ---

    ## The Settings File

    All Foundation projects include a settings file, named `_settings.scss`. If you're using the CLI to create a Foundation for Sites project, you can find the settings file under scss/ (basic template) or src/assets/scss/ (ZURB template). If you're installing the framework standalone using npm, there's a settings file included in this package, which you can move into your own Sass files to work with.

    Every component includes a set of variables that modify core structural or visual styles. If there's something you can't customize with a variable, you can just write your own CSS to add it.

    <div class="callout warning">
      <p>Once you've set up a new project, your settings file can't be automatically updated when new versions change, add, or remove variables. Keep tabs on new <a href="https://github.com/foundation/foundation-sites/releases">Foundation releases</a> so you know when things change.</p>
    </div>

    Here's an example set of settings variables. These change the default styling of [buttons](button.html):

    ```scss
    // Default padding for button.
    $button-padding: 0.85em 1em !default;

    // Default margin for button.
    $button-margin: 0 $global-padding $global-padding 0 !default;

    // Default fill for button. Is either solid or hollow.
    $button-fill: solid !default;

    // Default background color for button.
    $button-background: $primary-color !default;

    // Default hover background color for button.
    $button-background-hover: scale-color($button-background, $lightness: -15%) !default;

    // Default font color for button.
    $button-font-color: #fff !default;

    // Default alternative font color for button.
    $button-font-color-alt: #000 !default;

    // Default radius for button.
    $button-radius: 0 !default;

    // Default sizes for button.
    $button-sizes: (
      tiny: 0.7,
      small: 0.8,
      medium: 1,
      large: 1.3,
    ) !default;

    // Default font size for button.
    $button-font-size: 0.9rem !default;

    // Default opacity for a disabled button.
    $button-opacity-disabled: 0.25 !default;
    ```"""

    pass


class SLIDER:
    """---
    title: Slider
    description: This handy lil slider is perfect for setting specific values within a range.
    sass: scss/components/_slider.scss
    js: js/foundation.slider.js
    video: 'i_BTQiXBvhU'
    tags:
      - range
    ---

    ## Basics

    Create a slider by adding the class `.slider` and the attribute `data-slider` to a container element. You should also define both a starting and maximum value for the slider.

    Inside the container are three elements:
    - The handle (`.slider-handle`), which the user drags.
    - The fill (`.slider-fill`), which resizes dynamically based on where the handle is.
    - A hidden `<input>`, which is where the value of the slider is stored.

    The `data-initial-start=""` value is where along the slider the handle starts. The `data-end=""` is the maximum value for the slider. In the below example, starting at 50 of 200 means the slider handle will start at 25% of the total.

    <p>
      <a class="" data-open-video="1:00"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/MmGpWR?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="slider" data-slider data-initial-start="50" data-end="200">
      <span class="slider-handle"  data-slider-handle role="slider" tabindex="1"></span>
      <span class="slider-fill" data-slider-fill></span>
      <input type="hidden">
    </div>
    ```

    ---

    ## Vertical

    To get *vertical*, just add a `.vertical` class and `data-vertical="true"` the slider.

    <p>
      <a class="" data-open-video="3:24"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/eWrvRm?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="slider vertical" data-slider data-initial-start="25" data-end="200" data-vertical="true">
      <span class="slider-handle" data-slider-handle role="slider" tabindex="1"></span>
      <span class="slider-fill" data-slider-fill></span>
      <input type="hidden">
    </div>
    ```

    ---

    ## Disabled

    Add the class `.disabled` to disable interaction with the slider.

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/aWjqVJ?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="slider disabled" data-slider data-initial-start="78">
      <span class="slider-handle" data-slider-handle role="slider" tabindex="1"></span>
      <span class="slider-fill" data-slider-fill></span>
      <input type="hidden">
    </div>
    ```

    ---

    ## Two Handles

    Two-handle sliders can be used to define a range of values, versus a single value. To make a two-handle slider, add a second handle, and a second `<input>`. This works with horizontal and vertical sliders.

    You can add IDs to the `<input>`s inside the sliders to make it easier to access the values. If you don't, the plugin will add an ID to each for you.

    Note that the first handle manipulates the first `<input>`, while the second handle manipulates the second `<input>`.

    <p>
      <a class="" data-open-video="8:18"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/oWdwdX?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="slider" data-slider data-initial-start="25" data-initial-end="75">
      <span class="slider-handle" data-slider-handle role="slider" tabindex="1"></span>
      <span class="slider-fill" data-slider-fill></span>
      <span class="slider-handle" data-slider-handle role="slider" tabindex="1"></span>
      <input type="hidden">
      <input type="hidden">
    </div>
    ```

    ---

    ## Data Binding

    Data binding allows you to connect the slider to an external `<input>` field. With data binding set up, dragging the handle will change the value inside the text field, and editing the number in the text field will move the slider in real-time.

    To set it all up, create an `<input>` with an ID and add `aria-controls="id"` to the slider handle, where `id` is the ID of the `<input>`.

    <p>
      <a class="" data-open-video="4:56"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/dWeRRy?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-margin-x">
      <div class="cell small-10">
        <div class="slider" data-slider data-initial-start="50">
          <span class="slider-handle"  data-slider-handle role="slider" tabindex="1" aria-controls="sliderOutput1"></span>
          <span class="slider-fill" data-slider-fill></span>
        </div>
      </div>
      <div class="cell small-2">
        <input type="number" id="sliderOutput1">
      </div>
    </div>
    ```

    ---

    Or with a step size:

    ```html
    <div class="grid-x grid-margin-x">
      <div class="cell small-10">
        <div class="slider" data-slider data-initial-start="50" data-step="5">
          <span class="slider-handle"  data-slider-handle role="slider" tabindex="1" aria-controls="sliderOutput2"></span>
          <span class="slider-fill" data-slider-fill></span>
        </div>
      </div>
      <div class="cell small-2">
        <input type="number" id="sliderOutput2">
      </div>
    </div>
    ```
    ---

    ## Native Range Slider

    In Foundation 6.2, we introduced styles for `<input type="range">`, the native HTML element for range sliders. It's not supported in every browser, namely IE9 and some older mobile browsers. [View browser support for the range input type.](https://caniuse.com/#feat=input-range)

    <p>
      <a class="" data-open-video="10:05"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/GmdEem?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <input type="range" min="1" max="100" step="1">
    ```

    If you're using the Sass version of Foundation, add this line to your main Sass file:

    ```scss
    @include foundation-range-input;
    ```

    It's possible to use both the JavaScript slider and the native slider in the same codebase, as the CSS selectors used don't overlap. Here's what's different about the native slider:

    - Less markup: just write `<input type="range">` and you're good.
    - No JavaScript is needed, which guarantees it runs faster in most browsers.
    - To disable the slider, add `disabled` as an attribute, instead of a class.
    - No support for vertical orientation.
    - No support for two handles.

    ---

    ## Non-linear value translation

    Sometimes not every value is of equal importance. In the example below, the slider focusses on the higher numbers by adding a `log`-type position value function.
    Alternatively there is also a `pow`-type position value function available, making the reverse possible.

    The nonLinearBase-option is optional and defaults to 5.

    ```html
    <div class="grid-x grid-margin-x">
      <div class="cell small-10">
        <div class="slider" data-slider data-initial-start="50" data-step="1" data-position-value-function="log" data-non-linear-base="5">
          <span class="slider-handle" data-slider-handle role="slider" tabindex="1" aria-controls="sliderOutputNonLinear"></span>
        </div>
      </div>
      <div class="cell small-2">
        <input type="number" id="sliderOutputNonLinear">
      </div>
    </div>
    ```

    ## Reflow

    The slider takes into account the width of the handles when calculating how to display itself. This means that if the slider is initially hidden, or hidden while the value is adjusted, the resulting visual will be slightly different because the width of the handle is indeterminate.  If this is problematic, you can use JavaScript to cause the slider to reflow at the time that you change it from being hidden.  Example:

    ```js
    $('#my-slider').show();
    $('#my-slider').foundation('_reflow');
    ```"""

    pass


class SMOOTH_SCROLL:
    """---
    title: Smooth Scroll
    description: Allows internal links smooth scrolling.
    js: js/foundation.smoothScroll.js
    tags:
      - navigation
    ---

    <ul class="menu align-center" data-smooth-scroll>
      <li><a href="#setup">Setup</a></li>
      <li><a href="#javascript-reference">Javascript Reference</a></li>
    </ul>

    <hr>

    ## Setup

    To enable SmoothScroll on internal links, just add the attribute `data-smooth-scroll` to the parent container like our [Menu](menu.html). Please note that each section needs a unique ID.

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/jwOEEM?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="menu" data-smooth-scroll>
      <li><a href="#first">First Arrival</a></li>
      <li><a href="#second">Second Arrival</a></li>
      <li><a href="#third">Third Arrival</a></li>
    </ul>
    <div class="sections">
      <section id="first">First Section</section>
      <section id="second">Second Section</section>
      <section id="third">Third Section</section>
    </div>
    ```

    You can also setup SmoothScroll directly via individual link.

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/NgWPab?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <a href="#exclusive" data-smooth-scroll>Exclusive Section</a>
    <section id="exclusive">The Exclusive Section</section>
    ```"""

    pass


class STARTER_PROJECTS:
    """---
    title: Starter Projects
    description: We have a few starter project templates that can be installed with the Foundation CLI. You can also download them manually!
    video: 'lFrpnk0Oo_8'
    ---


    Our project templates give you a solid... *Foundation* on which to start a new project. Both templates use the [Gulp](https://gulpjs.com) build system to automate the process of compiling Sass, processing JavaScript, copying files, and more.

    ## Basic Template

    <div class="responsive-embed widescreen mb1">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/ofSZUKkjPRY" frameborder="0" allowfullscreen></iframe>
      <a id="docs-mobile-video-link" class="docs-mobile-video" target="_blank" href="https://youtu.be/ofSZUKkjPRY"></a>
    </div>

    Our basic project template is a lot like the Sass template from Foundation 5. The project has a flat directory structure and only compiles Sass. It's great if you want to quickly put together a simple project and only need to use Sass.

    <!--
    You can set up a basic project through the Foundation CLI with this command:

    ```bash
    foundation new --framework sites --template basic
    ```
    -->

    You can manually install the template with:
     ```bash
    # Download the template with Git
    git clone https://github.com/foundation/foundation-sites-template projectname

    # Move to the project folder, and install dependencies
    cd projectname
    yarn

    # Build the Sass files
    yarn start
    ```

    Your project will be recompiled every time you save a Sass file in `dist/.

    ---

    ## ZURB Template

    <div class="responsive-embed widescreen mb1">
      <iframe id="zurb-template-starter" data-linkable-video="3Uj74uJ3GSQ" width="500" height="315" src="https://www.youtube.com/embed/3Uj74uJ3GSQ?enablejsapi=1" enablejsapi="1" frameborder="0" allowfullscreen ></iframe>
      <a id="docs-mobile-video-link" class="docs-mobile-video" target="_blank" href="https://www.youtube.com/watch?v=3Uj74uJ3GSQ"></a>
    </div>

    The official ZURB Template includes not only Sass processing, but also JavaScript processing, Handlebars templating, and image compression. We use this exact template at ZURB for our client work!

    <!--
    You can set up an advanced project through the Foundation CLI with this command:

    ```bash
    foundation new --framework sites --template zurb
    ```
    -->

    You can manually install the template with:
    ```bash
    # Download the ZURB template with Git
    git clone https://github.com/foundation/foundation-zurb-template projectname

    # Move to the project folder, and install dependencies
    cd projectname
    yarn

    # Build the project
    yarn start
    ```

    Once compiled, you project is viewable at: <a class="button primary" href="http://localhost:8000" target="_blank">http://localhost:8000</a>

    The biggest difference between this and the basic template is the folder structure. In the ZURB Template, your project has a `src/` folder which contains your source files, and a separate `dist/` folder with your finished website. As you work on your project, Gulp continuously updates your `dist/` folder with new versions of files. To compile a production build, run `yarn build`.

    To override or add to the default styles of the ZURB Template, in your project's `src/assets/scss/` folder
     - Change Sass variables in `_settings.scss`
     - Add custom SCSS and css to new files in the `components` folder then import those files at the bottom of `app.scss`

    The `_settings.scss` and `app.scss` files are not changed when upgrading an existing project. As a result, you must manually edit your `_settings.scss` file to incorporate any Sass changes found [in the release notes](https://github.com/foundation/foundation-sites/releases).

    ### Features

    Here's an overview of what the ZURB Template can do:

    * **Asset Copying**

      Gulp will copy anything out of the `src/assets` folder as-is to the `assets` folder of your final project. Note that Sass files, JavaScript files, and images are *not* **part of this copying process, as they have their own steps.**


    * **Page Compilation**

      The `src/` directory includes three folders used to create HTML pages: `pages/`, `layouts/`, and `partials/`. A flat file compiler called [Panini](panini.html) is used to process your project's various pages, inserting them into a common template, and injecting any HTML partials. This is done with a templating language called [Handlebars](https://handlebarsjs.com/).

      Panini has a dedicated page here in the docs that explains its various features. **[Learn more about Panini.](panini.html)**

    * **Sass Compilation**

      Sass is compiled to CSS using [Libsass](https://sass-lang.com/libsass) (via [node-sass](https://github.com/sass/node-sass)). The main Sass file is under `src/assets/scss/app.scss`, and imports Foundation and Motion UI. Any new Sass partials you create should be in this folder as well.

      The CSS is output in the `nested` style, which is readable like normal CSS. A source map is also created, which can be read by developer tools such as the Chrome Web Inspector. When building for production, the CSS is also compressed with [clean-css](https://github.com/jakubpawlowicz/clean-css/issues), and pruned with [UnCSS](https://github.com/giakki/uncss). UnCSS scans the HTML of your pages and removes any CSS classes you didn't use.

    * **JavaScript Compilation**

      JavaScript is transpiled using [Babel](https://babeljs.io) (with the [es2015 plugin](https://babeljs.io/docs/plugins/#es2015)) so you can use [ES2015 features](https://babeljs.io/learn-es2015/).
      The main Js file is under `src/assets/js/app.js`, and imports Foundation, jQuery and whatInput. You can import there installed packages and custom files, they will be included in the build.

      A source map is created that maps back to the original files. By default, the bundled `app.js` is uncompressed. When building for production, the file is run through [UglifyJS](https://github.com/mishoo/UglifyJS) for compression.

      The whole bundling process is handled by [webpack](https://webpack.js.org): it manages all assets and dependencies for you and compiles them into one single file. If you're unfamiliar with imports or module bundling, check out:
      * [What are ES6 imports](https://2ality.com/2014/09/es6-modules-final.html)
      * [Beginner’s guide to webpack](https://medium.com/javascript-training/beginner-s-guide-to-webpack-b1f1a3638460)
      * [Beginner’s guide to JavaScript Modules](https://medium.freecodecamp.org/javascript-modules-a-beginner-s-guide-783f7d7a5fcc).

    * **Image Compression**

      By default, all images are copied as-is from `assets/img` to your `dist` folder. When building for production, images are run through [gulp-imagemin](https://github.com/sindresorhus/gulp-imagemin) for compression. The plugin supports JPEG, PNG, SVG, and GIF files.

    * **BrowserSync**

      The template creates a [BrowserSync](https://www.browsersync.io/) server, which is at `http://localhost:8000`. Load this URL to see your compiled templates. While the server is running, any time you save a file, any pages you have open will automatically refresh, allowing you to see changes in real-time as you work.

    * **Style Guide Creation**

      Under `src/styleguide` are two files to create a style guide for your project. The style guide is generated using Style Sherpa, a small plugin created by ZURB.

    Style Sherpa has a dedicated page here in the docs that explains its various features. **[Learn more about Style Sherpa.](style-sherpa.html)**

    ### Tutorials

    - [What the ZURB Stack Does](https://get.foundation/learn/foundation-6-zurb-stack-part-1.html) via ZURB
    - [Overview of Foundation's ZURB Stack and File Structure](https://get.foundation/learn/foundation-6-stack-file-structure.html) via ZURB
    - [All about the ZURB Template](https://zendev.com/2017/09/05/front-end-development-kickstarter-zurb-template.html#scss) via Kevin Ball
    """

    pass


class STICKY:
    """---
    title: Sticky
    description: Stick nearly anything, anywhere you like!
    video: '5KQmh0Eh-p8'
    js: js/foundation.sticky.js
    ---

    ## Basics

    Add the `.sticky` class and `[data-sticky]` to an element to create something that sticks. Sticky elements must be wrapped in a container, which will determine your sizing and grid layout, with `[data-sticky-container]`.

    <p>
      <a class="" data-open-video="0:35"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/GmGbjK?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="cell small-6 right" data-sticky-container>
      <div class="sticky" data-sticky data-margin-top="0">
        <img class="thumbnail" src="assets/img/generic/rectangle-3.jpg">
        <!-- This sticky element would stick to the window, with a marginTop of 0 -->
      </div>
    </div>

    <div class="cell small-6 right" data-sticky-container>
      <div class="sticky" data-sticky data-anchor="foo">
        <img class="thumbnail" src="assets/img/generic/rectangle-3.jpg">
        <!-- This sticky element would stick to the window for the height of the element #foo, with a 1em marginTop -->
      </div>
    </div>
    ```

    <!-- ```html -->
    <div class="grid-x grid-margin-x">
      <div class="cell small-6" id="example1" data-something>
        <p id="doodle">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
      </div>
      <div class="cell small-6 right" data-sticky-container>
        <div class="sticky" data-sticky data-margin-top="6" data-anchor="example1" data-sticky-on="small">
          <img class="thumbnail" src="assets/img/generic/rectangle-3.jpg">
        </div>
      </div>
    </div>

    ## Advanced

    You can also use two anchors, if you please. Using `data-top-anchor="idOfSomething"`, `data-btm-anchor="idOfSomething:[top/bottom]"`, or a set pixel number `data-top-anchor="150"`. If you use an element id with no top/bottom specified, it defaults to the top.

    <p>
      <a class="" data-open-video="3:55"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/rmKEmd?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="cell small-6 right" data-sticky-container>
      <div class="sticky" data-sticky data-top-anchor="example2:top" data-btm-anchor="foo:bottom">
        <img class="thumbnail" src="assets/img/generic/rectangle-5.jpg">
      </div>
    </div>
    ```


    <div class="grid-x grid-margin-x">
      <div class="cell small-6">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
        <p id="example2">
        <strong>The image to the right will be sticky when it hits the top of this paragraph element.</strong>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p id="foo">
          <strong>The image to the right will lose stickiness when it hits the bottom of this paragraph element.</strong>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
      </div>
      <div class="cell small-6 right" data-sticky-container>
        <div class="sticky" data-sticky data-margin-top="6" data-top-anchor="example2:top" data-btm-anchor="foo:bottom">
          <img class="thumbnail" src="assets/img/generic/rectangle-5.jpg">
        </div>
      </div>
    </div>

    ## Stick to bottom

    You can also stick to bottom.
    Using `data-stick-to="bottom"`.
    Here is an example using two anchors (like above) with a stick to bottom.
    ```html
    <div class="cell small-6 right" data-sticky-container>
      <div class="sticky" data-sticky data-stick-to="bottom" data-top-anchor="example3" data-btm-anchor="foo2:top">
        <img class="thumbnail" src="assets/img/generic/rectangle-5.jpg">
      </div>
    </div>
    ```


    <div class="grid-x grid-margin-x">
      <div class="cell small-6">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p id="example3"><strong>The image to the right will be sticky when it hits the top of this paragraph element.</strong>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p id="foo2">
          <strong>The image to the right will lose stickiness when it hits the top of this paragraph element.</strong>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
      </div>
      <div class="cell small-6 right" data-sticky-container>
        <div class="sticky" data-sticky data-margin-top="6" data-top-anchor="example3:top" data-btm-anchor="foo2:top" data-stick-to="bottom">
          <img class="thumbnail" src="assets/img/generic/rectangle-5.jpg">
        </div>
      </div>
    </div>

    ## Sticky Navigation

    Sometimes you want a sticky nav bar or side nav, this is pretty simple, but does involve an extra step from Foundation 5's `sticky` class addition to Top Bar. The minimum to make a stick nav bar is below, and you can swap out `.title-bar` for another menu component. Please note the style `width:100%`, you can do it inline, or in your style sheets.

    ```html
    <div data-sticky-container>
      <div class="title-bar" data-sticky data-options="marginTop:0;" style="width:100%">
        <div class="title-bar-left"><!-- Content --></div>
        <div class="title-bar-right"><!-- Content --></div>
      </div>
    </div>
    ```
    With the minimum markup above, your nav bar will be sticky for the entire page. You could change this up by using anchor points, so it sticks and breaks at important markers on the page. A top anchor point of '1' will make it stick at the top of the page, a bottom anchor of `content:bottom` will make it break at the bottom of your `#content` element. This is useful if you want a sticky nav element, but not for the full length of the page.

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/aWaJpM?editors=1010" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div data-sticky-container>
      <div class="title-bar" data-sticky data-options="marginTop:0;" style="width:100%" data-top-anchor="1" data-btm-anchor="content:bottom">
        <div class="title-bar-left"><!-- Content --></div>
        <div class="title-bar-right"><!-- Content --></div>
      </div>
    </div>
    ```

    <iframe src="./assets/partials/sticky-nav.html" width="100%" height="300px" frameborder="0"></iframe>
    <!-- ``` -->"""

    pass


class STYLE_SHERPA:
    """---
    title: Style Sherpa
    description: Bundled with the ZURB Template, Style Sherpa makes it easy to create a style guide for your codebase, with just two files.
    library:
      github: https://github.com/foundation/style-sherpa
      docs: https://github.com/foundation/style-sherpa
    video: 'paIqrjCm9_k'
    ---

    Style guides are a critical component of a CSS codebase, especially one used by many people. It's important that everyone on a team knows how to build a component. Style guides are that documentation. The docs you're reading right now are a style guide of sorts, for the core Foundation styles.

    [Style Sherpa](https://github.com/foundation/style-sherpa) is a small tool bundled with the [ZURB Template](starter-projects.html#zurb-template) that can generate a basic style guide for you quickly. The style guide is created from a single Markdown file, which contains all of the page content, and an HTML template, which defines the structure around the content.

    ---

    ## Usage

    <p>
      <a class="" data-open-video="1:43"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    The ZURB Template includes the folder `src/styleguide/`, which contains both of the files you need to build your style guide. Like everything else in the ZURB Template, just edit the files and your changes will instantly be compiled

    One is a Markdown file, `index.md`. This file contains the contents of your style guide.

    The other is a Handlebars template, `template.html`. The contents of your style guide are inserted into this template as HTML. The final file is included in the `dist/` folder of your project as `styleguide.html`.

    ---

    ## Writing Content

    <p>
      <a class="" data-open-video="5:09"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    The style guide is divided into sections. Generally, each component in your codebase&mdash;think buttons, panels, modals, form controls, and so on&mdash;will have its own section.

    Sections are titled with a Markdown heading, which is a single hash mark:

    ```markdown
    # Buttons

    Lorem ipsum dolor sit amet, **consectetur adipisicing** elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    ```

    To create a new section, add four line breaks and a new heading:

    ```markdown
    # Buttons

    Lorem ipsum dolor sit amet, **consectetur adipisicing** elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.



    # Forms

    Lorem ipsum dolor sit amet, `<form>` elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    ```

    ### Code Samples

    <p>
      <a class="" data-open-video="6:28"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    A style guide should always have HTML examples, which explain how to build something. To create a code block in Markdown, surround the code with three backticks. You can also set the language of the code block after the first set of backticks. Style Sherpa will color the syntax for you in the final output.

        ```html
        <button class="button" type="button">This is a button.</button>
        ```

    You'll also want to show a live demo of the component below the code sample, so developers can see both the HTML for an element, and what the HTML looks live rendered in one place. Style Sherpa has a shortcut for this: instead of setting `html` as the language in Markdown, set it to `html`. This will print a code sample and a live demo with the same code all in one go.

        ```html
        <button class="button" type="button">This is a button.</button>
        ```

    The output looks something like this:

    ```html
    <button class="button" type="button">This is a button.</button>
    ```

    ---

    ## Changing the Template

    <p>
      <a class="" data-open-video="3:32"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    The ZURB Template includes a minimal boilerplate for your style guide, but you're free to customize it however you want.

    The boilerplate uses Foundation's Vertical Menu&mdash;one item is made for each section. Here's what the Handlebars code looks like:

    {{{{raw}}}}
    ```handlebars
    <div class="row">

      <div class="large-3 medium-4 columns">
        <dl class="vertical tabs" data-tab>
          {{#each pages}}
            <dd{{#if @first}} class="active"{{/if}}><a href="#{{ anchor }}">{{ title }}</a></dd>
          {{/each}}
        </dl>
      </div>

      <div class="large-9 medium-8 columns">
        <div class="tabs-content">
          {{#each pages}}
            <section class="content {{#if @first}}active{{/if}}" id="{{ anchor }}">
              {{ body }}
            </section>
          {{/each}}
        </div>
      </div>

    </div>
    ```

    The template has access to a `pages` variable, which is an array with the data for each page. When looping through `pages` using `{{#each}}`, you have access to these variables:

    - `title`: The name of the section.
    - `anchor`: The name of the section, formatted as a URL anchor.
    - `body`: The content of the section.

    {{{{/raw}}}}"""

    pass


class SWITCH:
    """---
    title: Switch
    description: Create pure CSS3 On/Off switches with animated transitions. Now you can tell your users to flip the switch or switch off.
    video: 'AEL2Mj0DT3o'
    sass: scss/components/_switch.scss
    ---

    ## Basics

    Add the `.switch` class to an element to create a switch. Inside the switch, add an `<input type="checkbox">` with the class `.switch-input`. Next to that, create a `<label>` with the class `.switch-paddle`.

    Give the `<input>` a unique ID and point the `<label>` to it with the `for` attribute. This makes the switch clickable.

    <div class="primary callout">
      <p>Inside the switch label is screen reader-only text, which uses the <code>.show-for-sr</code> class to visually mask the text.</p>
    </div>

    <div class="primary callout">
      <p>Inspecting the value of the underlying input should be done by evaluating the <code>checked</code> property of said input.</p>
    </div>

    <div class="callout warning">
      <p>Make sure the HTML of the switch goes in the order you see above&mdash;<code>&lt;input&gt;</code>, then <code>&lt;label&gt;</code></p>
    </div>

    <p>
      <a class="" data-open-video="0:30"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/aWGpGg?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="switch">
      <input class="switch-input" id="exampleSwitch" type="checkbox" name="exampleSwitch">
      <label class="switch-paddle" for="exampleSwitch">
        <span class="show-for-sr">Download Kittens</span>
      </label>
    </div>
    ```

    ---

    ## Disabled

    There may be times when you want to fix a switch into a position.  This can be accomplished by setting the `disabled` option on the switch input.

    ```html
    <div class="switch">
      <input class="switch-input" disabled checked="checked" id="exampleCheckedDisabledSwitch" type="checkbox" name="exampleCheckedDisabledSwitch">
      <label class="switch-paddle" for="exampleCheckedDisabledSwitch">
        <span class="show-for-sr">Can't Touch This Checked</span>
      </label>
    </div>

    <div class="switch">
      <input class="switch-input" disabled id="exampleUncheckedDisabledSwitch" type="checkbox" name="exampleUncheckedDisabledSwitch">
      <label class="switch-paddle" for="exampleUncheckedDisabledSwitch">
        <span class="show-for-sr">Can't Touch This Unchecked</span>
      </label>
    </div>
    ```

    ---

    ## Radio Switch

    You can also use `<input type="radio">` instead of `checkbox` to create a series of options.

    <p>
      <a class="" data-open-video="4:17"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/GmdrYW?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="switch">
      <input class="switch-input" id="exampleRadioSwitch1" type="radio" checked name="testGroup">
      <label class="switch-paddle" for="exampleRadioSwitch1">
        <span class="show-for-sr">Bulbasaur</span>
      </label>
    </div>
    ```

    <div class="switch">
      <input class="switch-input" id="exampleRadioSwitch2" type="radio" name="testGroup">
      <label class="switch-paddle" for="exampleRadioSwitch2">
        <span class="show-for-sr">Charmander</span>
      </label>
    </div>

    <div class="switch">
      <input class="switch-input" id="exampleRadioSwitch3" type="radio" name="testGroup">
      <label class="switch-paddle" for="exampleRadioSwitch3">
        <span class="show-for-sr">Squirtle</span>
      </label>
    </div>

    ---

    ## Sizing Classes

    Use the classes `.tiny`, `.small`, or `.large` to change the switch size.

    <p>
      <a class="" data-open-video="6:47"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/mmLRgm?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="switch tiny">
      <input class="switch-input" id="tinySwitch" type="checkbox" name="exampleSwitch">
      <label class="switch-paddle" for="tinySwitch">
        <span class="show-for-sr">Tiny Sandwiches Enabled</span>
      </label>
    </div>

    <div class="switch small">
      <input class="switch-input" id="smallSwitch" type="checkbox" name="exampleSwitch">
      <label class="switch-paddle" for="smallSwitch">
        <span class="show-for-sr">Small Portions Only</span>
      </label>
    </div>

    <div class="switch large">
      <input class="switch-input" id="largeSwitch" type="checkbox" name="exampleSwitch">
      <label class="switch-paddle" for="largeSwitch">
        <span class="show-for-sr">Show Large Elephants</span>
      </label>
    </div>
    ```

    ---

    ## Inner Labels

    You can place active and inactive text inside of a switch. The active text (`.switch-active`) only displays when the switch is on, and the inactive text (`.switch-inactive`) only displays when the switch is off.

    Active/inactive text goes inside of the switch's `<label>`.

    <div class="primary callout">
      <p>Depending on the length of the words you place inside the switch, you may need to fine-tune the <code>left</code> or <code>right</code> CSS properties of the text to get it positioned right.</p>
    </div>

    <a class="" data-open-video="8:07"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>

    <div class="primary callout">
      <p>Add <code>aria-hidden="true"</code> to these labels to prevent AT from reading them.</p>
    </div>


    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/qmYRzb?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <p>Do you like me?</p>
    <div class="switch large">
      <input class="switch-input" id="yes-no" type="checkbox" name="exampleSwitch">
      <label class="switch-paddle" for="yes-no">
        <span class="show-for-sr">Do you like me?</span>
        <span class="switch-active" aria-hidden="true">Yes</span>
        <span class="switch-inactive" aria-hidden="true">No</span>
      </label>
    </div>
    ```"""

    pass


class TABLE:
    """---
    title: Tables
    description: Okay, they're not the sexiest things ever, but tables get the job done (for tabular data, of course). They have responsive modifiers to help solve some of your layout issues based on your tables needs.
    video: '-Omv7c3Qg4s'
    sass: scss/components/_table.scss
    ---

    ## Basics

    No bells or whistles here, just a straight up table for all of your basic table needs.

    <p>
      <a class="" data-open-video="0:28"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/zwaazZ?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <table>
      <thead>
        <tr>
          <th width="200">Table Header</th>
          <th>Table Header</th>
          <th width="150">Table Header</th>
          <th width="150">Table Header</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Content Goes Here</td>
          <td>This is longer content Donec id elit non mi porta gravida at eget metus.</td>
          <td>Content Goes Here</td>
          <td>Content Goes Here</td>
        </tr>
        <tr>
          <td>Content Goes Here</td>
          <td>This is longer Content Goes Here Donec id elit non mi porta gravida at eget metus.</td>
          <td>Content Goes Here</td>
          <td>Content Goes Here</td>
        </tr>
        <tr>
          <td>Content Goes Here</td>
          <td>This is longer Content Goes Here Donec id elit non mi porta gravida at eget metus.</td>
          <td>Content Goes Here</td>
          <td>Content Goes Here</td>
        </tr>
      </tbody>
    </table>
    ```

    ---

    ## Hover State

    Need to spiff up the table just a tad? Just add the class `.hover` to lightly darken the table rows on hover.

    <p>
      <a class="" data-open-video="2:49"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/xdzzgr?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <table class="hover">
    </table>
    ```

    <table class="hover">
      <thead>
        <tr>
          <th width="200">Table Header</th>
          <th>Table Header</th>
          <th width="150">Table Header</th>
          <th width="150">Table Header</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Content Goes Here</td>
          <td>This is longer content Donec id elit non mi porta gravida at eget metus.</td>
          <td>Content Goes Here</td>
          <td>Content Goes Here</td>
        </tr>
        <tr>
          <td>Content Goes Here</td>
          <td>This is longer Content Goes Here Donec id elit non mi porta gravida at eget metus.</td>
          <td>Content Goes Here</td>
          <td>Content Goes Here</td>
        </tr>
        <tr>
          <td>Content Goes Here</td>
          <td>This is longer Content Goes Here Donec id elit non mi porta gravida at eget metus.</td>
          <td>Content Goes Here</td>
          <td>Content Goes Here</td>
        </tr>
      </tbody>
    </table>

    ---

    ## Stripes

    By default, table rows are striped. There's an `.unstriped` class to remove the stripes. If you change `$table-is-striped` to `false` to remove stripes from all tables, use the `.striped` class to add stripes.

    <p>
      <a class="" data-open-video="2:18"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/MmBQag?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <table class="unstriped">
    </table>
    ```

    <table class="unstriped">
      <thead>
        <tr>
          <th width="200">Table Header</th>
          <th>Table Header</th>
          <th width="150">Table Header</th>
          <th width="150">Table Header</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Content Goes Here</td>
          <td>This is longer content Donec id elit non mi porta gravida at eget metus.</td>
          <td>Content Goes Here</td>
          <td>Content Goes Here</td>
        </tr>
        <tr>
          <td>Content Goes Here</td>
          <td>This is longer Content Goes Here Donec id elit non mi porta gravida at eget metus.</td>
          <td>Content Goes Here</td>
          <td>Content Goes Here</td>
        </tr>
        <tr>
          <td>Content Goes Here</td>
          <td>This is longer Content Goes Here Donec id elit non mi porta gravida at eget metus.</td>
          <td>Content Goes Here</td>
          <td>Content Goes Here</td>
        </tr>
      </tbody>
    </table>

    ---

    ## Stacked Table

    To stack a table on small screens, add the class `.stack`.

    <p>
      <a class="" data-open-video="3:23"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/EmpQPK?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <table class="stack">
    </table>
    ```

    <table class="stack">
      <thead>
        <tr>
          <th>Cookies</th>
          <th>Taste</th>
          <th>Calories</th>
          <th>Overall</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Chocolate Chip</td>
          <td>Tastey</td>
          <td>120cal</td>
          <td>7.5/10</td>
        </tr>
        <tr>
          <td>Snickerdoodle</td>
          <td>Delicious</td>
          <td>95cal</td>
          <td>8/10</td>
        </tr>
        <tr>
          <td>Oatmeal Raisin</td>
          <td>Superb</td>
          <td>10cal</td>
          <td>11/10</td>
        </tr>
      </tbody>
    </table>

    ---

    ## Scrolling Table

    Got a lot of tubular tabular data? Add a wrapper element with the class `.table-scroll` around your table to enable horizontal scrolling.


    <p>
      <a class="" data-open-video="3:48"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="primary callout">
      <p>The wrapping element was added in Foundation 6.2&mdash;prior to that, you just added the class <code>.scroll</code> to the table itself. However, this method doesn't work great with Internet Explorer 9. <strong>If you don't need IE9 support, you can just add <code>.scroll</code> to your table, and the wrapping element isn't necessary.</strong>
    </div>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/vmadKp?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="table-scroll">
      <table></table>
    </div>
    ```

    <div class="table-scroll">
      <table>
        <thead>
          <tr>
            <th>This is the description!</th>
            <th>One</th>
            <th>Two</th>
            <th>Three</th>
            <th>Four</th>
            <th>Five</th>
            <th>Six</th>
            <th>Seven</th>
            <th>Eight</th>
            <th>Nine</th>
            <th>Ten</th>
            <th>Eleven</th>
            <th>Twelve</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="display:block; width:400px;">These are all the words that people use to describe Foundation 6!</td>
            <td>Cool</td>
            <td>Swag</td>
            <td>Chill</td>
            <td>Killer</td>
            <td>Rad</td>
            <td>Baller</td>
            <td>OMG</td>
            <td>Sweet</td>
            <td>Awesome</td>
            <td>Beast</td>
            <td>Dope</td>
            <td>Tubular</td>
          </tr>
          <tr>
            <td>These are some words that people use to describe other web frameworks.</td>
            <td>Whatevs</td>
            <td>Ugh.</td>
            <td>LOL</td>
            <td>K</td>
            <td>Aight</td>
            <td>Eh.</td>
            <td>Grrr...</td>
            <td>Meh.</td>
            <td>TTYL</td>
            <td>Bleh.</td>
            <td>Really?</td>
            <td>Why?</td>
          </tr>
          <tr>
            <td>Here are some great super heros.</td>
            <td>Batman</td>
            <td>Superman</td>
            <td>Spiderman</td>
            <td>Wonder Woman</td>
            <td>Hulk</td>
            <td>Nicolas Cage</td>
            <td>Antman</td>
            <td>Aquaman</td>
            <td>Captain America</td>
            <td>Wolverine</td>
            <td>Thor</td>
            <td>Iron Man</td>
          </tr>
        </tbody>
        <tfoot>
          <tr>
            <td>Here's a footer, just in case</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
          </tr>
        </tfoot>
      </table>
    </div>"""

    pass


class TABS:
    """---
    title: Tabs
    description: Tabs are elements that help you organize and navigate multiple documents in a single container. They can be used for switching between items in the container.
    video: '8FtJRXPF5Cs'
    sass: scss/components/_tabs.scss
    js: js/foundation.tabs.js
    ---

    ## Basics

    There are two pieces to a tabbed interface: the tabs themselves, and the content for each tab. The tabs are an element with the class `.tabs`, and each item has the class `.tabs-title`. Each tab contains a link to a tab. The `href` of each link should match the ID of a tab. Alternatively, the ID can be specified with the attribute `data-tabs-target`.

    ```html
    <ul class="tabs" data-tabs id="example-tabs">
      <li class="tabs-title is-active"><a href="#panel1" aria-selected="true">Tab 1</a></li>
      <li class="tabs-title"><a data-tabs-target="panel2" href="#panel2">Tab 2</a></li>
    </ul>
    ```

    The tab content container has the class `.tabs-content`, while each section has the class `.tabs-panel`. Each content pane also has a unique ID, which is targeted by a link in the tabstrip.

    <p>
      <a class="" data-open-video="0:50"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/VbdGKj?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="tabs-content" data-tabs-content="example-tabs">
      <div class="tabs-panel is-active" id="panel1">
        <p>Vivamus hendrerit arcu sed erat molestie vehicula. Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor. Ut in nulla enim. Phasellus molestie magna non est bibendum non venenatis nisl tempor. Suspendisse dictum feugiat nisl ut dapibus.</p>
      </div>
      <div class="tabs-panel" id="panel2">
        <p>Suspendisse dictum feugiat nisl ut dapibus.  Vivamus hendrerit arcu sed erat molestie vehicula. Ut in nulla enim. Phasellus molestie magna non est bibendum non venenatis nisl tempor.  Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor.</p>
      </div>
    </div>
    ```

    Put it all together, and we get this:

    <ul class="tabs" data-tabs id="example-tabs">
      <li class="tabs-title is-active"><a href="#panel1" aria-selected="true">Tab 1</a></li>
      <li class="tabs-title"><a href="#panel2">Tab 2</a></li>
      <li class="tabs-title"><a href="#panel3">Tab 3</a></li>
      <li class="tabs-title"><a href="#panel4">Tab 4</a></li>
      <li class="tabs-title"><a href="#panel5">Tab 5</a></li>
      <li class="tabs-title"><a href="#panel6">Tab 6</a></li>
    </ul>

    <div class="tabs-content" data-tabs-content="example-tabs">
      <div class="tabs-panel is-active" id="panel1">
        <p>one</p>
        <p>Check me out! I'm a super cool Tab panel with text content!</p>
        <p><a href="#">I am a link but don't do anything</a></p>
      </div>
      <div class="tabs-panel" id="panel2">
        <p>two</p>
        <textarea></textarea>
        <button class="button">I do nothing!</button>
      </div>
      <div class="tabs-panel" id="panel3">
        <p>three</p>
        <p>Check me out! I'm a super cool Tab panel with text content!</p>
      </div>
      <div class="tabs-panel" id="panel4">
        <p>four</p>
        <img class="thumbnail" src="assets/img/generic/rectangle-2.jpg">
      </div>
      <div class="tabs-panel" id="panel5">
        <p>five</p>
        <p>Check me out! I'm a super cool Tab panel with text content!</p>
      </div>
      <div class="tabs-panel" id="panel6">
        <p>six</p>
        <img class="thumbnail" src="assets/img/generic/rectangle-8.jpg">
      </div>
    </div>

    ---

    ## Vertical Tabs

    Add the `.vertical` class to a tabstrip and tab contents to stack tabs vertically. You can also remove the `.grid-margin-x` class from the wrapping div to make them sit side-by-side.

    <p>
      <a class="" data-open-video="3:46"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/eWKLdX?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-container">
      <div class="grid-x">
        <div class="cell medium-3">
          <ul class="vertical tabs" data-tabs id="example-tabs">
            <li class="tabs-title is-active"><a href="#panel1v" aria-selected="true">Tab 1</a></li>
            <li class="tabs-title"><a href="#panel2v">Tab 2</a></li>
            <li class="tabs-title"><a href="#panel3v">Tab 3</a></li>
            <li class="tabs-title"><a href="#panel4v">Tab 4</a></li>
            <li class="tabs-title"><a href="#panel5v">Tab 5</a></li>
            <li class="tabs-title"><a href="#panel6v">Tab 6</a></li>
          </ul>
        </div>
        <div class="cell medium-9">
          <div class="tabs-content vertical" data-tabs-content="example-tabs">
            <div class="tabs-panel is-active" id="panel1v">
              <p>One</p>
              <p>Check me out! I'm a super cool Tab panel with text content!</p>
            </div>
            <div class="tabs-panel" id="panel2v">
              <p>Two</p>
              <img class="thumbnail" src="assets/img/generic/rectangle-7.jpg">
            </div>
            <div class="tabs-panel" id="panel3v">
              <p>Three</p>
              <p>Check me out! I'm a super cool Tab panel with text content!</p>
            </div>
            <div class="tabs-panel" id="panel4v">
              <p>Four</p>
              <img class="thumbnail" src="assets/img/generic/rectangle-2.jpg">
            </div>
            <div class="tabs-panel" id="panel5v">
              <p>Five</p>
              <p>Check me out! I'm a super cool Tab panel with text content!</p>
            </div>
            <div class="tabs-panel" id="panel6v">
              <p>Six</p>
              <img class="thumbnail" src="assets/img/generic/rectangle-8.jpg">
            </div>
          </div>
        </div>
      </div>
    </div>
    ```

    ---

    ## Collapsing Tabs

    Add the attribute `data-active-collapse="true"` to a tabstrip to collapse active tabs.

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/LyrJQZ?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="tabs" data-active-collapse="true" data-tabs id="collapsing-tabs">
      <li class="tabs-title is-active"><a href="#panel1c" aria-selected="true">Tab 1</a></li>
      <li class="tabs-title"><a href="#panel2c">Tab 2</a></li>
      <li class="tabs-title"><a href="#panel3c">Tab 3</a></li>
      <li class="tabs-title"><a href="#panel4c">Tab 4</a></li>
    </ul>

    <div class="tabs-content" data-tabs-content="collapsing-tabs">
      <div class="tabs-panel is-active" id="panel1c">
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
      </div>
      <div class="tabs-panel" id="panel2c">
        <p>Vivamus hendrerit arcu sed erat molestie vehicula. Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor. Ut in nulla enim. Phasellus molestie magna non est bibendum non venenatis nisl tempor. Suspendisse dictum feugiat nisl ut dapibus.</p>
      </div>
      <div class="tabs-panel" id="panel3c">
        <img class="thumbnail" src="assets/img/generic/rectangle-3.jpg">
      </div>
      <div class="tabs-panel" id="panel4c">
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
      </div>
    </div>
    ```

    ---

    ## Tabs and URLs

    ### Browser history

    When the `data-deep-link` option is set to `true`, the current state of the tabset is recorded by adding a hash with the tab panel ID to the browser URL when a tab opens. By default, tabs *replace* the browser history (using `history.replaceState()`). Modify this behavior by using attribute `data-update-history="true"` to *append* to the browser history (using `history.pushState()`). In the latter case the browser back button will track each click that opens a tab panel.

    By using deep linking (see below), the open state of a page's tabset may be shared by copy-pasting the browser URL.

    ### Deep linking

    Add the attribute `data-deep-link="true"` to a tabstrip to:
    - modify the browser history when a tab is clicked
    - allow users to open a particular tab at page load with a hash-appended URL

    <p>
      <a class="" data-open-video="5:14"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    ```html
    <ul class="tabs" data-deep-link="true" data-update-history="true" data-deep-link-smudge="true" data-deep-link-smudge-delay="500" data-tabs id="deeplinked-tabs">
      <li class="tabs-title is-active"><a href="#panel1d" aria-selected="true">Tab 1</a></li>
      <li class="tabs-title"><a href="#panel2d">Tab 2</a></li>
      <li class="tabs-title"><a href="#panel3d">Tab 3</a></li>
      <li class="tabs-title"><a href="#panel4d">Tab 4</a></li>
    </ul>

    <div class="tabs-content" data-tabs-content="deeplinked-tabs">
      <div class="tabs-panel is-active" id="panel1d">
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
      </div>
      <div class="tabs-panel" id="panel2d">
        <p>Vivamus hendrerit arcu sed erat molestie vehicula. Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor. Ut in nulla enim. Phasellus molestie magna non est bibendum non venenatis nisl tempor. Suspendisse dictum feugiat nisl ut dapibus.</p>
      </div>
      <div class="tabs-panel" id="panel3d">
        <img class="thumbnail" src="assets/img/generic/rectangle-3.jpg">
      </div>
      <div class="tabs-panel" id="panel4d">
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
      </div>
    </div>
    ```

    For example, <a target="_blank" href="#panel3d">https://example.com/#panel3d</a> will open the third tab panel at page load. This example will open a new browser tab and scroll you to the open tab.

    When linking directly to a tab panel, it might not be obvious that the content appears within a tab panel. An additional attribute `data-deep-link-smudge` rolls the page up slightly after deep linking (to a horizontal tabset) so that the tabstrip is at the top of the viewport.

    ```html
    <ul class="tabs" data-deep-link="true" data-deep-link-smudge="true" data-deep-link-smudge-delay="600" data-tabs id="deeplinked-tabs-with-smudge">
    ```"""

    pass


class THUMBNAIL:
    """---
    title: Thumbnail
    description: If you're going to use an image as an anchor, we've got you covered. All you gotta do is add one class to your image and voilà!
    video: 'BOtW8oacFZk'
    sass: scss/components/_thumbnail.scss
    ---

    The `.thumbnail` class can be applied directly to an `<img>` element, or an `<a>` that wraps it. Make sure the `<img>` has an `alt` attribute that describes the contents of the image.

    <p>
      <a class="" data-open-video="0:30"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/EmLexY?editors=1100" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <img class="thumbnail" src="assets/img/thumbnail/01.jpg" alt="Photo of Uranus.">
    <a href="#" class="thumbnail"><img src="assets/img/thumbnail/02.jpg" alt="Photo of Neptune."></a>
    <img class="thumbnail" src="assets/img/thumbnail/03.jpg" alt="Photo of Pluto.">
    ```

    <div class="grid-x grid-margin-x">
      <div class="cell small-4 text-center">
        <img class="thumbnail" src="assets/img/thumbnail/01.jpg" alt="Photo of Uranus.">
      </div>
      <div class="cell small-4 text-center">
        <a href="#" class="thumbnail"><img src="assets/img/thumbnail/02.jpg" alt="Photo of Neptune."></a>
      </div>
      <div class="cell small-4 text-center">
        <img class="thumbnail" src="assets/img/thumbnail/03.jpg" alt="Photo of Pluto.">
      </div>
    </div>"""

    pass


class TOGGLER:
    """---
    title: Toggler
    description: Toggler makes it easy to toggle CSS or animate any element with a click.
    js: js/foundation.toggler.js
    mui: true
    video: 'wHpZCrpKlBc'
    ---

    ## Toggle a CSS class

    To setup a class toggle, start by adding the attribute `data-toggler` to an element. The value of `data-toggler` is the class you want to toggle (like `.classname` and `classname`). Also give the element a unique ID so it can be targeted.

    <p>
      <a class="" data-open-video="0:53"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/brettsmason/pen/xdzmmO?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="menu" id="menuBar" data-toggler=".expanded">
      <li><a href="#">One</a></li>
      <li><a href="#">Two</a></li>
      <li><a href="#">Three</a></li>
      <li><a href="#">Four</a></li>
    </ul>
    ```

    Then, add `data-toggle` to any element, with the ID of the target as the value of the attribute. Now, any time you click on this element, the class will toggle on and off on the target.

    ```html
    <p><a data-toggle="menuBar">Expand!</a></p>
    ```

    <p><a data-toggle="menuBar">Expand!</a></p>

    <ul class="menu" id="menuBar" data-toggler=".expanded">
      <li><a href="#">One</a></li>
      <li><a href="#">Two</a></li>
      <li><a href="#">Three</a></li>
      <li><a href="#">Four</a></li>
    </ul>

    ---

    ## Toggle with Animation

    Instead of toggling a class, you can also toggle visibility. When toggled, the element comes into or out of view using a Motion UI class.

    Instead of `data-toggler`, add the attribute `data-animate`. The value of the attribute is the *in animation* you want, followed by the *out animation*.
    <p>
      <a class="" data-open-video="3:49"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/brettsmason/pen/ZKRVNE?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <p><a data-toggle="panel">Toggle Panel</a></p>

    <div class="callout" id="panel" data-toggler data-animate="hinge-in-from-top spin-out">
      <h4>Hello!</h4>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dicta quas optio alias voluptas nobis iusto mollitia asperiores incidunt reprehenderit doloribus voluptatibus officiis minus, inventore, quasi nisi. Consequuntur, quidem. Sint, dicta?</p>
    </div>
    ```

    ---

    ## Mark as Closable

    To create an element that can be closed once, add the attribute `data-closable`. Then add a click trigger inside the element using `data-close`.
    <p>
      <a class="" data-open-video="7:42"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/brettsmason/pen/ZKRwEY?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="callout" data-closable>
      <button class="close-button" data-close>&times;</button>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Labore praesentium sint alias dolorum qui vel quaerat, libero consequatur non esse asperiores veritatis commodi, odit eum ipsam nemo dicta iste aliquam.</p>
    </div>
    ```

    ---

    ### With Alternate Animation

    `data-closable` can be configured with a custom exit animation.

    <p>
      <a class="" data-open-video="9:35"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/brettsmason/pen/mmKvdx?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="callout" data-closable="slide-out-right">
      <button class="close-button" data-close>&times;</button>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Labore praesentium sint alias dolorum qui vel quaerat, libero consequatur non esse asperiores veritatis commodi, odit eum ipsam nemo dicta iste aliquam.</p>
    </div>
    ```

    ---

    ### Toggle on focus

    The `data-toggle` attribute only toggles classes/visibility on click. You can also have the toggle fire when an element is *focused* or *unfocused* using `data-toggle-focus`.

    <p>
      <a class="" data-open-video="10:27"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/brettsmason/pen/gWKqbj?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <input type="text" data-toggle-focus="form-callout" placeholder="Click in here to reveal extra content">

    <div class="secondary callout is-hidden" id="form-callout" data-toggler="is-hidden">
      <p>This is only visible when the above field has focus.</p>
    </div>
    ```

    ---

    ## Multiple Targets

    The `data-toggle`, `data-close`, and `data-open` attributes can now target multiple elements! The syntax is simple; just pass a *space* separated list to the `data-x` attribute like so:
    <p>
      <a class="" data-open-video="12:52"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/brettsmason/pen/YVvBXY?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <button class="button" data-toggle="foo bar baz">Toggle things</button>
    ```
    Then the elements with ids of `foo`, `bar`, and `baz` will be toggled any time your button, (or any other element you choose), is clicked.

    <button class="button primary" data-toggle="thumb1 thumb2 thumb3">Toggle All These</button>
    <div class="grid-x grid-margin-x">
      <div class="cell small-4">
        <img class="thumbnail" id="thumb1" data-toggler data-animate="hinge-in-from-top spin-out" src="assets/img/thumbnail/01.jpg" alt="Photo of Uranus.">
      </div>
      <div class="cell small-4">
        <img class="thumbnail" id="thumb2" data-toggler data-animate="hinge-in-from-top spin-out" src="assets/img/thumbnail/02.jpg" alt="Photo of Uranus.">
      </div>
      <div class="cell small-4">
        <img class="thumbnail" id="thumb3" data-toggler data-animate="hinge-in-from-top spin-out" src="assets/img/thumbnail/03.jpg" alt="Photo of Uranus.">
      </div>
    </div>"""

    pass


class TOOLTIP:
    """---
    title: Tooltip
    description: Tooltips? More like <em>Cooltips</em>. But really though, tooltips are nifty for displaying extended information for a term or action on a page.
    video: 'PJMYScItyP4'
    sass: scss/components/_tooltip.scss
    js: js/foundation.tooltip.js
    ---


    ## Basic Tooltip
    By default, a tooltip appears below the defined term on hover.

    <p>
      <a class="" data-open-video="0:49"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/zwLxaY?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    The <span data-tooltip tabindex="1" title="Fancy word for a beetle.">scarabaeus</span> hung quite
    clear of any branches, and, if allowed to fall, would have fallen at our feet.
    ```

    ---

    ## Tooltip Top
    To get a tip-top top tooltip (lol), just add the class `.top` to the `<span>` element.

    <p>
      <a class="" data-open-video="3:00"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/BRPyqx?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    The <span data-tooltip class="top" tabindex="2" title="Fancy word for a beetle.">scarabaeus</span>
    hung quite clear of any branches, and, if allowed to fall, would have fallen at our feet.
    ```

    ---

    ## Tooltip clicking

    By default, clicking on a tooltip will leave it open until you click somewhere else.  However, you can disable that by adding `data-click-open="false"`

    <p>
      <a class="" data-open-video="4:12"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/XRBJvm?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    this
    <span data-tooltip class="top" tabindex="2" title="You see?  I'm open!">
      tooltip will stay open
    </span>
    while
    <span data-tooltip class="top" data-click-open="false" tabindex="2" title="I don't stay open">
      this one will only be open when hovered
    </span>
    ```

    ---

    ## Tooltip Right and Left

    You can also position the tooltips to the right and left of the word by adding the classes `.right` or `.left` to the `<span>` element.

    <p>
      <a class="" data-open-video="3:00"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="primary callout">
      <p>When using Foundation in <a href="rtl.html">right-to-left</a> mode, "right" still means right, and "left" still means left.</p>
    </div>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/EmpaJP?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    When he was dressed he went down the hall into the
    <span data-tooltip class="right" tabindex="3" title="Aligned on the right">kitchen</span>.
    The table was almost hidden beneath all Dudley's birthday presents. It looked as though
    <span data-tooltip class="left" tabindex="4" title="Aligned on the left">Dudley</span>
    had gotten the new computer he wanted, not to mention the second television and the racing bike.
    ```

    ---

    ## Explicit Positioning

    <div class="callout primary">
      <p><strong>New in v6.4:</strong> Heads up! This explicit positioning model is a new feature in v6.4.</p>
    </div>

    Now with tooltips you can define both positions for the tip. These tooltips have a fully explicit positioning model through which you can use both `data-position` and `data-alignment` to define both positions of the box.

    These dropdowns sets various positioning and alignments. Valid positions are left/right/top/bottom. Valid alignments are left/right/top/bottom/center. Left align means left sides should line up. Right align means right sides should line up. Center align means centers should line up.

    #### Top and Bottom positioned

    ```html
    <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="bottom" data-alignment="left">
      Bottom Left
    </button>

    <button class="button" type="button"  data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="bottom" data-alignment="center">
      Bottom Center
    </button>

    <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="bottom" data-alignment="right">
      Bottom Right
    </button>

    <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="top" data-alignment="left">
      Top Left
    </button>

    <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="top" data-alignment="center">
      Top Center
    </button>

    <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="top" data-alignment="right">
      Top Right
    </button>
    ```

    <div class="grid-x grid-margin-x small-up-1 medium-up-3">
      <div class="cell">
        <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="bottom" data-alignment="left">
          Bottom Left
        </button>
      </div>

      <div class="cell">
        <button class="button" type="button"  data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="bottom" data-alignment="center">
          Bottom Center
        </button>
      </div>

      <div class="cell">
        <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="bottom" data-alignment="right">
          Bottom Right
        </button>
      </div>

      <div class="cell">
        <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="top" data-alignment="left">
          Top Left
        </button>
      </div>

      <div class="cell">
        <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="top" data-alignment="center">
          Top Center
        </button>
      </div>

      <div class="cell">
        <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="top" data-alignment="right">
          Top Right
        </button>
      </div>
    </div>

    <br>

    #### Left and Right Positioned

    ```html
    <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="right" data-alignment="top">
      Right Top
    </button>

    <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="left" data-alignment="top">
      Left Top
    </button>

    <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="right" data-alignment="center">
      Right Center
    </button>

    <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="left" data-alignment="center">
      Left Center
    </button>

    <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="right" data-alignment="bottom">
      Right Bottom
    </button>

    <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="left" data-alignment="bottom">
      Left Bottom
    </button>
    ```

    <div class="grid-x grid-margin-x small-up-1 medium-up-2">
      <div class="cell">
        <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="right" data-alignment="top">
          Right Top
        </button>
      </div>
      <div class="cell">
        <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="left" data-alignment="top">
          Left Top
        </button>
      </div>

      <div class="cell">
        <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="right" data-alignment="center">
          Right Center
        </button>
      </div>
      <div class="cell">
        <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="left" data-alignment="center">
          Left Center
        </button>
      </div>

      <div class="cell">
        <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="right" data-alignment="bottom">
          Right Bottom
        </button>
      </div>
      <div class="cell">
        <button class="button" type="button" data-tooltip tabindex="1" title="Fancy word for a beetle." data-position="left" data-alignment="bottom">
          Left Bottom
        </button>
      </div>
    </div>"""

    pass


class TOP_BAR:
    """---
    title: Top Bar
    description: The new top bar is a simpler wrapper around our flexible menu components.
    video: cxPwwixHEJg
    sass: ./scss/components/_top-bar.scss
    flex: true
    ---

    <!-- <div class="callout training-callout">
      <p>Navigation is one the most crucial part of your site. Be a navigation guru with our Foundation online webinar training. You’ll learn techniques for creating responsive navigations that work with any type of site. In addition to that you can learn tips and tricks and best practices for all of Foundation’s components.</p>
      <a href="https://zurb.com/university/foundation-intro" target="_blank">Find out more about Foundation training classes →</a>
    </div> -->

    ## Basics

    A top bar (`.top-bar`) can have two sections: a left-hand section (`.top-bar-left`) and a right-hand section (`.top-bar-right`). On small screens, these sections stack on top of each other.

    In the below example, our top bar includes a [dropdown menu](dropdown-menu.html), along with a text input field and action button. The dropdown menu inherits the background color of the top bar. If you're using the Sass version of Foundation, you can change this with the `$topbar-submenu-background` variable.

    <p>
      <a class="" data-open-video="0:58"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/eWrwKP?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="top-bar">
      <div class="top-bar-left">
        <ul class="dropdown menu" data-dropdown-menu>
          <li class="menu-text">Site Title</li>
          <li>
            <a href="#">One</a>
            <ul class="menu vertical">
              <li><a href="#">One</a></li>
              <li><a href="#">Two</a></li>
              <li><a href="#">Three</a></li>
            </ul>
          </li>
          <li><a href="#">Two</a></li>
          <li><a href="#">Three</a></li>
        </ul>
      </div>
      <div class="top-bar-right">
        <ul class="menu">
          <li><input type="search" placeholder="Search"></li>
          <li><button type="button" class="button">Search</button></li>
        </ul>
      </div>
    </div>
    ```

    <br>

    <div class="primary callout">
      <p>The features of Foundation 5's top bar are still around, but they've been reworked into smaller, individual plugins. Check out our page on <a href="responsive-navigation.html">responsive navigation</a> to learn more.</p>
    </div>

    ---

    ## Advanced Layout

    <p>To set up a Responsive menu with toggle click trigger on mobile, first give your menu a unique ID. Next, add a title bar with the class <code>.title-bar</code> and the attribute <code>data-responsive-toggle</code>. The value of <code>data-responsive-toggle</code> should be the ID of the menu you're toggling. Lastly, add <code>data-toggle</code> to the element that will trigger the toggle. The value of <code>data-toggle</code> should also be the ID of the menu you're toggling.</p>

    <p>By default, the title bar will be visible on small screens, and the Menu hides. At the medium breakpoint, the title bar disappears, and the menu is always visible. This breakpoint can be changed with the <code>data-hide-for</code> attribute in HTML, or the <code>hideFor</code> setting in JavaScript.</p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/LymroM?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="title-bar" data-responsive-toggle="responsive-menu" data-hide-for="medium">
      <button class="menu-icon" type="button" data-toggle="responsive-menu"></button>
      <div class="title-bar-title">Menu</div>
    </div>

    <div class="top-bar" id="responsive-menu">
      <div class="top-bar-left">
        <ul class="dropdown menu" data-dropdown-menu>
          <li class="menu-text">Site Title</li>
          <li class="has-submenu">
            <a href="#0">One</a>
            <ul class="submenu menu vertical" data-submenu>
              <li><a href="#0">One</a></li>
              <li><a href="#0">Two</a></li>
              <li><a href="#0">Three</a></li>
            </ul>
          </li>
          <li><a href="#0">Two</a></li>
          <li><a href="#0">Three</a></li>
        </ul>
      </div>
      <div class="top-bar-right">
        <ul class="menu">
          <li><input type="search" placeholder="Search"></li>
          <li><button type="button" class="button">Search</button></li>
        </ul>
      </div>
    </div>
    ```

    ---

    ## Stacking

    By default, the two sections of a top bar will stack on top of each other on small screens. This can be changed by adding the class `.stacked-for-medium` or `.stacked-for-large`.

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/XRYbZa?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="top-bar stacked-for-medium">
      <!-- ... -->
    </div>
    ```

    <div class="top-bar stacked-for-medium">
      <div class="top-bar-left">
        <ul class="dropdown menu" data-dropdown-menu>
          <li class="menu-text">Site Title</li>
          <li>
            <a href="#">One</a>
            <ul class="menu vertical">
              <li><a href="#">One</a></li>
              <li><a href="#">Two</a></li>
              <li><a href="#">Three</a></li>
            </ul>
          </li>
          <li><a href="#">Two</a></li>
          <li><a href="#">Three</a></li>
        </ul>
      </div>
      <div class="top-bar-right">
        <ul class="menu">
          <li><input type="search" placeholder="Search"></li>
          <li><button type="button" class="button">Search</button></li>
        </ul>
      </div>
    </div>

    ---

    ## Sticky Navigation

    See the documentation for the [Sticky](sticky.html#sticky-navigation) plugin to see how to easily make a sticky nav bar.
    """

    pass


class TYPOGRAPHY_BASE:
    """---
    title: Base Typography
    description: Typography in Foundation 6 is meant to make your life easier by providing clean, attractive, simple default styles for all of the most basic typographical elements.
    video: pzAyIfsXis4
    sass:
      - scss/typography/_base.scss
      - scss/typography/_print.scss
    tags:
      - paragraph
      - heading
      - link
      - definition
      - blockquote
      - abbreviation
      - acronym
      - code
      - keystroke
    ---

    ## Paragraphs

    This is a paragraph. Paragraphs are preset with a font size, line height and spacing to match the overall vertical rhythm. To show what a paragraph looks like this needs a little more content&mdash;so, did you know that there are storms occurring on Jupiter that are larger than the Earth? Pretty cool. Use the `<strong>` and `<em>` tags to denote text that should be displayed or read with emphasis. Browsers will **bold** and *italicize* the words, while screen readers will read them with *emphasis*.

    <div class="callout primary">
      <p>If the emphasis of a phrase is important, don't make the emphasis purely visual&mdash;use the <code>&lt;em&gt;</code> or <code>&lt;strong&gt;</code> tags to mark it as well. Both of these tags have built-in styles, but there's no harm in adding additional styles in specific contexts.</p>
    </div>

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/oWMEOd?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <p>This is a paragraph. Paragraphs are preset with a font size, line height and spacing to match the overall vertical rhythm. To show what a paragraph looks like this needs a little more content so, did you know that there are storms occurring on Jupiter that are larger than the Earth? Pretty cool. Wrap strong around type to <strong>make it bold!</strong>. You can also use em to <em>italicize your words</em>.</p>
    ```

    ---

    ## Header

    Foundation includes styles for all headings&mdash;they're balanced and sized along a modular scale.

    <a class="" data-open-video="0:25"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    <div class="callout primary">
      <p>Avoid skipping heading levels when structuring your document, as it confuses screen readers. For example, after using an <code>&lt;h2&gt;</code> in your code, the next heading used should be either <code>&lt;h2&gt;</code> or <code>&lt;h3&gt;</code>. If you need a heading to look bigger or smaller to match a specific style, use CSS to override the default size.</p>
    </div>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/PmeKme" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <h1>h1. This is a very large header.</h1>
    <h2>h2. This is a large header.</h2>
    <h3>h3. This is a medium header.</h3>
    <h4>h4. This is a moderate header.</h4>
    <h5>h5. This is a small header.</h5>
    <h6>h6. This is a tiny header.</h6>
    ```

    ---

    ### Header Styles

    The framework includes two typographic scales&mdash;one uses a narrow range of sizes for small-sized screens, and the other uses a larger range of sizes for medium- and larger-sized screens. You can change these scales, or add new ones for other breakpoints, by editing the `$header-styles` map in your project's <a href="sass.html#the-settings-file">Settings File</a>.

    <a class="" data-open-video="1:28"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>

    Header  | Default | Medium and up
    --------|---------|--------------
    `<h1>`  | 24px    | 48px
    `<h2>`  | 20px    | 40px
    `<h3>`  | 19px    | 31px
    `<h4>`  | 18px    | 25px
    `<h5>`  | 17px    | 20px
    `<h6>`  | 16px    | 16px

    You can also adjust line height, margin top and margin bottom for each heading size by adding values in your <a href="sass.html#the-settings-file">Settings File</a>.

    In its most complete form the `$header-styles` map looks like this:

    ```
    $header-styles: (
      'small': (
        'h1': ('font-size': 24, 'line-height': $header-lineheight, 'margin-top': 0, 'margin-bottom': $header-margin-bottom),
        'h2': ('font-size': 20, 'line-height': $header-lineheight, 'margin-top': 0, 'margin-bottom': $header-margin-bottom),
        'h3': ('font-size': 19, 'line-height': $header-lineheight, 'margin-top': 0, 'margin-bottom': $header-margin-bottom),
        'h4': ('font-size': 18, 'line-height': $header-lineheight, 'margin-top': 0, 'margin-bottom': $header-margin-bottom),
        'h5': ('font-size': 17, 'line-height': $header-lineheight, 'margin-top': 0, 'margin-bottom': $header-margin-bottom),
        'h6': ('font-size': 16, 'line-height': $header-lineheight, 'margin-top': 0, 'margin-bottom': $header-margin-bottom)
      ),
      'medium': (
        'h1': ('font-size': 48, 'line-height': $header-lineheight, 'margin-top': 0, 'margin-bottom': $header-margin-bottom),
        'h2': ('font-size': 40, 'line-height': $header-lineheight, 'margin-top': 0, 'margin-bottom': $header-margin-bottom),
        'h3': ('font-size': 31, 'line-height': $header-lineheight, 'margin-top': 0, 'margin-bottom': $header-margin-bottom),
        'h4': ('font-size': 25, 'line-height': $header-lineheight, 'margin-top': 0, 'margin-bottom': $header-margin-bottom),
        'h5': ('font-size': 20, 'line-height': $header-lineheight, 'margin-top': 0, 'margin-bottom': $header-margin-bottom),
        'h6': ('font-size': 16, 'line-height': $header-lineheight, 'margin-top': 0, 'margin-bottom': $header-margin-bottom)
      ),
      ...
    );
    ```

    Because this is a little bit lengthy we have also introduced a short form, that you can use alternatively:

    ```
    $header-styles: (
      'small': (
        'h1': ('fs': 24, 'lh': $header-lineheight, 'mt': 0, 'mb': $header-margin-bottom),
        'h2': ('fs': 20, 'lh': $header-lineheight, 'mt': 0, 'mb': $header-margin-bottom),
        'h3': ('fs': 19, 'lh': $header-lineheight, 'mt': 0, 'mb': $header-margin-bottom),
        'h4': ('fs': 18, 'lh': $header-lineheight, 'mt': 0, 'mb': $header-margin-bottom),
        'h5': ('fs': 17, 'lh': $header-lineheight, 'mt': 0, 'mb': $header-margin-bottom),
        'h6': ('fs': 16, 'lh': $header-lineheight, 'mt': 0, 'mb': $header-margin-bottom)
      ),
      'medium': (
        'h1': ('fs': 48, 'lh': $header-lineheight, 'mt': 0, 'mb': $header-margin-bottom),
        'h2': ('fs': 40, 'lh': $header-lineheight, 'mt': 0, 'mb': $header-margin-bottom),
        'h3': ('fs': 31, 'lh': $header-lineheight, 'mt': 0, 'mb': $header-margin-bottom),
        'h4': ('fs': 25, 'lh': $header-lineheight, 'mt': 0, 'mb': $header-margin-bottom),
        'h5': ('fs': 20, 'lh': $header-lineheight, 'mt': 0, 'mb': $header-margin-bottom),
        'h6': ('fs': 16, 'lh': $header-lineheight, 'mt': 0, 'mb': $header-margin-bottom)
      ),
      ...
    );
    ```

    The values for `'font-size'`/`'fs'`, `'margin-top'`/`'mt'` and `'margin-bottom'`/`'mb'` are transformed into 'rem's. You can use any unit, but if you don't, we assume that you mean 'px'. If you do not set the keys `'font-size'`/`'fs'` defaults to `1rem`, `'margin-top'`/`'mt'` to `0` and `'margin-bottom'`/`'mb'` to `$header-margin-bottom` for size `'small'`. Thereafter the values for a larger size are inherited from the values of the smaller size if no value is entered for a larger breakpoint.

    The value for `'line-height'`/`'lh'` is transformed into a unitless number, that expresses the line-height relative to the fonts-size. You can also input any unit. If you don't, we assume that for numbers smaller than or equal to 10, you mean a typical relative line-height. However, if you put in anything larger than 10, we assume you mean 'px', since we have not yet seen relative line-heights that were larger than 10. If you do not set `'line-height'`/`'lh'` it defaults to `$header-lineheight` for size `'small'`. Thereafter the value for a larger size is inherited from the values of the smaller size.

    <div class="callout alert">
      <p><strong>The `$header-styles` map has replaced `$header-sizes` map in version 6.3. `$header-styles` map is a more general map than `$header-sizes`.</strong></p>
      <p>`$header-sizes` map is still working and is used to initialize the `$header-styles` map. In version 6.4 the `$header-sizes` is going to be deprecated.</p>
    </div>

    ---

    ### Small Header Segments

    By inserting a `<small>` element into a header Foundation will scale the header font size down for an inline element, allowing you to use this for subtitles or other secondary header text.

    <p>
      <a class="" data-open-video="2:46"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/eWrEEm" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <h3>Foundation for Sites <small>Version 6.6.1</small></h3>
    ```

    ---

    ## Links

    Links are very standard, and the color is preset to the Foundation primary color. <a href="global.html">Learn more about Foundation's global colors.</a>

    <a class="" data-open-video="3:22"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    <div class="callout">
      <p>To make links screen reader-friendly, avoid using vague words like "here" or "read more" within link text. The text of the link itself should adequately describe where the link goes.</p>
    </div>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/wdjqrY" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <p>Links are very standard, and the color is preset to the Foundation primary color. <a href="global.html">Learn more about Foundation's global colors.</a></p>
    ```

    ---

    ## Dividers

    Use dividers to define thematic breaks between paragraphs. To denote the end of one section of a page and the start of another, it's better to use the `<section>` tag.

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/Vbxzrz" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <hr>
    ```

    ---

    ## Unordered Lists

    Use an unordered list to... *list things*, if the order of the items doesn't matter.

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/mmLMXx" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul>
      <li>List item with a much longer description or more content.</li>
      <li>List item</li>
      <li>List item
        <ul>
          <li>Nested list item</li>
          <li>Nested list item</li>
          <li>Nested list item</li>
        </ul>
      </li>
      <li>List item</li>
      <li>List item</li>
      <li>List item</li>
    </ul>
    ```

    ---

    ## Ordered Lists

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/XRqaBd" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ol>
      <li>Cheese (essential)</li>
      <li>Pepperoni</li>
      <li>Bacon
        <ol>
          <li>Normal bacon</li>
          <li>Canadian bacon</li>
        </ol>
      </li>
      <li>Sausage</li>
      <li>Onions</li>
      <li>Mushrooms</li>
    </ol>
    ```

    ---

    ## Definition Lists

    A definition list (`<dl>`) is used to display name-value pairs, like metadata or a dictionary definition. Each term (`<dt>`) is paired with one or more definitions (`<dd>`).

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/oWdeMe" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <dl>
      <dt>Time</dt>
      <dd>The indefinite continued progress of existence and events in the past, present, and future regarded as a whole.</dd>
      <dt>Space</dt>
      <dd>A continuous area or expanse that is free, available, or unoccupied.</dd>
      <dd>The dimensions of height, depth, and width within which all things exist and move.</dd>
    </dl>
    ```

    ---

    ## Blockquotes

    Sometimes other people say smart things, and you may want to mention those things with a quote. We've got you covered.

    <div class="callout">
      By default, `<cite>` takes the look of the `.cite-block` component. In Sass, you can customize it with <a href="#sass-variables">`$cite-*` variables</a> or disable it by setting `$enable-cite-block` to false.
    </div>

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/ZKoJMb" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <blockquote>
      Those people who think they know everything are a great annoyance to those of us who do.
      <cite>Isaac Asimov</cite>
    </blockquote>
    ```

    ---

    ## Abbreviations

    Use the `<abbr>` tag to annotate a shortened term. Abbreviations must always have a `title` attribute which clarifies the full term.

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/jmpzNW?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <p>In my dream last night, I saw <abbr title="John Ronald Reuel">J. R. R.</abbr> Tolkien and George <abbr title="Raymond Richard">R. R.</abbr> Martin hanging out on Sunset <abbr title="Boulevard">Blvd</abbr>.</p>
    ```

    ---

    ## Code

    Format references to code with the `<code>` tag. In order for angle brackets `<>` to render correctly, you need to change them to `&lt; and &gt;`.

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/LymjvO" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    Remember to escape angle brackets when printing HTML: <code>&lt;div&gt;</code>
    ```

    ---

    Use `.code-inline` component to apply the code style when you want.

    ```html
    <span class="code-inline">I am not code, but I am displayed as if.</span>
    ```

    ---

    Use the `.code-block` component to create a block of code.

    ```html
    <code class="code-block">{
        "What I am": "I am a big chunk of code. I can have very long lines, I will not break and show a scrollbar instead.",
        ...
    }</code>
    ```

    <div class="callout info">
      <p>It is recommended to use the appropriate semantic markup for your content (`<code>` for code, `<pre>` for pre-formatted text). Styling classes `.code-inline` and `.code-block` should be used without semantic markup only if the content is NOT code/pre-formatted text but should be displayed as if.</p>
    </div>

    ---

    ## Keystrokes

    Use the `<kbd>` element to annotate a key stroke or combination.

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/GmBxRL?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <p>Press <kbd>Cmd+Q</kbd> (or <kbd>Ctrl+Q</kbd> on Windows) to play Half-Life 3.</p>
    ```

    ---

    ## Accessibility

    Text is core to the content of your page, so making it accessible to everyone is important. Here are some general guidelines to follow.

    ### Text vs. Images

    Prefer using actual text over text inside a graphic. Assistive technologies can't read an image, and the text in an image can't be resized by a browser, like normal text. If an image has text that needs to be read, add it in the `alt` attribute of the image.

    ```html
    <img src="assets/img/buy-now.jpg" alt="Buy now">
    ```

    ---

    ### Contrast

    The contrast between the color of an element's text and its background should be high enough that low-vision users can read it. **The minimum recommended contrast ratio is 4.5:1.** There are no automated tools that can effectively check this for you, but if you aren't sure about a specific color combination, you can run it through one of many color contrast checkers, such as [WebAIM's color contrast checker](https://webaim.org/resources/contrastchecker/).

    Google Chrome's [Accessibility Developer Tools](https://chrome.google.com/webstore/detail/accessibility-developer-t/fpkknkljclfencbdbgkenhalefipecmb?hl=en) also includes a contrast checker. By selecting an element in the inspector, you can see if the contrast meets the minimum standards.

    <img class="thumbnail" src="assets/img/a11y/chrome-a11y-inspector.jpg" alt="Screenshot of Google Chrome's Accessibility Tools">

    ---

    ### Type Size

    When possible, use the `rem` and `em` units to size everything. Not just font size, but also padding, margins, and any length value. This ensures that your design scales up and down uniformly if the user changes their browser's text size. It's common for vision-impaired users to resize their browser up to 200% zoom.

    We use the `rem` unit nearly everywhere in Foundation, and even wrote a Sass function to make it a little easier. The `rem-calc()` function can take one or more pixel values and convert them to proper `rem` values.

    ```scss
    .element {
      width: rem-calc(300);
      padding: rem-calc(10 16);
    }
    ```

    ---

    ### More Resources

    - [WebAIM: Fonts](https://webaim.org/techniques/fonts/)
    - [WebAIM: Links and HyperText](https://webaim.org/techniques/hypertext/)
    - [WebAIM: Writing Clearly and Simply](https://webaim.org/techniques/semanticstructure/)
    - [WebAIM: Color Contrast Checker](https://webaim.org/resources/contrastchecker/)

    ---

    ## Print Styles

    Foundation includes print styles developed by HTML5 Boilerplate to give you some basic print-specific styles. These are activated when you print through a media query. It includes:

    - Clearing out backgrounds, box shadows and text shadows
    - Appending link URLs after the anchor text
    - Adding borders to `<blockquote>` and `<pre>` elements
    - Page cleanup and window minimization

    On top of that, Foundation includes a couple of simple classes you can use to control elements printing, or not printing. Simply attach `.show-for-print` to an element to only show when printing, and `.hide-for-print` to hide something when printing.

    <a class="" data-open-video="4:42"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>

    <div class="callout primary">
      <p>Print styles use `!important` to ensure they aren't overridden by more specific selectors. This framework conscientiously avoids using `!important` declarations. This is one of the few components that does.</p>
    </div>"""

    pass


class TYPOGRAPHY_HELPERS:
    """---
    title: Typography Helpers
    description: Our helper classes allow you to scaffold certain typographic styles faster.
    video: dq7s3PVpQ7M
    sass:
      - scss/typography/_helpers.scss
      - scss/typography/_alignment.scss
    tags:
      - alignment
      - subheader
      - lead
      - statistic
    ---

    ## Text Alignment

    You can change the text alignment of an element by adding `.text-left`, `.text-right`, `.text-center` or `.text-justify` to an element.

    Adding a breakpoint to the front of a text alignment class will cause it to only be applied on that size screen or larger. For example, `.medium-text-center` will keep text left-aligned on the smallest screens, but switch to center-aligned on medium screens and larger.

    <p>
      <a class="" data-open-video="1:01"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/QvBQOe?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <p class="text-left"><!-- ... --></p>
    <p class="text-right"><!-- ... --></p>
    <p class="text-center"><!-- ... --></p>
    <p class="text-justify"><!-- ... --></p>
    ```

    <p class="text-left"><strong>This text is left-aligned.</strong> Set in the year 0 F.E. ("Foundation Era"), The Psychohistorians opens on Trantor, the capital of the 12,000-year-old Galactic Empire. Though the empire appears stable and powerful, it is slowly decaying in ways that parallel the decline of the Western Roman Empire.</p>

    <p class="text-right"><strong>This text is right-aligned.</strong> Set in the year 0 F.E. ("Foundation Era"), The Psychohistorians opens on Trantor, the capital of the 12,000-year-old Galactic Empire. Though the empire appears stable and powerful, it is slowly decaying in ways that parallel the decline of the Western Roman Empire.</p>

    <p class="text-center"><strong>This text is center-aligned.</strong> Set in the year 0 F.E. ("Foundation Era"), The Psychohistorians opens on Trantor, the capital of the 12,000-year-old Galactic Empire. Though the empire appears stable and powerful, it is slowly decaying in ways that parallel the decline of the Western Roman Empire.</p>

    <p class="text-justify"><strong>This text is justified.</strong> Set in the year 0 F.E. ("Foundation Era"), The Psychohistorians opens on Trantor, the capital of the 12,000-year-old Galactic Empire. Though the empire appears stable and powerful, it is slowly decaying in ways that parallel the decline of the Western Roman Empire.</p>

    ---

    ## Subheader

    Lighten up your headers by adding a class of `.subheader` to any header element.

    <p>
      <a class="" data-open-video="3:50"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/vmadjr?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <h1 class="subheader">h1.subheader</h1>
    <h2 class="subheader">h2.subheader</h2>
    <h3 class="subheader">h3.subheader</h3>
    <h4 class="subheader">h4.subheader</h4>
    <h5 class="subheader">h5.subheader</h5>
    <h6 class="subheader">h6.subheader</h6>
    ```

    ---

    ## Lead Paragraph

    A slightly-larger-than-normal block of text, useful for decks, blurbs, or other descriptive text.

    <p>
      <a class="" data-open-video="3:24"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/GmBQGY?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <p class="lead">What are your cats <em>really</em> dreaming about while they sleep?</p>
    ```

    ---

    ## Un-bulleted List

    In Foundation, the `<ul>` is a bulleted list and `<ol>` is a numbered list by default, but you can add the class `.no-bullet` to remove the bullets and numbers respectively.

    #### Unordered List

    <p>
      <a class="" data-open-video="5:18"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/wdxyxb?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <ul class="no-bullet">
      <li>List item with a much longer description or more content.</li>
      <li>List item</li>
      <li>List item
        <ul>
          <li>Nested list item</li>
          <li>Nested list item</li>
          <li>Nested list item</li>
        </ul>
      </li>
      <li>List item</li>
      <li>List item</li>
      <li>List item</li>
    </ul>
    ```

    #### Ordered List

    ```html
    <ol class="no-bullet">
      <li>List item with a much longer description or more content.</li>
      <li>List item</li>
      <li>List item
        <ol>
          <li>Nested list item</li>
          <li>Nested list item</li>
          <li>Nested list item</li>
        </ol>
      </li>
      <li>List item</li>
      <li>List item</li>
      <li>List item</li>
    </ol>
    ```

    ---

    ## Typescale

    Adjust font-size by overriding an element’s default size. This can be useful to size a `<p>` or `<h1>` through `<h6>` using Foundation's existing header sizes.

    <div class="callout primary">
      <p><strong>Especially useful because:</strong> It's important to avoid skipping heading levels when structuring your document, as it confuses screen readers. For example, after using an <code>&lt;h2&gt;</code> in your code, the next heading used should be either <code>&lt;h2&gt;</code> or <code>&lt;h3&gt;</code>. If you need a heading to look bigger or smaller to match a specific style, use CSS to override the default size.</p>
    </div>

    For headers:

    ```html
    <h2 class="h1">Lorem Ipsum Dolor</h2>
    <h3 class="h2">Lorem Ipsum Dolor</h3>
    <h4 class="h3">Lorem Ipsum Dolor</h4>
    <h5 class="h4">Lorem Ipsum Dolor</h5>
    <h6 class="h5">Lorem Ipsum Dolor</h6>
    ```

    For text:

    ```html
    <p class="h1">Lorem Ipsum Dolor</p>
    <p class="h2">Lorem Ipsum Dolor</p>
    <p class="h3">Lorem Ipsum Dolor</p>
    <p class="h4">Lorem Ipsum Dolor</p>
    <p class="h5">Lorem Ipsum Dolor</p>
    <p class="h6">Lorem Ipsum Dolor</p>
    ```

    ---

    ## Statistics

    If you're building a dashboard, you might need to display some important numbers *real big*. Just add the `.stat` class to any element to amp up the font size.

    <p>
      <a class="" data-open-video="4:38"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
      <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/XRBZxp?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <p>Days without merge conflict</p>
    <div class="stat">128</div>
    ```"""

    pass


class VISIBILITY:
    """---
    title: Visibility Classes
    description: Visibility classes let you show or hide elements based on screen size or device orientation. You can also use visibility classes to control which elements users see depending on their browsing environment.
    video: 'j__6VmFdSnc'
    sass: scss/components/_visibility.scss
    tags:
      - hide
      - show
    ---

    <div class="callout primary">
      <p>Visibility classes use `!important` to ensure they aren't overridden by more specific selectors. This framework conscientiously avoids using `!important` declarations. This is one of the few components that does.</p>
    </div>

    <div class="callout warning">
      <p>There are no classes to detect touchscreen devices, as both desktop and mobile browsers inconsistently report touch support. Learn more here: <a href="http://www.stucox.com/blog/you-cant-detect-a-touchscreen/">You Can't Detect a Touchscreen</a></p>
    </div>

    ## Show by Screen Size

    In this example, we use the `.show` visibility classes to show certain strings of text based on the device on which users view a page. If their browser meets the class's conditions, the element will be shown. If not, it will be hidden.

    ```html
    <p>You are on a small screen or larger.</p>
    <p class="show-for-medium">You are on a medium screen or larger.</p>
    <p class="show-for-large">You are on a large screen or larger.</p>
    ```

    These classes automatically hide the element on screen sizes *below* what's specified in the class. So `.show-for-medium` will hide the element on small, and show it on medium and larger.

    A separate set of classes allow you to show content *only* on a certain screen size. Just add `-only` to the end of the class.

    <div class="primary callout">
      <p>Don't see any text below the code sample? You must be on an *extra* large screen.</p>
    </div>

    ```html
    <p class="show-for-small-only">You are <em>definitely</em> on a small screen.</p>
    <p class="show-for-medium-only">You are <em>definitely</em> on a medium screen.</p>
    <p class="show-for-large-only">You are <em>definitely</em> on a large screen.</p>
    ```

    ---

    ## Hide by Screen Size

    This example shows the opposite: It uses the `.hide` visibility classes to state which elements should disappear based on the device's screen size.

    <div class="primary callout">
      <p>There's no <code>.hide-for-small</code> class, because that would just permanently hide the element. For that, you can use the plain old <code>.hide</code> class instead.</p>
    </div>

    ```html
    <p class="hide-for-medium">You are <em>not</em> on a medium screen or larger.</p>
    <p class="hide-for-large">You are <em>not</em> on a large screen or larger.</p>
    ```

    <p class="show-for-large">If you're reading this, you're on a large screen, and can't see either of the above examples.</p>

    Like with `.show`, these classes also have `-only` versions.

    ```html
    <p class="hide-for-small-only">You are <em>definitely not</em> on a small screen.</p>
    <p class="hide-for-medium-only">You are <em>definitely not</em> on a medium screen.</p>
    <p class="hide-for-large-only">You are <em>definitely not</em> on a large screen.</p>
    ```

    ### Generic Hide Classes

    And if you really just need something hidden no matter what, there are classes for that as well. The `.hide` and `.invisible` classes respectively set `display: none` and `visibility: hidden` on an element. Note that both of these classes hide content from screen readers.

    ```html
    <p class="hide">Can't touch this.</p>
    <p class="invisible">Can sort of touch this.</p>
    <p class="visible">You can see this.</p>
    ```

    ---

    ## Orientation Detection

    This straightforward example shows how two strings of text determine whether or not an element is visible in different orientations. This will change on mobile devices when you rotate the device. On desktop, the orientation is almost always reported as landscape.

    ```html
    <p class="show-for-landscape">You are in landscape orientation.</p>
    <p class="show-for-portrait">You are in portrait orientation.</p>
    ```

    ---

    ## Accessibility

    Adding `display: none` to an element will prevent screen readers from reading it. However, there are techniques to hide content while still making it readable by screen readers.

    ### Show for Screen Readers Only

    To visually hide content, while still allowing assistive technology to read it, add the class show-for-sr.

    ```html
    <p class="show-for-sr">This text can only be read by a screen reader.</p>
    <p>There's a line of text above this one, you just can't see it.</p>
    ```

    ### Hide for Screen Readers Only

    To hide text from assistive technology, while still keeping it visible, add the attribute `aria-hidden="true"`. This doesn't affect how the element looks, but screen readers will skip over it.

    <div class="primary callout">
      <p>It's usually not a good idea to hide content from screen readers. <code>aria-hidden</code> is best used to mask purely visual elements of a page.</p>
    </div>

    ```html
    <p aria-hidden="true">This text can be seen, but won't be read by a screen reader.</p>
    ```

    ### Creating Skip Links

    If your site has a lot of navigation, a screen reader will have to read through the entire navigation to get to your site's content. To remedy this, you can add a *skip link* at the very top of your page, which will send the user farther down the page, past the navigation when clicked on.

    Use the class `.show-on-focus` to hide an element, except when it has focus. Adding `tabindex="-1"` to the target element makes it focusable. (Or set it to `0` if the user should be able to tab to that element as well. See also [the MDN docs on `tabindex`](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex).)

    ```html
    <p><a class="show-on-focus" href="#mainContent">Skip to Content</a></p>

    <header id="header" role="banner">
    </header>

    <main id="mainContent" role="main" tabindex="0">
    </main>
    ```

    ### IE10+ Detection

    The demise of Internet Explorer cannot come soon enough. These classes will help you target all IE10+ browsers with the `show-for-ie` and `hide-for-ie` classes.

    ```html
    <p class="show-for-ie">Please get a new browser.</p>
    <p class="hide-for-ie">Thanks for not using Interner Explorer.</p>
    ```

    ### Dark Mode Detection

    Dark mode has become popular over the past couple of years. The `show-for-dark-mode` and `hide-for-dark-mode` classes will allow you to easily show and hide content when desinging for dark mode.

    ```html
    <p class="show-for-dark-mode">It's scary in the dark.</p>
    <p class="hide-for-dark-mode">You can see the light.</p>
    ```

    ### Sticky Mode Detection

    If you are using the [Sticky plugin](sticky.html) these classes could help you with showing and hiding elements when the Sticky component is stuck. The `show-for-sticky` and `hide-for-sticky` classes will allow you easily target these items inside of a sticky container.

    ```html
    <div data-sticky-container>
      <div class="sticky" data-sticky>
        <p class="hide-for-sticky">We be scrolling...</p>
        <p class="show-for-sticky">I'm going to rest here for a sec. You keep scrolling.</p>
      </div>
    </div>
    ```
    """

    pass


class XY_GRID:
    """---
    title: XY Grid
    description: A fully reworked new grid system in v6.4 which has all the variety inbuilt in the form of multiple grid types which includes margin grid, padding grid, frame grid, block grid and vertical grid.
    video: tjjVKGeoi3A
    sass: scss/xy-grid/*.scss
    ---

    <!-- <div class="callout training-callout">
      <p>The XY Grid is a huge advancement in Grids. Stay up-to-date with all the new features in Foundation 6.4 with our online webinar training. You’ll come away knowing the ins and outs of the XY Grid to create complex layouts faster and with less code. Not to mention all the useful UI components and Foundation JavaScript you’ll learn. You’ll make your coworkers jealous.</p>
      <a href="https://zurb.com/university/foundation-intro" target="_blank">Don’t miss out on the upcoming Foundation trainings →</a>
    </div> -->

    ## XY Grid Basics

    The XY grid works very similarly to the standard float grid, but includes a number of useful features only possible with Flexbox, like horizontal and vertical alignment, automatic sizing and a full vertical grid.

    ---

    ## Browser support

    The XY grid is supported in Chrome, Firefox, Safari 6+, IE11, iOS 7+, and Android 4.4+. Flexbox is supported in Android 2, but not reliably enough for use with this grid. ([View Flexbox browser support.](http://caniuse.com/#feat=flexbox)) We recommend only using the XY grid on projects that can live with purely cutting-edge browser support.

    ---

    ## Importing

    **XY grid is the default Foundation grid**. It is present by default in `foundation.css` of CDN link or package managers. In Sass, it will be generated by default by `@include foundation-everything` (unless `$flex` or `$xy-grid` are set to false).

    If `$xy-grid` is set to false, the flex grid is used.
    If `$flex` is set to false, the float grid is used instead.

    You can manually generate the XY Grid with:
    ```scss
    @import 'foundation';

    @include foundation-xy-grid-classes(
      /* options
      $base-grid: true,
      $margin-grid: true,
      $padding-grid: true,
      $block-grid: true,
      $collapse: true,
      $offset: true,
      $vertical-grid: true,
      $frame-grid: true
      */
    );
    ```

    ---

    ## Basics

    The structure of XY grid uses `.grid-x`, `.grid-y`, and `.cell` as its base. Without [defining a gutter type](#gutters) the cells will simply split up the space without any gutters.

    <p>
      <a class="" data-open-video="3:47"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/gRYeMQ?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x">
      <div class="cell">full width cell</div>
      <div class="cell">full width cell</div>
    </div>
    <div class="grid-x">
      <div class="cell small-6">6 cells</div>
      <div class="cell small-6">6 cells</div>
    </div>
    <div class="grid-x">
      <div class="cell medium-6 large-4">12/6/4 cells</div>
      <div class="cell medium-6 large-8">12/6/8 cells</div>
    </div>
    ```

    ---

    ## Gutters

    The defining feature of the XY grid is the ability to use margin AND padding grids in harmony.
    To define a grid type, simply set `.grid-margin-x`/`.grid-margin-y` or `.grid-padding-x`/`.grid-padding-y` on the grid.

    <p>
      <a class="" data-open-video="5:43"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/owvqYp?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-margin-x">
      <div class="cell medium-6 large-4">12/6/4 cells</div>
      <div class="cell medium-6 large-8">12/6/8 cells</div>
    </div>
    <div class="grid-x grid-padding-x">
      <div class="cell medium-6 large-4">12/6/4 cells</div>
      <div class="cell medium-6 large-8">12/6/8 cells</div>
    </div>
    ```
    ---

    ## Grid Container

    The grid defaults to the full width of the available space. To contain it horizontally use the `grid-container` class. The container will be centered and have a max-width equal to your `$grid-container` setting (1200px by default), along with padding on the left/right equal to half your `$grid-container-padding` setting.

    ```html
    <div class="grid-container">
      <div class="grid-x grid-margin-x">
        <div class="cell small-4">cell</div>
        <div class="cell small-4">cell</div>
        <div class="cell small-4">cell</div>
      </div>
    </div>
    ```
    ### Grid Container Fluid

    To stretch the content to the full width of the available space, simply add the class `fluid` to your `grid-container`.

    ```html
    <div class="grid-container fluid">
      <div class="grid-x grid-margin-x">
        <div class="cell small-4">cell</div>
        <div class="cell small-4">cell</div>
        <div class="cell small-4">cell</div>
      </div>
    </div>
    ```

    ### Grid Container Full

    To stretch the content to the full width of the available space and remove grid container padding, simply add the class `full` to your `grid-container`. Note that this variation is primarily for use for the `grid-margin-x` - it works with `grid-padding-x` too, but will work the same as `.grid-container.fluid`.

    <div class="callout alert">
      <p>Please note that when you are using `grid-margin-x` on a `grid-container` with `full` class you will also need to hide the horizontal overflow in order for this to work correctly if your content is going to touch the sides of the viewport.</p>
      <p>The best way to do this is:&nbsp; `body {overflow-x: hidden;}`</p>
    </div>

    ```html
    <div class="grid-container full">
      <div class="grid-x grid-margin-x">
        <div class="cell small-4">cell</div>
        <div class="cell small-4">cell</div>
        <div class="cell small-4">cell</div>
      </div>
    </div>
    ```
    ---

    ## Auto Sizing

    If the class `.auto` or `.[size]-auto` is added to the cell, it will take up the remaining space.

    ```html
    <div class="grid-x grid-margin-x">
      <div class="cell small-4">4 cells</div>
      <div class="cell auto">Whatever's left!</div>
    </div>
    ```

    ---

    Multiple expanding cells will share the leftover space equally.

    ```html
    <div class="grid-x grid-margin-x">
      <div class="cell small-4">4 cells</div>
      <div class="cell auto">Whatever's left!</div>
      <div class="cell auto">Whatever's left!</div>
    </div>
    ```

    ---

    A cell can also be made to *shrink*, by adding the `.shrink` or `.[size]-shrink` class. This means it will only take up the space its contents need.

    ```html
    <div class="grid-x grid-margin-x">
      <div class="cell shrink">Shrink!</div>
      <div class="cell auto">Expand!</div>
    </div>
    ```

    ---

    ## Responsive Adjustments

    To switch back to the auto behavior from a percentage or shrink behavior, use the classes `.[size]-auto` or `.[size]-shrink`. In the below example, the cells stack on small screens, and become even-width on large screens.

    ```html
    <div class="grid-x">
      <div class="cell large-auto">One</div>
      <div class="cell large-auto">Two</div>
      <div class="cell large-auto">Three</div>
      <div class="cell large-auto">Four</div>
      <div class="cell large-auto">Five</div>
      <div class="cell large-auto">Six</div>
    </div>
    ```

    ---

    ## Collapse Cells <span class="label secondary">X Grid only</span>

    The `.[size]-[gutter-type]-collapse` class lets you remove cell gutters.

    There are times when you won't want each media query to be collapsed. In this case, use the media query size you want and collapse and add that to your grid element. Example shows gutters at small and no gutters on medium and up.

    ```html
    <div class="grid-x grid-margin-x medium-margin-collapse">
      <div class="cell small-6">
        Gutters at small no gutters at medium.
      </div>
      <div class="cell small-6">
        Gutters at small no gutters at medium.
      </div>
    </div>
    ```

    ---

    ## Offsets <span class="label secondary">X Grid only</span>

    Offsets work by applying `margin-left` to a grid.

    ```html
    <div class="grid-x grid-margin-x">
      <div class="cell small-4 large-offset-2">Offset 2 on large</div>
      <div class="cell small-4">4 cells</div>
    </div>
    ```

    ---

    ## Block Grids <span class="label secondary">X Grid only</span>

    To define cell widths within a direction-level, instead of the individual cell level, add the class `.[size]-up-[n]` to a `grid-x`, where `[n]` is the number of cells to display per direction, and `[size]` is the breakpoint at which to apply the effect.

    <div class="callout primary">This example uses padding grid but this can be used with margin grid too.</div>

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/IamManchanda/pen/PjBLxE?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-x grid-padding-x small-up-2 medium-up-4 large-up-6">
      <div class="cell">cell</div>
      <div class="cell">cell</div>
      <div class="cell">cell</div>
      <div class="cell">cell</div>
      <div class="cell">cell</div>
      <div class="cell">cell</div>
    </div>
    ```

    Block Grids are not available for the vertical grids. Use the [basic layout](#vertical-grids) with a size applied on each cell of the grid instead.

    ---

    ## Looking for Push/Pull?

    Push and pull are a bit of a hack solution and was only necessary for Float based grids. But for flexbox, this hack is not needed as [source ordering](flexbox-utilities.html#source-ordering) does this with ease.

    ---

    ## Vertical Grids

    The XY grid also supports vertical grids. Simply apply `.grid-y` instead of `.grid-x`.
    The internal cells will shift automatically to provide spacing vertically rather than horizontally.

    You can also apply margin or padding with `.grid-margin-y` and `.grid-padding-y` to apply spacing to the top and bottom of cells.

    <p>
      <a class="" data-open-video="10:31"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="callout">
      <p>Please note for vertical grids to work, the grid needs a height. You can also use [grid frame](#grid-frame) to create a 100% viewport height vertical grid (or height:100%; if nested).</p>
    </div>


    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/JJPLYJ?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-y" style="height: 500px;">
      <div class="cell small-6 medium-8 large-2">
        6/8/2
      </div>
      <div class="cell small-6 medium-4 large-10">
        6/4/10
      </div>
    </div>
    ```

    ---

    ## Grid Frame

    The XY grid incorporates the grid frame from Foundation for Apps plus many other useful features.
    To start, add `.grid-frame` to the grid. This sets the grid to be 100vh (the full height of the browser window).

    <div class="callout warning">
      Please note that to use `.grid-margin-x` or `.grid-margin-y` with `.grid-frame` you need to hide the overflow on the body like so: `body {overflow: hidden;}`. However, take care not to unintentionally hide overflow body content on small screens when using `.medium-grid-frame`.
    </div>

    Here's an example of what you can do:

    <p>
      <a class="" data-open-video="12:09"><img src="{{root}}assets/img/icons/watch-video-icon.svg" class="video-icon" height="30" width="30" alt=""> Watch this part in video</a>
    </p>

    <div class="docs-codepen-container">
    <a class="codepen-logo-link" href="https://codepen.io/ZURBFoundation/pen/MogrXG?editors=1000" target="_blank"><img src="{{root}}assets/img/logos/edit-in-browser.svg" class="" height="" width="" alt="edit on codepen button"></a>
    </div>

    ```html
    <div class="grid-y medium-grid-frame">
      <div class="cell shrink header medium-cell-block-container">
        <h1>Grid Frame Header</h1>
        <div class="grid-x grid-padding-x">
          <div class="cell medium-4">
            A medium 4 cell
          </div>
          <div class="cell medium-4 medium-cell-block">
            <p style="width:80vw;">A medium 4 cell block... on medium this content should overflow and let you horizontally scroll across... one might use this for an array of options</p>
          </div>
          <div class="cell medium-4">
            A medium 4 cell
          </div>
        </div>
      </div>
      <div class="cell medium-auto medium-cell-block-container">
        <div class="grid-x grid-padding-x">
          <div class="cell medium-4 medium-cell-block-y">
            <h2>Independent scrolling sidebar</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer lacus odio, accumsan id ullamcorper eget, varius nec erat. Nulla facilisi. Donec dui felis, euismod nec finibus vitae, dapibus quis arcu. Maecenas tempor et ipsum quis venenatis. Ut posuere sed augue sit amet efficitur. Sed imperdiet, justo id tempus rhoncus, est est viverra turpis, non vulputate magna lectus et nisl. Pellentesque ultrices porttitor vehicula. Ut aliquet efficitur ligula, a consectetur felis. Proin tristique ut augue nec luctus. Curabitur a sapien pretium, auctor elit a, efficitur erat. Donec tincidunt dui vel velit bibendum euismod. Cras vitae nibh dui. Aliquam erat volutpat. Etiam sit amet arcu a erat efficitur facilisis. Ut viverra dapibus turpis, et ornare justo. Integer in dui cursus, dignissim tortor a, hendrerit risus.</p>

            <p>Suspendisse pulvinar, massa iaculis feugiat lobortis, dolor sapien vestibulum nulla, vel cursus tellus leo in lorem. Aliquam eu placerat urna. Suspendisse sed viverra orci, ut mattis neque. Fusce non ultrices nisi. In sagittis varius mollis. Quisque dolor quam, consectetur eu lacinia ac, ullamcorper vel arcu. Nullam mattis imperdiet nulla sed ornare. Praesent tristique, est id eleifend vestibulum, neque nibh condimentum ex, nec lobortis purus justo a libero. Phasellus id ex ac nunc hendrerit hendrerit. Nullam urna ipsum, rutrum at fringilla vel, venenatis non purus. Maecenas egestas ex vitae venenatis molestie. Ut et odio egestas, accumsan neque et, viverra nisl. Sed faucibus nec nulla sed imperdiet. Fusce quis sem ac urna semper tempor a id elit. Nulla fringilla vitae sapien a vehicula.</p>

          </div>
          <div class="cell medium-8 medium-cell-block-y">
            <h2>Independent scrolling body</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer lacus odio, accumsan id ullamcorper eget, varius nec erat. Nulla facilisi. Donec dui felis, euismod nec finibus vitae, dapibus quis arcu. Maecenas tempor et ipsum quis venenatis. Ut posuere sed augue sit amet efficitur. Sed imperdiet, justo id tempus rhoncus, est est viverra turpis, non vulputate magna lectus et nisl. Pellentesque ultrices porttitor vehicula. Ut aliquet efficitur ligula, a consectetur felis. Proin tristique ut augue nec luctus. Curabitur a sapien pretium, auctor elit a, efficitur erat. Donec tincidunt dui vel velit bibendum euismod. Cras vitae nibh dui. Aliquam erat volutpat. Etiam sit amet arcu a erat efficitur facilisis. Ut viverra dapibus turpis, et ornare justo. Integer in dui cursus, dignissim tortor a, hendrerit risus.</p>
            <p>Suspendisse pulvinar, massa iaculis feugiat lobortis, dolor sapien vestibulum nulla, vel cursus tellus leo in lorem. Aliquam eu placerat urna. Suspendisse sed viverra orci, ut mattis neque. Fusce non ultrices nisi. In sagittis varius mollis. Quisque dolor quam, consectetur eu lacinia ac, ullamcorper vel arcu. Nullam mattis imperdiet nulla sed ornare. Praesent tristique, est id eleifend vestibulum, neque nibh condimentum ex, nec lobortis purus justo a libero. Phasellus id ex ac nunc hendrerit hendrerit. Nullam urna ipsum, rutrum at fringilla vel, venenatis non purus. Maecenas egestas ex vitae venenatis molestie. Ut et odio egestas, accumsan neque et, viverra nisl. Sed faucibus nec nulla sed imperdiet. Fusce quis sem ac urna semper tempor a id elit. Nulla fringilla vitae sapien a vehicula.</p>
            <p>Nullam vestibulum lorem nec lectus egestas, nec ullamcorper diam maximus. Maecenas condimentum, nibh at blandit semper, ex erat tempus magna, id maximus neque velit accumsan nibh. Aenean dignissim lorem eu nisl laoreet vestibulum. Vivamus efficitur et augue vitae tincidunt. Etiam et magna felis. Integer mattis, nisi aliquet scelerisque blandit, ex mi sodales ante, eget accumsan quam magna et ligula. Curabitur id tristique leo. Proin rutrum mi vitae enim rhoncus, at cursus neque eleifend. Integer ultrices volutpat tellus ac porta. Fusce sollicitudin venenatis lacinia. Fusce ante lorem, gravida semper varius non, pharetra non erat. Sed dapibus arcu turpis, ac sollicitudin nibh lacinia vel. Nullam at enim porta, luctus metus sit amet, rutrum odio. Cras tempor enim vel pellentesque sollicitudin. Maecenas ullamcorper, sem non accumsan volutpat, neque tortor pulvinar orci, ut ultrices ligula lorem ut risus.</p>
            <p>Aliquam facilisis, nibh eget posuere suscipit, arcu sapien iaculis odio, in molestie dolor lectus vitae sem. Cras id nunc mollis mi rutrum dapibus. Quisque rutrum a augue at scelerisque. Praesent faucibus ac enim vitae gravida. Sed et sodales elit. Duis magna lectus, interdum sit amet metus a, sagittis varius magna. Proin nibh lectus, egestas a luctus ut, dapibus et enim. Curabitur fringilla ipsum vitae nunc imperdiet consectetur eget non neque. Suspendisse ultricies odio quis lorem vulputate, ac vulputate turpis feugiat. Maecenas posuere rhoncus orci, in ornare velit suscipit tempor. Curabitur pretium nisl id lorem placerat consequat. In quis quam eros. Nam mattis elit eu quam sagittis, in varius erat tempor.</p>
            <p>Fusce felis magna, pellentesque eget mollis a, rutrum id eros. Curabitur auctor varius arcu a consequat. Phasellus quis pulvinar enim, eu ultricies justo. Pellentesque risus libero, dapibus at erat ultricies, gravida varius erat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla tempus, justo ut laoreet mollis, nunc tellus convallis urna, vel pretium dui velit eget ligula. Aliquam semper sed nulla a molestie. Maecenas at egestas massa, vitae aliquam mi. Fusce nec sem egestas, pretium lacus non, tincidunt sapien. Sed tristique odio at ultricies vulputate. Integer et convallis augue, eu aliquam enim. Mauris ut faucibus diam. Donec vulputate nunc sed congue accumsan. Etiam lobortis nisi quis lacinia pharetra.</p>
          </div>
        </div>
      </div>
      <div class="cell shrink footer">
        <h3>Here's my footer</h3>
      </div>
    </div>
    ```

    ---

    ## Building Semantically

    XY grid CSS is generated with a powerful set of Sass mixins, which you can use in your own code to build a semantic grid.

    ### Grid Container

    Use the `xy-grid-container()` mixin to create a grid container. This contains the grid to the width specified in `$grid-container`.

    ```scss
    .container {
      @include xy-grid-container;
    }
    ```
    ---

    ### Grids

    Use the `xy-grid()` mixin to create a grid.

    ```scss
    .my-grid {
      @include xy-grid;
    }
    ```
    ---

    ### Gutters

    Use the `xy-gutters()` mixin to add gutters to an item. The `xy-cell` mixin used this to output gutters, but you can use this to add responsive gutters to anything you like.
    This is especially powerful as you can specify where you want the gutters, like so:

    ```scss
    .gallery-item {
      @include xy-gutters($gutter-position: left right bottom);
    }
    ```
    ---

    ### Cells

    Use the `xy-cell()` mixin to create a cell. There are a number of ways to define the size of a cell.
    `xy-cell` accepts a few different keywords as well as specific sizes: `full` (full width), `auto` (automatic width) and `shrink` (take up only the space it needs) or any fraction (`6`, `50%`, `1 of 2` or `1/2`...).

    ```scss
    .main-content {
      // Use the full column count (100%)
      @include xy-cell();

      // Use a column count (33%);
      @include xy-cell(4);

      // Use a percentage (15%)
      @include xy-cell(15%);

      // Use a custom fraction (20%)
      @include xy-cell(1 of 5);
    }
    ```

    The cell size calculator can also be accessed as a function. This gives you the percentage value, without any of the grid cell CSS.

    ```scss
    .main-content {
      width: xy-cell-size(1 of 7);
    }
    ```

    A cell is composed of 3 parts: the base, the size and the gutters. In order to avoid duplicating properties, you can choose the parts to generate with the `$output` option, or call the XY cell mixins dedicated to each part individually.

    ```scss
    .my-cell {
      @include xy-cell(12, $gutters: none);
    }
    .my-cell.half-size {
      @include xy-cell(6, $gutters: none, $output: (size));
      // Or @include xy-cell-size(6);
    }
    ```

    <div class="callout warn">
      XY cell with margin gutters (by default) has gutters defined within their width/height. For this reason, you need to generate the gutter part of cells with margin gutters even when you only want to change the size.
    </div>

    Refer to the Sass documentation of the [xy-cell](#xy-cell) mixin for the full list of arguments. See also [xy-cell-base](#xy-cell-base), [xy-cell-size](#xy-cell-size) and [xy-cellgutters](#xy-cellgutters).

    ---

    ### Responsive Grids

    Pair `xy-cell` with the `breakpoint()` mixin to make your grid responsive. The `xy-grid` mixin will automatically detect the breakpoint in which it is, but you can force it with the `$breakpoint` option.
    Refer to the Sass documentation below to learn how each mixin works and the available arguments.

    ```scss
    .my-cell-medium-only-8 {
      @include xy-cell();

      // Generate a cell with a 8/12 width on medium breakpoint only
      @include breakpoint(medium) {
        @include xy-cell(8);
      }
    }
    ```

    You can also use for more advanced responsive cells:

    ```scss
      // ... with a 8/12 width on medium breakpoint and above (with the medium gutters)
      @include breakpoint(medium up) {
        @include xy-cell(8);
      }
    ```

    ```scss
      // ... with a 8/12 width on medium, large and xlarge (with the corresponding gutters)
      @include breakpoint(medium, large, xlarge up) {
        @include xy-cell(8);
      }
    ```

    <div class="callout warning">
      If you pass multiple breakpoints to the <code>breakpoint</code> mixin, it will duplicate its content for each of them. Be careful to only use <code>breakpoint</code> with properties that should change across breakpoints.
    </div>

    ---

    ### Custom Block Grid

    Use the `xy-grid-layout()` mixin to create your own block grid.
    By default the mixin takes 2 parameters:
    - number of columns
    - child selector

    Refer to the Sass documentation [below](#xy-grid-layout) for the full list of arguments.

    Here's an example:

    ```scss
    .gallery {
      @include xy-grid;
      @include xy-grid-layout(3, '.gallery-item');
    }
    ```
    That outputs this CSS:

    ```
    .gallery > .gallery-item {
      width: calc(33.33333% - 1.25rem);
      margin-right: 0.625rem;
      margin-left: 0.625rem;
    }
    ```"""

    pass
