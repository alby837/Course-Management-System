function validateForm(){

    let name=document.getElementById("course_name").value;
    let code=document.getElementById("course_code").value;
    let duration=document.getElementById("duration").value;
    let fee=document.getElementById("fee").value;

    if(name=="" || code=="" || duration=="" || fee==""){
        alert("Please fill all the fields.");
        return false;
    }

    return true;
}