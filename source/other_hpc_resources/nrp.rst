.. _nrp-access:

.. |namespace| replace:: <NAMESPACE>

==========================================
Accessing the National Research Platform
==========================================

.. note::

   **Audience:** UCO researchers, faculty, and students who need GPU or
   container-based compute beyond what Buddy provides.

   **Last reviewed:** <DATE>. Verify links against the `NRP documentation
   <https://nrp.ai/documentation>`__ before publishing.

.. contents:: On this page
   :local:
   :depth: 2


What NRP is, and when to use it
===============================

The **National Research Platform (NRP)** is an NSF-funded, community-owned
computing platform shared across 50+ institutions. **Nautilus** is the
Kubernetes cluster the NRP runs on — it is the name you will see in the
documentation and in the tooling itself. It is free to use for non-profit
research and education.

UCO has its own namespace on Nautilus: |namespace|. A namespace is an isolated
space in the cluster where your pods run and your data lives.

NRP vs. Buddy
-------------

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Use Buddy when…
     - Use NRP when…
   * - Your work fits a Slurm batch job
     - You need containers, or a long-lived web service
   * - You need our installed module stack (EasyBuild/Lmod)
     - You need GPUs we don't have locally, or more of them
   * - You need traditional MPI across nodes
     - Your workflow is already Docker/Kubernetes-shaped
   * - Your data must stay on UCO-managed storage
     - Your data is non-sensitive and portable

.. warning::

   **They are not interchangeable.** NRP has no Slurm, no shared ``/home`` with
   Buddy, and no UCO-managed backups. Treat anything you put there as
   reproducible-from-scratch.


Step 1 — Log in to create your account
======================================

You must do this **before** we can add you to the namespace. There is no way for
us to create an account on your behalf — your identity has to exist in the
portal first.

#. Go to `nrp.ai <https://nrp.ai>`__ and click **Log In** (top right).

#. You are redirected to **CILogon**, where you select an **Identity Provider**.
   **Select** ``Microsoft``. UCO is not listed individually in the CILogon
   dropdown — do not scroll looking for it. UCO accounts authenticate through
   Microsoft.

#. At the Microsoft prompt, sign in with your **UCO email address** and your
   normal UCO password. Use your ``@uco.edu`` address, not a personal Google,
   GitHub, or other account — we can only match you to the UCO namespace by
   your UCO identity.

#. Complete the login. Your account is created automatically with **guest**
   status.

.. important::

   **Guests cannot run anything.** This is expected. You are not done yet.


Step 2 — Request namespace membership
=====================================

Email **hpc@uco.edu** with:

* Confirmation that you have completed the portal login in Step 1, and the
  **UCO email address** you logged in with (this is how we find your account)
* Your department and, if you're a student, your faculty supervisor
* A one-line description of what you plan to run

We add you to |namespace|, which promotes your account from **guest** to
**user**. You'll get a reply when it's done.


Step 3 — Confirm and accept the policies
========================================

#. Log back in to `nrp.ai <https://nrp.ai>`__ and open the `Namespaces manager
   <https://nrp.ai/namespaces>`__. Namespaces you belong to are shown in bold.

#. Read and accept the `NRP Acceptable Use Policy
   <https://nrp.ai/NRP-AUP.pdf>`__.

#. Read the `Cluster Policies
   <https://nrp.ai/documentation/userdocs/start/policies/>`__.

#. **Join the Nautilus Support chat.** All NRP users are expected to join it —
   it is the primary support channel and where outage notices appear.
   Registration instructions are at `nrp.ai/contact
   <https://nrp.ai/contact>`__.


Step 4 — Start working
======================

Option A: Hosted JupyterHub
---------------------------

**Recommended starting point.** No Kubernetes knowledge required. This is where
most people should begin.

#. Go to `jupyterhub-west.nrp-nautilus.io
   <https://jupyterhub-west.nrp-nautilus.io>`__.
#. Log in with CILogon — again choosing ``Microsoft`` and your UCO email
   address.
#. Choose your hardware specs (CPU/RAM/GPU) on the spawn page.
#. Work in Jupyter as normal.

Things to know
^^^^^^^^^^^^^^

* Your persistent home folder starts at **5 GB**. Larger allocations can be
  requested.
* **Your container shuts down one hour after your browser disconnects.**
  Closing the laptop lid, sleeping the machine, or losing Wi-Fi will end your
  session. Do not use JupyterHub for long unattended runs — use a batch Job
  instead (Option B).
* Available images are listed in the `science images documentation
  <https://nrp.ai/documentation/userdocs/running/sci-img/>`__.

Option B: ``kubectl`` from your own machine
-------------------------------------------

Needed for batch jobs, long-running work, persistent storage, and anything that
has to survive a browser closing.

NRP maintains the authoritative setup instructions, and they change as the
cluster's authentication stack changes. **Follow their documentation directly
rather than any copy of it** — a stale copy is worse than no copy:

.. admonition:: Start here
   :class: tip

   `NRP — Getting access to Nautilus
   <https://nrp.ai/documentation/userdocs/start/getting-started/>`__

That page walks through the full sequence:

#. Install the ``kubectl`` command-line tool.
#. Install the **kubelogin** plugin — this is mandatory; without it your config
   file will not authenticate.
#. Download your cluster config file (the **Download Config File** button on
   that page) and save it as ``config``, with no file extension, in a ``.kube``
   folder in your home directory.
#. Select the ``nautilus`` context and authenticate through CILogon.
#. Verify you can see your namespace.

The same page has a cross-platform troubleshooting section covering the usual
first-run failures: WSL browser launch problems, headless/SSH sessions with no
local browser, port binding conflicts, and keyring errors.

**Video walkthroughs** of the ``kubectl`` and ``kubelogin`` install are
published by NRP alongside their `training materials
<https://github.com/nrp-nautilus/NRP-Winter2026-Training>`__.

**Then work through the tutorial** before writing your own manifests:
`NRP basic tutorial
<https://nrp.ai/documentation/userdocs/tutorial/basic/>`__.

Two things to know going in
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* When you check your namespace and get ``No resources found``, that is a
  **success** message. It means you can see the namespace and nothing is
  running in it yet.
* Access tokens expire after about half an hour and renew automatically. **If
  you set up** ``kubectl`` **before we added you to the namespace**, your
  cached token still says "guest" and you'll be denied. The Getting Started
  page above documents how to invalidate the cached token so the next command
  re-authenticates with your new permissions — or you can simply wait out the
  half hour.

If you get stuck on setup, the **Nautilus Support** chat is the right place to
ask. UCO HPC can confirm your namespace membership, but we don't maintain the
NRP client tooling and can't debug your local ``kubectl`` install for you.


Rules that will get your access revoked
=======================================

Read these before you run anything.

* **Containers are stateless.** Everything not written to a persistent volume
  is gone when the container restarts — and restarts are normal, not a fault.
* **Never run a Job whose command never exits.** A ``sleep`` loop or equivalent
  used to hold a pod open is grounds for being banned from the cluster.
* **Never force-delete pods.**
* **Do not store protected data.** NRP storage is not approved for FERPA,
  HIPAA, PII, or other regulated data.


Getting help
============

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Issue
     - Where to go
   * - Namespace membership, UCO account questions
     - **hpc@uco.edu**
   * - Cluster problems, pods stuck, GPU availability
     - Nautilus Support chat — `nrp.ai/contact <https://nrp.ai/contact>`__
   * - Learning Kubernetes
     - `NRP basic tutorial
       <https://nrp.ai/documentation/userdocs/tutorial/basic/>`__
   * - General NRP documentation
     - `nrp.ai/documentation <https://nrp.ai/documentation/>`__

When you post to Nautilus Support, include your **namespace name**, the **pod
name**, and the smallest YAML that reproduces the problem. That gets a useful
answer far faster.

NRP is a community-supported platform run by a small NSF-funded team. It is
largely self-service, and the expectation is learn-by-doing. UCO HPC can help
with access and with deciding whether NRP or Buddy is the right fit, but we do
not operate the cluster and cannot fix problems inside it.
