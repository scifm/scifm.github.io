---
layout: default
title: Get Involved
permalink: /get-involved/
---

<div class="row">
  <div class="col-md-8 mb-5">
    <h1>Get Involved</h1>
    <p class="lead">Join the SciFM community shaping the future of scientific discovery.</p>
    <p>Join our mailing lists and community — fill out the form below. You can update the fields and processing later (e.g., wire to Mailchimp or a server endpoint).</p>

    <!-- Placeholder signup form: update `action` to your form processor later -->
    <form id="getInvolvedForm" action="#" method="post" novalidate>
      <div class="mb-3">
        <label for="firstName" class="form-label">First name <span class="text-muted">(required)</span></label>
        <input type="text" class="form-control" id="firstName" name="firstName" required autocomplete="given-name" aria-describedby="firstNameHelp">
        <div class="invalid-feedback">Please provide your first name.</div>
      </div>

      <div class="mb-3">
        <label for="lastName" class="form-label">Last name <span class="text-muted">(required)</span></label>
        <input type="text" class="form-control" id="lastName" name="lastName" required autocomplete="family-name" aria-describedby="lastNameHelp">
        <div class="invalid-feedback">Please provide your last name.</div>
      </div>

      <div class="mb-3">
        <label for="email" class="form-label">Email address <span class="text-muted">(required)</span></label>
        <input type="email" class="form-control" id="email" name="email" required autocomplete="email" aria-describedby="emailHelp">
        <div class="invalid-feedback">Please provide a valid email address.</div>
      </div>

      <div class="mb-3">
        <label for="org" class="form-label">Organization</label>
        <input type="text" class="form-control" id="org" name="organization" autocomplete="organization" aria-describedby="orgHelp">
      </div>

      <fieldset class="mb-3">
        <legend class="col-form-label pt-0">Role (select one)</legend>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="role" id="roleStudent" value="student" checked>
          <label class="form-check-label" for="roleStudent">Student</label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="role" id="roleFaculty" value="faculty">
          <label class="form-check-label" for="roleFaculty">Faculty</label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="role" id="roleIndustry" value="industry">
          <label class="form-check-label" for="roleIndustry">Industry</label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="role" id="roleOther" value="other">
          <label class="form-check-label" for="roleOther">Other</label>
        </div>
      </fieldset>

      <div class="mb-3 form-check">
        <input type="checkbox" class="form-check-input" id="consent" name="consent" required>
        <label class="form-check-label" for="consent">I agree to receive emails from SciFM about events and news.</label>
        <div class="invalid-feedback">You must agree to receive emails to join.</div>
      </div>

      <button type="submit" class="btn btn-primary" id="submitBtn">Sign Up</button>
    </form>

    <div id="successMessage" class="alert alert-success mt-4" role="status" style="display:none;">
      <h4 class="alert-heading">Thanks—you’re in!</h4>
      <p>We've received your sign-up. Check your email for a confirmation message.</p>
    </div>

    <script>
      // Client-side validation + success replacement
      (function() {
        var form = document.getElementById('getInvolvedForm');
        var success = document.getElementById('successMessage');
        form.addEventListener('submit', function(event) {
          event.preventDefault();
          event.stopPropagation();
          var valid = true;
          // use built-in validity checks
          if (!form.checkValidity()) valid = false;
          // show/hide browser validation UI via classes
          var elements = form.querySelectorAll('input,select');
          elements.forEach(function(el){
            if (!el.checkValidity()) {
              el.classList.add('is-invalid');
            } else {
              el.classList.remove('is-invalid');
              el.classList.add('is-valid');
            }
          });
          if (!valid) return;
          // Simulate a successful submit — replace form with success message
          form.style.display = 'none';
          success.style.display = 'block';
          // TODO: actually post data to your form handler here
        }, false);
      })();
    </script>
  </div>

  <div class="col-md-4 mb-5">
    <!-- Sidebar will still render here by the layout include -->
    <h3>Questions?</h3>
    <p>Email <a href="mailto:micde-contact@umich.edu">micde-contact@umich.edu</a></p>
    <p><a href="/contact/">Contact page</a></p>
  </div>
</div>
