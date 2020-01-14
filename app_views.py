class View(object):
    def page_open(self):
        pageOpen = """
<!DOCTYPE HTML>
<html>
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
 <meta http-equiv="X-UA-Compatible" content="ie=edge">
 <meta name="description" content="">
 <meta name="author" content="">
 <link rel="icon" href="static/src/cbr_icon.png">
	<link rel="stylesheet" href="static/css/bootstrap.min.css" type="text/css">
    <link rel="stylesheet" href="static/css/fontawesome-all.css" type="text/css">
    <link rel="stylesheet" href="static/css/cbr.css" type="text/css">
<title>CBR | FVS Recruitment Tracker</title>
</head>
<body class="bg-white">
<section class="container mt-2 pt-4 pb-4 cbr-bg-color border rounded">
<img src="static/src/cbr_logo.png" style="width: 40%;" class="mx-auto d-block"/>
<h3 class="display-5 text-center">FVS Recruitment Tracker</h3>
        """
        return pageOpen

    def page_close(self, today_date):
        pageClose = """
</section>
<!--FOOTER-->
<section class="text-center mt-3">
  <p class="mt-1 text-dark"><label>Today is %s</label><br/>
                          <label>&copy; Center for Bioethics and Research 2018.</label></p>
</section>
    <script src="static/js/jquery.min.js"></script>
    <script src="static/js/jquery-ui.min.js"></script>
	<script src="static/js/bootstrap.min.js"></script>
	<script src="static/js/main.js"></script>
 </body>
 </html>
        """ % today_date
        return pageClose

    def page_nav(self, field_staff_available, field_staff_name=""):
        if field_staff_available == True:
            field_staff_links = """
                <ul class="navbar-nav mr-auto">
                  <li class="nav-item">
                    <a class="nav-link" href="staff_participants"><i class="fas fa-cogs"></i> New Participants</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="summary_statistics?cat=ALS"><i class="fas fa-cogs"></i> Summary Statistics</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="generate_followups?date=Six_months"><i class="fas fa-folder"></i> Follow Ups</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="trace_missing"><i class="fas fa-folder"></i> Trace SES</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="exit_application"><i class="fas fa-folder"></i> Exit Application</a>
                  </li>
                </ul>
            """
            field_staff_notification = "<span class=\"text-success\">"+field_staff_name+"</span>"
        else:
            field_staff_links = """
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item">
                        <label>Initial Setup for Recruitment Field Staffs</label>
                    </li>
                </ul>
            """
            field_staff_notification = "<span class=\"text-danger\"> No Staff Set!</span>"

        pageNav = """
<!--NAVIGATION GOES HERE-->
<nav class="navbar navbar-expand-md">
  <section class="container-fluid">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarDefault" aria-controls="navbarDefault" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon border-info"><i class="fas fa-bars"></i></span>
    </button>
    <section class="collapse navbar-collapse" id="navbarDefault">
      <!--LEFTHAND NAVBAR-->
      %s

      <!--RIGHTHAND NAVBAR-->
        <span class="navbar-text">
           <i class="fas fa-user"></i> Field Staff: %s
        </span>
    </section>
  </section>
</nav>
        """ % (field_staff_links, field_staff_notification)
        return pageNav

    def field_staff_display(self, output):
        return output

    def field_staff_form(self):
        fieldStaffForm = """
            <section class="pb-4 text-center w-50 mx-auto mt-3">
            <h3 class="display-3">Field Staff Setup</h3>
            <form action="staff_participants" method="POST">
                 <section class="form-group">
                     <input type="text" name="ffq_staff_name" class="form-control form-control-md" placeholder="enter your name" required>
                 </section>
                 <input type="submit" value="Set me up for the Recruitment Tracker" class="btn btn-secondary btn-block">
             </form>
            </section>
        """
        return fieldStaffForm

    def field_staff_form_success(self):
        fieldStaffFormSuccess = """
            <section class="alert alert-success alert-dismissible fade show w-50 mx-auto mt-3">
              <strong>Field Staff Setup!</strong><br/> You have successfully setup your application for the FFQ and 24hrs Recall.<br/>
              <button type="button" class="btn btn-secondary btn-sm btn-block"><a href="index" class="text-white">Add Participants Now</a></button>
            </section>
        """
        return fieldStaffFormSuccess

    def participants_fill_form(self):
        fillForm = """
            <form action="staff_participants" method="POST">
                 <section class="form-group border border-primary rounded p-2">
                     <section class="row">
                        <section class="col-sm-6">
                            <label for=""><i class="fas fa-user"></i> Baseline Date</label>
                            <input type="date" name="ffq_base_date" class="form-control form-control-sm" placeholder="Baseline date" value="2018-11-22" min="2018-11-22" required>
                            <label for=""><i class="fas fa-user"></i> FFQ ID </label>
                            <input type="number" name="ffq_q_id" class="form-control form-control-sm" placeholder="888011---" min="888011001" max="888011250" step="1" maxlength="11" required>
                            <label for=""><i class="fas fa-user"></i> 24hrs Recall ID </label>
                            <input type="number" name="ffq_24_id" class="form-control form-control-sm" placeholder="444011---" min="444011001" max="444011250" step="1" maxlength="11" required>
                            <label for=""><i class="fas fa-user"></i> Age Category</label><br/>
                            <label class="form-check-label"><input class="form-check-input" type="radio" name="ffq_age_cat" value="21-30" required> 21-30</label>
                            <label class="form-check-label"><input class="form-check-input" type="radio" name="ffq_age_cat" value="31-40"> 31-40</label>
                            <label class="form-check-label"><input class="form-check-input" type="radio" name="ffq_age_cat" value="41-50"> 41-50</label>
                            <label class="form-check-label"><input class="form-check-input" type="radio" name="ffq_age_cat" value="51-60"> 51-60</label>
                            <label class="form-check-label"><input class="form-check-input" type="radio" name="ffq_age_cat" value="Above 60"> Above 60</label><br/>
                        </section>
                        <section class="col-sm-6">
                            <label for=""><i class="fas fa-user"></i> Names</label>
                            <input type="text" name="ffq_names" class="form-control form-control-sm" placeholder="Names here" required>
                            <label for=""><i class="fas fa-user"></i> Sex</label><br/>
                            <label class="form-check-label"><input class="form-check-input" type="radio" name="ffq_sex" value="Male" required> Male</label>
                            <label class="form-check-label"><input class="form-check-input" type="radio" name="ffq_sex" value="Female"> Female</label><br/>
                            <label for=""><i class="fas fa-user"></i> Ethnic Group</label><br/>
                            <label class="form-check-label"><input class="form-check-input" type="radio" name="ffq_tribe" value="Igbo" required> Igbo</label>
                            <label class="form-check-label"><input class="form-check-input" type="radio" name="ffq_tribe" value="Hausa"> Hausa</label>
                            <label class="form-check-label"><input class="form-check-input" type="radio" name="ffq_tribe" value="Yoruba"> Yoruba</label><br/>
                            <label for=""><i class="fas fa-user"></i> SocioEcnomic Status</label><br/>
                            <label class="form-check-label"><input class="form-check-input" type="radio" name="ffq_ses" value="Low" required> Low</label>
                            <label class="form-check-label"><input class="form-check-input" type="radio" name="ffq_ses" value="LowMI"> Low MI</label>
                            <label class="form-check-label"><input class="form-check-input" type="radio" name="ffq_ses" value="HighMI"> High MI</label>
                            <label class="form-check-label"><input class="form-check-input" type="radio" name="ffq_ses" value="High"> High</label><br/>
                        </section>
                     </section>

                     <section class="row">
                        <section class="col-sm-6">
                            <label for=""><i class="fas fa-user"></i> Phone number 1</label>
                            <input type="text" name="ffq_pnum_1" class="form-control form-control-sm" placeholder="Phone Number 1" required>
                        </section>
                        <section class="col-sm-6">
                            <label for=""><i class="fas fa-user"></i> Phone number 2</label>
                            <input type="text" name="ffq_pnum_2" class="form-control form-control-sm" placeholder="Phone Number 2">
                        </section>
                     </section>
                 </section>
                 <input type="submit" value="Add Participant" class="btn btn-secondary btn-block">
             </form>
        """
        return fillForm

    def participants_list(self, data):
        if data['count_participants'] == 0:
            data_list = """
                <section class="alert alert-secondary alert-dismissible fade show">
                <strong>Participants' Status!</strong><br/>
                <label class="text-center">No current participants to display.</label><br/>
                <label class="text-center">Add Participants Now.</label>
                </section>
            """
        else:
            data_list = "".join(["<a href='staff_participants?id="+i[2]+"&action=preview'>"+i[2]+"</a><br/>" for i in data['all_participants']])

        listParticipants = """
        <section class="" style="max-height: 320px; overflow-y: scroll;">
        <label><strong>Participants</strong> %s</label><br/>
            %s
        </section>
        """ % (data['count_participants'], data_list)
        return listParticipants

    def field_staff_participants(self, participants = {}):
        if "insert_error" in participants.keys():
            participants_info = participants['insert_error']
        elif "insert_success" in participants.keys():
            participants_info = participants['insert_success']
        else:
            participants_info = self.participants_fill_form()

        if "details" in participants.keys():
            if participants['data'] == "preview":
                participants_details = """
                <section class="">
                <label><strong>Follow up on FFQ and 24hrs Recall</strong></label><br/>
                <label><strong>Names:</strong> %s</label><br/>
                <label><strong>FFQ ID:</strong> %s</label><br/>
                <label><strong>24hrs ID:</strong> %s</label><br/>
                <label><strong>Sex:</strong> %s</label><br/>
                <label><strong>Age Cat:</strong> %s</label><br/>
                <label><strong>Ethnic Group:</strong> %s</label><br/>
                <label><strong>SES:</strong> %s</label><br/>
                <label><strong>Phone number:</strong> %s, %s</label><br/>
                <button class="btn btn-secondary btn-block"><a href='staff_participants?id=%s&action=edit' class='text-light'>Edit Information</a></button>
                </section>
                """ % (participants['details'][0][4], participants['details'][0][2], participants['details'][0][3],
                        participants['details'][0][5],
                        participants['details'][0][7],
                        participants['details'][0][6],
                        participants['details'][0][10],
                        participants['details'][0][8],
                        participants['details'][0][9],
                        participants['details'][0][2])
            elif participants['data'] == "edit":
                if participants['details'][0][7] == "21-30":
                    edit_age_grp = """
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="21-30" checked required> 21-30</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="31-40"> 31-40</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="41-50"> 41-50</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="51-60"> 51-60</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="Above 60"> Above 60</label><br/>
                    """
                elif participants['details'][0][7] == "31-40":
                    edit_age_grp = """
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="21-30" required> 21-30</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="31-40" checked> 31-40</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="41-50"> 41-50</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="51-60"> 51-60</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="Above 60"> Above 60</label><br/>
                    """
                elif participants['details'][0][7] == "41-50":
                    edit_age_grp = """
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="21-30" required> 21-30</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="31-40"> 31-40</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="41-50" checked> 41-50</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="51-60"> 51-60</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="Above 60"> Above 60</label><br/>
                    """
                elif participants['details'][0][7] == "51-60":
                    edit_age_grp = """
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="21-30" required> 21-30</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="31-40"> 31-40</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="41-50"> 41-50</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="51-60" checked> 51-60</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="Above 60"> Above 60</label><br/>
                    """
                elif participants['details'][0][7] == "Above 60":
                    edit_age_grp = """
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="21-30" required> 21-30</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="31-40"> 31-40</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="41-50"> 41-50</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="51-60"> 51-60</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_age_cat" value="Above 60" checked> Above 60</label><br/>
                    """
                if participants['details'][0][5] == "Male":
                    edit_sex_grp = """
                    <label for=""><i class="fas fa-user"></i> Sex</label><br/>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_sex" value="Male" checked required> Male</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_sex" value="Female"> Female</label><br/>
                    """
                elif participants['details'][0][5] == "Female":
                    edit_sex_grp = """
                    <label for=""><i class="fas fa-user"></i> Sex</label><br/>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_sex" value="Male" required> Male</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_sex" value="Female" checked> Female</label><br/>
                    """
                if participants['details'][0][6] == "Igbo":
                    edit_tribe_grp = """
                    <label for=""><i class="fas fa-user"></i> Ethnic Group</label><br/>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_tribe" value="Igbo" checked required> Igbo</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_tribe" value="Hausa"> Hausa</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_tribe" value="Yoruba"> Yoruba</label><br/>
                    """
                elif participants['details'][0][6] == "Hausa":
                    edit_tribe_grp = """
                    <label for=""><i class="fas fa-user"></i> Ethnic Group</label><br/>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_tribe" value="Igbo" required> Igbo</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_tribe" value="Hausa" checked> Hausa</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_tribe" value="Yoruba"> Yoruba</label><br/>
                    """
                elif participants['details'][0][6] == "Yoruba":
                    edit_tribe_grp = """
                    <label for=""><i class="fas fa-user"></i> Ethnic Group</label><br/>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_tribe" value="Igbo" required> Igbo</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_tribe" value="Hausa"> Hausa</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_tribe" value="Yoruba" checked> Yoruba</label><br/>
                    """
                if participants['details'][0][10] == "Low":
                    edit_ses_grp = """
                    <label for=""><i class="fas fa-user"></i> SocioEcnomic Status</label><br/>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="Low" checked required> Low</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="LowMI"> Low MI</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="HighMI"> High MI</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="High"> High</label><br/>
                    """
                elif participants['details'][0][10] == "LowMI":
                    edit_ses_grp = """
                    <label for=""><i class="fas fa-user"></i> SocioEcnomic Status</label><br/>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="Low" required> Low</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="LowMI" checked> Low MI</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="HighMI"> High MI</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="High"> High</label><br/>
                    """
                elif participants['details'][0][10] == "HighMI":
                    edit_ses_grp = """
                    <label for=""><i class="fas fa-user"></i> SocioEcnomic Status</label><br/>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="Low" required> Low</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="LowMI"> Low MI</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="HighMI" checked> High MI</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="High"> High</label><br/>
                    """
                elif participants['details'][0][10] == "High":
                    edit_ses_grp = """
                    <label for=""><i class="fas fa-user"></i> SocioEcnomic Status</label><br/>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="Low" required> Low</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="LowMI"> Low MI</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="HighMI"> High MI</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="High" checked> High</label><br/>
                    """
                else:
                    edit_ses_grp = """
                    <label for=""><i class="fas fa-user"></i> SocioEcnomic Status</label><br/>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="Low" required> Low</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="LowMI"> Low MI</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="HighMI"> High MI</label>
                    <label class="form-check-label"><input class="form-check-input" type="radio" name="edit_ses" value="High"> High</label><br/>
                    """
                participants_details = """
                <section class="">
                <label><strong>Editing participant's Information</strong></label><br/>
                <form action="staff_participants?id=%s&action=edit" method="POST">
                     <section class="form-group p-2">
                         <section class="row">
                            <section class="col-sm-6">
                                <label for=""><i class="fas fa-user"></i> Baseline Date</label>
                                <input type="date" name="edit_base_date" class="form-control form-control-sm" value="%s" required>
                                <label for=""><i class="fas fa-user"></i> FFQ ID </label>
                                <input type="number" name="edit_q_id" class="form-control form-control-sm" value="%s" disabled>
                                <label for=""><i class="fas fa-user"></i> 24hrs Recall ID </label>
                                <input type="number" name="edit_24_id" class="form-control form-control-sm" value="%s" disabled>
                                <label for=""><i class="fas fa-user"></i> Age Category</label><br/>
                                    %s
                            </section>
                            <section class="col-sm-6">
                                <label for=""><i class="fas fa-user"></i> Names</label>
                                <input type="text" name="edit_names" class="form-control form-control-sm" value="%s" required>
                                    %s %s %s
                            </section>
                         </section>

                         <section class="row">
                            <section class="col-sm-6">
                                <label for=""><i class="fas fa-user"></i> Phone number 1</label>
                                <input type="text" name="edit_pnum_1" class="form-control form-control-sm" value="%s" required>
                            </section>
                            <section class="col-sm-6">
                                <label for=""><i class="fas fa-user"></i> Phone number 2</label>
                                <input type="text" name="edit_pnum_2" class="form-control form-control-sm" value="%s">
                            </section>
                         </section>
                     </section>
                     <input type="submit" value="Update Information" class="btn btn-secondary btn-block">
                </form>
                </section>
                """ % (participants['details'][0][2], participants['details'][0][1],
                        participants['details'][0][2],
                        participants['details'][0][3],
                        edit_age_grp,
                        participants['details'][0][4],
                        edit_sex_grp, edit_tribe_grp, edit_ses_grp,
                        participants['details'][0][8],
                        participants['details'][0][9])
            elif participants['data'] == "update":
                participants_details = """
                <section class="alert alert-success alert-dismissible fade show mt-3">
                  <strong>Participant's Information Update!</strong><br/> You have successfully updated the information for %s.
                </section>
                """ % (participants['details'][0][4].title())
        else:
            participants_details = ""

        fieldStaffParticipants = """
        <section class="row pl-2 pr-2">
            <section class="col-md-5">
            <h4 class="display-5 text-center">Participant's Information</h4>
                %s
            </section>

            <section class="col-md-2">
            <h4 class="display-5">Participant's List</h4>
                %s
            </section>

            <section class="col-md-5">
                <section class="mt-2">
                    %s
                </section>
            </section>
        </section>
        """ % (participants_info, self.participants_list(participants), participants_details)
        return fieldStaffParticipants

    def summary_statistics_als(self, dummy):
        t_21 = dummy[('21-30', 'Hausa', 'Male')]['count']+dummy[('21-30', 'Hausa', 'Female')]['count']+dummy[('21-30', 'Igbo', 'Male')]['count']+dummy[('21-30', 'Igbo', 'Female')]['count']+dummy[('21-30', 'Yoruba', 'Male')]['count']+dummy[('21-30', 'Yoruba', 'Female')]['count']
        t_31 = dummy[('31-40', 'Hausa', 'Male')]['count']+dummy[('31-40', 'Hausa', 'Female')]['count']+dummy[('31-40', 'Igbo', 'Male')]['count']+dummy[('31-40', 'Igbo', 'Female')]['count']+dummy[('31-40', 'Yoruba', 'Male')]['count']+dummy[('31-40', 'Yoruba', 'Female')]['count']
        t_41 = dummy[('41-50', 'Hausa', 'Male')]['count']+dummy[('41-50', 'Hausa', 'Female')]['count']+dummy[('41-50', 'Igbo', 'Male')]['count']+dummy[('41-50', 'Igbo', 'Female')]['count']+dummy[('41-50', 'Yoruba', 'Male')]['count']+dummy[('41-50', 'Yoruba', 'Female')]['count']
        t_51 = dummy[('51-60', 'Hausa', 'Male')]['count']+dummy[('51-60', 'Hausa', 'Female')]['count']+dummy[('51-60', 'Igbo', 'Male')]['count']+dummy[('51-60', 'Igbo', 'Female')]['count']+dummy[('51-60', 'Yoruba', 'Male')]['count']+dummy[('51-60', 'Yoruba', 'Female')]['count']
        t_61 = dummy[('Above 60', 'Hausa', 'Male')]['count']+dummy[('Above 60', 'Hausa', 'Female')]['count']+dummy[('Above 60', 'Igbo', 'Male')]['count']+dummy[('Above 60', 'Igbo', 'Female')]['count']+dummy[('Above 60', 'Yoruba', 'Male')]['count']+dummy[('Above 60', 'Yoruba', 'Female')]['count']

        t_hausaM = dummy[('21-30', 'Hausa', 'Male')]['count']+dummy[('31-40', 'Hausa', 'Male')]['count']+dummy[('41-50', 'Hausa', 'Male')]['count']+dummy[('51-60', 'Hausa', 'Male')]['count']+dummy[('Above 60', 'Hausa', 'Male')]['count']
        t_hausaF = dummy[('21-30', 'Hausa', 'Female')]['count']+dummy[('31-40', 'Hausa', 'Female')]['count']+dummy[('41-50', 'Hausa', 'Female')]['count']+dummy[('51-60', 'Hausa', 'Female')]['count']+dummy[('Above 60', 'Hausa', 'Female')]['count']
        t_igboM = dummy[('21-30', 'Igbo', 'Male')]['count']+dummy[('31-40', 'Igbo', 'Male')]['count']+dummy[('41-50', 'Igbo', 'Male')]['count']+dummy[('51-60', 'Igbo', 'Male')]['count']+dummy[('Above 60', 'Igbo', 'Male')]['count']
        t_igboF = dummy[('21-30', 'Igbo', 'Female')]['count']+dummy[('31-40', 'Igbo', 'Female')]['count']+dummy[('41-50', 'Igbo', 'Female')]['count']+dummy[('51-60', 'Igbo', 'Female')]['count']+dummy[('Above 60', 'Igbo', 'Female')]['count']
        t_yorubaM = dummy[('21-30', 'Yoruba', 'Male')]['count']+dummy[('31-40', 'Yoruba', 'Male')]['count']+dummy[('41-50', 'Yoruba', 'Male')]['count']+dummy[('51-60', 'Yoruba', 'Male')]['count']+dummy[('Above 60', 'Yoruba', 'Male')]['count']
        t_yorubaF = dummy[('21-30', 'Yoruba', 'Female')]['count']+dummy[('31-40', 'Yoruba', 'Female')]['count']+dummy[('41-50', 'Yoruba', 'Female')]['count']+dummy[('51-60', 'Yoruba', 'Female')]['count']+dummy[('Above 60', 'Yoruba', 'Female')]['count']

        t_total = t_21+t_31+t_41+t_51+t_61

        summary_table = """
        <table class="table table-bordered table-hover">
        <thead class="">
        <tr><th>LANGUAGES</th><th>Hausa</th><th>&nbsp;</th><th>Igbo</th><th>&nbsp;</th><th>Yoruba</th><th>&nbsp;</th><th>&nbsp;</th></tr>
        <tr><th>AGE GROUPS</th><th>M</th><th>F</th><th>M</th><th>F</th><th>M</th><th>F</th><th>TOTAL</th></tr>
        </thead>
        <tbody>
        <tr><td>21-30</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>31-40</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>41-50</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>51-60</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>61 above</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td><strong>TOTAL</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td></tr>
        </tbody>
        </table>
        """ % (dummy[('21-30', 'Hausa', 'Male')]['count'],
                dummy[('21-30', 'Hausa', 'Female')]['count'],
                dummy[('21-30', 'Igbo', 'Male')]['count'],
                dummy[('21-30', 'Igbo', 'Female')]['count'],
                dummy[('21-30', 'Yoruba', 'Male')]['count'],
                dummy[('21-30', 'Yoruba', 'Female')]['count'],
                t_21,
                dummy[('31-40', 'Hausa', 'Male')]['count'],
                dummy[('31-40', 'Hausa', 'Female')]['count'],
                dummy[('31-40', 'Igbo', 'Male')]['count'],
                dummy[('31-40', 'Igbo', 'Female')]['count'],
                dummy[('31-40', 'Yoruba', 'Male')]['count'],
                dummy[('31-40', 'Yoruba', 'Female')]['count'],
                t_31,
                dummy[('41-50', 'Hausa', 'Male')]['count'],
                dummy[('41-50', 'Hausa', 'Female')]['count'],
                dummy[('41-50', 'Igbo', 'Male')]['count'],
                dummy[('41-50', 'Igbo', 'Female')]['count'],
                dummy[('41-50', 'Yoruba', 'Male')]['count'],
                dummy[('41-50', 'Yoruba', 'Female')]['count'],
                t_41,
                dummy[('51-60', 'Hausa', 'Male')]['count'],
                dummy[('51-60', 'Hausa', 'Female')]['count'],
                dummy[('51-60', 'Igbo', 'Male')]['count'],
                dummy[('51-60', 'Igbo', 'Female')]['count'],
                dummy[('51-60', 'Yoruba', 'Male')]['count'],
                dummy[('51-60', 'Yoruba', 'Female')]['count'],
                t_51,
                dummy[('Above 60', 'Hausa', 'Male')]['count'],
                dummy[('Above 60', 'Hausa', 'Female')]['count'],
                dummy[('Above 60', 'Igbo', 'Male')]['count'],
                dummy[('Above 60', 'Igbo', 'Female')]['count'],
                dummy[('Above 60', 'Yoruba', 'Male')]['count'],
                dummy[('Above 60', 'Yoruba', 'Female')]['count'],
                t_61,
                t_hausaM, t_hausaF, t_igboM, t_igboF, t_yorubaM, t_yorubaF, t_total)

        summaryAls = """
        <section class="row pl-2 pr-2">
            <section class="col-md-3">
                <section class="list-group">
                  <a href="summary_statistics?cat=ALS" class="list-group-item">Summary by ALS</a>
                  <a href="summary_statistics?cat=SES_ALS" class="list-group-item">Summary by SES-ALS</a>
                </section>
            </section>
            <section class="col-md-7">
            <h4 class="display-5 text-center">Summary Table</h4>
                %s
            </section>

            <section class="col-md-2">
            <h4 class="display-5">&nbsp;</h4>

            </section>
        </section>
        """ % (summary_table)
        return summaryAls

    def summary_statistics_sals(self, dummy):
        #Summary by Low SES
        low_t_21 = dummy[('Low', '21-30', 'Hausa', 'Male')]['count']+dummy[('Low', '21-30', 'Hausa', 'Female')]['count']+dummy[('Low', '21-30', 'Igbo', 'Male')]['count']+dummy[('Low', '21-30', 'Igbo', 'Female')]['count']+dummy[('Low', '21-30', 'Yoruba', 'Male')]['count']+dummy[('Low', '21-30', 'Yoruba', 'Female')]['count']
        low_t_31 = dummy[('Low', '31-40', 'Hausa', 'Male')]['count']+dummy[('Low', '31-40', 'Hausa', 'Female')]['count']+dummy[('Low', '31-40', 'Igbo', 'Male')]['count']+dummy[('Low', '31-40', 'Igbo', 'Female')]['count']+dummy[('Low', '31-40', 'Yoruba', 'Male')]['count']+dummy[('Low', '31-40', 'Yoruba', 'Female')]['count']
        low_t_41 = dummy[('Low', '41-50', 'Hausa', 'Male')]['count']+dummy[('Low', '41-50', 'Hausa', 'Female')]['count']+dummy[('Low', '41-50', 'Igbo', 'Male')]['count']+dummy[('Low', '41-50', 'Igbo', 'Female')]['count']+dummy[('Low', '41-50', 'Yoruba', 'Male')]['count']+dummy[('Low', '41-50', 'Yoruba', 'Female')]['count']
        low_t_51 = dummy[('Low', '51-60', 'Hausa', 'Male')]['count']+dummy[('Low', '51-60', 'Hausa', 'Female')]['count']+dummy[('Low', '51-60', 'Igbo', 'Male')]['count']+dummy[('Low', '51-60', 'Igbo', 'Female')]['count']+dummy[('Low', '51-60', 'Yoruba', 'Male')]['count']+dummy[('Low', '51-60', 'Yoruba', 'Female')]['count']
        low_t_61 = dummy[('Low', 'Above 60', 'Hausa', 'Male')]['count']+dummy[('Low', 'Above 60', 'Hausa', 'Female')]['count']+dummy[('Low', 'Above 60', 'Igbo', 'Male')]['count']+dummy[('Low', 'Above 60', 'Igbo', 'Female')]['count']+dummy[('Low', 'Above 60', 'Yoruba', 'Male')]['count']+dummy[('Low', 'Above 60', 'Yoruba', 'Female')]['count']

        low_t_hausaM = dummy[('Low', '21-30', 'Hausa', 'Male')]['count']+dummy[('Low', '31-40', 'Hausa', 'Male')]['count']+dummy[('Low', '41-50', 'Hausa', 'Male')]['count']+dummy[('Low', '51-60', 'Hausa', 'Male')]['count']+dummy[('Low', 'Above 60', 'Hausa', 'Male')]['count']
        low_t_hausaF = dummy[('Low', '21-30', 'Hausa', 'Female')]['count']+dummy[('Low', '31-40', 'Hausa', 'Female')]['count']+dummy[('Low', '41-50', 'Hausa', 'Female')]['count']+dummy[('Low', '51-60', 'Hausa', 'Female')]['count']+dummy[('Low', 'Above 60', 'Hausa', 'Female')]['count']
        low_t_igboM = dummy[('Low', '21-30', 'Igbo', 'Male')]['count']+dummy[('Low', '31-40', 'Igbo', 'Male')]['count']+dummy[('Low', '41-50', 'Igbo', 'Male')]['count']+dummy[('Low', '51-60', 'Igbo', 'Male')]['count']+dummy[('Low', 'Above 60', 'Igbo', 'Male')]['count']
        low_t_igboF = dummy[('Low', '21-30', 'Igbo', 'Female')]['count']+dummy[('Low', '31-40', 'Igbo', 'Female')]['count']+dummy[('Low', '41-50', 'Igbo', 'Female')]['count']+dummy[('Low', '51-60', 'Igbo', 'Female')]['count']+dummy[('Low', 'Above 60', 'Igbo', 'Female')]['count']
        low_t_yorubaM = dummy[('Low', '21-30', 'Yoruba', 'Male')]['count']+dummy[('Low', '31-40', 'Yoruba', 'Male')]['count']+dummy[('Low', '41-50', 'Yoruba', 'Male')]['count']+dummy[('Low', '51-60', 'Yoruba', 'Male')]['count']+dummy[('Low', 'Above 60', 'Yoruba', 'Male')]['count']
        low_t_yorubaF = dummy[('Low', '21-30', 'Yoruba', 'Female')]['count']+dummy[('Low', '31-40', 'Yoruba', 'Female')]['count']+dummy[('Low', '41-50', 'Yoruba', 'Female')]['count']+dummy[('Low', '51-60', 'Yoruba', 'Female')]['count']+dummy[('Low', 'Above 60', 'Yoruba', 'Female')]['count']

        low_t_total = low_t_21+low_t_31+low_t_41+low_t_51+low_t_61

        summary_table_low = """
        <h4 class="display-5 text-center">Summary Table By SES: Low Income</h4>
        <table class="table table-bordered table-hover">
        <thead class="">
        <tr><th>LANGUAGES</th><th>Hausa</th><th>&nbsp;</th><th>Igbo</th><th>&nbsp;</th><th>Yoruba</th><th>&nbsp;</th><th>&nbsp;</th></tr>
        <tr><th>AGE GROUPS</th><th>M</th><th>F</th><th>M</th><th>F</th><th>M</th><th>F</th><th>TOTAL</th></tr>
        </thead>
        <tbody>
        <tr><td>21-30</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>31-40</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>41-50</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>51-60</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>61 above</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td><strong>TOTAL</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td></tr>
        </tbody>
        </table>
        """ % (dummy[('Low', '21-30', 'Hausa', 'Male')]['count'],
                dummy[('Low', '21-30', 'Hausa', 'Female')]['count'],
                dummy[('Low', '21-30', 'Igbo', 'Male')]['count'],
                dummy[('Low', '21-30', 'Igbo', 'Female')]['count'],
                dummy[('Low', '21-30', 'Yoruba', 'Male')]['count'],
                dummy[('Low', '21-30', 'Yoruba', 'Female')]['count'],
                low_t_21,
                dummy[('Low', '31-40', 'Hausa', 'Male')]['count'],
                dummy[('Low', '31-40', 'Hausa', 'Female')]['count'],
                dummy[('Low', '31-40', 'Igbo', 'Male')]['count'],
                dummy[('Low', '31-40', 'Igbo', 'Female')]['count'],
                dummy[('Low', '31-40', 'Yoruba', 'Male')]['count'],
                dummy[('Low', '31-40', 'Yoruba', 'Female')]['count'],
                low_t_31,
                dummy[('Low', '41-50', 'Hausa', 'Male')]['count'],
                dummy[('Low', '41-50', 'Hausa', 'Female')]['count'],
                dummy[('Low', '41-50', 'Igbo', 'Male')]['count'],
                dummy[('Low', '41-50', 'Igbo', 'Female')]['count'],
                dummy[('Low', '41-50', 'Yoruba', 'Male')]['count'],
                dummy[('Low', '41-50', 'Yoruba', 'Female')]['count'],
                low_t_41,
                dummy[('Low', '51-60', 'Hausa', 'Male')]['count'],
                dummy[('Low', '51-60', 'Hausa', 'Female')]['count'],
                dummy[('Low', '51-60', 'Igbo', 'Male')]['count'],
                dummy[('Low', '51-60', 'Igbo', 'Female')]['count'],
                dummy[('Low', '51-60', 'Yoruba', 'Male')]['count'],
                dummy[('Low', '51-60', 'Yoruba', 'Female')]['count'],
                low_t_51,
                dummy[('Low', 'Above 60', 'Hausa', 'Male')]['count'],
                dummy[('Low', 'Above 60', 'Hausa', 'Female')]['count'],
                dummy[('Low', 'Above 60', 'Igbo', 'Male')]['count'],
                dummy[('Low', 'Above 60', 'Igbo', 'Female')]['count'],
                dummy[('Low', 'Above 60', 'Yoruba', 'Male')]['count'],
                dummy[('Low', 'Above 60', 'Yoruba', 'Female')]['count'],
                low_t_61,
                low_t_hausaM, low_t_hausaF, low_t_igboM, low_t_igboF, low_t_yorubaM, low_t_yorubaF, low_t_total)

        #Summary by LowMI SES
        lowMI_t_21 = dummy[('LowMI', '21-30', 'Hausa', 'Male')]['count']+dummy[('LowMI', '21-30', 'Hausa', 'Female')]['count']+dummy[('LowMI', '21-30', 'Igbo', 'Male')]['count']+dummy[('LowMI', '21-30', 'Igbo', 'Female')]['count']+dummy[('LowMI', '21-30', 'Yoruba', 'Male')]['count']+dummy[('LowMI', '21-30', 'Yoruba', 'Female')]['count']
        lowMI_t_31 = dummy[('LowMI', '31-40', 'Hausa', 'Male')]['count']+dummy[('LowMI', '31-40', 'Hausa', 'Female')]['count']+dummy[('LowMI', '31-40', 'Igbo', 'Male')]['count']+dummy[('LowMI', '31-40', 'Igbo', 'Female')]['count']+dummy[('LowMI', '31-40', 'Yoruba', 'Male')]['count']+dummy[('LowMI', '31-40', 'Yoruba', 'Female')]['count']
        lowMI_t_41 = dummy[('LowMI', '41-50', 'Hausa', 'Male')]['count']+dummy[('LowMI', '41-50', 'Hausa', 'Female')]['count']+dummy[('LowMI', '41-50', 'Igbo', 'Male')]['count']+dummy[('LowMI', '41-50', 'Igbo', 'Female')]['count']+dummy[('LowMI', '41-50', 'Yoruba', 'Male')]['count']+dummy[('LowMI', '41-50', 'Yoruba', 'Female')]['count']
        lowMI_t_51 = dummy[('LowMI', '51-60', 'Hausa', 'Male')]['count']+dummy[('LowMI', '51-60', 'Hausa', 'Female')]['count']+dummy[('LowMI', '51-60', 'Igbo', 'Male')]['count']+dummy[('LowMI', '51-60', 'Igbo', 'Female')]['count']+dummy[('LowMI', '51-60', 'Yoruba', 'Male')]['count']+dummy[('LowMI', '51-60', 'Yoruba', 'Female')]['count']
        lowMI_t_61 = dummy[('LowMI', 'Above 60', 'Hausa', 'Male')]['count']+dummy[('LowMI', 'Above 60', 'Hausa', 'Female')]['count']+dummy[('LowMI', 'Above 60', 'Igbo', 'Male')]['count']+dummy[('LowMI', 'Above 60', 'Igbo', 'Female')]['count']+dummy[('LowMI', 'Above 60', 'Yoruba', 'Male')]['count']+dummy[('LowMI', 'Above 60', 'Yoruba', 'Female')]['count']

        lowMI_t_hausaM = dummy[('LowMI', '21-30', 'Hausa', 'Male')]['count']+dummy[('LowMI', '31-40', 'Hausa', 'Male')]['count']+dummy[('LowMI', '41-50', 'Hausa', 'Male')]['count']+dummy[('LowMI', '51-60', 'Hausa', 'Male')]['count']+dummy[('LowMI', 'Above 60', 'Hausa', 'Male')]['count']
        lowMI_t_hausaF = dummy[('LowMI', '21-30', 'Hausa', 'Female')]['count']+dummy[('LowMI', '31-40', 'Hausa', 'Female')]['count']+dummy[('LowMI', '41-50', 'Hausa', 'Female')]['count']+dummy[('LowMI', '51-60', 'Hausa', 'Female')]['count']+dummy[('LowMI', 'Above 60', 'Hausa', 'Female')]['count']
        lowMI_t_igboM = dummy[('LowMI', '21-30', 'Igbo', 'Male')]['count']+dummy[('LowMI', '31-40', 'Igbo', 'Male')]['count']+dummy[('LowMI', '41-50', 'Igbo', 'Male')]['count']+dummy[('LowMI', '51-60', 'Igbo', 'Male')]['count']+dummy[('LowMI', 'Above 60', 'Igbo', 'Male')]['count']
        lowMI_t_igboF = dummy[('LowMI', '21-30', 'Igbo', 'Female')]['count']+dummy[('LowMI', '31-40', 'Igbo', 'Female')]['count']+dummy[('LowMI', '41-50', 'Igbo', 'Female')]['count']+dummy[('LowMI', '51-60', 'Igbo', 'Female')]['count']+dummy[('LowMI', 'Above 60', 'Igbo', 'Female')]['count']
        lowMI_t_yorubaM = dummy[('LowMI', '21-30', 'Yoruba', 'Male')]['count']+dummy[('LowMI', '31-40', 'Yoruba', 'Male')]['count']+dummy[('LowMI', '41-50', 'Yoruba', 'Male')]['count']+dummy[('LowMI', '51-60', 'Yoruba', 'Male')]['count']+dummy[('LowMI', 'Above 60', 'Yoruba', 'Male')]['count']
        lowMI_t_yorubaF = dummy[('LowMI', '21-30', 'Yoruba', 'Female')]['count']+dummy[('LowMI', '31-40', 'Yoruba', 'Female')]['count']+dummy[('LowMI', '41-50', 'Yoruba', 'Female')]['count']+dummy[('LowMI', '51-60', 'Yoruba', 'Female')]['count']+dummy[('LowMI', 'Above 60', 'Yoruba', 'Female')]['count']

        lowMI_t_total = lowMI_t_21+lowMI_t_31+lowMI_t_41+lowMI_t_51+lowMI_t_61

        summary_table_lowMI = """
        <h4 class="display-5 text-center">Summary Table By SES: Low Middle Income</h4>
        <table class="table table-bordered table-hover">
        <thead class="">
        <tr><th>LANGUAGES</th><th>Hausa</th><th>&nbsp;</th><th>Igbo</th><th>&nbsp;</th><th>Yoruba</th><th>&nbsp;</th><th>&nbsp;</th></tr>
        <tr><th>AGE GROUPS</th><th>M</th><th>F</th><th>M</th><th>F</th><th>M</th><th>F</th><th>TOTAL</th></tr>
        </thead>
        <tbody>
        <tr><td>21-30</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>31-40</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>41-50</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>51-60</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>61 above</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td><strong>TOTAL</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td></tr>
        </tbody>
        </table>
        """ % (dummy[('LowMI', '21-30', 'Hausa', 'Male')]['count'],
                dummy[('LowMI', '21-30', 'Hausa', 'Female')]['count'],
                dummy[('LowMI', '21-30', 'Igbo', 'Male')]['count'],
                dummy[('LowMI', '21-30', 'Igbo', 'Female')]['count'],
                dummy[('LowMI', '21-30', 'Yoruba', 'Male')]['count'],
                dummy[('LowMI', '21-30', 'Yoruba', 'Female')]['count'],
                lowMI_t_21,
                dummy[('LowMI', '31-40', 'Hausa', 'Male')]['count'],
                dummy[('LowMI', '31-40', 'Hausa', 'Female')]['count'],
                dummy[('LowMI', '31-40', 'Igbo', 'Male')]['count'],
                dummy[('LowMI', '31-40', 'Igbo', 'Female')]['count'],
                dummy[('LowMI', '31-40', 'Yoruba', 'Male')]['count'],
                dummy[('LowMI', '31-40', 'Yoruba', 'Female')]['count'],
                lowMI_t_31,
                dummy[('LowMI', '41-50', 'Hausa', 'Male')]['count'],
                dummy[('LowMI', '41-50', 'Hausa', 'Female')]['count'],
                dummy[('LowMI', '41-50', 'Igbo', 'Male')]['count'],
                dummy[('LowMI', '41-50', 'Igbo', 'Female')]['count'],
                dummy[('LowMI', '41-50', 'Yoruba', 'Male')]['count'],
                dummy[('LowMI', '41-50', 'Yoruba', 'Female')]['count'],
                lowMI_t_41,
                dummy[('LowMI', '51-60', 'Hausa', 'Male')]['count'],
                dummy[('LowMI', '51-60', 'Hausa', 'Female')]['count'],
                dummy[('LowMI', '51-60', 'Igbo', 'Male')]['count'],
                dummy[('LowMI', '51-60', 'Igbo', 'Female')]['count'],
                dummy[('LowMI', '51-60', 'Yoruba', 'Male')]['count'],
                dummy[('LowMI', '51-60', 'Yoruba', 'Female')]['count'],
                lowMI_t_51,
                dummy[('LowMI', 'Above 60', 'Hausa', 'Male')]['count'],
                dummy[('LowMI', 'Above 60', 'Hausa', 'Female')]['count'],
                dummy[('LowMI', 'Above 60', 'Igbo', 'Male')]['count'],
                dummy[('LowMI', 'Above 60', 'Igbo', 'Female')]['count'],
                dummy[('LowMI', 'Above 60', 'Yoruba', 'Male')]['count'],
                dummy[('LowMI', 'Above 60', 'Yoruba', 'Female')]['count'],
                lowMI_t_61,
                lowMI_t_hausaM, lowMI_t_hausaF, lowMI_t_igboM, lowMI_t_igboF, lowMI_t_yorubaM, lowMI_t_yorubaF, lowMI_t_total)

        #Summary by HighMI SES
        highMI_t_21 = dummy[('HighMI', '21-30', 'Hausa', 'Male')]['count']+dummy[('HighMI', '21-30', 'Hausa', 'Female')]['count']+dummy[('HighMI', '21-30', 'Igbo', 'Male')]['count']+dummy[('HighMI', '21-30', 'Igbo', 'Female')]['count']+dummy[('HighMI', '21-30', 'Yoruba', 'Male')]['count']+dummy[('HighMI', '21-30', 'Yoruba', 'Female')]['count']
        highMI_t_31 = dummy[('HighMI', '31-40', 'Hausa', 'Male')]['count']+dummy[('HighMI', '31-40', 'Hausa', 'Female')]['count']+dummy[('HighMI', '31-40', 'Igbo', 'Male')]['count']+dummy[('HighMI', '31-40', 'Igbo', 'Female')]['count']+dummy[('HighMI', '31-40', 'Yoruba', 'Male')]['count']+dummy[('HighMI', '31-40', 'Yoruba', 'Female')]['count']
        highMI_t_41 = dummy[('HighMI', '41-50', 'Hausa', 'Male')]['count']+dummy[('HighMI', '41-50', 'Hausa', 'Female')]['count']+dummy[('HighMI', '41-50', 'Igbo', 'Male')]['count']+dummy[('HighMI', '41-50', 'Igbo', 'Female')]['count']+dummy[('HighMI', '41-50', 'Yoruba', 'Male')]['count']+dummy[('HighMI', '41-50', 'Yoruba', 'Female')]['count']
        highMI_t_51 = dummy[('HighMI', '51-60', 'Hausa', 'Male')]['count']+dummy[('HighMI', '51-60', 'Hausa', 'Female')]['count']+dummy[('HighMI', '51-60', 'Igbo', 'Male')]['count']+dummy[('HighMI', '51-60', 'Igbo', 'Female')]['count']+dummy[('HighMI', '51-60', 'Yoruba', 'Male')]['count']+dummy[('HighMI', '51-60', 'Yoruba', 'Female')]['count']
        highMI_t_61 = dummy[('HighMI', 'Above 60', 'Hausa', 'Male')]['count']+dummy[('HighMI', 'Above 60', 'Hausa', 'Female')]['count']+dummy[('HighMI', 'Above 60', 'Igbo', 'Male')]['count']+dummy[('HighMI', 'Above 60', 'Igbo', 'Female')]['count']+dummy[('HighMI', 'Above 60', 'Yoruba', 'Male')]['count']+dummy[('HighMI', 'Above 60', 'Yoruba', 'Female')]['count']

        highMI_t_hausaM = dummy[('HighMI', '21-30', 'Hausa', 'Male')]['count']+dummy[('HighMI', '31-40', 'Hausa', 'Male')]['count']+dummy[('HighMI', '41-50', 'Hausa', 'Male')]['count']+dummy[('HighMI', '51-60', 'Hausa', 'Male')]['count']+dummy[('HighMI', 'Above 60', 'Hausa', 'Male')]['count']
        highMI_t_hausaF = dummy[('HighMI', '21-30', 'Hausa', 'Female')]['count']+dummy[('HighMI', '31-40', 'Hausa', 'Female')]['count']+dummy[('HighMI', '41-50', 'Hausa', 'Female')]['count']+dummy[('HighMI', '51-60', 'Hausa', 'Female')]['count']+dummy[('HighMI', 'Above 60', 'Hausa', 'Female')]['count']
        highMI_t_igboM = dummy[('HighMI', '21-30', 'Igbo', 'Male')]['count']+dummy[('HighMI', '31-40', 'Igbo', 'Male')]['count']+dummy[('HighMI', '41-50', 'Igbo', 'Male')]['count']+dummy[('HighMI', '51-60', 'Igbo', 'Male')]['count']+dummy[('HighMI', 'Above 60', 'Igbo', 'Male')]['count']
        highMI_t_igboF = dummy[('HighMI', '21-30', 'Igbo', 'Female')]['count']+dummy[('HighMI', '31-40', 'Igbo', 'Female')]['count']+dummy[('HighMI', '41-50', 'Igbo', 'Female')]['count']+dummy[('HighMI', '51-60', 'Igbo', 'Female')]['count']+dummy[('HighMI', 'Above 60', 'Igbo', 'Female')]['count']
        highMI_t_yorubaM = dummy[('HighMI', '21-30', 'Yoruba', 'Male')]['count']+dummy[('HighMI', '31-40', 'Yoruba', 'Male')]['count']+dummy[('HighMI', '41-50', 'Yoruba', 'Male')]['count']+dummy[('HighMI', '51-60', 'Yoruba', 'Male')]['count']+dummy[('HighMI', 'Above 60', 'Yoruba', 'Male')]['count']
        highMI_t_yorubaF = dummy[('HighMI', '21-30', 'Yoruba', 'Female')]['count']+dummy[('HighMI', '31-40', 'Yoruba', 'Female')]['count']+dummy[('HighMI', '41-50', 'Yoruba', 'Female')]['count']+dummy[('HighMI', '51-60', 'Yoruba', 'Female')]['count']+dummy[('HighMI', 'Above 60', 'Yoruba', 'Female')]['count']

        highMI_t_total = highMI_t_21+highMI_t_31+highMI_t_41+highMI_t_51+highMI_t_61

        summary_table_highMI = """
        <h4 class="display-5 text-center">Summary Table By SES: High Middle Income</h4>
        <table class="table table-bordered table-hover">
        <thead class="">
        <tr><th>LANGUAGES</th><th>Hausa</th><th>&nbsp;</th><th>Igbo</th><th>&nbsp;</th><th>Yoruba</th><th>&nbsp;</th><th>&nbsp;</th></tr>
        <tr><th>AGE GROUPS</th><th>M</th><th>F</th><th>M</th><th>F</th><th>M</th><th>F</th><th>TOTAL</th></tr>
        </thead>
        <tbody>
        <tr><td>21-30</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>31-40</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>41-50</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>51-60</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>61 above</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td><strong>TOTAL</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td></tr>
        </tbody>
        </table>
        """ % (dummy[('HighMI', '21-30', 'Hausa', 'Male')]['count'],
                dummy[('HighMI', '21-30', 'Hausa', 'Female')]['count'],
                dummy[('HighMI', '21-30', 'Igbo', 'Male')]['count'],
                dummy[('HighMI', '21-30', 'Igbo', 'Female')]['count'],
                dummy[('HighMI', '21-30', 'Yoruba', 'Male')]['count'],
                dummy[('HighMI', '21-30', 'Yoruba', 'Female')]['count'],
                highMI_t_21,
                dummy[('HighMI', '31-40', 'Hausa', 'Male')]['count'],
                dummy[('HighMI', '31-40', 'Hausa', 'Female')]['count'],
                dummy[('HighMI', '31-40', 'Igbo', 'Male')]['count'],
                dummy[('HighMI', '31-40', 'Igbo', 'Female')]['count'],
                dummy[('HighMI', '31-40', 'Yoruba', 'Male')]['count'],
                dummy[('HighMI', '31-40', 'Yoruba', 'Female')]['count'],
                highMI_t_31,
                dummy[('HighMI', '41-50', 'Hausa', 'Male')]['count'],
                dummy[('HighMI', '41-50', 'Hausa', 'Female')]['count'],
                dummy[('HighMI', '41-50', 'Igbo', 'Male')]['count'],
                dummy[('HighMI', '41-50', 'Igbo', 'Female')]['count'],
                dummy[('HighMI', '41-50', 'Yoruba', 'Male')]['count'],
                dummy[('HighMI', '41-50', 'Yoruba', 'Female')]['count'],
                highMI_t_41,
                dummy[('HighMI', '51-60', 'Hausa', 'Male')]['count'],
                dummy[('HighMI', '51-60', 'Hausa', 'Female')]['count'],
                dummy[('HighMI', '51-60', 'Igbo', 'Male')]['count'],
                dummy[('HighMI', '51-60', 'Igbo', 'Female')]['count'],
                dummy[('HighMI', '51-60', 'Yoruba', 'Male')]['count'],
                dummy[('HighMI', '51-60', 'Yoruba', 'Female')]['count'],
                highMI_t_51,
                dummy[('HighMI', 'Above 60', 'Hausa', 'Male')]['count'],
                dummy[('HighMI', 'Above 60', 'Hausa', 'Female')]['count'],
                dummy[('HighMI', 'Above 60', 'Igbo', 'Male')]['count'],
                dummy[('HighMI', 'Above 60', 'Igbo', 'Female')]['count'],
                dummy[('HighMI', 'Above 60', 'Yoruba', 'Male')]['count'],
                dummy[('HighMI', 'Above 60', 'Yoruba', 'Female')]['count'],
                highMI_t_61,
                highMI_t_hausaM, highMI_t_hausaF, highMI_t_igboM, highMI_t_igboF, highMI_t_yorubaM, highMI_t_yorubaF, highMI_t_total)

        #Summary by High SES
        high_t_21 = dummy[('High', '21-30', 'Hausa', 'Male')]['count']+dummy[('High', '21-30', 'Hausa', 'Female')]['count']+dummy[('High', '21-30', 'Igbo', 'Male')]['count']+dummy[('High', '21-30', 'Igbo', 'Female')]['count']+dummy[('High', '21-30', 'Yoruba', 'Male')]['count']+dummy[('High', '21-30', 'Yoruba', 'Female')]['count']
        high_t_31 = dummy[('High', '31-40', 'Hausa', 'Male')]['count']+dummy[('High', '31-40', 'Hausa', 'Female')]['count']+dummy[('High', '31-40', 'Igbo', 'Male')]['count']+dummy[('High', '31-40', 'Igbo', 'Female')]['count']+dummy[('High', '31-40', 'Yoruba', 'Male')]['count']+dummy[('High', '31-40', 'Yoruba', 'Female')]['count']
        high_t_41 = dummy[('High', '41-50', 'Hausa', 'Male')]['count']+dummy[('High', '41-50', 'Hausa', 'Female')]['count']+dummy[('High', '41-50', 'Igbo', 'Male')]['count']+dummy[('High', '41-50', 'Igbo', 'Female')]['count']+dummy[('High', '41-50', 'Yoruba', 'Male')]['count']+dummy[('High', '41-50', 'Yoruba', 'Female')]['count']
        high_t_51 = dummy[('High', '51-60', 'Hausa', 'Male')]['count']+dummy[('High', '51-60', 'Hausa', 'Female')]['count']+dummy[('High', '51-60', 'Igbo', 'Male')]['count']+dummy[('High', '51-60', 'Igbo', 'Female')]['count']+dummy[('High', '51-60', 'Yoruba', 'Male')]['count']+dummy[('High', '51-60', 'Yoruba', 'Female')]['count']
        high_t_61 = dummy[('High', 'Above 60', 'Hausa', 'Male')]['count']+dummy[('High', 'Above 60', 'Hausa', 'Female')]['count']+dummy[('High', 'Above 60', 'Igbo', 'Male')]['count']+dummy[('High', 'Above 60', 'Igbo', 'Female')]['count']+dummy[('High', 'Above 60', 'Yoruba', 'Male')]['count']+dummy[('High', 'Above 60', 'Yoruba', 'Female')]['count']

        high_t_hausaM = dummy[('High', '21-30', 'Hausa', 'Male')]['count']+dummy[('High', '31-40', 'Hausa', 'Male')]['count']+dummy[('High', '41-50', 'Hausa', 'Male')]['count']+dummy[('High', '51-60', 'Hausa', 'Male')]['count']+dummy[('High', 'Above 60', 'Hausa', 'Male')]['count']
        high_t_hausaF = dummy[('High', '21-30', 'Hausa', 'Female')]['count']+dummy[('High', '31-40', 'Hausa', 'Female')]['count']+dummy[('High', '41-50', 'Hausa', 'Female')]['count']+dummy[('High', '51-60', 'Hausa', 'Female')]['count']+dummy[('High', 'Above 60', 'Hausa', 'Female')]['count']
        high_t_igboM = dummy[('High', '21-30', 'Igbo', 'Male')]['count']+dummy[('High', '31-40', 'Igbo', 'Male')]['count']+dummy[('High', '41-50', 'Igbo', 'Male')]['count']+dummy[('High', '51-60', 'Igbo', 'Male')]['count']+dummy[('High', 'Above 60', 'Igbo', 'Male')]['count']
        high_t_igboF = dummy[('High', '21-30', 'Igbo', 'Female')]['count']+dummy[('High', '31-40', 'Igbo', 'Female')]['count']+dummy[('High', '41-50', 'Igbo', 'Female')]['count']+dummy[('High', '51-60', 'Igbo', 'Female')]['count']+dummy[('High', 'Above 60', 'Igbo', 'Female')]['count']
        high_t_yorubaM = dummy[('High', '21-30', 'Yoruba', 'Male')]['count']+dummy[('High', '31-40', 'Yoruba', 'Male')]['count']+dummy[('High', '41-50', 'Yoruba', 'Male')]['count']+dummy[('High', '51-60', 'Yoruba', 'Male')]['count']+dummy[('High', 'Above 60', 'Yoruba', 'Male')]['count']
        high_t_yorubaF = dummy[('High', '21-30', 'Yoruba', 'Female')]['count']+dummy[('High', '31-40', 'Yoruba', 'Female')]['count']+dummy[('High', '41-50', 'Yoruba', 'Female')]['count']+dummy[('High', '51-60', 'Yoruba', 'Female')]['count']+dummy[('High', 'Above 60', 'Yoruba', 'Female')]['count']

        high_t_total = high_t_21+high_t_31+high_t_41+high_t_51+high_t_61

        summary_table_high = """
        <h4 class="display-5 text-center">Summary Table By SES: High Income</h4>
        <table class="table table-bordered table-hover">
        <thead class="">
        <tr><th>LANGUAGES</th><th>Hausa</th><th>&nbsp;</th><th>Igbo</th><th>&nbsp;</th><th>Yoruba</th><th>&nbsp;</th><th>&nbsp;</th></tr>
        <tr><th>AGE GROUPS</th><th>M</th><th>F</th><th>M</th><th>F</th><th>M</th><th>F</th><th>TOTAL</th></tr>
        </thead>
        <tbody>
        <tr><td>21-30</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>31-40</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>41-50</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>51-60</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td>61 above</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><strong>%s</strong></td></tr>
        <tr><td><strong>TOTAL</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td><td><strong>%s</strong></td></tr>
        </tbody>
        </table>
        """ % (dummy[('High', '21-30', 'Hausa', 'Male')]['count'],
                dummy[('High', '21-30', 'Hausa', 'Female')]['count'],
                dummy[('High', '21-30', 'Igbo', 'Male')]['count'],
                dummy[('High', '21-30', 'Igbo', 'Female')]['count'],
                dummy[('High', '21-30', 'Yoruba', 'Male')]['count'],
                dummy[('High', '21-30', 'Yoruba', 'Female')]['count'],
                high_t_21,
                dummy[('High', '31-40', 'Hausa', 'Male')]['count'],
                dummy[('High', '31-40', 'Hausa', 'Female')]['count'],
                dummy[('High', '31-40', 'Igbo', 'Male')]['count'],
                dummy[('High', '31-40', 'Igbo', 'Female')]['count'],
                dummy[('High', '31-40', 'Yoruba', 'Male')]['count'],
                dummy[('High', '31-40', 'Yoruba', 'Female')]['count'],
                high_t_31,
                dummy[('High', '41-50', 'Hausa', 'Male')]['count'],
                dummy[('High', '41-50', 'Hausa', 'Female')]['count'],
                dummy[('High', '41-50', 'Igbo', 'Male')]['count'],
                dummy[('High', '41-50', 'Igbo', 'Female')]['count'],
                dummy[('High', '41-50', 'Yoruba', 'Male')]['count'],
                dummy[('High', '41-50', 'Yoruba', 'Female')]['count'],
                high_t_41,
                dummy[('High', '51-60', 'Hausa', 'Male')]['count'],
                dummy[('High', '51-60', 'Hausa', 'Female')]['count'],
                dummy[('High', '51-60', 'Igbo', 'Male')]['count'],
                dummy[('High', '51-60', 'Igbo', 'Female')]['count'],
                dummy[('High', '51-60', 'Yoruba', 'Male')]['count'],
                dummy[('High', '51-60', 'Yoruba', 'Female')]['count'],
                high_t_51,
                dummy[('High', 'Above 60', 'Hausa', 'Male')]['count'],
                dummy[('High', 'Above 60', 'Hausa', 'Female')]['count'],
                dummy[('High', 'Above 60', 'Igbo', 'Male')]['count'],
                dummy[('High', 'Above 60', 'Igbo', 'Female')]['count'],
                dummy[('High', 'Above 60', 'Yoruba', 'Male')]['count'],
                dummy[('High', 'Above 60', 'Yoruba', 'Female')]['count'],
                high_t_61,
                high_t_hausaM, high_t_hausaF, high_t_igboM, high_t_igboF, high_t_yorubaM, high_t_yorubaF, high_t_total)

        summarySals = """
        <section class="row pl-2 pr-2">
            <section class="col-md-3">
                <section class="list-group">
                  <a href="summary_statistics?cat=ALS" class="list-group-item">Summary by ALS</a>
                  <a href="summary_statistics?cat=SES_ALS" class="list-group-item">Summary by SES-ALS</a>
                </section>
            </section>
            <section class="col-md-7">
                %s
                <hr/>
                %s
                <hr/>
                %s
                <hr/>
                %s
            </section>

            <section class="col-md-2">
            <h4 class="display-5">&nbsp;</h4>

            </section>
        </section>
        """ % (summary_table_low, summary_table_lowMI, summary_table_highMI, summary_table_high)
        return summarySals

    def generate_followups_display(self, data, f_date):
        f_data = ["<tr><td>"+i[0]+"</td><td>"+i[1]+"</td><td>"+i[2]+"</td><td>"+i[3]+"</td><td>"+i[4]+"</td><td>"+i[5]+"</td></tr>" for i in data]

        follow_table = """
            <table class="table table-bordered table-hover">
            <thead>
            <tr><th>ID</th><th>Baseline</th><th>Names</th><th>Phone Numbers</th><th>%s 1</th><th>%s 2</th></tr>
            </thead>
            <tbody>
            %s
            </tbody>
            </table>
        """ % (f_date, f_date, "".join(f_data))

        generateFollow = """
        <section class="row pl-2 pr-2">
            <section class="col-md-2">
                <section class="list-group">
                  <a href="generate_followups?date=Baseline" class="list-group-item">Baseline</a>
                  <a href="generate_followups?date=Six_months" class="list-group-item">6th Month</a>
                  <a href="generate_followups?date=Twelve_months" class="list-group-item">12th Month</a>
                  <a href="generate_followups?date=Eighteen_months" class="list-group-item">18th Month</a>
                </section>
            </section>
            <section class="col-md-10" style="max-height: 350px; overflow-y: scroll;">
            <h4 class="display-5 text-center">Follow Up Table &nbsp; <span><a href="generate_followups?date=%s&export=true" class="btn btn-dark btn-sm">Export to file</a></span></h4>
                %s
            </section>
        </section>
        """ % (f_date, follow_table)
        return generateFollow

    def trace_missing_display(self, data):
        a = 10
        allData = ["<label><a href='staff_participants?id="+i[2]+"&action=preview'>"+i[2]+"</a>, <span>"+i[4]+"</span> <span><em>SES</em>: "+str(i[10])+"</span></label><br/>" for i in data]
        sdata = "".join(allData)
        allDisplay = """
        <section class="w-50 mx-auto">
            %s
        </section>
        """ % sdata
        return allDisplay
