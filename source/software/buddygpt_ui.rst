User Interface
==============

Chat Interface
--------------

Model Selection
~~~~~~~~~~~~~~~

The chat interface allows you to select from a list of available models to interface with. This list includes both base models available to all users as well as any custom models you have created (covered below).

You may also select multiple models to compare the output for any prompt. In this case, your prompt will be sent to all selected models and the results displayed side-by-side.

If there are additional open-source models you would like to use that are not available in the drop-down, please send a request to hpc@uco.edu. We are able to provide access to most open-source models.

.. image:: /_static/img/buddygpt_ui_model_selection.PNG
   :width: 50%
   :align: center
   :alt: BuddyGPT model selection interface

Sending a Message
~~~~~~~~~~~~~~~~~

Sending a prompt is as simple as adding text into the message bar. By clicking the microphone or headset buttons you can also use a speech-to-text service or have a "call" with the model where you can speak and the model will speak back.

You can also add a document to give the model specific context to respond to the prompt with. If you would like this context to be persisted, upload it to documents or add it to a custom model as discussed below. To add an existing document that was previously uploaded into the document interface to the context of a chat, use '#' and then the name of the document before entering your prompt.

When you get a model response, you can take various actions including editing, copying, or reading the response out loud, and view statistics about the generation with the options available at the bottom of the response.

.. image:: /_static/img/buddygpt_ui_chat.PNG
   :width: 75%
   :align: center
   :alt: BuddyGPT chat interface with message

Other Controls
~~~~~~~~~~~~~~

From the top right of the screen, you can access various controls which enable you to tweak the parameters and system prompt for the chat. To persist this information, use a custom model. From these options you are also able to download chats and change other settings related to the UI.

On the left of the screen you can create new chats, access your chat history, and access the workspace where you can upload documents and create custom models.

.. image:: /_static/img/buddygpt_ui_other_controls.PNG
   :width: 50%
   :align: center
   :alt: BuddyGPT controls menu

Workspace
---------

From the workspace you can upload documents and create models with RAG functionality.

Documents
~~~~~~~~~

In the documents tab, use the '+' button to upload documents. Select documents using the upload functionality then add it to a collection if you wish by specifying a name. The collection can be used to create different groupings of documents, for example to create custom RAGs focusing on different tasks. Documents will not be shared across users, but please do not upload documents with sensitive information or that are subject to regulations.

.. warning::
   Do not upload documents containing sensitive, proprietary, or regulated data (HIPAA, Export Controlled, SSNs, biometric data, etc.).

.. image:: /_static/img/buddygpt_ui_chat_documents_upload.PNG
   :width: 50%
   :align: center
   :alt: Documents upload and collection interface

Models
~~~~~~

To create a custom model, navigate to the Models tab in the workspace and click "New model".

From here, you can customize a model by specifying the base model, system prompt, and any context documents or collections of documents, among other customizations. Documents/collections must be uploaded in the document tab before they will be accessible here. Once the model has been created it will show up in the model list in the chat interface.

.. image:: /_static/img/buddygpt_ui_model_selection.PNG
   :width: 50%
   :align: center
   :alt: Workspace model selection in Models tab
