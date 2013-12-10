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


Switch
======

Syntaxe du switch ::

      Switch (value)
      {
      case 1: case 2: case 3:
          // Do Something
          break;
      case 4: case 5: case 6:
          // Do Something
          break;
      default:
          // Do Something
          break;
      }

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


Layout
======

Voir cette article
http://www.codeproject.com/Articles/30904/WPF-Layouts-A-Visual-Quick-Start


Textbox
=======

Ordre des controles avec la touche Tab : voir propriété TabIndex

Avoir le focus sur un controle donné ::

  FocusManager.FocusedElement="{Binding ElementName=ComboBoxIdOpe}

Plus exactement à utiliser au niveau du layout ::

  <Grid x:Name="Main" Margin="0,-7,0,7" FocusManager.FocusedElement="{Binding ElementName=ComboBoxIdOpe}">

Au niveau du fichier xaml


Send email via outlook
======================

Resource à étudier : http://social.msdn.microsoft.com/Forums/vstudio/en-US/3602242c-fc81-4ffd-917e-cf78cf34288e/link-email-address-and-send-email-via-outlook-in-wpf?forum=wpf


   private void FillDataGrid()
        {
            //this.Factory.

            DataTable table = new DataTable();
            SqlDataAdapter a = new SqlDataAdapter("SELECT * from job_deal", this.Factory.GetDbConnection());
            a.Fill(table);



            //this.DataGridListDeals. .DataContext = table;
        }


A lire sur le MVVM
http://msdn.microsoft.com/en-us/magazine/dd419663.aspx
