*******
c sharp
*******

Visual Studio Shortcut
======================

http://www.shortcutworld.com/en/win/Visual-Studio_2010.html#link_2
http://msdn.microsoft.com/en-us/library/bb531266(v=vs.90).aspx

mode colonne : shift + alt + fleche up/down
ajouter bookmark : ctlr+k ctrl+k
supprimer bookmark : ctrl+k ctrl+k


WPF
===

Problème pour tester le code retour ::

        if ( OpenDealFile.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                return OpenDealFile.FileName;
            }
            return "NoFile";



CSV
===

http://www.codeproject.com/Questions/450672/Import-CSV-File-into-DataGrid-using-DataTable-WPF

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



Curseur
=======

Changer le curseur pour patienter lors d'une opération longue ::

   Mouse.OverrideCursor = System.Windows.Input.Cursors.Wait;
   Mouse.OverrideCursor = System.Windows.Input.Cursors.Arrow;

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

méthode et parametre outlook
============================

Exemple de méthode ::

 public void GetResultAfterSimulation(long IdJobDeal, out int CountColisPrives, out int CountRejets, out int CountDoublon)
        {

            SqlCommand scCommand = new SqlCommand("dbo.get_info_rejets_nb_colis_doublon", this.DbConnection);
            scCommand.CommandType = System.Data.CommandType.StoredProcedure;
            scCommand.Parameters.AddWithValue("@pl_id_job_deal", IdJobDeal);
            scCommand.Parameters.AddWithValue("@pb_Traitement", realTraitement);
            scCommand.Parameters.AddWithValue("@pl_NumClient", NumClient);
            scCommand.Parameters.AddWithValue("@pl_Dossier", NameClient);
            scCommand.Parameters.AddWithValue("@pi_ProdTransp", CodeTransporteur);
            scCommand.Parameters.AddWithValue("@ps_NumDossier", LibelleOpe);
            scCommand.Parameters.AddWithValue("@pi_IdExpe", IdExpediteur);
            scCommand.Parameters.AddWithValue("@ps_NomFic1", Filename);
            scCommand.ExecuteNonQuery();
        }


Documenter une méthode
----------------------

Exemple ::

        /// <summary>
        /// Description de la méthode
        /// </summary>
        /// <param name="Param1">Description du parametre 1</param>
        /// <param name="Param2">Description du parametre 2</param>
        /// <returns>Explication valeur retournée</returns>
        public Boolean MaMethode(Param1, Param2)
        {
        ...
        }

.NET & WPF
==========

App.config et dictionnaire
--------------------------

Par exemple nous avons cette section
-------------------------------------
exemple de configuration ::

    <?xml version="1.0" encoding="utf-8"?>
    <configuration>
      <configSections>
        <section
          name="CodeProduitTransporteur"
          type="System.Configuration.DictionarySectionHandler" />
        <section
         name="CodeAdresseRetour"
         type="System.Configuration.DictionarySectionHandler" />
      </configSections>
      ...
    <CodeProduitTransporteur>
      <add key="A" value="35"/>
      <add key="N" value="38"/>
    </CodeProduitTransporteur>

Le code charger le dictionnaire ::

   tmpHashtable = (Hashtable)ConfigurationManager.GetSection("CodeProduitTransporteur");
   DictCodeProduitTransporteur = tmpHashtable.Cast<DictionaryEntry>().ToDictionary(d => (string)d.Key, d => (string)d.Value);

Ajouter un clé de configuration à l'application
-----------------------------------------------

exemple de fichier app.config ::

  <appSettings>
    <add key="DirectoryInputFiles" value="R:\Tmp\TestChargement\anthony" />
    <add key="DirectoryOutputFile" value="R:\Tmp\TestChargement\anthony\output" />
    <add key="NumberOfDotInReportFile" value="35" />
    <add key="CsvSeparator" value=";"></add>
    <add key="CsvIndexColumnStatistics" value="10"></add>
    <add key="ClientSettingsProvider.ServiceUri" value="" />
  </appSettings>

Le code pour lire le parametre dans le fichier de config ::

   this.InputDirectoryFiles = ConfigurationManager.AppSettings["DirectoryInputFiles"];

Generer un identifiant unique
-----------------------------

Il convient d'utiliser la méthode ::

   System.Guid.NewGuid()

Voir ici http://stackoverflow.com/questions/8477664/how-can-i-generate-uuid-in-c-sharp

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

Vérifier encodage d'un fichier
==============================

http://encodingchecker.codeplex.com/