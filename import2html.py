#coding=utf-8
#将图片转换成字符串绘制的图片，按照像素点的颜色值来替换
#关于语法的解释，参考https://www.zhihu.com/question/25950466  头一次了解到@是语法糖
from PIL import Image

color = 'Q$|-,.'

def to_html(func):
    html_head = '''
            <html>
              <head>
                <style type="text/css">
                  body {font-family:Monospace; font-size:5px;}
                </style>
              </head>
            <body> '''
    html_tail = '</body></html>'

    def wrapper(img):
        pic_str = func(img)
        pic_str = ''.join(l + ' <br/>' for l in pic_str.splitlines())
        return html_head + pic_str + html_tail

    return wrapper

@to_html
def make_char_img(img):
    pix = img.load()
    pic_str = ''
    width, height = img.size
    for h in xrange(height/4):
        for w in xrange(width/2):
            pic_str += color[int(pix[2*w, 4*h]) * 5 / 255]
        pic_str += '\n'
    return pic_str

def preprocess(img_name):
    img = Image.open(img_name)

    w, h = img.size
    m = max(img.size)
    delta = m / 200.0
    w, h = int(w / delta), int(h / delta)
    img = img.resize((w, h))
    img = img.convert('L')

    return img

def save_to_file(filename, pic_str):
    outfile = open(filename, 'w')
    outfile.write(pic_str)
    outfile.close()

def main():
    img = preprocess('ow1.png')
    pic_str = make_char_img(img)
    save_to_file('char.html', pic_str)

if __name__ == '__main__':
    main()
