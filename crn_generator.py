# Certificate Recipients Name Generator
# using Python Pillow https://pypi.org/project/Pillow/

from PIL import Image, ImageDraw, ImageFont


with open("certificate_recipients_name_generator/recipients.txt") as fp_recipients:
    
    #recipients_info = []

    for line in fp_recipients:
        fields = line.split(";")
        field_no = fields[0].strip()
        field_name = fields[1].strip()

        #print(field_no)
        #print(field_name)

        # Open image and create black ribbon as a guide for the text
        # Size of the ribbon is w=3508, h=256
        # This black ribbon will be used as a guide for centering the text.
        # Will be commented when published

        image = Image.open('certificate_recipients_name_generator/e-cert_blank.jpg')
        ribbon_width, ribbon_height = (3508, 256)
        #-- ribbon = Image.new('RGB', (ribbon_width, ribbon_height), (0, 0, 0))
        #-- image.paste(ribbon, (0, 1111))

        # Draw image
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype('certificate_recipients_name_generator/Nunito-Regular.ttf', size=150)
        color = 'rgb(2, 113, 194)' #0271c2 blue

        text = field_name
        text_width, text_height = draw.textsize(text, font)
        position = (0+((ribbon_width-text_width)/2), 1090+((ribbon_height-text_height)/2))
        #-- print(position)

        # Draw text
        draw.text(position, text, color, font=font)

        fp = 'certificate_recipients_name_generator/certificates/e-cert_' + field_no + '.jpg'
        image.save(fp, 'JPEG', quality=95)
