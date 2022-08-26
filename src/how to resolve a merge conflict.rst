===============================
How to Resolve a Merge Conflict
===============================

.. note::

   This article explains how to resolve merge conflicts by using Visual Studio Code. The instructions are designed for beginners.

A merge conflict occurs when you attempt to merge two branches, and they both contain changes in the same line of the same file.

When you create a pull request for such branches in the web interface, you will see a warning that this pull request cannot be merged because of the conflicts:

.. figure:: ../_static/bitbucket_PR.png

Finding the conflicting file
============================

.. important::

   In this article, we will use the following terms:
   
   *  **source branch**—the branch you want merge (for example, a user branch or a bugfix branch)

   *  **destination branch**—the branch you want to merge into (for example, the main branch)

To find out, which file is conflicting, go to your local repository and run the following commands::

   $ git checkout <source branch>
   $ git pull origin <destination branch>

You will get a message with the name of the conflicting file.

That can be a binary or a text file:

.. figure:: ../_static/conflict_in_binary.png

   Merge conflict in a binary file

.. figure:: ../_static/conflict_in_text.png

   Merge conflict in a text file

To resolve the conflict, perform the steps described in the following sections, depending on the type of the conflicting file.

Merge conflict in a binary file
===============================

*To resolve a merge conflict in a binary file:*

#. Copy the conflicting file to any location outside the repository.

   We will further refer to this copy as the **backup version**.

#. Run ``git status`` and copy the path to the conflicting file:

   .. figure:: ../_static/unmerged.png

#. Run the following command::

      git checkout --theirs -- <path to the conflicting file>

   For example:

   .. figure:: ../_static/checkout_theirs.png

   The file from the **destination branch** will be saved, and the file from the **source branch** will be ignored (but we will still have the backup version from step 1).

#. Run the following commands::

      $ git commit -m "Resolved merge conflict"
      $ git push origin HEAD

#. Open the pull request page in the web interface.

   The warning will disappear, and the pull request will become available for merge.

#. Merge the pull request.

#. Compare the file in repository with the backup version:

   *  If the backup version is newer, and you want to have it in the destination branch, replace the file, and then perform commit & push.

   *  If both files contain required changes, copy the changes from the backup version to the file in the repository, and then perform commit & push.

   *  If the backup version doesn't contain any required changes, do nothing.

Merge conflict in a text file
=============================

.. note::

   The following instructions are for Visual Studio Code with the `GitLens <https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens>`_ extension.

*To resolve a merge conflict in a text file:*

#. Open the conflicting file in Visual Studio Code.

   The conflicting lines will be highlighted:

   .. figure:: ../_static/conflict_lines.png

#. For each conflicting line, select one of the following options:

   *  Accept Current Change
   *  Accept Incoming Change
   *  Accept Both Changes

   .. figure:: ../_static/lines_select.png

#. Save the file (Ctrl+S).

#. Run the following commands::

      $ git add -A
      $ git commit -m "Resolved merge conflict"
      $ git push origin HEAD

#. Open the pull request page in the web interface.

   The warning will disappear, and the pull request will become available for merge.

#. Merge the pull request.
