
function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}


function move_selected( from, to )
{
  // Get the Select Elements
  var s = document.getElementById(from);
  var t = document.getElementById(to);

  // Put the selected elements in an array
  var opt = [];
  var to_be_deleted = [];
  var j = 0;
  var i = 0;
  for( i=0;i<s.options.length;i++)
  {
    if( s.options[i].selected == true )
    {
      // Copy Value+TEXT for moving
      opt[ s.options[i].value ]  =  s.options[i].text;

      // Store the Index, for Deletion
      to_be_deleted[j] = i;
      j++;
    }
  }

  // Delete the selected Option from Source select element
  for( i=0;i<to_be_deleted.length;i++)
   s.options.remove( to_be_deleted[i] );

  // Iterate thorough all Saved option Value+Text
  // and Insert Into the Target Select element
  for( var key in opt )
  {
    // Create new Option
    var no = new Option( opt[key], key );

    // Insert
    t.options[ t.options.length ] = no;
  }

  // SORT the Target Select Element
  select_elem_sort(to);
}

function validateForm() {
  let x = document.forms["myForm"]["fname"].value;
  if (x == "") {
    alert("Name must be filled out");
    return false;
  }
}

// Move ALL Items from one to other SelectBox
function move_all( from, to )
{
  // Get the Select Elements
  var s = document.getElementById(from);
  var t = document.getElementById(to);

  // ITERATE Source Element's Option List
  var i = 0;
  for( i=0;i<s.options.length;i++)
  {
      // Create new Option
      var no = new Option( s.options[i].text, s.options[i].value );

      // Insert
      t.options[ t.options.length ] = no;
  }

  // Delete All options from source Element
  s.options.length = 0;

  // SORT the Target Select Element
  select_elem_sort(to);
}

// This is for sorting the Option List
function select_elem_sort(t)
{

    // Get the TARGET Select element
    var s = document.getElementById(t);

    // Iterate through its options and create
    // a reference array with option VALUE:TEXT
    var opt_reference = [];
    var opt_text_arry = [];

    // Our copying starts from Index 0
    for( var i=0; i<s.options.length; i++)
    {
       // Store Option value and text to reference array
       opt_reference [ s.options[i].value ] = s.options[i].text ;

       // Store only the TEXT to the second array for sorting
       opt_text_arry[i] = s.options[i].text;
    }

    // Sort the Array Ascending
    opt_text_arry.sort( function(a, b) {
        if(a>b) return 1;
        if(a<b) return -1;
        return 0;
    } );

    var i=0;
    /// Iterate the array and Re-create options
    for(i=0; i<opt_text_arry.length; i++ )
    {
      var option_text = opt_text_arry[i];

      /// FETCH the corresponding option value
      /// against the option text
      var option_val = "";
      for( var key in opt_reference)
      {
         // Option Text matched
         if( opt_reference[key] == option_text )
         {
           option_val = key;
           break;
         }

      }

      // Create the new Option
      var opt = new Option( option_text, option_val);

      // Put the new option in the Options Array
      // of Select element. We are re-creating
      // new options from index 0 onwards
      s.options[i] = opt;
    }
}
