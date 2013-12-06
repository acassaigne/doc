*******
c sharp
*******

WPF
===

Problème pour tester le code retour ::

        if ( OpenDealFile.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                return OpenDealFile.FileName;
            }
            return "NoFile";



Quelques resources
==================

- http://dotnet.developpez.com/faq/csharp/?page=lang#lang_devtools
- http://dotnet.developpez.com/csharp/

Shortcut
========

- re-indent : Ctrl + K , Ctrl + E
- Supprimer ligne Ctrl-X

Snippet
=======

propfull --> génération de propriété

Norme de codage
===============

Variable privé a un sufiixe.


ComboBox
========

  //ComboBoxNumClient.Items.Add("CD2075 - Client 1");
            //ComboBoxNumClient.Items.Add("CC2254 - Client 2");
            //ComboBoxNumClient.Items.Add("CO2000 - Client 3");
            //ComboBoxNumClient.Items.Add("WCMI   - Client 4");
            //ComboBoxNumClient.Items.Add("CM2041 - Client 5");
            //ComboBoxNumClient.Items.Add("CC2251 - Client 6");
            //ComboBoxNumClient.Items.Add("SAMSAR - Client 7");
            //ComboBoxNumClient.Items.Add("CD2076 - Client 8");

Alerte

     System.Windows.Forms.MessageBox.Show("Vous devez selectionner un fichier !", "Alert selectionner fichier !",
                                                       MessageBoxButtons.OK,
                                                       MessageBoxIcon.Warning);

Send email via outlook
======================

Resource à étudier : http://social.msdn.microsoft.com/Forums/vstudio/en-US/3602242c-fc81-4ffd-917e-cf78cf34288e/link-email-address-and-send-email-via-outlook-in-wpf?forum=wpf
