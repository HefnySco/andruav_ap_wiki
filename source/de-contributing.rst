.. _de-contributing:

Contributing to the DroneEngage Wiki
====================================

Welcome to the DroneEngage Ardupilot Wiki! We encourage contributions to improve our documentation for DroneEngage, a cloud-based platform for Ardupilot drone operations. This guide explains how to contribute to the wiki, hosted at `https://github.com/DroneEngage/droneengage_ap_wiki <https://github.com/DroneEngage/droneengage_ap_wiki>`_.

The DroneEngage project includes repositories like `droneengage_communication <https://github.com/DroneEngage/droneengage_communication>`_, `droneengage_mavlink <https://github.com/DroneEngage/droneengage_mavlink>`_, `droneengage_camera <https://github.com/DroneEngage/droneengage_camera>`_, and `droneengage_webclient_react <https://github.com/DroneEngage/droneengage_webclient_react>`_. This wiki focuses on user and developer documentation, and your contributions help make it clearer and more comprehensive.

Overview
--------

You can contribute by:
- Fixing typos or improving clarity in existing pages (e.g., :ref:`de-getting-started`, :ref:`de-faq`).
- Adding new topics, such as tutorials or troubleshooting guides.
- Updating outdated content, like binary versions in :ref:`de-install-unit`.
- Suggesting improvements via `GitHub Issues <https://github.com/DroneEngage/droneengage_ap_wiki/issues>`_.

No contribution is too small! Whether you’re a drone enthusiast or a developer, your input is valuable.

Prerequisites
-------------

- **GitHub Account**: Create one at `https://github.com <https://github.com>`_.
- **Git**: Install Git on your computer (`https://git-scm.com/downloads <https://git-scm.com/downloads>`_).
- **Docker**: Install Docker to test changes locally (`https://docs.docker.com/get-docker/ <https://docs.docker.com/get-docker/>`_).
- **Text Editor**: Use any editor (e.g., VS Code, Notepad++) to edit reStructuredText (RST) files.
- **RST Knowledge**: Familiarity with RST syntax is helpful (see `RST Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_).

Contribution Steps
------------------

1. **Fork the Repository**:
   - Go to `https://github.com/DroneEngage/droneengage_ap_wiki <https://github.com/DroneEngage/droneengage_ap_wiki>`_.
   - Click **Fork** to create a copy under your GitHub account.

2. **Clone Your Fork**:
   - Run in your terminal:

     .. code-block:: bash

        $ git clone https://github.com/YOUR_USERNAME/droneengage_ap_wiki.git
        $ cd droneengage_ap_wiki

3. **Create a Branch**:
   - Create a new branch for your changes:

     .. code-block:: bash

        $ git checkout -b my-contribution

4. **Edit RST Files**:
   - Navigate to the `docs/` folder (or wherever RST files are stored).
   - Edit existing files (e.g., `de-faq.rst`, `de-install-unit.rst`) or create new ones.
   - Follow RST syntax and reference existing files for style (e.g., use :doc:`de-config-mavlink` for cross-links).
   - Example: To add a new FAQ, edit `de-faq.rst` and add a numbered entry.

5. **Test Changes Locally**:
   - Build the wiki using Docker:

     .. code-block:: bash

        $ ./docker.create.sh
        $ ./docker.run.sh

   - Output appears in the `./build` folder. Open the generated `index.html` in a browser to preview.
   - Ensure links (e.g., :doc:`glossary`) and formatting work correctly.

6. **Commit and Push**:
   - Commit your changes:

     .. code-block:: bash

        $ git add .
        $ git commit -m "Add new FAQ entry about camera setup"
        $ git push origin my-contribution

7. **Submit a Pull Request**:
   - Go to your fork on GitHub.
   - Click **Compare & pull request**.
   - Describe your changes clearly (e.g., “Updated FAQ with camera troubleshooting”).
   - Submit to the `main` branch of `DroneEngage/droneengage_ap_wiki`.

8. **Respond to Feedback**:
   - Maintainers may request changes. Update your branch and push new commits if needed.

Testing Changes
---------------

To ensure your changes render correctly:
- Run the Docker scripts to build the wiki (see :doc:`de-dev` for related build info).
- Check for broken links or formatting errors in the `./build` folder.
- If adding code blocks (e.g., JSON in :doc:`de-config-comm`), verify syntax.

Contribution Ideas
------------------

- **Fix Typos**: Improve clarity in pages like :doc:`de-what-is` or :doc:`de-config-mavlink`.
- **Add Tutorials**: Create guides for features like swarm operations (:ref:`de-advanced`) or SITL (:ref:`de-simulators`).
- **Update Binaries**: Keep installation instructions current (e.g., reference `https://cloud.ardupilot.org/downloads/RPI/Latest/ <https://cloud.ardupilot.org/downloads/RPI/Latest/>`_).
- **Expand FAQ**: Add questions to :ref:`de-faq` based on user feedback.

Contact
-------

For questions or ideas, open an issue at `https://github.com/DroneEngage/droneengage_ap_wiki/issues <https://github.com/DroneEngage/droneengage_ap_wiki/issues>`_ or email `team@ardupilot.org <mailto:team@ardupilot.org>`_. Join our community to help improve DroneEngage for everyone!