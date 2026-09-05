/* =====================================================
   STUDENT MANAGEMENT SYSTEM
   Main JavaScript File
===================================================== */


/* =====================================================
   SAMPLE DATA
===================================================== */

const data = {

    /* ================= STUDENTS ================= */

    students: [

        {
            id: "ST-1001",
            name: "Ali Rezaei",
            email: "ali.rezaei@example.com",
            dept: "Computer Science",
            year: "3rd Year",
            status: "Active"
        },

        {
            id: "ST-1002",
            name: "Sara Ahmadi",
            email: "sara.ahmadi@example.com",
            dept: "Software Engineering",
            year: "2nd Year",
            status: "Active"
        },

        {
            id: "ST-1003",
            name: "Hossein Karimi",
            email: "hossein.karimi@example.com",
            dept: "Artificial Intelligence",
            year: "4th Year",
            status: "Inactive"
        },

        {
            id: "ST-1004",
            name: "Zahra Moradi",
            email: "zahra.moradi@example.com",
            dept: "Data Science",
            year: "3rd Year",
            status: "Active"
        },

        {
            id: "ST-1005",
            name: "Reza Hassani",
            email: "reza.hassani@example.com",
            dept: "Computer Science",
            year: "1st Year",
            status: "Active"
        }

    ],


    /* ================= PROFESSORS ================= */

    professors: [

        {
            id: "PR-201",
            name: "Dr. Mohammad Smith",
            email: "m.smith@university.edu",
            dept: "Computer Science",
            courses: 5,
            status: "Active"
        },

        {
            id: "PR-202",
            name: "Dr. Sarah Johnson",
            email: "s.johnson@university.edu",
            dept: "Software Engineering",
            courses: 4,
            status: "Active"
        },

        {
            id: "PR-203",
            name: "Dr. David Brown",
            email: "d.brown@university.edu",
            dept: "Artificial Intelligence",
            courses: 6,
            status: "Active"
        },

        {
            id: "PR-204",
            name: "Dr. Mary Wilson",
            email: "m.wilson@university.edu",
            dept: "Mathematics",
            courses: 3,
            status: "On Leave"
        }

    ],


    /* ================= COURSES ================= */

    courses: [

        {
            id: "CS101",
            name: "Introduction to Programming",
            dept: "Computer Science",
            prof: "Dr. Smith",
            credits: 3,
            students: 82,
            status: "Active"
        },

        {
            id: "CS202",
            name: "Data Structures",
            dept: "Computer Science",
            prof: "Dr. Smith",
            credits: 3,
            students: 74,
            status: "Active"
        },

        {
            id: "CS305",
            name: "Database Systems",
            dept: "Software Engineering",
            prof: "Dr. Johnson",
            credits: 3,
            students: 68,
            status: "Active"
        },

        {
            id: "AI401",
            name: "Artificial Intelligence",
            dept: "Artificial Intelligence",
            prof: "Dr. Brown",
            credits: 3,
            students: 54,
            status: "Active"
        },

        {
            id: "OS310",
            name: "Operating Systems",
            dept: "Computer Science",
            prof: "Dr. Smith",
            credits: 3,
            students: 61,
            status: "Active"
        }

    ],


    /* ================= ENROLLMENTS ================= */

    enrollments: [

        {
            id: "EN-5001",
            student: "Ali Rezaei",
            course: "Data Structures",
            term: "Fall 2026",
            date: "2026-09-01",
            status: "Active"
        },

        {
            id: "EN-5002",
            student: "Sara Ahmadi",
            course: "Database Systems",
            term: "Fall 2026",
            date: "2026-09-01",
            status: "Active"
        },

        {
            id: "EN-5003",
            student: "Zahra Moradi",
            course: "Artificial Intelligence",
            term: "Fall 2026",
            date: "2026-09-02",
            status: "Pending"
        },

        {
            id: "EN-5004",
            student: "Reza Hassani",
            course: "Operating Systems",
            term: "Fall 2026",
            date: "2026-09-02",
            status: "Active"
        }

    ],


    /* ================= GRADES ================= */

    grades: [

        {
            student: "Ali Rezaei",
            course: "Data Structures",
            score: 18.5,
            grade: "A",
            semester: "Fall 2026"
        },

        {
            student: "Sara Ahmadi",
            course: "Database Systems",
            score: 17,
            grade: "A-",
            semester: "Fall 2026"
        },

        {
            student: "Zahra Moradi",
            course: "Artificial Intelligence",
            score: 19,
            grade: "A+",
            semester: "Fall 2026"
        },

        {
            student: "Reza Hassani",
            course: "Operating Systems",
            score: 15.5,
            grade: "B+",
            semester: "Fall 2026"
        }

    ],


    /* ================= USERS ================= */

    users: [

        {
            id: "U-001",
            name: "Asma Mirzaei",
            email: "asma@example.com",
            role: "Administrator",
            status: "Active"
        },

        {
            id: "U-002",
            name: "Dr. Mohammad Smith",
            email: "m.smith@university.edu",
            role: "Professor",
            status: "Active"
        },

        {
            id: "U-003",
            name: "Ali Rezaei",
            email: "ali.rezaei@example.com",
            role: "Student",
            status: "Active"
        }

    ]

};


/* =====================================================
   PAGE INFORMATION
===================================================== */

const meta = {

    dashboard: [
        "Dashboard",
        "Overview of your university system"
    ],

    students: [
        "Students",
        "Manage student records and academic information"
    ],

    professors: [
        "Professors",
        "Manage professors and teaching assignments"
    ],

    courses: [
        "Courses",
        "Manage courses, credits and instructors"
    ],

    enrollments: [
        "Enrollments",
        "Register students in university courses"
    ],

    grades: [
        "Grades",
        "Manage academic grades and student performance"
    ],

    users: [
        "Users",
        "Manage system users and permissions"
    ],

    reports: [
        "Reports",
        "Analytics and academic reports"
    ],

    settings: [
        "Settings",
        "Configure your student management system"
    ]

};


/* =====================================================
   UPDATE HEADER
===================================================== */

function setHeader(page) {

    document.getElementById("pageTitle").textContent =
        meta[page][0];

    document.getElementById("pageSubtitle").textContent =
        meta[page][1];


    document
        .querySelectorAll(".nav")
        .forEach(function (item) {

            item.classList.toggle(
                "active",
                item.dataset.page === page
            );

        });

}


/* =====================================================
   HTML ESCAPE
===================================================== */

function esc(value) {

    return String(value).replace(
        /[&<>"']/g,

        function (character) {

            const entities = {

                "&": "&amp;",
                "<": "&lt;",
                ">": "&gt;",
                '"': "&quot;",
                "'": "&#039;"

            };

            return entities[character];

        }
    );

}


/* =====================================================
   STATUS BADGE
===================================================== */

function badge(status) {

    let className = "inactive";


    if (status === "Active") {

        className = "active";

    }

    else if (status === "Pending") {

        className = "pending";

    }


    return `
        <span class="badge ${className}">
            ${esc(status)}
        </span>
    `;

}


/* =====================================================
   ACTION BUTTONS
===================================================== */

function actionBtns(type, id) {

    return `

        <div class="actions">

            <button
                onclick="viewItem('${type}', '${esc(id)}')"
            >
                View
            </button>


            <button
                onclick="openForm('${type}', '${esc(id)}')"
            >
                Edit
            </button>


            <button
                onclick="deleteItem('${type}', '${esc(id)}')"
            >
                Delete
            </button>

        </div>

    `;

}


/* =====================================================
   GENERATE TABLE PAGE
===================================================== */

function tablePage(
    type,
    title,
    headers,
    rows,
    buttonLabel
) {

    return `

        <div class="card table-card">

            <div class="card-head">

                <h2>
                    ${title}
                </h2>


                <div class="toolbar">

                    <input
                        type="text"
                        placeholder="Search ${title.toLowerCase()}..."
                        oninput="filterTable(this)"
                    >


                    <button
                        class="btn"
                        onclick="openForm('${type}')"
                    >
                        + ${buttonLabel}
                    </button>

                </div>

            </div>


            <table>

                <thead>

                    <tr>

                        ${headers
                            .map(function (header) {

                                return `
                                    <th>
                                        ${header}
                                    </th>
                                `;

                            })
                            .join("")
                        }

                    </tr>

                </thead>


                <tbody id="dataTable">

                    ${rows}

                </tbody>

            </table>

        </div>

    `;

}


/* =====================================================
   DASHBOARD
===================================================== */

function dashboard() {

    return `

        <!-- STATISTICS -->

        <div class="grid stats">


            <div class="stat">

                <div class="stat-icon purple">
                    👥
                </div>

                <div>

                    <h2>
                        1,248
                    </h2>

                    <p>
                        Total Students
                    </p>

                    <span class="up">
                        ↑ 12.5%
                        <span class="muted">
                            from last month
                        </span>
                    </span>

                </div>

            </div>


            <div class="stat">

                <div class="stat-icon blue">
                    👨‍🏫
                </div>

                <div>

                    <h2>
                        98
                    </h2>

                    <p>
                        Total Professors
                    </p>

                    <span class="up">
                        ↑ 8.3%
                        <span class="muted">
                            from last month
                        </span>
                    </span>

                </div>

            </div>


            <div class="stat">

                <div class="stat-icon green">
                    📚
                </div>

                <div>

                    <h2>
                        156
                    </h2>

                    <p>
                        Total Courses
                    </p>

                    <span class="up">
                        ↑ 15.2%
                        <span class="muted">
                            from last month
                        </span>
                    </span>

                </div>

            </div>


            <div class="stat">

                <div class="stat-icon orange">
                    📝
                </div>

                <div>

                    <h2>
                        2,450
                    </h2>

                    <p>
                        Total Enrollments
                    </p>

                    <span class="up">
                        ↑ 10.1%
                        <span class="muted">
                            from last month
                        </span>
                    </span>

                </div>

            </div>

        </div>


        <!-- MIDDLE SECTION -->

        <div class="grid two">


            <!-- Enrollment Chart -->

            <div class="card">

                <div class="card-head">

                    <h2>
                        Enrollments Overview
                    </h2>

                    <select class="select">

                        <option>
                            This Semester
                        </option>

                        <option>
                            Last Semester
                        </option>

                    </select>

                </div>


                <div class="chart">

                    ${[
                        38,
                        46,
                        65,
                        62,
                        55,
                        74,
                        92,
                        67,
                        52,
                        71,
                        58,
                        79
                    ]
                        .map(function (height, index) {

                            return `

                                <div class="bar-group">

                                    <div
                                        class="bar ${
                                            index % 3 === 0
                                                ? "alt"
                                                : ""
                                        }"
                                        style="height:${height}%"
                                    >
                                    </div>

                                </div>

                            `;

                        })
                        .join("")
                    }

                </div>


                <div class="months">

                    <span>Sep</span>
                    <span>Oct</span>
                    <span>Nov</span>
                    <span>Dec</span>
                    <span>Jan</span>
                    <span>Feb</span>

                </div>

            </div>


            <!-- Recent Activities -->

            <div class="card">

                <div class="card-head">

                    <h2>
                        Recent Activities
                    </h2>

                </div>


                ${[
                    [
                        "➕",
                        "New student registered",
                        "Ali Rezaei",
                        "10 min ago",
                        "purple"
                    ],

                    [
                        "✉",
                        "Course “Data Structures” updated",
                        "Dr. Smith",
                        "1 hour ago",
                        "blue"
                    ],

                    [
                        "✓",
                        "New enrollment",
                        "Sara Ahmadi in Database Course",
                        "2 hours ago",
                        "green"
                    ],

                    [
                        "★",
                        "Grade submitted",
                        "Math Course - 25 Students",
                        "3 hours ago",
                        "orange"
                    ],

                    [
                        "👤",
                        "New professor joined",
                        "Dr. Johnson",
                        "5 hours ago",
                        "purple"
                    ]

                ]
                    .map(function (activity) {

                        return `

                            <div class="activity">

                                <div
                                    class="activity-icon ${activity[4]}"
                                >
                                    ${activity[0]}
                                </div>


                                <div class="body">

                                    <b>
                                        ${activity[1]}
                                    </b>

                                    <p>
                                        ${activity[2]}
                                    </p>

                                </div>


                                <time>
                                    ${activity[3]}
                                </time>

                            </div>

                        `;

                    })
                    .join("")
                }

            </div>

        </div>


        <!-- BOTTOM SECTION -->

        <div class="grid three">


            <!-- Recent Students -->

            <div class="card">

                <div class="card-head">

                    <h2>
                        Recent Students
                    </h2>

                    <button
                        class="btn secondary"
                        onclick="navigate('students')"
                    >
                        View all
                    </button>

                </div>


                <table>

                    <thead>

                        <tr>

                            <th>
                                ID
                            </th>

                            <th>
                                Name
                            </th>

                            <th>
                                Department
                            </th>

                            <th>
                                Status
                            </th>

                        </tr>

                    </thead>


                    <tbody>

                        ${data.students
                            .slice(0, 5)
                            .map(function (student) {

                                return `

                                    <tr>

                                        <td>
                                            ${student.id}
                                        </td>

                                        <td>
                                            <strong>
                                                ${student.name}
                                            </strong>
                                        </td>

                                        <td>
                                            ${student.dept}
                                        </td>

                                        <td>
                                            ${badge(student.status)}
                                        </td>

                                    </tr>

                                `;

                            })
                            .join("")
                        }

                    </tbody>

                </table>

            </div>


            <!-- Top Courses -->

            <div class="card">

                <div class="card-head">

                    <h2>
                        Top Courses
                    </h2>

                </div>


                <div
                    style="
                        display:flex;
                        align-items:center;
                        gap:25px;
                    "
                >

                    <div
                        style="
                            width:145px;
                            height:145px;
                            border-radius:50%;
                            background:
                            conic-gradient(
                                #7564f5 0 25%,
                                #62a4f5 25% 45%,
                                #51c982 45% 63%,
                                #f5ad45 63% 78%,
                                #d9dce5 78%
                            );
                        "
                    >
                    </div>


                    <div
                        style="
                            font-size:10px;
                            line-height:2.5;
                        "
                    >

                        🟣 Data Structures 25%

                        <br>

                        🔵 Database Systems 20%

                        <br>

                        🟢 Algorithms 18%

                        <br>

                        🟠 Operating Systems 15%

                        <br>

                        ⚪ Others 22%

                    </div>

                </div>

            </div>

        </div>

    `;

}


/* =====================================================
   STUDENTS PAGE
===================================================== */

function students() {

    const rows = data.students
        .map(function (student) {

            return `

                <tr>

                    <td>
                        ${student.id}
                    </td>

                    <td>
                        <strong>
                            ${student.name}
                        </strong>
                    </td>

                    <td>
                        ${student.email}
                    </td>

                    <td>
                        ${student.dept}
                    </td>

                    <td>
                        ${student.year}
                    </td>

                    <td>
                        ${badge(student.status)}
                    </td>

                    <td>
                        ${actionBtns(
                            "student",
                            student.id
                        )}
                    </td>

                </tr>

            `;

        })
        .join("");


    return tablePage(
        "student",
        "All Students",

        [
            "ID",
            "Name",
            "Email",
            "Department",
            "Year",
            "Status",
            "Actions"
        ],

        rows,

        "Add Student"
    );

}


/* =====================================================
   PROFESSORS PAGE
===================================================== */

function professors() {

    const rows = data.professors
        .map(function (professor) {

            return `

                <tr>

                    <td>
                        ${professor.id}
                    </td>

                    <td>
                        <strong>
                            ${professor.name}
                        </strong>
                    </td>

                    <td>
                        ${professor.email}
                    </td>

                    <td>
                        ${professor.dept}
                    </td>

                    <td>
                        ${professor.courses}
                    </td>

                    <td>
                        ${badge(professor.status)}
                    </td>

                    <td>
                        ${actionBtns(
                            "professor",
                            professor.id
                        )}
                    </td>

                </tr>

            `;

        })
        .join("");


    return tablePage(
        "professor",
        "All Professors",

        [
            "ID",
            "Name",
            "Email",
            "Department",
            "Courses",
            "Status",
            "Actions"
        ],

        rows,

        "Add Professor"
    );

}


/* =====================================================
   COURSES PAGE
===================================================== */

function courses() {

    const rows = data.courses
        .map(function (course) {

            return `

                <tr>

                    <td>
                        ${course.id}
                    </td>

                    <td>
                        <strong>
                            ${course.name}
                        </strong>
                    </td>

                    <td>
                        ${course.dept}
                    </td>

                    <td>
                        ${course.prof}
                    </td>

                    <td>
                        ${course.credits}
                    </td>

                    <td>
                        ${course.students}
                    </td>

                    <td>
                        ${badge(course.status)}
                    </td>

                    <td>
                        ${actionBtns(
                            "course",
                            course.id
                        )}
                    </td>

                </tr>

            `;

        })
        .join("");


    return tablePage(
        "course",
        "All Courses",

        [
            "Code",
            "Course Name",
            "Department",
            "Professor",
            "Credits",
            "Students",
            "Status",
            "Actions"
        ],

        rows,

        "Add Course"
    );

}


/* =====================================================
   ENROLLMENTS PAGE
===================================================== */

function enrollments() {

    const rows = data.enrollments
        .map(function (enrollment) {

            return `

                <tr>

                    <td>
                        ${enrollment.id}
                    </td>

                    <td>
                        ${enrollment.student}
                    </td>

                    <td>
                        ${enrollment.course}
                    </td>

                    <td>
                        ${enrollment.term}
                    </td>

                    <td>
                        ${enrollment.date}
                    </td>

                    <td>
                        ${badge(enrollment.status)}
                    </td>

                    <td>
                        ${actionBtns(
                            "enrollment",
                            enrollment.id
                        )}
                    </td>

                </tr>

            `;

        })
        .join("");


    return tablePage(
        "enrollment",
        "Course Enrollments",

        [
            "ID",
            "Student",
            "Course",
            "Term",
            "Date",
            "Status",
            "Actions"
        ],

        rows,

        "New Enrollment"
    );

}


/* =====================================================
   GRADES PAGE
===================================================== */

function grades() {

    const rows = data.grades
        .map(function (grade) {

            return `

                <tr>

                    <td>
                        ${grade.student}
                    </td>

                    <td>
                        ${grade.course}
                    </td>

                    <td>
                        ${grade.semester}
                    </td>

                    <td>
                        <strong>
                            ${grade.score}
                        </strong>
                    </td>

                    <td>
                        ${grade.grade}
                    </td>

                    <td>
                        ${actionBtns(
                            "grade",
                            grade.student
                        )}
                    </td>

                </tr>

            `;

        })
        .join("");


    return tablePage(
        "grade",
        "Student Grades",

        [
            "Student",
            "Course",
            "Semester",
            "Score",
            "Grade",
            "Actions"
        ],

        rows,

        "Add Grade"
    );

}


/* =====================================================
   USERS PAGE
===================================================== */

function users() {

    const rows = data.users
        .map(function (user) {

            return `

                <tr>

                    <td>
                        ${user.id}
                    </td>

                    <td>
                        <strong>
                            ${user.name}
                        </strong>
                    </td>

                    <td>
                        ${user.email}
                    </td>

                    <td>
                        ${user.role}
                    </td>

                    <td>
                        ${badge(user.status)}
                    </td>

                    <td>
                        ${actionBtns(
                            "user",
                            user.id
                        )}
                    </td>

                </tr>

            `;

        })
        .join("");


    return tablePage(
        "user",
        "System Users",

        [
            "ID",
            "Name",
            "Email",
            "Role",
            "Status",
            "Actions"
        ],

        rows,

        "Add User"
    );

}


/* =====================================================
   REPORTS PAGE
===================================================== */

function reports() {

    return `

        <div class="grid kpis">


            <div class="kpi">

                <b>
                    94.2%
                </b>

                <p>
                    Average Attendance
                </p>

            </div>


            <div class="kpi">

                <b>
                    87.6%
                </b>

                <p>
                    Pass Rate
                </p>

            </div>


            <div class="kpi">

                <b>
                    3.42
                </b>

                <p>
                    Average GPA
                </p>

            </div>

        </div>


        <div class="grid two">


            <div class="card">

                <div class="card-head">

                    <h2>
                        Academic Performance
                    </h2>

                    <button class="btn secondary">
                        Export PDF
                    </button>

                </div>


                <div class="chart">

                    ${[
                        55,
                        63,
                        72,
                        68,
                        81,
                        76,
                        90,
                        84
                    ]
                        .map(function (height) {

                            return `

                                <div class="bar-group">

                                    <div
                                        class="bar"
                                        style="
                                            height:${height}%
                                        "
                                    >
                                    </div>

                                </div>

                            `;

                        })
                        .join("")
                    }

                </div>

            </div>


            <div class="card">

                <div class="card-head">

                    <h2>
                        Report Center
                    </h2>

                </div>


                ${[
                    "Student performance report",
                    "Course enrollment report",
                    "Professor workload report",
                    "Grade distribution report",
                    "Attendance report"
                ]
                    .map(function (report) {

                        return `

                            <div class="setting-row">

                                <div>

                                    <b>
                                        ${report}
                                    </b>

                                    <p>
                                        Generate detailed report
                                    </p>

                                </div>


                                <button class="btn secondary">
                                    Generate
                                </button>

                            </div>

                        `;

                    })
                    .join("")
                }

            </div>

        </div>

    `;

}


/* =====================================================
   SETTINGS PAGE
===================================================== */

function settings() {

    return `

        <div class="settings">


            <div class="card settings-menu">

                <div class="item active">
                    General
                </div>

                <div class="item">
                    Appearance
                </div>

                <div class="item">
                    Notifications
                </div>

                <div class="item">
                    Security
                </div>

                <div class="item">
                    Backup
                </div>

            </div>


            <div class="card">

                <div class="card-head">

                    <h2>
                        General Settings
                    </h2>

                    <button class="btn">
                        Save Changes
                    </button>

                </div>


                <div class="setting-row">

                    <div>

                        <b>
                            University Name
                        </b>

                        <p>
                            The name displayed throughout the application.
                        </p>

                    </div>

                    <input
                        value="Student Management System"
                        style="
                            width:260px;
                            height:36px;
                            border:1px solid var(--border);
                            border-radius:8px;
                            padding:0 10px;
                            font-size:11px;
                        "
                    >

                </div>


                <div class="setting-row">

                    <div>

                        <b>
                            Academic Year
                        </b>

                        <p>
                            Current academic year.
                        </p>

                    </div>

                    <input
                        value="2026-2027"
                        style="
                            width:260px;
                            height:36px;
                            border:1px solid var(--border);
                            border-radius:8px;
                            padding:0 10px;
                            font-size:11px;
                        "
                    >

                </div>


                <div class="setting-row">

                    <div>

                        <b>
                            Default Language
                        </b>

                        <p>
                            Interface language.
                        </p>

                    </div>

                    <input
                        value="English"
                        style="
                            width:260px;
                            height:36px;
                            border:1px solid var(--border);
                            border-radius:8px;
                            padding:0 10px;
                            font-size:11px;
                        "
                    >

                </div>


                <div class="setting-row">

                    <div>

                        <b>
                            Email Notifications
                        </b>

                        <p>
                            Receive important system notifications.
                        </p>

                    </div>

                    <div class="switch on"></div>

                </div>

            </div>

        </div>

    `;

}


/* =====================================================
   FORM MODAL
===================================================== */

function openForm(type, id) {

    const fields = {

        student: [
            ["name", "Full Name"],
            ["email", "Email"],
            ["dept", "Department"],
            ["year", "Year"]
        ],

        professor: [
            ["name", "Full Name"],
            ["email", "Email"],
            ["dept", "Department"]
        ],

        course: [
            ["id", "Course Code"],
            ["name", "Course Name"],
            ["dept", "Department"],
            ["prof", "Professor"],
            ["credits", "Credits"]
        ],

        enrollment: [
            ["student", "Student"],
            ["course", "Course"],
            ["term", "Term"],
            ["date", "Date"]
        ],

        grade: [
            ["student", "Student"],
            ["course", "Course"],
            ["score", "Score"],
            ["grade", "Grade"]
        ],

        user: [
            ["name", "Full Name"],
            ["email", "Email"],
            ["role", "Role"]
        ]

    }[type] || [];


    document.getElementById("modalRoot").innerHTML = `

        <div
            class="modal-backdrop"
            onclick="
                if(event.target === this)
                    closeModal()
            "
        >

            <div class="modal">

                <h2>
                    ${id ? "Edit" : "Add"} ${type}
                </h2>


                <div class="form-grid">

                    ${fields
                        .map(function (field) {

                            return `

                                <div class="field">

                                    <label>
                                        ${field[1]}
                                    </label>

                                    <input
                                        id="f_${field[0]}"
                                        placeholder="${field[1]}"
                                    >

                                </div>

                            `;

                        })
                        .join("")
                    }

                </div>


                <div class="modal-actions">

                    <button
                        class="btn secondary"
                        onclick="closeModal()"
                    >
                        Cancel
                    </button>


                    <button
                        class="btn"
                        onclick="
                            saveForm(
                                '${type}',
                                '${id || ""}'
                            )
                        "
                    >
                        Save
                    </button>

                </div>

            </div>

        </div>

    `;

}


/* =====================================================
   CLOSE MODAL
===================================================== */

function closeModal() {

    document.getElementById(
        "modalRoot"
    ).innerHTML = "";

}


/* =====================================================
   SAVE FORM
===================================================== */

function saveForm(type, id) {

    closeModal();


    alert(
        "Form saved. Connect this action to your Python/backend CRUD when the frontend is ready."
    );

}


/* =====================================================
   DELETE ITEM
===================================================== */

function deleteItem(type, id) {

    const confirmed = confirm(
        "Delete this record?"
    );


    if (confirmed) {

        alert(
            "Delete action is ready to connect to your backend."
        );

    }

}


/* =====================================================
   VIEW ITEM
===================================================== */

function viewItem(type, id) {

    alert(
        "Details view for " +
        id +
        " is ready to connect to your backend."
    );

}


/* =====================================================
   FILTER TABLE
===================================================== */

function filterTable(input) {

    const query =
        input.value.toLowerCase();


    document
        .querySelectorAll("#dataTable tr")
        .forEach(function (row) {

            row.style.display =
                row.innerText
                    .toLowerCase()
                    .includes(query)
                    ? ""
                    : "none";

        });

}


/* =====================================================
   NAVIGATION
===================================================== */

function navigate(page) {

    setHeader(page);


    const views = {

        dashboard,
        students,
        professors,
        courses,
        enrollments,
        grades,
        users,
        reports,
        settings

    };


    document.getElementById("page").innerHTML =
        views[page]();

}


/* =====================================================
   SIDEBAR EVENTS
===================================================== */

document
    .querySelectorAll(".nav")
    .forEach(function (navItem) {

        navItem.addEventListener(
            "click",
            function () {

                navigate(
                    navItem.dataset.page
                );

            }
        );

    });


/* =====================================================
   GLOBAL SEARCH
===================================================== */

document
    .getElementById("globalSearch")
    .addEventListener(
        "input",
        function (event) {

            const query =
                event.target.value.toLowerCase();


            const table =
                document.querySelector("#dataTable");


            if (!table) {
                return;
            }


            table
                .querySelectorAll("tr")
                .forEach(function (row) {

                    row.style.display =
                        row.innerText
                            .toLowerCase()
                            .includes(query)
                            ? ""
                            : "none";

                });

        }
    );


/* =====================================================
   INITIAL PAGE
===================================================== */

navigate("dashboard");