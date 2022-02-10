"""
    Build 2018
    Purpose:
    A browser-oriented program to keep up with the groups of participants recruited for a study.

"""
#Import default and third-party python packages.
import os
#import subprocess
import cherrypy as mainframe
import webbrowser as webfront
import datetime as dt

#Import custom application libraries from core.
from app_views import View
from app_model import Model
from app_helpers import GenerateFollowUpSeries, ValId, ProcessSummary

#subprocess.call('start', shell=True)
class Catalogue(object):
    #Class variables
    url = "http://127.0.0.1:4000"
    today_date = dt.date.today()
    field_data = {}

    def __init__(self):
        self.display = View()
        webfront.open(self.url)

        #Create all directories for application
        if not os.path.exists("database"):
            os.makedirs("database")

        #Check for General Sender Settings
        try:
            dbase = Model()
            field_staff = dbase.view_field_staff_information()
        except Exception as e:
            #No Classical error to be raised at Initialization
            field_staff_available = False
        else:
            if field_staff == []:
                self.field_staff_available = False
                self.field_staff_name = ""
            else:
                self.field_staff_available = True
                self.field_staff_name = field_staff[0][1].capitalize()

    @mainframe.expose(['staff_participants'])
    def index(self, **kwargs):
        dbase = Model()
        """
            Initialization of the application
            Display of form for input for participants
        """
        if self.field_staff_available == True:
            participants = {}
            participants['all_participants'] = dbase.view_participant_log()
            participants['count_participants'] = len(dbase.view_participant_log())
            if kwargs == {}:
                output = self.display.field_staff_participants(participants)
            elif all(keys in kwargs for keys in ("q_base_date", "q_q_id", "q_id", "q_names", "q_sex", "q_tribe", "q_age_cat", "q_pnum_1", "q_pnum_2", "q_ses")):
                try:
                    dbase.insert_participant_log(kwargs['q_base_date'], kwargs['q_q_id'], kwargs['q_id'], kwargs['q_names'], kwargs['q_sex'], kwargs['q_tribe'], kwargs['q_age_cat'], kwargs['q_pnum_1'], kwargs['q_pnum_2'], kwargs['q_ses'])
                except Exception as e:
                    participants['insert_error'] = """
                    <section class="alert alert-danger alert-dismissible fade show mt-3">
                      <strong>Database Error!</strong><br/>%s.
                    </section>
                    """ % str(e)
                    output = self.display.field_staff_participants(participants)
                else:
                    participants['insert_success'] = """
                    <section class="alert alert-success alert-dismissible fade show mt-3">
                      <strong>Participant Succefully Added!</strong><br/> %s, has been added to the database.<br/>
                      <button type="button" class="btn btn-secondary btn-md btn-block"><a href="staff_participants" class="text-white">Add Another Participant</a></button>
                    </section>
                    """ % kwargs['q_names'].capitalize()
                    output = self.display.field_staff_participants(participants)
            elif "id" in kwargs.keys():
                participants['details'] = dbase.view_participant_log_by_id(kwargs['id'])
                if "action" in kwargs.keys() and kwargs['action'] == "preview":
                    participants['data'] = "preview"
                    #participants['follow_up'] = GenerateFollowUpSeries(dt.datetime.strptime(participants['details'][0][8], '%Y-%m-%d')).gen24HrsRecallSeries()
                    participants['follow_up'] = GenerateFollowUpSeries(participants['details'][0][1]).gen24HrsRecallSeries()
                    #participants['follow_up_alerts'] = GenerateFollowUpSeries(dt.datetime.strptime(participants['details'][0][1], '%Y-%m-%d')).gen24HrsRecallAlerts()
                    output = self.display.field_staff_participants(participants)
                    #14:27:05.223368
                    #'%Y-%m-%d %H:%M:%S.%f'
                elif "action" in kwargs.keys() and kwargs['action'] == "edit":
                    if "edit_sex" in kwargs.keys():
                        try:
                            dbase.update_participant_log(kwargs['id'], kwargs['edit_base_date'],
                            kwargs['edit_names'], kwargs['edit_sex'], kwargs['edit_tribe'], kwargs['edit_age_cat'],
                            kwargs['edit_pnum_1'], kwargs['edit_pnum_2'], kwargs['edit_ses'])
                        except Exception as e:
                            raise
                        else:
                            participants['data'] = "update"
                            output = self.display.field_staff_participants(participants)
                    else:
                        participants['data'] = "edit"
                        #elif all(keys in kwargs for keys in ("ffq_base_date", "ffq_q_id", "ffq_24_id", "ffq_names", "ffq_sex", "ffq_tribe", "ffq_age_cat", "ffq_pnum_1", "ffq_pnum_2")):
                        output = self.display.field_staff_participants(participants)
        else:
            if kwargs == {}:
                output = self.display.field_staff_form()
            elif "ffq_staff_name" in kwargs.keys():
                try:
                    dbase.insert_field_staff_information(kwargs['ffq_staff_name'])
                except Exception as e:
                    output = """
                    <section class="alert alert-danger alert-dismissible fade show w-50 mx-auto mt-3">
                      <strong>Database Error!</strong><br/>%s.
                    </section>
                    """ % str(e)
                else:
                    self.field_staff_available = True
                    self.field_staff_name = dbase.view_field_staff_information()[0][1].capitalize()
                    output = self.display.field_staff_form_success()
        return self.display.page_open(), self.display.page_nav(self.field_staff_available, self.field_staff_name), self.display.field_staff_display(str(output)), self.display.page_close(self.today_date.strftime("%A, %B %d, %Y."))

    @mainframe.expose()
    def summary_statistics(self, **kwargs):
        dbase = Model()
        optsummary = {}
        if "cat" in kwargs.keys() and kwargs['cat'] == "ALS":
            output = self.display.summary_statistics_als(ProcessSummary(dbase.view_participant_log()).summaryALS())
        elif "cat" in kwargs.keys() and kwargs['cat'] == "SES_ALS":
            output = self.display.summary_statistics_sals(ProcessSummary(dbase.view_participant_log()).summarySALS())
        return self.display.page_open(), self.display.page_nav(self.field_staff_available, self.field_staff_name), str(output), self.display.page_close(self.today_date.strftime("%A, %B %d, %Y."))

    @mainframe.expose()
    def trace_missing(self):
        dbase = Model()
        output = self.display.trace_missing_display(dbase.view_participant_log())
        return self.display.page_open(), self.display.page_nav(self.field_staff_available, self.field_staff_name), str(output), self.display.page_close(self.today_date.strftime("%A, %B %d, %Y."))

    @mainframe.expose()
    def generate_followups(self, **kwargs):
        dbase = Model()
        series_data = []
        GenerateFollowUpSeries
        for each_part in dbase.view_participant_log():
            series_all = GenerateFollowUpSeries(each_part[1])
            s_a = series_all.gen24HrsRecallSeries()
            if "date" in kwargs.keys() and kwargs['date'] == "Baseline":
                series_data.append([ValId.new_id(each_part[2]), s_a['Baseline_1'], each_part[4], each_part[8]+", "+each_part[9], s_a['Baseline_1'], s_a['Baseline_2']])
            if "date" in kwargs.keys() and kwargs['date'] == "Six_months":
                series_data.append([ValId.new_id(each_part[2]), s_a['Baseline_1'], each_part[4], each_part[8]+", "+each_part[9], s_a['Six_months_1'], s_a['Six_months_2']])
            elif "date" in kwargs.keys() and kwargs['date'] == "Twelve_months":
                series_data.append([ValId.new_id(each_part[2]), s_a['Baseline_1'], each_part[4], each_part[8]+", "+each_part[9], s_a['Twelve_months_1'], s_a['Twelve_months_2']])
            elif "date" in kwargs.keys() and kwargs['date'] == "Eighteen_months":
                series_data.append([ValId.new_id(each_part[2]), s_a['Baseline_1'], each_part[4], each_part[8]+", "+each_part[9], s_a['Eighteen_months_1'], s_a['Eighteen_months_2']])

        #export date to excel or csv file
        if "export" in kwargs.keys():
            import csv
            with open("database/"+kwargs['date']+".csv",'w') as datafile:
                header = ['ID', 'Baseline', 'Names', 'Phone Numbers', kwargs['date']+" 1", kwargs['date']+" 2"]
                writer = csv.writer(datafile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(header)
                for i in series_data:
                    writer.writerow(i)

        output = self.display.generate_followups_display(series_data, kwargs['date'])
        return self.display.page_open(), self.display.page_nav(self.field_staff_available, self.field_staff_name), str(output), self.display.page_close(self.today_date.strftime("%A, %B %d, %Y."))

    @mainframe.expose()
    def exit_application(self):
        mainframe.engine.exit()
        output = """
            <section class="alert alert-info alert-dismissible fade show w-50 mx-auto mt-3 p-3">
              <strong>Application Exit!</strong><br/>
                  <section class="text-center">
                  <label>You have closed the FVS Recruitment Tracker</label><br/>
                  <label>Good Bye</label>
              </section>
            </section>
        """
        return self.display.page_open(), self.display.page_nav(self.field_staff_available, self.field_staff_name), str(output), self.display.page_close(self.today_date.strftime("%A, %B %d, %Y."))
#Initialization of application on custom server and port
if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    conf = {"global": {"server.socket_host": '127.0.0.1',
                        "server.socket_port": 4000,
                        "server.thread_pool": 10},
            "/": {"tools.staticdir.on": True,
                    "tools.staticdir.dir": current_dir,
                    "tools.sessions.on": True}
                }
    mainframe.quickstart(Catalogue(), "/", config=conf)
