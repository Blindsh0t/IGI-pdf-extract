# Main CSV has this many fields, we will try to extract important data which we can find
# from certificates and add those to CSV

import PyPDF2 as pdf
import glob
import os
import re
import csv
import datetime


csv_header = ["vib_a",	"vib_s", 	"vib_of_percentage",	"vib_of_rt", 	"vib_of_amt",	"vib_l",	"vib_cer",	"vib_stno",	"vib_img",	"vib_360", "vib_shape",	"vib_size",	"vib_col",	"vib_cler",	"vib_rap", 	"vib_a_percentage", 	"vib_a_rt", 	"vib_a_amt", 	"vib_ha", 	"vib_fcut_prop",	"vib_fin_pol",	"vib_sym",	"vib_fluro",	"vib_lw", 	"vib_measurement", 	"vib_depth", 	"vib_table", 	"vib_cr", 	"vib_pv", 	"vib_girdle_percentage", 	"vib_culet", 	"vib_lb", 	"vib_certificate_no", 	"vib_certificate_dt",	"vib_tbl_blk", 	"vib_side_blk", 	"vib_tbl_wht", 	"vib_side_wht", 	"vib_tbl_op",
              "vib_cr_op", 	"vib_pv_op ", "vib_gir_op", "vib_milky", 	"vib_tinge", 	"vib_eyeclean", 	"vib_graining", 	"vib_cr_percentage", 	"vib_cr_rt", 	"vib_cr_amt", 	"vib_cr_memo", 	"vib_memo_dt", 	"vib_hold", 	"vib_user", 	"vib_h_dt ",	"vib_h_loc", 	"vib_hold_sold", 	"vib_hs_dt", 	"vib_hs_loc", 	"vib_girdle", 	"vib_fr_loc", 	"vib_box_code", 	"vib_non_accept", 	"vib_note", 	"vib_remark", 	"vib_narration", 	"vib_color_desc", 	"vib_sgm_photo", 	"vib_fno", 	"vib_ftray", 	"vib_parameter_comment", 	"vib_lot", 	"vib_incription", 	"vib_import_remark"]

# Navigate to folder where all PDF's are kept
# will try to extract data online / no need to download if possible
os.chdir("/Users/test_pdf/")

# Make a CSV with max fields headings
with open('Master_sample.csv', 'a') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(csv_header)
    csvfile.close()

# Get all PDF's in that folder
pdf_name = glob.glob("*.pdf")

# Get number of PDF's to iterate over later
number_of_files = len(pdf_name)

# Looping over PDF's
for things in range(number_of_files):
    main_file = pdf_name[things]
    reader = pdf.PdfFileReader(main_file)
    pageObj = reader.getPage(0)
    page_info = pageObj.extractText().lower()

    # There are 2 types of PDF certificate
#     One has less lines and other more
# So we will ceck if this one has less than 100 lines, if so will extract data
    for idx, line in enumerate(page_info.split('\n')):
        a = idx

    if a < 100:
        page_info = page_info.replace('\n', " ").strip(' ')
        usless, *table = page_info.split(" ")
        
#         This unnessary data which we captured, need to dump it out
        to_remove = ('laboratory', 'description', 'grown',
                     'diamond', 'and', 'laserscribe', 'to', 'whom', 'it', 'may', 'concern', ' ', '', 'shape')
#   Loop to remove usless fields so we can grab important fields later on
        table = [e for e in table if e not in to_remove]
#   Getting important fields

        vib_cer = ''.join(table[64]).upper()
        vib_certificate_no = ''.join(table[0]).upper()
        vib_shape = ' '.join(table[2:4]).upper()
        vib_fin_pol = ''.join(table[17]).upper()
        vib_measurement = ' '.join(table[23:29])
        vib_table = ''.join(table[31])
        vib_girdle_percentage = ''.join(table[42]).upper()
        vib_culet = ''.join(table[45]).upper()
        vib_depth = ''.join(table[48])
        vib_size = ''.join(table[6])
        vib_col = ''.join(table[10]).upper()
        vib_cler = ''.join(table[13:15]).upper()
        vib_sym = ''.join(table[21]).upper()
        vib_fluro = ''.join(table[50]).upper()
        vib_parameter_comment = ' '.join(table[52:61]).title()
        vib_lot = ''.join(table[62]).upper()
        get_month = datetime.datetime.strptime(table[68], "%B")
        month = str(get_month.month)
        vib_certificate_dt = month + '/' + \
            table[69].strip(',') + '/' + table[70]
#         Writing those fields to CSV with under right heading

        with open('Master_sample.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            data = [" ",	" ",	" ",	" ",	" ",	" ",	vib_cer,	" ",	" ",	" ",	vib_shape,	vib_size,	vib_col, 	vib_cler, " ",	" ",	" ",	" ",	" ",	" ",	vib_fin_pol, 	vib_sym,	vib_fluro, " ",	vib_measurement,	vib_depth,	vib_table,	" ",	" ",	vib_girdle_percentage,	vib_culet,	" ",	vib_certificate_no,	vib_certificate_dt,	" ",	" ",	" ",	" ",
                    " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", vib_parameter_comment, vib_lot, " ", " "]
            csvwriter.writerow(data)
            csvfile.close()
# repeating the same for big PDF
# This one had too many lines to process so have to find sweet spot [75:513]
# then will get important fields from these lines
    else:
        table_date = re.compile(r'^[0-9]{2}[\/][0-9]{2}[\/][0-9]{4}$')
        for line in page_info.split('\n'):
            if table_date.match(line):
                main = (page_info[75:513])
                main = main.replace('\n', " ").strip(' ')

                main2 = (page_info[100:7000])
                main2 = main2.replace('\n', " ").strip(' ')

        vib_certificate_dt, *table = main.split(" ")
        to_remove = ('measurements', 'report', 'number', 'shape', 'and', 'cutting', 'style',
                     'grading', 'results', 'carat', 'carats', 'weight', 'additional', 'grading', 'information', 'labgrown', 'inscription(s)', 'brilliant', 'clarity', 'character', 'characteris', 'good', "cut", 'cushion', 'clarit', 'characteri', 'characte', 'characteri', 'characterist')
        table = [e for e in table if e not in to_remove]
        vib_cer = ''.join(table[0]).upper()
        vib_certificate_no = ''.join(table[1]).upper()
        vib_shape = ''.join(table[2]).upper()
        vib_measurement = ' '.join(table[3:9])
        vib_size = ''.join(table[9])
        vib_col = ''.join(table[12]).upper()
        vib_cler = ''.join(table[14:16]).upper()
        vib_fin_pol = ''.join(table[17]).upper()

        if 'VERY' in vib_fin_pol:
            vib_fin_pol = "VERY GOOD"

        vib_sym = ''.join(table[19]).upper()

        if 'VERY' in vib_sym:
            vib_sym = "VERY GOOD"

        vib_fluro = ''.join(table[21]).upper()
        vib_parameter_comment = ' '.join(table[25:38]).title()
        vib_lot = ''.join(table[-1]).upper()

        other, *things = main2.split(" ")
        r = re.compile("^[0-9]{2}.|[0-9]%$")
        newlist = list(filter(r.match, things))
        newlist = set(newlist)
        re_move_date = re.compile(r"^[0-9]{2}\S[0-9]{2}\S[0-9]{4}$")
        filtered = [i for i in newlist if not re_move_date.match(i)]
        vib_girdle_percentage = ' '.join(filtered)

        with open('Master_sample.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            data = [" ",	" ",	" ",	" ",	" ",	" ",	vib_cer,	" ",	" ",	" ",	vib_shape,	vib_size,	vib_col, 	vib_cler, " ",	" ",	" ",	" ",	" ",	" ",	vib_fin_pol, 	vib_sym,	vib_fluro, " ",	vib_measurement, " ",	" ",	" ",	" ",	vib_girdle_percentage,	" ",	" ",	vib_certificate_no,	vib_certificate_dt,	" ",	" ",	" ",	" ",
                    " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", vib_parameter_comment, vib_lot, " ", " "]
            csvwriter.writerow(data)
            csvfile.close()
#             Above all process almost same as for small PDF

    print("DONE !!  - > " + main_file)
