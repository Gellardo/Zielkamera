#!/usr/bin/env/python3

import cv2
import argparse
import numpy as np

def processVideo(video, offset=100, finish_width=2, progress=False):
    cap = cv2.VideoCapture(video)
    final = None
    while True:
        ret, frame = cap.read()

        if ret:
            finish_line = frame[:,offset:offset+finish_width]
            if final is None:
                final = np.array(finish_line)
            else:
                final = np.append(final, finish_line, axis=1)

            shape = frame.shape
            for y in range(shape[0]):
                frame[y][offset] = [255,255,255]

            if progress:
                cv2.imshow("frame",frame)
                cv2.imshow("final",final)
                cv2.waitKey(1)
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    if progress:
        cv2.imshow("final",final)
        cv2.waitKey(2000)
    cv2.destroyAllWindows()
    return final


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert video to striped image')
    parser.add_argument('video', help='the original video')
    parser.add_argument('image', help='the output image')
    parser.add_argument('--finish_offset', type=int, default=100, help='the vertical offset of the finish line')
    parser.add_argument('--finish_width',  type=int, default=2, help='how many pixels to extract per frame')
    parser.add_argument('--progress', default=False, action='store_true', help='show images being processed')

    args = parser.parse_args()
    processVideo(args.video, offset=args.finish_offset, finish_width=args.finish_width, progress=args.progress)
