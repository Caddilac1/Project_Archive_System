function showStudentFields() {
  // Show the student-specific fields
  document.getElementById('studentFields').style.display = 'block';

  // Add 'required' attributes to student fields
  document.getElementById("facultySelect").setAttribute("required", "required");
  document.getElementById("departmentSelect").setAttribute("required", "required");
  document.getElementById("courseSelect").setAttribute("required", "required");
  document.getElementById("indexNumber").setAttribute("required", "required");
}

function hideStudentFields() {
  // Hide the student-specific fields
  document.getElementById('studentFields').style.display = 'none';

  // Remove 'required' attributes from student fields
  document.getElementById("facultySelect").removeAttribute("required");
  document.getElementById("departmentSelect").removeAttribute("required");
  document.getElementById("courseSelect").removeAttribute("required");
  document.getElementById("indexNumber").removeAttribute("required");
}

document.getElementById("facultySelect").addEventListener("change", function () {
  var faculty = this.value;
  var departmentSelect = document.getElementById("departmentSelect");
  var courseSelect = document.getElementById("courseSelect");

  departmentSelect.innerHTML = '<option value="">- Select your department -</option>';
  courseSelect.innerHTML = '<option value="">- Select your course -</option>';

  var departments = {
    "FoE": [
      "Telecommunications Engineering Department",
      "Electrical and Electronics Engineering Department",
      "Mathematics and Statistics Department",
      "Department of Computer Engineering"
    ],
    "FoCIS": [
      "Computer Science Department",
      "Information Technology Department",
      "Information Systems Department",
      "Mobile and Pervasive Computing Department"
    ],
    "GCTU_Business": [
      "Management Studies Department",
      "Economic Department",
      "Marketing Department",
      "Procurement and Logistics Department",
      "Accounting, Banking and Finance Department"
    ]
  };

  if (departments[faculty]) {
    departments[faculty].forEach(function (department) {
      var option = document.createElement("option");
      option.value = department;
      option.textContent = department;
      departmentSelect.appendChild(option);
    });
  }
});

document.getElementById("departmentSelect").addEventListener("change", function () {
  var department = this.value;
  var courseSelect = document.getElementById("courseSelect");

  courseSelect.innerHTML = '<option value="">- Select your course -</option>';

  var courses = {
    "Telecommunications Engineering Department": [
      "BSc. Telecommunications Engineering",
      "Diploma in Telecommunications Engineering"
    ],
    "Electrical and Electronics Engineering Department": [
      "BSc. Electrical and Electronic Engineering"
    ],
    "Mathematics and Statistics Department": [
      "BSc. Mathematics"
    ],
    "Department of Computer Engineering": [
      "BSc. Computer Engineering"
    ],
    "Computer Science Department": [
      "BSc. Data Science and Analytics",
      "BSc. Computer Science",
      "BSc. Software Engineering",
      "BSc. Computer Science (Cyber Security)",
      "Diploma in Computer Science",
      "Diploma in Cyber Security",
      "Diploma in Data Science and Analytics"
    ],
    "Information Technology Department": [
      "BSc. Information Technology",
      "Diploma in Information Technology"
    ],
    "Information Systems Department": [
      "BSc. Information Systems"
    ],
    "Mobile and Pervasive Computing Department": [
      "BSc. Mobile Computing",
      "Diploma in Web Application Development",
      "Diploma in Multimedia Technology"
    ],
    "Management Studies Department": [
      "Diploma in Public Relations",
      "MBA Management Studies"
    ],
    "Economic Department": [
      "BSc. Economics"
    ],
    "Marketing Department": [
      "BBA Marketing",
      "MBA Marketing"
    ],
    "Procurement and Logistics Department": [
      "BSc. Procurement and Logistics"
    ],
    "Accounting, Banking and Finance Department": [
      "BSc. Accounting and Computing",
      "BSc. Business Administration (Accounting Option)",
      "BSc. Business Administration (Banking and Finance Option)",
      "BSc. Business Administration (Management Option)",
      "BSc. Business Administration (HRM Option)",
      "BSc. Business Administration (Marketing Option)",
      "Diploma in Business Administration (Marketing Option)",
      "Diploma in Business Administration (Management Option)"
    ]
  };

  if (courses[department]) {
    courses[department].forEach(function (course) {
      var option = document.createElement("option");
      option.value = course;
      option.textContent = course;
      courseSelect.appendChild(option);
    });
  }
});

// Event listeners for user type selection
document.getElementById("student").addEventListener("click", showStudentFields);
document.getElementById("lecturer").addEventListener("click", hideStudentFields);
document.getElementById("researcher").addEventListener("click", hideStudentFields);



