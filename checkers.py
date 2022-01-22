################################################
#                                              #
# Institute: University of Sussex              #
# Project Type: Assignment                     #
#                                              #
# G6019: Knowledge & Reasoning                 #
# Minimax With Alpha-Beta Pruning Agent        #
# Instructor: Dr Ronald Grau                   #
#                                              #
################################################
#                                              #
# Script Writor: Equosile (jk488@sussex.ac.uk) #
# https://github.com/Equosile/Turtle-Checkers  #
#                                              #
################################################
#
# The Python 3 Library Named "Turtle" Is Tested In This Project.
# The Same Licence Of Python Libraries Has Been Applied For This Project.
#
###################################################################################
#                                                                                 # 
# The BSD Zero Clause License (0BSD)                                              #
#                                                                                 #
# Copyright (c) [year] [company].                                                 #
#                                                                                 #
# Permission to use, copy, modify, and/or distribute this software for any        #
# purpose with or without fee is hereby granted.                                  #
#                                                                                 #
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH   #
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY     #
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,    #
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM     #
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR   #
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR          #
# PERFORMANCE OF THIS SOFTWARE.                                                   #
#                                                                                 #
###################################################################################
#




#FOR LOCAL SYSTEM
import turtle
import random
import time
import copy
import math

#WINDOW SIZE (GAME BOARD)
LENGTH_UNIT = 3
SIZE_MULTIPLIER = 7
BOARD_SIZE = 100
SCREEN_WIDTH = BOARD_SIZE*SIZE_MULTIPLIER + BOARD_SIZE*2
SCREEN_HEIGHT = BOARD_SIZE*SIZE_MULTIPLIER

#COLOURS
bg_colour = "black"
board_colour = "darkgreen"
check_colour_A = "darkred"
check_colour_B = "antiquewhite"
check_colour_C = "firebrick"
debug_colour = "white"
TYPEFACE = "Courier"

#OUTSKIRT WINDOW => checkers_app
checkers_app = turtle.Screen()
checkers_app.title("Checkers by Python 3 Turtle")
checkers_app.bgcolor(bg_colour)
checkers_app.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
#WINDOW UPDATE MODULE
checkers_app.tracer(0)

#GAME BOARD
game_board_A1 = turtle.Turtle()
game_board_A2 = turtle.Turtle()
game_board_A3 = turtle.Turtle()
game_board_A4 = turtle.Turtle()
game_board_A5 = turtle.Turtle()
game_board_A6 = turtle.Turtle()
game_board_A7 = turtle.Turtle()
game_board_A8 = turtle.Turtle()
game_board_A9 = turtle.Turtle()
game_board_A10 = turtle.Turtle()
game_board_A11 = turtle.Turtle()
game_board_A12 = turtle.Turtle()
game_board_A13 = turtle.Turtle()
game_board_A14 = turtle.Turtle()
game_board_A15 = turtle.Turtle()
game_board_A16 = turtle.Turtle()
game_board_A17 = turtle.Turtle()
game_board_A18 = turtle.Turtle()
game_board_A19 = turtle.Turtle()
game_board_A20 = turtle.Turtle()
game_board_A21 = turtle.Turtle()
game_board_A22 = turtle.Turtle()
game_board_A23 = turtle.Turtle()
game_board_A24 = turtle.Turtle()
game_board_A25 = turtle.Turtle()
game_board_A26 = turtle.Turtle()
game_board_A27 = turtle.Turtle()
game_board_A28 = turtle.Turtle()
game_board_A29 = turtle.Turtle()
game_board_A30 = turtle.Turtle()
game_board_A31 = turtle.Turtle()
game_board_A32 = turtle.Turtle()

#Animation Speed; 0 = Maximum
game_board_A1.speed(0)
game_board_A2.speed(0)
game_board_A3.speed(0)
game_board_A4.speed(0)
game_board_A5.speed(0)
game_board_A6.speed(0)
game_board_A7.speed(0)
game_board_A8.speed(0)
game_board_A9.speed(0)
game_board_A10.speed(0)
game_board_A11.speed(0)
game_board_A12.speed(0)
game_board_A13.speed(0)
game_board_A14.speed(0)
game_board_A15.speed(0)
game_board_A16.speed(0)
game_board_A17.speed(0)
game_board_A18.speed(0)
game_board_A19.speed(0)
game_board_A20.speed(0)
game_board_A21.speed(0)
game_board_A22.speed(0)
game_board_A23.speed(0)
game_board_A24.speed(0)
game_board_A25.speed(0)
game_board_A26.speed(0)
game_board_A27.speed(0)
game_board_A28.speed(0)
game_board_A29.speed(0)
game_board_A30.speed(0)
game_board_A31.speed(0)
game_board_A32.speed(0)
game_board_A1.shape("square")
game_board_A2.shape("square")
game_board_A3.shape("square")
game_board_A4.shape("square")
game_board_A5.shape("square")
game_board_A6.shape("square")
game_board_A7.shape("square")
game_board_A8.shape("square")
game_board_A9.shape("square")
game_board_A10.shape("square")
game_board_A11.shape("square")
game_board_A12.shape("square")
game_board_A13.shape("square")
game_board_A14.shape("square")
game_board_A15.shape("square")
game_board_A16.shape("square")
game_board_A17.shape("square")
game_board_A18.shape("square")
game_board_A19.shape("square")
game_board_A20.shape("square")
game_board_A21.shape("square")
game_board_A22.shape("square")
game_board_A23.shape("square")
game_board_A24.shape("square")
game_board_A25.shape("square")
game_board_A26.shape("square")
game_board_A27.shape("square")
game_board_A28.shape("square")
game_board_A29.shape("square")
game_board_A30.shape("square")
game_board_A31.shape("square")
game_board_A32.shape("square")
game_board_A1.color(board_colour)
game_board_A2.color(board_colour)
game_board_A3.color(board_colour)
game_board_A4.color(board_colour)
game_board_A5.color(board_colour)
game_board_A6.color(board_colour)
game_board_A7.color(board_colour)
game_board_A8.color(board_colour)
game_board_A9.color(board_colour)
game_board_A10.color(board_colour)
game_board_A11.color(board_colour)
game_board_A12.color(board_colour)
game_board_A13.color(board_colour)
game_board_A14.color(board_colour)
game_board_A15.color(board_colour)
game_board_A16.color(board_colour)
game_board_A17.color(board_colour)
game_board_A18.color(board_colour)
game_board_A19.color(board_colour)
game_board_A20.color(board_colour)
game_board_A21.color(board_colour)
game_board_A22.color(board_colour)
game_board_A23.color(board_colour)
game_board_A24.color(board_colour)
game_board_A25.color(board_colour)
game_board_A26.color(board_colour)
game_board_A27.color(board_colour)
game_board_A28.color(board_colour)
game_board_A29.color(board_colour)
game_board_A30.color(board_colour)
game_board_A31.color(board_colour)
game_board_A32.color(board_colour)
#Stretching the shape
game_board_A1.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A2.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A3.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A4.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A5.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A6.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A7.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A8.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A9.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A10.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A11.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A12.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A13.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A14.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A15.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A16.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A17.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A18.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A19.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A20.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A21.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A22.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A23.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A24.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A25.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A26.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A27.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A28.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A29.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A30.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A31.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
game_board_A32.shapesize(stretch_wid=LENGTH_UNIT, stretch_len=LENGTH_UNIT)
#Draw Lines
game_board_A1.penup()
game_board_A2.penup()
game_board_A3.penup()
game_board_A4.penup()
game_board_A5.penup()
game_board_A6.penup()
game_board_A7.penup()
game_board_A8.penup()
game_board_A9.penup()
game_board_A10.penup()
game_board_A11.penup()
game_board_A12.penup()
game_board_A13.penup()
game_board_A14.penup()
game_board_A15.penup()
game_board_A16.penup()
game_board_A17.penup()
game_board_A18.penup()
game_board_A19.penup()
game_board_A20.penup()
game_board_A21.penup()
game_board_A22.penup()
game_board_A23.penup()
game_board_A24.penup()
game_board_A25.penup()
game_board_A26.penup()
game_board_A27.penup()
game_board_A28.penup()
game_board_A29.penup()
game_board_A30.penup()
game_board_A31.penup()
game_board_A32.penup()
#Centre(0,0)
game_board_A1.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + LENGTH_UNIT*10 + BOARD_SIZE)
game_board_A2.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*5 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + LENGTH_UNIT*10 + BOARD_SIZE)
game_board_A3.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*9 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + LENGTH_UNIT*10 + BOARD_SIZE)
game_board_A4.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*13 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + LENGTH_UNIT*10 + BOARD_SIZE)
game_board_A5.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*3 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*3 + BOARD_SIZE))
game_board_A6.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*7 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*3 + BOARD_SIZE))
game_board_A7.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*11 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*3 + BOARD_SIZE))
game_board_A8.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*15 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*3 + BOARD_SIZE))
game_board_A9.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*5 + BOARD_SIZE))
game_board_A10.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*5 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*5 + BOARD_SIZE))
game_board_A11.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*9 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*5 + BOARD_SIZE))
game_board_A12.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*13 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*5 + BOARD_SIZE))
game_board_A13.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*3 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*7 + BOARD_SIZE))
game_board_A14.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*7 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*7 + BOARD_SIZE))
game_board_A15.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*11 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*7 + BOARD_SIZE))
game_board_A16.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*15 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*7 + BOARD_SIZE))
game_board_A17.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*9 + BOARD_SIZE))
game_board_A18.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*5 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*9 + BOARD_SIZE))
game_board_A19.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*9 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*9 + BOARD_SIZE))
game_board_A20.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*13 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*9 + BOARD_SIZE))
game_board_A21.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*3 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*11 + BOARD_SIZE))
game_board_A22.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*7 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*11 + BOARD_SIZE))
game_board_A23.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*11 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*11 + BOARD_SIZE))
game_board_A24.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*15 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*11 + BOARD_SIZE))
game_board_A25.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*13 + BOARD_SIZE))
game_board_A26.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*5 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*13 + BOARD_SIZE))
game_board_A27.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*9 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*13 + BOARD_SIZE))
game_board_A28.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*13 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*13 + BOARD_SIZE))
game_board_A29.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*3 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*15 + BOARD_SIZE))
game_board_A30.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*7 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*15 + BOARD_SIZE))
game_board_A31.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*11 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*15 + BOARD_SIZE))
game_board_A32.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*15 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*15 + BOARD_SIZE))

#TOKENS("MEN")
piece_A_1 = turtle.Turtle()
piece_A_2 = turtle.Turtle()
piece_A_3 = turtle.Turtle()
piece_A_4 = turtle.Turtle()
piece_A_5 = turtle.Turtle()
piece_A_6 = turtle.Turtle()
piece_A_7 = turtle.Turtle()
piece_A_8 = turtle.Turtle()
piece_A_9 = turtle.Turtle()
piece_A_10 = turtle.Turtle()
piece_A_11 = turtle.Turtle()
piece_A_12 = turtle.Turtle()
piece_A_1.speed(0)
piece_A_2.speed(0)
piece_A_3.speed(0)
piece_A_4.speed(0)
piece_A_5.speed(0)
piece_A_6.speed(0)
piece_A_7.speed(0)
piece_A_8.speed(0)
piece_A_9.speed(0)
piece_A_10.speed(0)
piece_A_11.speed(0)
piece_A_12.speed(0)
piece_A_1.shape("circle")
piece_A_2.shape("circle")
piece_A_3.shape("circle")
piece_A_4.shape("circle")
piece_A_5.shape("circle")
piece_A_6.shape("circle")
piece_A_7.shape("circle")
piece_A_8.shape("circle")
piece_A_9.shape("circle")
piece_A_10.shape("circle")
piece_A_11.shape("circle")
piece_A_12.shape("circle")
piece_A_1.color(check_colour_A)
piece_A_2.color(check_colour_A)
piece_A_3.color(check_colour_A)
piece_A_4.color(check_colour_A)
piece_A_5.color(check_colour_A)
piece_A_6.color(check_colour_A)
piece_A_7.color(check_colour_A)
piece_A_8.color(check_colour_A)
piece_A_9.color(check_colour_A)
piece_A_10.color(check_colour_A)
piece_A_11.color(check_colour_A)
piece_A_12.color(check_colour_A)
piece_A_1.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_A_2.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_A_3.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_A_4.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_A_5.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_A_6.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_A_7.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_A_8.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_A_9.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_A_10.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_A_11.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_A_12.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_A_1.penup()
piece_A_2.penup()
piece_A_3.penup()
piece_A_4.penup()
piece_A_5.penup()
piece_A_6.penup()
piece_A_7.penup()
piece_A_8.penup()
piece_A_9.penup()
piece_A_10.penup()
piece_A_11.penup()
piece_A_12.penup()

#TOKENS("AI")
piece_B_1 = turtle.Turtle()
piece_B_2 = turtle.Turtle()
piece_B_3 = turtle.Turtle()
piece_B_4 = turtle.Turtle()
piece_B_5 = turtle.Turtle()
piece_B_6 = turtle.Turtle()
piece_B_7 = turtle.Turtle()
piece_B_8 = turtle.Turtle()
piece_B_9 = turtle.Turtle()
piece_B_10 = turtle.Turtle()
piece_B_11 = turtle.Turtle()
piece_B_12 = turtle.Turtle()
piece_B_1.speed(0)
piece_B_2.speed(0)
piece_B_3.speed(0)
piece_B_4.speed(0)
piece_B_5.speed(0)
piece_B_6.speed(0)
piece_B_7.speed(0)
piece_B_8.speed(0)
piece_B_9.speed(0)
piece_B_10.speed(0)
piece_B_11.speed(0)
piece_B_12.speed(0)
piece_B_1.shape("circle")
piece_B_2.shape("circle")
piece_B_3.shape("circle")
piece_B_4.shape("circle")
piece_B_5.shape("circle")
piece_B_6.shape("circle")
piece_B_7.shape("circle")
piece_B_8.shape("circle")
piece_B_9.shape("circle")
piece_B_10.shape("circle")
piece_B_11.shape("circle")
piece_B_12.shape("circle")
piece_B_1.color(check_colour_B)
piece_B_2.color(check_colour_B)
piece_B_3.color(check_colour_B)
piece_B_4.color(check_colour_B)
piece_B_5.color(check_colour_B)
piece_B_6.color(check_colour_B)
piece_B_7.color(check_colour_B)
piece_B_8.color(check_colour_B)
piece_B_9.color(check_colour_B)
piece_B_10.color(check_colour_B)
piece_B_11.color(check_colour_B)
piece_B_12.color(check_colour_B)
piece_B_1.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_B_2.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_B_3.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_B_4.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_B_5.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_B_6.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_B_7.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_B_8.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_B_9.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_B_10.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_B_11.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_B_12.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_B_1.penup()
piece_B_2.penup()
piece_B_3.penup()
piece_B_4.penup()
piece_B_5.penup()
piece_B_6.penup()
piece_B_7.penup()
piece_B_8.penup()
piece_B_9.penup()
piece_B_10.penup()
piece_B_11.penup()
piece_B_12.penup()

#PROMOTION TOKEN FOR HUMAN
init_X = (-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE
init_Y = (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE
piece_AA_1 = turtle.Turtle(visible=False)
piece_AA_1.speed(0)
piece_AA_1.shape("turtle")
piece_AA_1.color(check_colour_A)
piece_AA_1.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_AA_1.penup()
piece_AA_1.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
piece_AA_2 = turtle.Turtle(visible=False)
piece_AA_2.speed(0)
piece_AA_2.shape("turtle")
piece_AA_2.color(check_colour_A)
piece_AA_2.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_AA_2.penup()
piece_AA_2.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
piece_AA_3 = turtle.Turtle(visible=False)
piece_AA_3.speed(0)
piece_AA_3.shape("turtle")
piece_AA_3.color(check_colour_A)
piece_AA_3.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_AA_3.penup()
piece_AA_3.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
piece_AA_4 = turtle.Turtle(visible=False)
piece_AA_4.speed(0)
piece_AA_4.shape("turtle")
piece_AA_4.color(check_colour_A)
piece_AA_4.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_AA_4.penup()
piece_AA_4.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
piece_AA_5 = turtle.Turtle(visible=False)
piece_AA_5.speed(0)
piece_AA_5.shape("turtle")
piece_AA_5.color(check_colour_A)
piece_AA_5.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_AA_5.penup()
piece_AA_5.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
piece_AA_6 = turtle.Turtle(visible=False)
piece_AA_6.speed(0)
piece_AA_6.shape("turtle")
piece_AA_6.color(check_colour_A)
piece_AA_6.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_AA_6.penup()
piece_AA_6.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
piece_AA_7 = turtle.Turtle(visible=False)
piece_AA_7.speed(0)
piece_AA_7.shape("turtle")
piece_AA_7.color(check_colour_A)
piece_AA_7.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_AA_7.penup()
piece_AA_7.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
piece_AA_8 = turtle.Turtle(visible=False)
piece_AA_8.speed(0)
piece_AA_8.shape("turtle")
piece_AA_8.color(check_colour_A)
piece_AA_8.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_AA_8.penup()
piece_AA_8.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
piece_AA_9 = turtle.Turtle(visible=False)
piece_AA_9.speed(0)
piece_AA_9.shape("turtle")
piece_AA_9.color(check_colour_A)
piece_AA_9.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_AA_9.penup()
piece_AA_9.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
piece_AA_10 = turtle.Turtle(visible=False)
piece_AA_10.speed(0)
piece_AA_10.shape("turtle")
piece_AA_10.color(check_colour_A)
piece_AA_10.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_AA_10.penup()
piece_AA_10.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
piece_AA_11 = turtle.Turtle(visible=False)
piece_AA_11.speed(0)
piece_AA_11.shape("turtle")
piece_AA_11.color(check_colour_A)
piece_AA_11.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_AA_11.penup()
piece_AA_11.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
piece_AA_12 = turtle.Turtle(visible=False)
piece_AA_12.speed(0)
piece_AA_12.shape("turtle")
piece_AA_12.color(check_colour_A)
piece_AA_12.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_AA_12.penup()
piece_AA_12.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)

#PROMOTION TOKEN FOR AI
piece_BB_1 = turtle.Turtle(visible=False)
piece_BB_1.speed(0)
piece_BB_1.shape("turtle")
piece_BB_1.color(check_colour_B)
piece_BB_1.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_BB_1.penup()
piece_BB_1.goto(init_X, init_Y)
piece_BB_2 = turtle.Turtle(visible=False)
piece_BB_2.speed(0)
piece_BB_2.shape("turtle")
piece_BB_2.color(check_colour_B)
piece_BB_2.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_BB_2.penup()
piece_BB_2.goto(init_X, init_Y)
piece_BB_3 = turtle.Turtle(visible=False)
piece_BB_3.speed(0)
piece_BB_3.shape("turtle")
piece_BB_3.color(check_colour_B)
piece_BB_3.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_BB_3.penup()
piece_BB_3.goto(init_X, init_Y)
piece_BB_4 = turtle.Turtle(visible=False)
piece_BB_4.speed(0)
piece_BB_4.shape("turtle")
piece_BB_4.color(check_colour_B)
piece_BB_4.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_BB_4.penup()
piece_BB_4.goto(init_X, init_Y)
piece_BB_5 = turtle.Turtle(visible=False)
piece_BB_5.speed(0)
piece_BB_5.shape("turtle")
piece_BB_5.color(check_colour_B)
piece_BB_5.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_BB_5.penup()
piece_BB_5.goto(init_X, init_Y)
piece_BB_6 = turtle.Turtle(visible=False)
piece_BB_6.speed(0)
piece_BB_6.shape("turtle")
piece_BB_6.color(check_colour_B)
piece_BB_6.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_BB_6.penup()
piece_BB_6.goto(init_X, init_Y)
piece_BB_7 = turtle.Turtle(visible=False)
piece_BB_7.speed(0)
piece_BB_7.shape("turtle")
piece_BB_7.color(check_colour_B)
piece_BB_7.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_BB_7.penup()
piece_BB_7.goto(init_X, init_Y)
piece_BB_8 = turtle.Turtle(visible=False)
piece_BB_8.speed(0)
piece_BB_8.shape("turtle")
piece_BB_8.color(check_colour_B)
piece_BB_8.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_BB_8.penup()
piece_BB_8.goto(init_X, init_Y)
piece_BB_9 = turtle.Turtle(visible=False)
piece_BB_9.speed(0)
piece_BB_9.shape("turtle")
piece_BB_9.color(check_colour_B)
piece_BB_9.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_BB_9.penup()
piece_BB_9.goto(init_X, init_Y)
piece_BB_10 = turtle.Turtle(visible=False)
piece_BB_10.speed(0)
piece_BB_10.shape("turtle")
piece_BB_10.color(check_colour_B)
piece_BB_10.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_BB_10.penup()
piece_BB_10.goto(init_X, init_Y)
piece_BB_11 = turtle.Turtle(visible=False)
piece_BB_11.speed(0)
piece_BB_11.shape("turtle")
piece_BB_11.color(check_colour_B)
piece_BB_11.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_BB_11.penup()
piece_BB_11.goto(init_X, init_Y)
piece_BB_12 = turtle.Turtle(visible=False)
piece_BB_12.speed(0)
piece_BB_12.shape("turtle")
piece_BB_12.color(check_colour_B)
piece_BB_12.shapesize(stretch_wid=(LENGTH_UNIT-1), stretch_len=(LENGTH_UNIT-1))
piece_BB_12.penup()
piece_BB_12.goto(init_X, init_Y)

#GHOST TOKEN
#piece_C_0 = turtle.Turtle()
piece_C_0 = turtle.Turtle(visible=False)
piece_C_0.speed(0)
piece_C_0.shape("circle")
piece_C_0.color(check_colour_C)
piece_C_0.fillcolor("")
piece_C_0.shapesize(stretch_wid=(LENGTH_UNIT-2), stretch_len=(LENGTH_UNIT-2))
piece_C_0.penup()
piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)

#BUTTONS
button_A_0 = turtle.Turtle()
button_A_0.speed(0)
button_A_0.shape("square")
button_A_0.color(debug_colour)
button_A_0.shapesize(stretch_wid=(LENGTH_UNIT-1),stretch_len=(LENGTH_UNIT+1))
button_A_0.penup()
button_A_0.goto((BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - ((BOARD_SIZE*3)/2))

#STRING
FONT_SIZE = 16
#A: GENERAL COORDINATES
#B: INDICATING INDEX (FROM MOUSE-POINTER COORDINATES)
#C: ASKING INDEX (WHERE A TOKEN IS PLACED)
#D: AI STRENGTH
#E: WIN
debug_pen_A = turtle.Turtle()
debug_pen_B = turtle.Turtle()
debug_pen_C = turtle.Turtle()
debug_pen_D = turtle.Turtle()
debug_pen_E = turtle.Turtle()
#Animation Speed
debug_pen_A.speed(0)
debug_pen_B.speed(0)
debug_pen_C.speed(0)
debug_pen_D.speed(0)
debug_pen_E.speed(0)
debug_pen_A.color(debug_colour)
debug_pen_B.color(debug_colour)
debug_pen_C.color(debug_colour)
debug_pen_D.color(debug_colour)
debug_pen_E.color(debug_colour)
#Drawing Style
debug_pen_A.penup()
debug_pen_B.penup()
debug_pen_C.penup()
debug_pen_D.penup()
debug_pen_E.penup()
#Focusing pen only
debug_pen_A.hideturtle()
debug_pen_B.hideturtle()
debug_pen_C.hideturtle()
debug_pen_D.hideturtle()
debug_pen_E.hideturtle()
debug_pen_A.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + (BOARD_SIZE/2), (BOARD_SIZE*SIZE_MULTIPLIER)/2 - (BOARD_SIZE/2))
debug_pen_B.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + (BOARD_SIZE/2), (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
debug_pen_C.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE*4, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
debug_pen_D.goto((BOARD_SIZE*SIZE_MULTIPLIER)/2 - ((BOARD_SIZE*2)/3), (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
debug_pen_E.goto((BOARD_SIZE*SIZE_MULTIPLIER)/2 - (BOARD_SIZE/3), (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE*2)
#ONLY FOR DEBUGGING LEVEL
debug_pen_A.write("( x , y )", align="center", font=(TYPEFACE, FONT_SIZE, "normal"))
debug_pen_B.write("?> ", align="center", font=(TYPEFACE, FONT_SIZE, "normal"))
debug_pen_C.write("( obj_x , obj_y )", align="center", font=(TYPEFACE, FONT_SIZE, "normal"))
debug_pen_D.write("AI Strength: ", align="center", font=(TYPEFACE, FONT_SIZE, "normal"))
debug_pen_E.write("GAME END: ", align="center", font=(TYPEFACE, FONT_SIZE, "normal"))
#CANVAS
debug_canvas = turtle.getcanvas()

####################
# GLOBAL VARIABLES #
####################

#debug_pen_B, Integrity Check
debug_record = 0

#Ghost Move
asking_token = 0
asking_cor = [0, 0]

#debug_pen_C
debug_Xcor = 0.0
debug_Ycor = 0.0

#History Tracker; Index#0=Bottom_Left=Board_Piece_#1, 1=Player, 0=Empty, -1=AI
list_Current = [1,1,1,1,
                1,1,1,1,
                1,1,1,1,
                0,0,0,0,
                0,0,0,0,
                -1,-1,-1,-1,
                -1,-1,-1,-1,
                -1,-1,-1,-1]

list_details = [1,2,3,4,
                5,6,7,8,
                9,10,11,12,
                0,0,0,0,
                0,0,0,0,
                -1,-2,-3,-4,
                -5,-6,-7,-8,
                -9,-10,-11,-12]

#TURN INDICATOR
int_Turn = 1
int_Victory = 0
int_Done = -1

#DIFFICULTIES
int_Difficulties = 0

#LISTS OF AVAILABLE MOVES; P=Player, AI=Computer
list_P_moves = list()
list_P_jumps = list()
list_P_mand = list()
list_AI_moves = list()
list_AI_jumps = list()
list_AI_mand = list()

#INDICATOR FOR USED TOKENS; PK=Player_Promotions, AIK=Computer_Promotions
int_PK = 0
int_AIK = 0

#############
# FUNCTIONS #
#############

#DUMMY FUNCTIONS
def dummy_func_A(x, y):
    print("DEBUGGING_POINT_A: {0}, {1}".format(x, y))
    piece_C_0.onclick(dummy_func_A)
def dummy_func_B(x, y):
    print("DEBUGGING_POINT_B: {0}, {1}".format(x, y))
    piece_C_0.onrelease(dummy_func_B)

#AI CLEVERNESS ADJUSTMENT
#BY CLICKING THE GIVEN BUTTON
def click_box(x, y):
    global int_Difficulties
    if int_Difficulties == 0:
        int_Difficulties = 1
    elif int_Difficulties == 1:
        int_Difficulties = 2
    elif int_Difficulties == 2:
        int_Difficulties = 0
    button_A_0.onrelease(click_box)

#REPORTING A CURRENT STATE OF THE GAME BOARD    
def print_board():
    int_t = 28
    for int_j in range(0, 8):
        for int_i in range(0, 4):
            print("{0}:{1}\t".format(list_Current[int_t + int_i],list_details[int_t + int_i]), end='')
        int_t = int_t - 4
        print("")

#LISTS OF INTERMEDIATE CELLS
def catch(source, target):
    if source != target:
        if (source in [1, 10] and target in [1, 10]) or (source in [2, 9] and target in [2, 9]):
            return 5
        elif (source in [2, 11] and target in [2, 11]) or (source in [3, 10] and target in [3, 10]):
            return 6
        elif (source in [3, 12] and target in [3, 12]) or (source in [4, 11] and target in [4, 11]):
            return 7
        elif (source in [5, 14] and target in [5, 14]) or (source in [6, 13] and target in [6, 13]):
            return 10
        elif (source in [6, 15] and target in [6, 15]) or (source in [7, 14] and target in [7, 14]):
            return 11
        elif (source in [7, 16] and target in [7, 16]) or (source in [8, 15] and target in [8, 15]):
            return 12
        elif (source in [10, 17] and target in [10, 17]) or (source in [9, 18] and target in [9, 18]):
            return 13
        elif (source in [11, 18] and target in [11, 18]) or (source in [10, 19] and target in [10, 19]):
            return 14
        elif (source in [11, 20] and target in [11, 20]) or (source in [12, 19] and target in [12, 19]):
            return 15
        elif (source in [13, 22] and target in [13, 22]) or (source in [14, 21] and target in [14, 21]):
            return 18
        elif (source in [14, 23] and target in [14, 23]) or (source in [15, 22] and target in [15, 22]):
            return 19
        elif (source in [15, 24] and target in [15, 24]) or (source in [16, 23] and target in [16, 23]):
            return 20
        elif (source in [17, 26] and target in [17, 26]) or (source in [18, 25] and target in [18, 25]):
            return 21
        elif (source in [18, 27] and target in [18, 27]) or (source in [19, 26] and target in [19, 26]):
            return 22
        elif (source in [19, 28] and target in [19, 28]) or (source in [20, 27] and target in [20, 27]):
            return 23
        elif (source in [21, 30] and target in [21, 30]) or (source in [22, 29] and target in [22, 29]):
            return 26
        elif (source in [22, 31] and target in [22, 31]) or (source in [23, 30] and target in [23, 30]):
            return 27
        elif (source in [23, 32] and target in [23, 32]) or (source in [24, 31] and target in [24, 31]):
            return 28
        else:
            print("catch_Debugging: The move is not about jump!")
            return -1
    else:
        print("catch_ERROR: INVALID ASSIGNMENT!")
        return -1
            
#COMPOSING MOVE LISTS
def state():
    global list_P_moves
    global list_P_jumps
    global list_AI_moves
    global list_AI_jumps
    
    #int_Turn=1 -> Player Turn
    if int_Turn == 1:
        list_P_moves = list()
        list_P_jumps = list()
        
        for int_i in range(1,33):
            #THE FIRST AND LAST COLUMN
            if int_i == 1:
                if list_Current[int_i-1] == 1:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 4] < 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_P_jumps.append([int_i,int_i+9])
                elif list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 4] < 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_P_jumps.append([int_i,int_i+9])
            elif (int_i == 9) or (int_i == 17):
                if list_Current[int_i-1] == 1:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 4] < 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_P_jumps.append([int_i,int_i+9])
                elif list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 4] < 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_P_jumps.append([int_i,int_i+9])
                    if list_Current[int_i-1 - 4] == 0:
                        list_P_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 4] < 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_P_jumps.append([int_i,int_i-7])
            elif int_i == 25:
                if list_Current[int_i-1] == 1:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                elif list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 - 4] == 0:
                        list_P_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 4] < 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_P_jumps.append([int_i,int_i-7])
            elif int_i == 8:
                if list_Current[int_i-1] == 1:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 4] < 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_P_jumps.append([int_i,int_i+7])
                elif list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 4] < 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_P_jumps.append([int_i,int_i+7])
                    if list_Current[int_i-1 - 4] == 0:
                        list_P_moves.append([int_i,int_i-4])
            elif (int_i == 16) or (int_i == 24):
                if list_Current[int_i-1] == 1:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 4] < 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_P_jumps.append([int_i,int_i+7])
                elif list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 4] < 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_P_jumps.append([int_i,int_i+7])
                    if list_Current[int_i-1 - 4] == 0:
                        list_P_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 4] < 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_P_jumps.append([int_i,int_i-9])
            #MIDDLE ODD COLUMNS
            elif (int_i == 2) or (int_i == 3):
                if list_Current[int_i-1] == 1:
                    if list_Current[int_i-1 + 3] == 0:
                        list_P_moves.append([int_i,int_i+3])
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 3] < 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_P_jumps.append([int_i,int_i+7])
                    if list_Current[int_i-1 + 4] < 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_P_jumps.append([int_i,int_i+9])
                elif list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 + 3] == 0:
                        list_P_moves.append([int_i,int_i+3])
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 3] < 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_P_jumps.append([int_i,int_i+7])
                    if list_Current[int_i-1 + 4] < 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_P_jumps.append([int_i,int_i+9])
            elif (int_i == 10) or (int_i == 11) or (int_i == 18) or (int_i == 19):
                if list_Current[int_i-1] == 1:
                    if list_Current[int_i-1 + 3] == 0:
                        list_P_moves.append([int_i,int_i+3])
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 3] < 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_P_jumps.append([int_i,int_i+7])
                    if list_Current[int_i-1 + 4] < 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_P_jumps.append([int_i,int_i+9])
                elif list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 + 3] == 0:
                        list_P_moves.append([int_i,int_i+3])
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 - 5] == 0:
                        list_P_moves.append([int_i,int_i-5])
                    if list_Current[int_i-1 - 4] == 0:
                        list_P_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 + 3] < 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_P_jumps.append([int_i,int_i+7])
                    if list_Current[int_i-1 + 4] < 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_P_jumps.append([int_i,int_i+9])
                    if list_Current[int_i-1 - 5] < 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_P_jumps.append([int_i,int_i-9])
                    if list_Current[int_i-1 - 4] < 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_P_jumps.append([int_i,int_i-7])
            elif int_i == 4:
                if list_Current[int_i-1] == 1:
                    if list_Current[int_i-1 + 3] == 0:
                        list_P_moves.append([int_i,int_i+3])
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 3] < 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_P_jumps.append([int_i,int_i+7])
                elif list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 + 3] == 0:
                        list_P_moves.append([int_i,int_i+3])
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 3] < 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_P_jumps.append([int_i,int_i+7])
            elif (int_i == 12) or (int_i == 20):
                if list_Current[int_i-1] == 1:
                    if list_Current[int_i-1 + 3] == 0:
                        list_P_moves.append([int_i,int_i+3])
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 3] < 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_P_jumps.append([int_i,int_i+7])
                elif list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 + 3] == 0:
                        list_P_moves.append([int_i,int_i+3])
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 3] < 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_P_jumps.append([int_i,int_i+7])
                    if list_Current[int_i-1 - 5] == 0:
                        list_P_moves.append([int_i,int_i-5])
                    if list_Current[int_i-1 - 4] == 0:
                        list_P_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 5] < 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_P_jumps.append([int_i,int_i-9])
            elif int_i == 28:
                if list_Current[int_i-1] == 1:
                    if list_Current[int_i-1 + 3] == 0:
                        list_P_moves.append([int_i,int_i+3])
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                elif list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 + 3] == 0:
                        list_P_moves.append([int_i,int_i+3])
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 - 5] == 0:
                        list_P_moves.append([int_i,int_i-5])
                    if list_Current[int_i-1 - 4] == 0:
                        list_P_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 5] < 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_P_jumps.append([int_i,int_i-9])                
            #MIDDLE EVEN COLUMNS
            elif int_i == 5:
                if list_Current[int_i-1] == 1:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 5] == 0:
                        list_P_moves.append([int_i,int_i+5])
                    if list_Current[int_i-1 + 5] < 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_P_jumps.append([int_i,int_i+9])
                elif list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 5] == 0:
                        list_P_moves.append([int_i,int_i+5])
                    if list_Current[int_i-1 + 5] < 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_P_jumps.append([int_i,int_i+9])
                    if list_Current[int_i-1 - 4] == 0:
                        list_P_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 3] == 0:
                        list_P_moves.append([int_i,int_i-3])
            elif (int_i == 6) or (int_i == 7):
                if list_Current[int_i-1] == 1:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 5] == 0:
                        list_P_moves.append([int_i,int_i+5])
                    if list_Current[int_i-1 + 4] < 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_P_jumps.append([int_i,int_i+7])
                    if list_Current[int_i-1 + 5] < 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_P_jumps.append([int_i,int_i+9])
                elif list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 5] == 0:
                        list_P_moves.append([int_i,int_i+5])
                    if list_Current[int_i-1 + 4] < 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_P_jumps.append([int_i,int_i+7])
                    if list_Current[int_i-1 + 5] < 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_P_jumps.append([int_i,int_i+9])
                    if list_Current[int_i-1 - 4] == 0:
                        list_P_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 3] == 0:
                        list_P_moves.append([int_i,int_i-3])
            elif (int_i == 13) or (int_i == 21):
                if list_Current[int_i-1] == 1:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 5] == 0:
                        list_P_moves.append([int_i,int_i+5])
                    if list_Current[int_i-1 + 5] < 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_P_jumps.append([int_i,int_i+9])
                elif list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 5] == 0:
                        list_P_moves.append([int_i,int_i+5])
                    if list_Current[int_i-1 + 5] < 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_P_jumps.append([int_i,int_i+9])
                    if list_Current[int_i-1 - 4] == 0:
                        list_P_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 3] == 0:
                        list_P_moves.append([int_i,int_i-3])
                    if list_Current[int_i-1 - 3] < 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_P_jumps.append([int_i,int_i-7])
            elif (int_i == 14) or (int_i == 15) or (int_i == 22) or (int_i == 23):
                if list_Current[int_i-1] == 1:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 5] == 0:
                        list_P_moves.append([int_i,int_i+5])
                    if list_Current[int_i-1 + 4] < 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_P_jumps.append([int_i,int_i+7])
                    if list_Current[int_i-1 + 5] < 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_P_jumps.append([int_i,int_i+9])
                elif list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 5] == 0:
                        list_P_moves.append([int_i,int_i+5])
                    if list_Current[int_i-1 + 4] < 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_P_jumps.append([int_i,int_i+7])
                    if list_Current[int_i-1 + 5] < 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_P_jumps.append([int_i,int_i+9])
                    if list_Current[int_i-1 - 4] == 0:
                        list_P_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 3] == 0:
                        list_P_moves.append([int_i,int_i-3])
                    if list_Current[int_i-1 - 4] < 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_P_jumps.append([int_i,int_i-9])
                    if list_Current[int_i-1 - 3] < 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_P_jumps.append([int_i,int_i-7])       
            #THE SECOND LAST ROW FOR PROMOTION; THE REST OF THE CELLS
            elif (int_i == 26) or (int_i == 27):
                if list_Current[int_i-1] == 1:
                    if list_Current[int_i-1 + 3] == 0:
                        list_P_moves.append([int_i,int_i+3])
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                elif list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 + 3] == 0:
                        list_P_moves.append([int_i,int_i+3])
                    if list_Current[int_i-1 + 4] == 0:
                        list_P_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 - 5] == 0:
                        list_P_moves.append([int_i,int_i-5])
                    if list_Current[int_i-1 - 4] == 0:
                        list_P_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 5] < 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_P_jumps.append([int_i,int_i-9])
                    if list_Current[int_i-1 - 4] < 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_P_jumps.append([int_i,int_i-7])
            #THE FINAL ROW
            elif int_i == 29:
                if list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 - 4] == 0:
                        list_P_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 3] == 0:
                        list_P_moves.append([int_i,int_i-3])
                    if list_Current[int_i-1 - 3] < 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_P_jumps.append([int_i,int_i-7])
            elif (int_i == 30) or (int_i == 31):
                if list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 - 4] == 0:
                        list_P_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 3] == 0:
                        list_P_moves.append([int_i,int_i-3])
                    if list_Current[int_i-1 - 4] < 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_P_jumps.append([int_i,int_i-9])
                    if list_Current[int_i-1 - 3] < 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_P_jumps.append([int_i,int_i-7])
            elif int_i == 32:
                if list_Current[int_i-1] == 2:
                    if list_Current[int_i-1 - 4] == 0:
                        list_P_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 4] < 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_P_jumps.append([int_i,int_i-9])
    #AI TURN
    elif int_Turn == -1:
        print("COMPUTER CALL")
        list_AI_moves = list()
        list_AI_jumps = list()
        
        for int_i in range(1,33):
            #THE FIRST AND LAST COLUMN
            if int_i == 32:
                if list_Current[int_i-1] == -1:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 4] > 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_AI_jumps.append([int_i,int_i-9])
                elif list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 4] > 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_AI_jumps.append([int_i,int_i-9])
            elif (int_i == 24) or (int_i == 16):
                if list_Current[int_i-1] == -1:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 4] > 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_AI_jumps.append([int_i,int_i-9])
                elif list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 - 4] > 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_AI_jumps.append([int_i,int_i-9])
                    if list_Current[int_i-1 + 4] == 0:
                        list_AI_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 4] > 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_AI_jumps.append([int_i,int_i+7])
            elif int_i == 8:
                if list_Current[int_i-1] == -1:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                elif list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 + 4] == 0:
                        list_AI_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 4] > 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_AI_jumps.append([int_i,int_i+7])
            elif int_i == 25:
                if list_Current[int_i-1] == -1:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 4] > 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_AI_jumps.append([int_i,int_i-7])
                elif list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 4] > 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_AI_jumps.append([int_i,int_i-7])
                    if list_Current[int_i-1 + 4] == 0:
                        list_AI_moves.append([int_i,int_i+4])
            elif (int_i == 17) or (int_i == 9):
                if list_Current[int_i-1] == -1:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 4] > 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_AI_jumps.append([int_i,int_i-7])
                elif list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 4] > 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_AI_jumps.append([int_i,int_i-7])
                    if list_Current[int_i-1 + 4] == 0:
                        list_AI_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 4] > 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_AI_jumps.append([int_i,int_i+9])
            #MIDDLE ODD COLUMNS
            elif (int_i == 31) or (int_i == 30):
                if list_Current[int_i-1] == -1:
                    if list_Current[int_i-1 - 3] == 0:
                        list_AI_moves.append([int_i,int_i-3])
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 3] > 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_AI_jumps.append([int_i,int_i-7])
                    if list_Current[int_i-1 - 4] > 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_AI_jumps.append([int_i,int_i-9])
                elif list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 - 3] == 0:
                        list_AI_moves.append([int_i,int_i-3])
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 3] > 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_AI_jumps.append([int_i,int_i-7])
                    if list_Current[int_i-1 - 4] > 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_AI_jumps.append([int_i,int_i-9])
            elif (int_i == 23) or (int_i == 22) or (int_i == 14) or (int_i == 15):
                if list_Current[int_i-1] == -1:
                    if list_Current[int_i-1 - 3] == 0:
                        list_AI_moves.append([int_i,int_i-3])
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 3] > 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_AI_jumps.append([int_i,int_i-7])
                    if list_Current[int_i-1 - 4] > 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_AI_jumps.append([int_i,int_i-9])
                elif list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 - 3] == 0:
                        list_AI_moves.append([int_i,int_i-3])
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 + 5] == 0:
                        list_AI_moves.append([int_i,int_i+5])
                    if list_Current[int_i-1 + 4] == 0:
                        list_AI_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 - 3] > 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_AI_jumps.append([int_i,int_i-7])
                    if list_Current[int_i-1 - 4] > 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_AI_jumps.append([int_i,int_i-9])
                    if list_Current[int_i-1 + 5] > 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_AI_jumps.append([int_i,int_i+9])
                    if list_Current[int_i-1 + 4] > 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_AI_jumps.append([int_i,int_i+7])
            elif int_i == 29:
                if list_Current[int_i-1] == -1:
                    if list_Current[int_i-1 - 3] == 0:
                        list_AI_moves.append([int_i,int_i-3])
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 3] > 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_AI_jumps.append([int_i,int_i-7])
                elif list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 - 3] == 0:
                        list_AI_moves.append([int_i,int_i-3])
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 3] > 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_AI_jumps.append([int_i,int_i-7])
            elif (int_i == 21) or (int_i == 13):
                if list_Current[int_i-1] == -1:
                    if list_Current[int_i-1 - 3] == 0:
                        list_AI_moves.append([int_i,int_i-3])
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 3] > 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_AI_jumps.append([int_i,int_i-7])
                elif list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 - 3] == 0:
                        list_AI_moves.append([int_i,int_i-3])
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 3] > 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_AI_jumps.append([int_i,int_i-7])
                    if list_Current[int_i-1 + 5] == 0:
                        list_AI_moves.append([int_i,int_i+5])
                    if list_Current[int_i-1 + 4] == 0:
                        list_AI_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 5] > 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_AI_jumps.append([int_i,int_i+9])
            elif int_i == 5:
                if list_Current[int_i-1] == -1:
                    if list_Current[int_i-1 - 3] == 0:
                        list_AI_moves.append([int_i,int_i-3])
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                elif list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 - 3] == 0:
                        list_AI_moves.append([int_i,int_i-3])
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 + 5] == 0:
                        list_AI_moves.append([int_i,int_i+5])
                    if list_Current[int_i-1 + 4] == 0:
                        list_AI_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 5] > 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_AI_jumps.append([int_i,int_i+9])                
            #MIDDLE EVEN COLUMNS
            elif int_i == 28:
                if list_Current[int_i-1] == -1:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 5] == 0:
                        list_AI_moves.append([int_i,int_i-5])
                    if list_Current[int_i-1 - 5] > 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_AI_jumps.append([int_i,int_i-9])
                elif list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 5] == 0:
                        list_AI_moves.append([int_i,int_i-5])
                    if list_Current[int_i-1 - 5] > 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_AI_jumps.append([int_i,int_i-9])
                    if list_Current[int_i-1 + 4] == 0:
                        list_AI_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 3] == 0:
                        list_AI_moves.append([int_i,int_i+3])
            elif (int_i == 26) or (int_i == 27):
                if list_Current[int_i-1] == -1:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 5] == 0:
                        list_AI_moves.append([int_i,int_i-5])
                    if list_Current[int_i-1 - 4] > 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_AI_jumps.append([int_i,int_i-7])
                    if list_Current[int_i-1 - 5] > 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_AI_jumps.append([int_i,int_i-9])
                elif list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 5] == 0:
                        list_AI_moves.append([int_i,int_i-5])
                    if list_Current[int_i-1 - 4] > 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_AI_jumps.append([int_i,int_i-7])
                    if list_Current[int_i-1 - 5] > 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_AI_jumps.append([int_i,int_i-9])
                    if list_Current[int_i-1 + 4] == 0:
                        list_AI_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 3] == 0:
                        list_AI_moves.append([int_i,int_i+3])
            elif (int_i == 12) or (int_i == 20):
                if list_Current[int_i-1] == -1:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 5] == 0:
                        list_AI_moves.append([int_i,int_i-5])
                    if list_Current[int_i-1 - 5] > 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_AI_jumps.append([int_i,int_i-9])
                elif list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 5] == 0:
                        list_AI_moves.append([int_i,int_i-5])
                    if list_Current[int_i-1 - 5] > 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_AI_jumps.append([int_i,int_i-9])
                    if list_Current[int_i-1 + 4] == 0:
                        list_AI_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 3] == 0:
                        list_AI_moves.append([int_i,int_i+3])
                    if list_Current[int_i-1 + 3] > 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_AI_jumps.append([int_i,int_i+7])
            elif (int_i == 18) or (int_i == 19) or (int_i == 10) or (int_i == 11):
                if list_Current[int_i-1] == -1:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 5] == 0:
                        list_AI_moves.append([int_i,int_i-5])
                    if list_Current[int_i-1 - 4] > 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_AI_jumps.append([int_i,int_i-7])
                    if list_Current[int_i-1 - 5] > 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_AI_jumps.append([int_i,int_i-9])
                elif list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 - 5] == 0:
                        list_AI_moves.append([int_i,int_i-5])
                    if list_Current[int_i-1 - 4] > 0:
                        if list_Current[int_i-1 - 7] == 0:
                            list_AI_jumps.append([int_i,int_i-7])
                    if list_Current[int_i-1 - 5] > 0:
                        if list_Current[int_i-1 - 9] == 0:
                            list_AI_jumps.append([int_i,int_i-9])
                    if list_Current[int_i-1 + 4] == 0:
                        list_AI_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 3] == 0:
                        list_AI_moves.append([int_i,int_i+3])
                    if list_Current[int_i-1 + 4] > 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_AI_jumps.append([int_i,int_i+9])
                    if list_Current[int_i-1 + 3] > 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_AI_jumps.append([int_i,int_i+7])       
            #THE SECOND LAST ROW FOR PROMOTION; THE REST OF THE CELLS
            elif (int_i == 6) or (int_i == 7):
                if list_Current[int_i-1] == -1:
                    if list_Current[int_i-1 - 3] == 0:
                        list_AI_moves.append([int_i,int_i-3])
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                elif list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 - 3] == 0:
                        list_AI_moves.append([int_i,int_i-3])
                    if list_Current[int_i-1 - 4] == 0:
                        list_AI_moves.append([int_i,int_i-4])
                    if list_Current[int_i-1 + 5] == 0:
                        list_AI_moves.append([int_i,int_i+5])
                    if list_Current[int_i-1 + 4] == 0:
                        list_AI_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 5] > 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_AI_jumps.append([int_i,int_i+9])
                    if list_Current[int_i-1 + 4] > 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_AI_jumps.append([int_i,int_i+7])
            #THE FINAL ROW
            elif int_i == 4:
                if list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 + 4] == 0:
                        list_AI_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 3] == 0:
                        list_AI_moves.append([int_i,int_i+3])
                    if list_Current[int_i-1 + 3] > 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_AI_jumps.append([int_i,int_i+7])
            elif (int_i == 2) or (int_i == 3):
                if list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 + 4] == 0:
                        list_AI_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 3] == 0:
                        list_AI_moves.append([int_i,int_i+3])
                    if list_Current[int_i-1 + 4] > 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_AI_jumps.append([int_i,int_i+9])
                    if list_Current[int_i-1 + 3] > 0:
                        if list_Current[int_i-1 + 7] == 0:
                            list_AI_jumps.append([int_i,int_i+7])
            elif int_i == 1:
                if list_Current[int_i-1] == -2:
                    if list_Current[int_i-1 + 4] == 0:
                        list_AI_moves.append([int_i,int_i+4])
                    if list_Current[int_i-1 + 4] > 0:
                        if list_Current[int_i-1 + 9] == 0:
                            list_AI_jumps.append([int_i,int_i+9])
    else:
        print("UNEXPECTED ERROR!")

#EUCLIDEAN DISTANCE
#x^2 + y^2 = r^2 in a circle
def radius_check(obj_token, obj_r, cor_X, cor_Y):
    if (obj_token.xcor()-cor_X)*(obj_token.xcor()-cor_X) + (obj_token.ycor()-cor_Y)*(obj_token.ycor()-cor_Y) < obj_r*obj_r:
        return True
    else:
        return False

#QUERY FOR A CERTAIN POSITION
def recording_position(cor_X, cor_Y):
    obj_X = 0    
    if radius_check(game_board_A1, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 1
        return obj_X    
    elif radius_check(game_board_A2, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 2
        return obj_X        
    elif radius_check(game_board_A3, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 3
        return obj_X    
    elif radius_check(game_board_A4, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 4
        return obj_X        
    elif radius_check(game_board_A5, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 5
        return obj_X        
    elif radius_check(game_board_A6, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 6
        return obj_X        
    elif radius_check(game_board_A7, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 7
        return obj_X        
    elif radius_check(game_board_A8, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 8
        return obj_X       
    elif radius_check(game_board_A9, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 9
        return obj_X        
    elif radius_check(game_board_A10, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 10
        return obj_X        
    elif radius_check(game_board_A11, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 11
        return obj_X        
    elif radius_check(game_board_A12, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 12
        return obj_X        
    elif radius_check(game_board_A13, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 13
        return obj_X        
    elif radius_check(game_board_A14, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 14
        return obj_X        
    elif radius_check(game_board_A15, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 15
        return obj_X        
    elif radius_check(game_board_A16, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 16
        return obj_X        
    elif radius_check(game_board_A17, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 17
        return obj_X        
    elif radius_check(game_board_A18, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 18
        return obj_X        
    elif radius_check(game_board_A19, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 19
        return obj_X        
    elif radius_check(game_board_A20, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 20
        return obj_X        
    elif radius_check(game_board_A21, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 21
        return obj_X        
    elif radius_check(game_board_A22, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 22
        return obj_X        
    elif radius_check(game_board_A23, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 23
        return obj_X        
    elif radius_check(game_board_A24, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 24
        return obj_X        
    elif radius_check(game_board_A25, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 25
        return obj_X        
    elif radius_check(game_board_A26, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 26
        return obj_X        
    elif radius_check(game_board_A27, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 27
        return obj_X        
    elif radius_check(game_board_A28, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 28
        return obj_X        
    elif radius_check(game_board_A29, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 29
        return obj_X        
    elif radius_check(game_board_A30, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 30
        return obj_X        
    elif radius_check(game_board_A31, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 31
        return obj_X       
    elif radius_check(game_board_A32, LENGTH_UNIT*10, cor_X, cor_Y):
        obj_X = 32
        return obj_X        
    else:
        obj_X = -1
        return obj_X

#OBJECTS <- ARRAY INDEX FROM 0 TO 31
def numToCor(obj_number):
    target_X = 0
    target_Y = 0
    list_cor = [0, 0]
    
    if obj_number == 1:
        target_X = game_board_A1.xcor()
        target_Y = game_board_A1.ycor()
    elif obj_number == 2:
        target_X = game_board_A2.xcor()
        target_Y = game_board_A2.ycor()
    elif obj_number == 3:
        target_X = game_board_A3.xcor()
        target_Y = game_board_A3.ycor()
    elif obj_number == 4:
        target_X = game_board_A4.xcor()
        target_Y = game_board_A4.ycor()
    elif obj_number == 5:
        target_X = game_board_A5.xcor()
        target_Y = game_board_A5.ycor()
    elif obj_number == 6:
        target_X = game_board_A6.xcor()
        target_Y = game_board_A6.ycor()
    elif obj_number == 7:
        target_X = game_board_A7.xcor()
        target_Y = game_board_A7.ycor()
    elif obj_number == 8:
        target_X = game_board_A8.xcor()
        target_Y = game_board_A8.ycor()
    elif obj_number == 9:
        target_X = game_board_A9.xcor()
        target_Y = game_board_A9.ycor()
    elif obj_number == 10:
        target_X = game_board_A10.xcor()
        target_Y = game_board_A10.ycor()
    elif obj_number == 11:
        target_X = game_board_A11.xcor()
        target_Y = game_board_A11.ycor()
    elif obj_number == 12:
        target_X = game_board_A12.xcor()
        target_Y = game_board_A12.ycor()
    elif obj_number == 13:
        target_X = game_board_A13.xcor()
        target_Y = game_board_A13.ycor()
    elif obj_number == 14:
        target_X = game_board_A14.xcor()
        target_Y = game_board_A14.ycor()
    elif obj_number == 15:
        target_X = game_board_A15.xcor()
        target_Y = game_board_A15.ycor()
    elif obj_number == 16:
        target_X = game_board_A16.xcor()
        target_Y = game_board_A16.ycor()
    elif obj_number == 17:
        target_X = game_board_A17.xcor()
        target_Y = game_board_A17.ycor()
    elif obj_number == 18:
        target_X = game_board_A18.xcor()
        target_Y = game_board_A18.ycor()
    elif obj_number == 19:
        target_X = game_board_A19.xcor()
        target_Y = game_board_A19.ycor()
    elif obj_number == 20:
        target_X = game_board_A20.xcor()
        target_Y = game_board_A20.ycor()
    elif obj_number == 21:
        target_X = game_board_A21.xcor()
        target_Y = game_board_A21.ycor()
    elif obj_number == 22:
        target_X = game_board_A22.xcor()
        target_Y = game_board_A22.ycor()
    elif obj_number == 23:
        target_X = game_board_A23.xcor()
        target_Y = game_board_A23.ycor()
    elif obj_number == 24:
        target_X = game_board_A24.xcor()
        target_Y = game_board_A24.ycor()
    elif obj_number == 25:
        target_X = game_board_A25.xcor()
        target_Y = game_board_A25.ycor()
    elif obj_number == 26:
        target_X = game_board_A26.xcor()
        target_Y = game_board_A26.ycor()
    elif obj_number == 27:
        target_X = game_board_A27.xcor()
        target_Y = game_board_A27.ycor()
    elif obj_number == 28:
        target_X = game_board_A28.xcor()
        target_Y = game_board_A28.ycor()
    elif obj_number == 29:
        target_X = game_board_A29.xcor()
        target_Y = game_board_A29.ycor()
    elif obj_number == 30:
        target_X = game_board_A30.xcor()
        target_Y = game_board_A30.ycor()
    elif obj_number == 31:
        target_X = game_board_A31.xcor()
        target_Y = game_board_A31.ycor()
    elif obj_number == 32:
        target_X = game_board_A32.xcor()
        target_Y = game_board_A32.ycor()
    else:
        target_X = -1
        target_Y = -1
    
    list_cor = [target_X, target_Y]
    return list_cor

#OBJECTS <- ARRAY INDEX FROM 0 TO 31
def numToObj(obj_number):
    print("numToObj: {0}".format(obj_number))
    
    if obj_number == 1:
        obj_out = piece_A_1
        return obj_out
    elif obj_number == 2:
        obj_out = piece_A_2
        return obj_out
    elif obj_number == 3:
        obj_out = piece_A_3
        return obj_out
    elif obj_number == 4:
        obj_out = piece_A_4
        return obj_out
    elif obj_number == 5:
        obj_out = piece_A_5
        return obj_out
    elif obj_number == 6:
        obj_out = piece_A_6
        return obj_out
    elif obj_number == 7:
        obj_out = piece_A_7
        return obj_out
    elif obj_number == 8:
        obj_out = piece_A_8
        return obj_out
    elif obj_number == 9:
        obj_out = piece_A_9
        return obj_out
    elif obj_number == 10:
        obj_out = piece_A_10
        return obj_out
    elif obj_number == 11:
        obj_out = piece_A_11
        return obj_out
    elif obj_number == 12:
        obj_out = piece_A_12
        return obj_out
    elif obj_number == -1:
        obj_out = piece_B_1
        return obj_out
    elif obj_number == -2:
        obj_out = piece_B_2
        return obj_out
    elif obj_number == -3:
        obj_out = piece_B_3
        return obj_out
    elif obj_number == -4:
        obj_out = piece_B_4
        return obj_out
    elif obj_number == -5:
        obj_out = piece_B_5
        return obj_out
    elif obj_number == -6:
        obj_out = piece_B_6
        return obj_out
    elif obj_number == -7:
        obj_out = piece_B_7
        return obj_out
    elif obj_number == -8:
        obj_out = piece_B_8
        return obj_out
    elif obj_number == -9:
        obj_out = piece_B_9
        return obj_out
    elif obj_number == -10:
        obj_out = piece_B_10
        return obj_out
    elif obj_number == -11:
        obj_out = piece_B_11
        return obj_out
    elif obj_number == -12:
        obj_out = piece_B_12
        return obj_out
    elif obj_number == 101:
        obj_out = piece_AA_1
        return obj_out
    elif obj_number == 102:
        obj_out = piece_AA_2
        return obj_out
    elif obj_number == 103:
        obj_out = piece_AA_3
        return obj_out
    elif obj_number == 104:
        obj_out = piece_AA_4
        return obj_out
    elif obj_number == 105:
        obj_out = piece_AA_5
        return obj_out
    elif obj_number == 106:
        obj_out = piece_AA_6
        return obj_out
    elif obj_number == 107:
        obj_out = piece_AA_7
        return obj_out
    elif obj_number == 108:
        obj_out = piece_AA_8
        return obj_out
    elif obj_number == 109:
        obj_out = piece_AA_9
        return obj_out
    elif obj_number == 110:
        obj_out = piece_AA_10
        return obj_out
    elif obj_number == 111:
        obj_out = piece_AA_11
        return obj_out
    elif obj_number == 112:
        obj_out = piece_AA_12
        return obj_out
    elif obj_number == -101:
        obj_out = piece_BB_1
        return obj_out
    elif obj_number == -102:
        obj_out = piece_BB_2
        return obj_out
    elif obj_number == -103:
        obj_out = piece_BB_3
        return obj_out
    elif obj_number == -104:
        obj_out = piece_BB_4
        return obj_out
    elif obj_number == -105:
        obj_out = piece_BB_5
        return obj_out
    elif obj_number == -106:
        obj_out = piece_BB_6
        return obj_out
    elif obj_number == -107:
        obj_out = piece_BB_7
        return obj_out
    elif obj_number == -108:
        obj_out = piece_BB_8
        return obj_out
    elif obj_number == -109:
        obj_out = piece_BB_9
        return obj_out
    elif obj_number == -110:
        obj_out = piece_BB_10
        return obj_out
    elif obj_number == -111:
        obj_out = piece_BB_11
        return obj_out
    elif obj_number == -112:
        obj_out = piece_BB_12
        return obj_out
    #elif Promoted Tokens:
    else:
        print("ERROR(numToObj): OUT OF INDEX!")
        return None

#OBJECTS TO NUMBERS
def objToNum(obj_number):
    
    print("objToNum: {0}".format(obj_number))
    if obj_number is piece_A_1:
        return 1
    elif obj_number is piece_A_2:
        return 2
    elif obj_number is piece_A_3:
        return 3
    elif obj_number is piece_A_4:
        return 4
    elif obj_number is piece_A_5:
        return 5
    elif obj_number is piece_A_6:
        return 6
    elif obj_number is piece_A_7:
        return 7
    elif obj_number is piece_A_8:
        return 8
    elif obj_number is piece_A_9:
        return 9
    elif obj_number is piece_A_10:
        return 10
    elif obj_number is piece_A_11:
        return 11
    elif obj_number is piece_A_12:
        return 12
    elif obj_number is piece_B_1:
        return (-1)
    elif obj_number is piece_B_2:
        return (-2)
    elif obj_number is piece_B_3:
        return (-3)
    elif obj_number is piece_B_4:
        return (-4)
    elif obj_number is piece_B_5:
        return (-5)
    elif obj_number is piece_B_6:
        return (-6)
    elif obj_number is piece_B_7:
        return (-7)
    elif obj_number is piece_B_8:
        return (-8)
    elif obj_number is piece_B_9:
        return (-9)
    elif obj_number is piece_B_10:
        return (-10)
    elif obj_number is piece_B_11:
        return (-11)
    elif obj_number is piece_B_12:
        return (-12)
    elif obj_number is piece_AA_1:
        return 101
    elif obj_number is piece_AA_2:
        return 102
    elif obj_number is piece_AA_3:
        return 103
    elif obj_number is piece_AA_4:
        return 104
    elif obj_number is piece_AA_5:
        return 105
    elif obj_number is piece_AA_6:
        return 106
    elif obj_number is piece_AA_7:
        return 107
    elif obj_number is piece_AA_8:
        return 108
    elif obj_number is piece_AA_9:
        return 109
    elif obj_number is piece_AA_10:
        return 110
    elif obj_number is piece_AA_11:
        return 111
    elif obj_number is piece_AA_12:
        return 112
    elif obj_number is piece_BB_1:
        return -101
    elif obj_number is piece_BB_2:
        return -102
    elif obj_number is piece_BB_3:
        return -103
    elif obj_number is piece_BB_4:
        return -104
    elif obj_number is piece_BB_5:
        return -105
    elif obj_number is piece_BB_6:
        return -106
    elif obj_number is piece_BB_7:
        return -107
    elif obj_number is piece_BB_8:
        return -108
    elif obj_number is piece_BB_9:
        return -109
    elif obj_number is piece_BB_10:
        return -110
    elif obj_number is piece_BB_11:
        return -111
    elif obj_number is piece_BB_12:
        return -112
    #elif Promoted Tokens:
    else:
        print("ERROR(objToNum): OUT OF INDEX!")
        return None

#REALTIME MONITOR FOR CHECKING UP CERTAIN STATES
def debug_monitor(m_event):
    global debug_Xcor
    global debug_Ycor
    global debug_record
    canvas_X, canvas_Y = m_event.x, m_event.y
    debug_Xcor = canvas_X - (SCREEN_WIDTH/2)
    debug_Ycor = (-1)*(canvas_Y - (SCREEN_HEIGHT/2))
    debug_record = recording_position(debug_Xcor, debug_Ycor)

#####################
# AI IMPLEMENTATION #
#####################

def random_move():
    global list_Current
    global list_details
    global int_Victory
    global int_AIK
    global list_AI_jumps
    global list_AI_mand
    
    time.sleep(1)
    #state(): UPDATE GAME BOARD SITUATIONS
    state()
    if len(list_AI_jumps) != 0:
        int_rand = random.randint(0,len(list_AI_jumps)-1)
        source_index = list_AI_jumps[int_rand][0]
        target_index = list_AI_jumps[int_rand][1]
        obj_X = numToObj(list_details[source_index-1])
        
        temp = numToCor(target_index)
        target_X = temp[0]
        target_Y = temp[1]
        obj_X.goto(target_X, target_Y)
        
        int_marker = -1
        if list_Current[source_index-1] == -2:
            int_marker = -2
        list_Current[source_index-1] = 0
        list_details[source_index-1] = 0
        list_Current[target_index-1] = int_marker
        list_details[target_index-1] = objToNum(obj_X)
        
        temp_coor = catch(source_index, target_index)
        temp_obj = numToObj(list_details[temp_coor-1])
        temp_obj.goto(init_X-BOARD_SIZE, init_Y-BOARD_SIZE-50)
        list_Current[temp_coor-1] = 0
        list_details[temp_coor-1] = 0
        
        #IF PROMOTION IS POSSIBLE:
        if target_index in [1, 2, 3, 4]:
            if int_marker == -1:
                if int_AIK == 0:
                    piece_BB_1.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_1.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -101
                    int_AIK = 1
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 1:
                    piece_BB_2.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_2.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -102
                    int_AIK = 2
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 2:
                    piece_BB_3.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_3.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -103
                    int_AIK = 3
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 3:
                    piece_BB_4.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_4.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -104
                    int_AIK = 4
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 4:
                    piece_BB_5.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_5.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -105
                    int_AIK = 5
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 5:
                    piece_BB_6.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_6.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -106
                    int_AIK = 6
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 6:
                    piece_BB_7.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_7.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -107
                    int_AIK = 7
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 7:
                    piece_BB_8.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_8.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -108
                    int_AIK = 8
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 8:
                    piece_BB_9.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_9.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -109
                    int_AIK = 9
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 9:
                    piece_BB_10.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_10.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -110
                    int_AIK = 10
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 10:
                    piece_BB_11.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_11.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -111
                    int_AIK = 11
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 11:
                    piece_BB_12.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_12.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -112
                    int_AIK = 12
                    #END THE TURN
                    list_AI_jumps = list()
                
        print_board()
        #IF A FURTHER MOVE IS POSSIBLE:
        #TURN OVER
        if len(list_AI_jumps) == 0:
            #int_Turn = int_Turn * (-1)
            switch_turn_to_Player()
        #else:
        #    list_AI_mand = list()
        #    list_AI_mand.append(target_index)
        #    AI_mand_move()
        else:
            state()
            mand_source = 0
            bool_mand = False
            for int_i in list_AI_jumps:
                if int_i[0] == target_index:
                    mand_source = int_i[0]
                    bool_mand = True
                    break
            if bool_mand:
                list_AI_mand = list()
                list_AI_mand.append(mand_source)
                AI_mand_move()
            else:
                switch_turn_to_Player()
    elif len(list_AI_moves) != 0:
        int_rand = random.randint(0,len(list_AI_moves)-1)
        source_index = list_AI_moves[int_rand][0]
        target_index = list_AI_moves[int_rand][1]
        obj_X = numToObj(list_details[source_index-1])
        
        temp = numToCor(target_index)
        target_X = temp[0]
        target_Y = temp[1]
        obj_X.goto(target_X, target_Y)
        
        int_marker = -1
        if list_Current[source_index-1] == -2:
            int_marker = -2
        list_Current[source_index-1] = 0
        list_details[source_index-1] = 0
        list_Current[target_index-1] = int_marker
        list_details[target_index-1] = objToNum(obj_X)
        
        #temp_coor = catch(source_index, target_index)
        #list_Current[temp_coor-1] = 0
        
        #IF PROMOTION IS POSSIBLE:
        if target_index in [1, 2, 3, 4]:
            if int_marker == -1:
                if int_AIK == 0:
                    piece_BB_1.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_1.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -101
                    int_AIK = 1
                elif int_AIK == 1:
                    piece_BB_2.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_2.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -102
                    int_AIK = 2
                elif int_AIK == 2:
                    piece_BB_3.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_3.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -103
                    int_AIK = 3
                elif int_AIK == 3:
                    piece_BB_4.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_4.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -104
                    int_AIK = 4
                elif int_AIK == 4:
                    piece_BB_5.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_5.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -105
                    int_AIK = 5
                elif int_AIK == 5:
                    piece_BB_6.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_6.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -106
                    int_AIK = 6
                elif int_AIK == 6:
                    piece_BB_7.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_7.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -107
                    int_AIK = 7
                elif int_AIK == 7:
                    piece_BB_8.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_8.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -108
                    int_AIK = 8
                elif int_AIK == 8:
                    piece_BB_9.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_9.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -109
                    int_AIK = 9
                elif int_AIK == 9:
                    piece_BB_10.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_10.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -110
                    int_AIK = 10
                elif int_AIK == 10:
                    piece_BB_11.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_11.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -111
                    int_AIK = 11
                elif int_AIK == 11:
                    piece_BB_12.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_12.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -112
                    int_AIK = 12
        
        print_board()
        #IF A FURTHER MOVE IS POSSIBLE:
        #TURN OVER
        #int_Turn = int_Turn * (-1)
        switch_turn_to_Player()
    else:
        int_Victory = 1
        print("NO POSSIBLE MOVE: {0} = {1}, {2}".format(int_Victory, list_AI_moves, list_AI_jumps))
        

#SIMULATION PARTS
def simulation_tree(list_board, int_max_turn):
    list_calculation = copy.deepcopy(list_board)
    list_children = list()
    
    list_temp_P_moves = list()
    list_temp_P_jumps = list()
    list_temp_AI_moves = list()
    list_temp_AI_jumps = list()
    
    #Calculate possible moves in the near futures
    #int_max_turn=1 -> Player Turn
    if int_max_turn > 0:
        for int_i in range(1,33):
            #THE FIRST AND LAST COLUMN
            if int_i == 1:
                if list_calculation[int_i-1] == 1:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 4] < 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i+9])
                elif list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 4] < 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i+9])
            elif (int_i == 9) or (int_i == 17):
                if list_calculation[int_i-1] == 1:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 4] < 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i+9])
                elif list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 4] < 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i+9])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_P_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 4] < 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i-7])
            elif int_i == 25:
                if list_calculation[int_i-1] == 1:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                elif list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_P_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 4] < 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i-7])
            elif int_i == 8:
                if list_calculation[int_i-1] == 1:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 4] < 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i+7])
                elif list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 4] < 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i+7])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_P_moves.append([int_i,int_i-4])
            elif (int_i == 16) or (int_i == 24):
                if list_calculation[int_i-1] == 1:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 4] < 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i+7])
                elif list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 4] < 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i+7])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_P_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 4] < 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i-9])
            #MIDDLE ODD COLUMNS
            elif (int_i == 2) or (int_i == 3):
                if list_calculation[int_i-1] == 1:
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_P_moves.append([int_i,int_i+3])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 3] < 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i+7])
                    if list_calculation[int_i-1 + 4] < 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i+9])
                elif list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_P_moves.append([int_i,int_i+3])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 3] < 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i+7])
                    if list_calculation[int_i-1 + 4] < 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i+9])
            elif (int_i == 10) or (int_i == 11) or (int_i == 18) or (int_i == 19):
                if list_calculation[int_i-1] == 1:
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_P_moves.append([int_i,int_i+3])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 3] < 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i+7])
                    if list_calculation[int_i-1 + 4] < 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i+9])
                elif list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_P_moves.append([int_i,int_i+3])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 - 5] == 0:
                        list_temp_P_moves.append([int_i,int_i-5])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_P_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 + 3] < 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i+7])
                    if list_calculation[int_i-1 + 4] < 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i+9])
                    if list_calculation[int_i-1 - 5] < 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i-9])
                    if list_calculation[int_i-1 - 4] < 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i-7])
            elif int_i == 4:
                if list_calculation[int_i-1] == 1:
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_P_moves.append([int_i,int_i+3])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 3] < 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i+7])
                elif list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_P_moves.append([int_i,int_i+3])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 3] < 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i+7])
            elif (int_i == 12) or (int_i == 20):
                if list_calculation[int_i-1] == 1:
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_P_moves.append([int_i,int_i+3])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 3] < 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i+7])
                elif list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_P_moves.append([int_i,int_i+3])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 3] < 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i+7])
                    if list_calculation[int_i-1 - 5] == 0:
                        list_temp_P_moves.append([int_i,int_i-5])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_P_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 5] < 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i-9])
            elif int_i == 28:
                if list_calculation[int_i-1] == 1:
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_P_moves.append([int_i,int_i+3])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                elif list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_P_moves.append([int_i,int_i+3])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 - 5] == 0:
                        list_temp_P_moves.append([int_i,int_i-5])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_P_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 5] < 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i-9])                
            #MIDDLE EVEN COLUMNS
            elif int_i == 5:
                if list_calculation[int_i-1] == 1:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 5] == 0:
                        list_temp_P_moves.append([int_i,int_i+5])
                    if list_calculation[int_i-1 + 5] < 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i+9])
                elif list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 5] == 0:
                        list_temp_P_moves.append([int_i,int_i+5])
                    if list_calculation[int_i-1 + 5] < 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i+9])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_P_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_P_moves.append([int_i,int_i-3])
            elif (int_i == 6) or (int_i == 7):
                if list_calculation[int_i-1] == 1:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 5] == 0:
                        list_temp_P_moves.append([int_i,int_i+5])
                    if list_calculation[int_i-1 + 4] < 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i+7])
                    if list_calculation[int_i-1 + 5] < 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i+9])
                elif list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 5] == 0:
                        list_temp_P_moves.append([int_i,int_i+5])
                    if list_calculation[int_i-1 + 4] < 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i+7])
                    if list_calculation[int_i-1 + 5] < 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i+9])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_P_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_P_moves.append([int_i,int_i-3])
            elif (int_i == 13) or (int_i == 21):
                if list_calculation[int_i-1] == 1:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 5] == 0:
                        list_temp_P_moves.append([int_i,int_i+5])
                    if list_calculation[int_i-1 + 5] < 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i+9])
                elif list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 5] == 0:
                        list_temp_P_moves.append([int_i,int_i+5])
                    if list_calculation[int_i-1 + 5] < 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i+9])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_P_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_P_moves.append([int_i,int_i-3])
                    if list_calculation[int_i-1 - 3] < 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i-7])
            elif (int_i == 14) or (int_i == 15) or (int_i == 22) or (int_i == 23):
                if list_calculation[int_i-1] == 1:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 5] == 0:
                        list_temp_P_moves.append([int_i,int_i+5])
                    if list_calculation[int_i-1 + 4] < 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i+7])
                    if list_calculation[int_i-1 + 5] < 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i+9])
                elif list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 5] == 0:
                        list_temp_P_moves.append([int_i,int_i+5])
                    if list_calculation[int_i-1 + 4] < 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i+7])
                    if list_calculation[int_i-1 + 5] < 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i+9])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_P_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_P_moves.append([int_i,int_i-3])
                    if list_calculation[int_i-1 - 4] < 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i-9])
                    if list_calculation[int_i-1 - 3] < 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i-7])       
            #THE SECOND LAST ROW FOR PROMOTION; THE REST OF THE CELLS
            elif (int_i == 26) or (int_i == 27):
                if list_calculation[int_i-1] == 1:
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_P_moves.append([int_i,int_i+3])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                elif list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_P_moves.append([int_i,int_i+3])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_P_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 - 5] == 0:
                        list_temp_P_moves.append([int_i,int_i-5])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_P_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 5] < 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i-9])
                    if list_calculation[int_i-1 - 4] < 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i-7])
            #THE FINAL ROW
            elif int_i == 29:
                if list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_P_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_P_moves.append([int_i,int_i-3])
                    if list_calculation[int_i-1 - 3] < 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i-7])
            elif (int_i == 30) or (int_i == 31):
                if list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_P_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_P_moves.append([int_i,int_i-3])
                    if list_calculation[int_i-1 - 4] < 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i-9])
                    if list_calculation[int_i-1 - 3] < 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_P_jumps.append([int_i,int_i-7])
            elif int_i == 32:
                if list_calculation[int_i-1] == 2:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_P_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 4] < 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_P_jumps.append([int_i,int_i-9])
    #int_max_turn=-1 -> AI Turn
    elif int_max_turn < 0:
        for int_i in range(1,33):
            #THE FIRST AND LAST COLUMN
            if int_i == 32:
                if list_calculation[int_i-1] == -1:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 4] > 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-9])
                elif list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 4] > 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-9])
            elif (int_i == 24) or (int_i == 16):
                if list_calculation[int_i-1] == -1:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 4] > 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-9])
                elif list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 - 4] > 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-9])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 4] > 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i+7])
            elif int_i == 8:
                if list_calculation[int_i-1] == -1:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                elif list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 4] > 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i+7])
            elif int_i == 25:
                if list_calculation[int_i-1] == -1:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 4] > 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-7])
                elif list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 4] > 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-7])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i+4])
            elif (int_i == 17) or (int_i == 9):
                if list_calculation[int_i-1] == -1:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 4] > 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-7])
                elif list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 4] > 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-7])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 4] > 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i+9])
            #MIDDLE ODD COLUMNS
            elif (int_i == 31) or (int_i == 30):
                if list_calculation[int_i-1] == -1:
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i-3])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 3] > 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-7])
                    if list_calculation[int_i-1 - 4] > 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-9])
                elif list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i-3])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 3] > 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-7])
                    if list_calculation[int_i-1 - 4] > 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-9])
            elif (int_i == 23) or (int_i == 22) or (int_i == 14) or (int_i == 15):
                if list_calculation[int_i-1] == -1:
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i-3])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 3] > 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-7])
                    if list_calculation[int_i-1 - 4] > 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-9])
                elif list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i-3])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 + 5] == 0:
                        list_temp_AI_moves.append([int_i,int_i+5])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 - 3] > 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-7])
                    if list_calculation[int_i-1 - 4] > 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-9])
                    if list_calculation[int_i-1 + 5] > 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i+9])
                    if list_calculation[int_i-1 + 4] > 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i+7])
            elif int_i == 29:
                if list_calculation[int_i-1] == -1:
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i-3])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 3] > 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-7])
                elif list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i-3])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 3] > 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-7])
            elif (int_i == 21) or (int_i == 13):
                if list_calculation[int_i-1] == -1:
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i-3])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 3] > 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-7])
                elif list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i-3])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 3] > 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-7])
                    if list_calculation[int_i-1 + 5] == 0:
                        list_temp_AI_moves.append([int_i,int_i+5])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 5] > 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i+9])
            elif int_i == 5:
                if list_calculation[int_i-1] == -1:
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i-3])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                elif list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i-3])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 + 5] == 0:
                        list_temp_AI_moves.append([int_i,int_i+5])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 5] > 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i+9])                
            #MIDDLE EVEN COLUMNS
            elif int_i == 28:
                if list_calculation[int_i-1] == -1:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 5] == 0:
                        list_temp_AI_moves.append([int_i,int_i-5])
                    if list_calculation[int_i-1 - 5] > 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-9])
                elif list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 5] == 0:
                        list_temp_AI_moves.append([int_i,int_i-5])
                    if list_calculation[int_i-1 - 5] > 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-9])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i+3])
            elif (int_i == 26) or (int_i == 27):
                if list_calculation[int_i-1] == -1:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 5] == 0:
                        list_temp_AI_moves.append([int_i,int_i-5])
                    if list_calculation[int_i-1 - 4] > 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-7])
                    if list_calculation[int_i-1 - 5] > 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-9])
                elif list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 5] == 0:
                        list_temp_AI_moves.append([int_i,int_i-5])
                    if list_calculation[int_i-1 - 4] > 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-7])
                    if list_calculation[int_i-1 - 5] > 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-9])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i+3])
            elif (int_i == 12) or (int_i == 20):
                if list_calculation[int_i-1] == -1:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 5] == 0:
                        list_temp_AI_moves.append([int_i,int_i-5])
                    if list_calculation[int_i-1 - 5] > 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-9])
                elif list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 5] == 0:
                        list_temp_AI_moves.append([int_i,int_i-5])
                    if list_calculation[int_i-1 - 5] > 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-9])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i+3])
                    if list_calculation[int_i-1 + 3] > 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i+7])
            elif (int_i == 18) or (int_i == 19) or (int_i == 10) or (int_i == 11):
                if list_calculation[int_i-1] == -1:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 5] == 0:
                        list_temp_AI_moves.append([int_i,int_i-5])
                    if list_calculation[int_i-1 - 4] > 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-7])
                    if list_calculation[int_i-1 - 5] > 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-9])
                elif list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 - 5] == 0:
                        list_temp_AI_moves.append([int_i,int_i-5])
                    if list_calculation[int_i-1 - 4] > 0:
                        if list_calculation[int_i-1 - 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-7])
                    if list_calculation[int_i-1 - 5] > 0:
                        if list_calculation[int_i-1 - 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i-9])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i+3])
                    if list_calculation[int_i-1 + 4] > 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i+9])
                    if list_calculation[int_i-1 + 3] > 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i+7])       
            #THE SECOND LAST ROW FOR PROMOTION; THE REST OF THE CELLS
            elif (int_i == 6) or (int_i == 7):
                if list_calculation[int_i-1] == -1:
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i-3])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                elif list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 - 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i-3])
                    if list_calculation[int_i-1 - 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i-4])
                    if list_calculation[int_i-1 + 5] == 0:
                        list_temp_AI_moves.append([int_i,int_i+5])
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 5] > 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i+9])
                    if list_calculation[int_i-1 + 4] > 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i+7])
            #THE FINAL ROW
            elif int_i == 4:
                if list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i+3])
                    if list_calculation[int_i-1 + 3] > 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i+7])
            elif (int_i == 2) or (int_i == 3):
                if list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 3] == 0:
                        list_temp_AI_moves.append([int_i,int_i+3])
                    if list_calculation[int_i-1 + 4] > 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i+9])
                    if list_calculation[int_i-1 + 3] > 0:
                        if list_calculation[int_i-1 + 7] == 0:
                            list_temp_AI_jumps.append([int_i,int_i+7])
            elif int_i == 1:
                if list_calculation[int_i-1] == -2:
                    if list_calculation[int_i-1 + 4] == 0:
                        list_temp_AI_moves.append([int_i,int_i+4])
                    if list_calculation[int_i-1 + 4] > 0:
                        if list_calculation[int_i-1 + 9] == 0:
                            list_temp_AI_jumps.append([int_i,int_i+9])
    else:
        print("calculate_UNEXPECTED ERROR!")
    
    #Contract all the possibilities into one list
    if int_max_turn > 0:
        if len(list_temp_P_jumps) != 0:
            #list_moves = copy.deepcopy(list_temp_P_jumps)
            for int_i in list_temp_P_jumps:
                list_temp = copy.deepcopy(list_board)
                index_source = int_i[0] - 1
                index_target = int_i[1] - 1
                index_catch = catch(int_i[0], int_i[1]) - 1
                int_marker = 1
                if list_Current[index_source] == 2:
                    int_marker = 2
                list_temp[index_source] = 0
                list_temp[index_catch] = 0
                list_temp[index_target] = int_marker
                list_children.append(list_temp)
        else:
            #list_moves = copy.deepcopy(list_temp_P_moves)
            for int_i in list_temp_P_moves:
                list_temp = copy.deepcopy(list_board)
                index_source = int_i[0] - 1
                index_target = int_i[1] - 1
                int_marker = 1
                if list_Current[index_source] == 2:
                    int_marker = 2
                list_temp[index_source] = 0
                list_temp[index_target] = int_marker
                list_children.append(list_temp)
    elif int_max_turn < 0:
        if len(list_temp_AI_jumps) != 0:
            #list_moves = copy.deepcopy(list_temp_AI_jumps)
            for int_i in list_temp_AI_jumps:
                list_temp = copy.deepcopy(list_board)
                index_source = int_i[0] - 1
                index_target = int_i[1] - 1
                index_catch = catch(int_i[0], int_i[1]) - 1
                int_marker = -1
                if list_Current[index_source] == -2:
                    int_marker = -2
                list_temp[index_source] = 0
                list_temp[index_catch] = 0
                list_temp[index_target] = int_marker
                list_children.append(list_temp)
        else:
            #list_moves = copy.deepcopy(list_temp_AI_moves)
            for int_i in list_temp_AI_moves:
                list_temp = copy.deepcopy(list_board)
                index_source = int_i[0] - 1
                index_target = int_i[1] - 1
                int_marker = -1
                if list_Current[index_source] == -2:
                    int_marker = -2
                list_temp[index_source] = 0
                list_temp[index_target] = int_marker
                list_children.append(list_temp)
    else:
        print("contract_UNEXPECTED ERROR!")
    
    print("debug_HT: \n{0}".format(list_children))
    return list_children
        
    
####################
# MINIMAX STRATEGY #
####################
#
#The NimmAB mechanisms of Dr Ronald Grau are utilised at this rate.
#

#def cloneHistory(source):
#    list_dest = list(len(source))
#    ...
#However, this feature will be replaced to python "deepcopy" for a safety reason.

#HEURISTIC SCORES
#One Man = +1 point
#One AI = -1 point
#One Promoted Man = +2 point
#One Promoted AI = -2 point
##############
# CRITICISM; #
##############
#Does really a promoted piece (or "King") have to be the double score of an ordinary piece?
# !!! As a limitation of this assignment, the precise heuristic score is undiscovered yet !!!
def heuristic_score(list_board):
    int_score = 0
    for int_i in list_board:
        int_score = int_score + (int_i * 5)
    
    int_score = (-1)*int_score
    
    if list_board[9] < 0 and list_board[0] == 0 and list_board[4] > 0:
        int_score = int_score + 3
    elif list_board[0] > 0 and list_board[9] == 0 and list_board[4] < 0:
        int_score = int_score - 3
    if list_board[8] < 0 and list_board[1] == 0 and list_board[4] > 0:
        int_score = int_score + 3
    elif list_board[1] > 0 and list_board[8] == 0 and list_board[4] < 0:
        int_score = int_score - 3
    if list_board[10] < 0 and list_board[1] == 0 and list_board[5] > 0:
        int_score = int_score + 3
    elif list_board[1] > 0 and list_board[10] == 0 and list_board[5] < 0:
        int_score = int_score - 3
    if list_board[9] < 0 and list_board[2] == 0 and list_board[5] > 0:
        int_score = int_score + 3
    elif list_board[2] > 0 and list_board[9] == 0 and list_board[5] < 0:
        int_score = int_score - 3
    if list_board[11] < 0 and list_board[2] == 0 and list_board[6] > 0:
        int_score = int_score + 3
    elif list_board[2] > 0 and list_board[11] == 0 and list_board[6] < 0:
        int_score = int_score - 3
    if list_board[10] < 0 and list_board[3] == 0 and list_board[6] > 0:
        int_score = int_score + 3
    elif list_board[3] > 0 and list_board[10] == 0 and list_board[6] < 0:
        int_score = int_score - 3
    if list_board[13] < 0 and list_board[4] == 0 and list_board[9] > 0:
        int_score = int_score + 3
    elif list_board[4] > 0 and list_board[13] == 0 and list_board[9] < 0:
        int_score = int_score - 3
    if list_board[12] < 0 and list_board[5] == 0 and list_board[9] > 0:
        int_score = int_score + 3
    elif list_board[5] > 0 and list_board[12] == 0 and list_board[9] < 0:
        int_score = int_score - 3
    if list_board[14] < 0 and list_board[5] == 0 and list_board[10] > 0:
        int_score = int_score + 3
    elif list_board[5] > 0 and list_board[14] == 0 and list_board[10] < 0:
        int_score = int_score - 3
    if list_board[13] < 0 and list_board[6] == 0 and list_board[10] > 0:
        int_score = int_score + 3
    elif list_board[6] > 0 and list_board[13] == 0 and list_board[10] < 0:
        int_score = int_score - 3
    if list_board[15] < 0 and list_board[6] == 0 and list_board[11] > 0:
        int_score = int_score + 3
    elif list_board[6] > 0 and list_board[15] == 0 and list_board[11] < 0:
        int_score = int_score - 3
    if list_board[14] < 0 and list_board[7] == 0 and list_board[11] > 0:
        int_score = int_score + 3
    elif list_board[7] > 0 and list_board[14] == 0 and list_board[11] < 0:
        int_score = int_score - 3
    if list_board[16] < 0 and list_board[9] == 0 and list_board[12] > 0:
        int_score = int_score + 3
    elif list_board[9] > 0 and list_board[16] == 0 and list_board[12] < 0:
        int_score = int_score - 3
    if list_board[17] < 0 and list_board[8] == 0 and list_board[12] > 0:
        int_score = int_score + 3
    elif list_board[8] > 0 and list_board[17] == 0 and list_board[12] < 0:
        int_score = int_score - 3
    if list_board[17] < 0 and list_board[10] == 0 and list_board[13] > 0:
        int_score = int_score + 3
    elif list_board[10] > 0 and list_board[17] == 0 and list_board[13] < 0:
        int_score = int_score - 3
    if list_board[18] < 0 and list_board[9] == 0 and list_board[13] > 0:
        int_score = int_score + 3
    elif list_board[9] > 0 and list_board[18] == 0 and list_board[13] < 0:
        int_score = int_score - 3
    if list_board[19] < 0 and list_board[10] == 0 and list_board[14] > 0:
        int_score = int_score + 3
    elif list_board[10] > 0 and list_board[19] == 0 and list_board[14] < 0:
        int_score = int_score - 3
    if list_board[18] < 0 and list_board[11] == 0 and list_board[14] > 0:
        int_score = int_score + 3
    elif list_board[11] > 0 and list_board[18] == 0 and list_board[14] < 0:
        int_score = int_score - 3
    if list_board[21] < 0 and list_board[12] == 0 and list_board[17] > 0:
        int_score = int_score + 3
    elif list_board[12] > 0 and list_board[21] == 0 and list_board[17] < 0:
        int_score = int_score - 3
    if list_board[20] < 0 and list_board[13] == 0 and list_board[17] > 0:
        int_score = int_score + 3
    elif list_board[13] > 0 and list_board[20] == 0 and list_board[17] < 0:
        int_score = int_score - 3
    if list_board[22] < 0 and list_board[13] == 0 and list_board[18] > 0:
        int_score = int_score + 3
    elif list_board[13] > 0 and list_board[22] == 0 and list_board[18] < 0:
        int_score = int_score - 3
    if list_board[21] < 0 and list_board[14] == 0 and list_board[18] > 0:
        int_score = int_score + 3
    elif list_board[14] > 0 and list_board[21] == 0 and list_board[18] < 0:
        int_score = int_score - 3
    if list_board[24] < 0 and list_board[15] == 0 and list_board[19] > 0:
        int_score = int_score + 3
    elif list_board[15] > 0 and list_board[24] == 0 and list_board[19] < 0:
        int_score = int_score - 3
    if list_board[22] < 0 and list_board[15] == 0 and list_board[19] > 0:
        int_score = int_score + 3
    elif list_board[15] > 0 and list_board[22] == 0 and list_board[19] < 0:
        int_score = int_score - 3
    if list_board[25] < 0 and list_board[16] == 0 and list_board[20] > 0:
        int_score = int_score + 3
    elif list_board[16] > 0 and list_board[25] == 0 and list_board[20] < 0:
        int_score = int_score - 3
    if list_board[24] < 0 and list_board[17] == 0 and list_board[20] > 0:
        int_score = int_score + 3
    elif list_board[17] > 0 and list_board[24] == 0 and list_board[20] < 0:
        int_score = int_score - 3
    if list_board[26] < 0 and list_board[17] == 0 and list_board[21] > 0:
        int_score = int_score + 3
    elif list_board[17] > 0 and list_board[26] == 0 and list_board[21] < 0:
        int_score = int_score - 3
    if list_board[25] < 0 and list_board[18] == 0 and list_board[21] > 0:
        int_score = int_score + 3
    elif list_board[18] > 0 and list_board[25] == 0 and list_board[21] < 0:
        int_score = int_score - 3
    if list_board[27] < 0 and list_board[18] == 0 and list_board[22] > 0:
        int_score = int_score + 3
    elif list_board[18] > 0 and list_board[27] == 0 and list_board[22] < 0:
        int_score = int_score - 3
    if list_board[26] < 0 and list_board[19] == 0 and list_board[22] > 0:
        int_score = int_score + 3
    elif list_board[19] > 0 and list_board[26] == 0 and list_board[22] < 0:
        int_score = int_score - 3
    if list_board[29] < 0 and list_board[20] == 0 and list_board[25] > 0:
        int_score = int_score + 3
    elif list_board[20] > 0 and list_board[29] == 0 and list_board[25] < 0:
        int_score = int_score - 3
    if list_board[28] < 0 and list_board[21] == 0 and list_board[25] > 0:
        int_score = int_score + 3
    elif list_board[21] > 0 and list_board[28] == 0 and list_board[25] < 0:
        int_score = int_score - 3
    if list_board[30] < 0 and list_board[21] == 0 and list_board[26] > 0:
        int_score = int_score + 3
    elif list_board[21] > 0 and list_board[30] == 0 and list_board[26] < 0:
        int_score = int_score - 3
    if list_board[29] < 0 and list_board[22] == 0 and list_board[26] > 0:
        int_score = int_score + 3
    elif list_board[22] > 0 and list_board[29] == 0 and list_board[26] < 0:
        int_score = int_score - 3
    if list_board[31] < 0 and list_board[22] == 0 and list_board[27] > 0:
        int_score = int_score + 3
    elif list_board[22] > 0 and list_board[31] == 0 and list_board[27] < 0:
        int_score = int_score - 3
    if list_board[30] < 0 and list_board[23] == 0 and list_board[27] > 0:
        int_score = int_score + 3
    elif list_board[23] > 0 and list_board[30] == 0 and list_board[27] < 0:
        int_score = int_score - 3
    
    print("DEBUGGING_HS:{0}".format(int_score))
    return int_score

#def minimax(depth, alpha, beta, player):
#    int_bestScore = 0
#    ...
def minimax(list_board, int_depth, alpha, beta, int_max_turn):
    if int_depth == 0:
        int_out = heuristic_score(list_board)
        #if int_max_turn < 0:
        #    int_out = (-1) * int_out
        return int_out
    list_level = copy.deepcopy(list_board)
    #int_max_turn = -1 or +1
    if int_max_turn < 0:
        evaluation_max = -math.inf
        list_next = simulation_tree(list_board, int_max_turn)
        for list_child in list_next:
            int_evaluation = minimax(list_child, int_depth-1, alpha, beta, 1)
            evaluation_max = max(evaluation_max, int_evaluation)
            alpha = max(alpha, int_evaluation)
            #ALPHA-BETA PRUNING
            if alpha >= beta:
                break
        #THIS LEVEL VALUE of "list_level" = evaluation_max
        return evaluation_max
    else:
        evaluation_min = math.inf
        list_next = simulation_tree(list_board, int_max_turn)
        for list_child in list_next:
            int_evaluation = minimax(list_child, int_depth-1, alpha, beta, -1)
            evaluation_min = min(evaluation_min, int_evaluation)
            beta = min(beta, int_evaluation)
            #ALPHA-BETA PRUNING
            if alpha >= beta:
                break
        #THIS LEVEL VALUE of "list_level" = evaluation_min
        return evaluation_min
        
#def getAIMove():
#    successorEvaluation = list()
#    ...
#A naming sense has been changed in this programme;
#getAIMove() -> heuristic_search()
def heuristic_search():
    global list_Current
    global list_details
    global list_AI_jumps
    global list_AI_mand
    global int_AIK
    global int_Victory
    
    list_temp_current = copy.deepcopy(list_Current)
    time.sleep(1)
    state()
    #NO MOVE POSSIBLE
    list_calculation = simulation_tree(list_temp_current, -1)
    if len(list_calculation) == 0:
        print("NO POSSIBLE MOVE FOR AI!")
        int_Victory = 1
    
    int_depth = 1
    if int_Difficulties == 1:
        int_depth = 1
    elif int_Difficulties == 2:
        int_depth = 4
    
    list_new = list()
    for list_i in list_calculation:
        list_temp = list()
        value_level = minimax(list_i, int_depth, -math.inf, math.inf, 1)
        list_temp.append(value_level)
        list_temp.append(list_i)
        list_new.append(list_temp)
    
    list_sorted = sorted(list_new,key=lambda x:x[0],reverse=True)
    if len(list_sorted[0][1]) == 0:
        print("NO POSSIBLE MOVE FOR AI!")
        int_Victory = 1
    else:
        list_next = copy.deepcopy(list_sorted[0][1])
    int_score = list_sorted[0][0]
    print("new_board_Debugging={0}\nold{1}\nnew{2}".format(int_score, list_temp_current, list_next))
    #DETECTING A NEW MOVE
    int_source = 0
    int_target = 0
    int_catch = 0
    for int_i in range(0,32):
        if list_temp_current[int_i] < 0:
            if list_next[int_i] == 0:
                int_source = int_i + 1
        if list_temp_current[int_i] == 0:
            if list_next[int_i] < 0:
                int_target = int_i + 1
    int_catch = catch(int_source, int_target)
    
    #Illustrating A MOVE
    print("DEBUGGING_next_move: S{0}, T{1}".format(int_source, int_target))
    obj_X = numToObj(list_details[int_source - 1])
    temp = numToCor(int_target)
    target_X = temp[0]
    target_Y = temp[1]
    obj_X.goto(target_X, target_Y)
    
    int_marker = -1
    if list_temp_current[int_source-1] == -2:
        int_marker = -2
    list_Current[int_source-1] = 0
    list_details[int_source-1] = 0
    list_Current[int_target-1] = int_marker
    list_details[int_target-1] = objToNum(obj_X)
    
    if int_catch != -1:
        temp_obj = numToObj(list_details[int_catch-1])
        temp_obj.goto(init_X-BOARD_SIZE, init_Y-BOARD_SIZE-50)
        list_Current[int_catch-1] = 0
        list_details[int_catch-1] = 0
        
    #IF PROMOTION IS POSSIBLE:
    if int_target in [1, 2, 3, 4]:
        if int_marker == -1:
            if int_AIK == 0:
                piece_BB_1.goto(target_X, target_Y)
                obj_X.goto(init_X, init_Y)
                obj_X.hideturtle()
                piece_BB_1.showturtle()
                list_Current[int_target-1] = -2
                list_details[int_target-1] = -101
                int_AIK = 1
                #END THE TURN
                list_AI_jumps = list()
            elif int_AIK == 1:
                piece_BB_2.goto(target_X, target_Y)
                obj_X.goto(init_X, init_Y)
                obj_X.hideturtle()
                piece_BB_2.showturtle()
                list_Current[int_target-1] = -2
                list_details[int_target-1] = -102
                int_AIK = 2
                #END THE TURN
                list_AI_jumps = list()
            elif int_AIK == 2:
                piece_BB_3.goto(target_X, target_Y)
                obj_X.goto(init_X, init_Y)
                obj_X.hideturtle()
                piece_BB_3.showturtle()
                list_Current[int_target-1] = -2
                list_details[int_target-1] = -103
                int_AIK = 3
                #END THE TURN
                list_AI_jumps = list()
            elif int_AIK == 3:
                piece_BB_4.goto(target_X, target_Y)
                obj_X.goto(init_X, init_Y)
                obj_X.hideturtle()
                piece_BB_4.showturtle()
                list_Current[int_target-1] = -2
                list_details[int_target-1] = -104
                int_AIK = 4
                #END THE TURN
                list_AI_jumps = list()
            elif int_AIK == 4:
                piece_BB_5.goto(target_X, target_Y)
                obj_X.goto(init_X, init_Y)
                obj_X.hideturtle()
                piece_BB_5.showturtle()
                list_Current[int_target-1] = -2
                list_details[int_target-1] = -105
                int_AIK = 5
                #END THE TURN
                list_AI_jumps = list()
            elif int_AIK == 5:
                piece_BB_6.goto(target_X, target_Y)
                obj_X.goto(init_X, init_Y)
                obj_X.hideturtle()
                piece_BB_6.showturtle()
                list_Current[int_target-1] = -2
                list_details[int_target-1] = -106
                int_AIK = 6
                #END THE TURN
                list_AI_jumps = list()
            elif int_AIK == 6:
                piece_BB_7.goto(target_X, target_Y)
                obj_X.goto(init_X, init_Y)
                obj_X.hideturtle()
                piece_BB_7.showturtle()
                list_Current[int_target-1] = -2
                list_details[int_target-1] = -107
                int_AIK = 7
                #END THE TURN
                list_AI_jumps = list()
            elif int_AIK == 7:
                piece_BB_8.goto(target_X, target_Y)
                obj_X.goto(init_X, init_Y)
                obj_X.hideturtle()
                piece_BB_8.showturtle()
                list_Current[int_target-1] = -2
                list_details[int_target-1] = -108
                int_AIK = 8
                #END THE TURN
                list_AI_jumps = list()
            elif int_AIK == 8:
                piece_BB_9.goto(target_X, target_Y)
                obj_X.goto(init_X, init_Y)
                obj_X.hideturtle()
                piece_BB_9.showturtle()
                list_Current[int_target-1] = -2
                list_details[int_target-1] = -109
                int_AIK = 9
                #END THE TURN
                list_AI_jumps = list()
            elif int_AIK == 9:
                piece_BB_10.goto(target_X, target_Y)
                obj_X.goto(init_X, init_Y)
                obj_X.hideturtle()
                piece_BB_10.showturtle()
                list_Current[int_target-1] = -2
                list_details[int_target-1] = -110
                int_AIK = 10
                #END THE TURN
                list_AI_jumps = list()
            elif int_AIK == 10:
                piece_BB_11.goto(target_X, target_Y)
                obj_X.goto(init_X, init_Y)
                obj_X.hideturtle()
                piece_BB_11.showturtle()
                list_Current[int_target-1] = -2
                list_details[int_target-1] = -111
                int_AIK = 11
                #END THE TURN
                list_AI_jumps = list()
            elif int_AIK == 11:
                piece_BB_12.goto(target_X, target_Y)
                obj_X.goto(init_X, init_Y)
                obj_X.hideturtle()
                piece_BB_12.showturtle()
                list_Current[int_target-1] = -2
                list_details[int_target-1] = -112
                int_AIK = 12
                #END THE TURN
                list_AI_jumps = list()

    print_board()
    #IF A FURTHER MOVE IS POSSIBLE:
    #TURN OVER
    if len(list_AI_jumps) == 0:
        #int_Turn = int_Turn * (-1)
        switch_turn_to_Player()
    #else:
    #    list_AI_mand = list()
    #    list_AI_mand.append(target_index)
    #    AI_mand_move()
    else:
        state()
        mand_source = 0
        bool_mand = False
        for int_i in list_AI_jumps:
            if int_i[0] == int_target:
                mand_source = int_i[0]
                bool_mand = True
                break
        if bool_mand:
            list_AI_mand = list()
            list_AI_mand.append(mand_source)
            AI_mand_move()
        else:
            switch_turn_to_Player()

#ASSIGNMENT
#TURN OVER
def switch_turn_to_AI():
    global int_Turn
    if int_Done > 0:
        int_Turn = -1
        AI_move()
    else:
        print("TURN ERROR: {0}".format(int_Done))
def switch_turn_to_Player():
    global int_Turn
    global int_Done
    if int_Done > 0:
        int_Done = -1
        int_Turn = 1
    else:
        print("TURN ERROR: {0}".format(int_Done))

#AI LOCOMOTION CAPABILITY
def AI_move():
    if int_Difficulties == 0:
        random_move()
    elif (int_Difficulties == 1) or (int_Difficulties == 2):
        heuristic_search()
    else:
        print("ERROR: INVALID LEVEL!")

#SPECIAL MOVE FOR AI TURN
def AI_mand_move():
    global list_Current
    global list_details
    global int_Victory
    global int_AIK
    global list_AI_jumps
    global list_AI_mand
    
    time.sleep(1)
    #state(): UPDATE GAME BOARD SITUATIONS
    state()
    if len(list_AI_jumps) != 0:
        source_index = list_AI_mand[0]
        target_index = 0
        #IF DIFFICULTIES == UNSTABLE:
        for int_i, int_j in list_AI_jumps:
            if int_i == source_index:
                target_index = int_j
        obj_X = numToObj(list_details[source_index-1])
        
        temp = numToCor(target_index)
        target_X = temp[0]
        target_Y = temp[1]
        obj_X.goto(target_X, target_Y)
        
        int_marker = -1
        if list_Current[source_index-1] == -2:
            int_marker = -2
        list_Current[source_index-1] = 0
        list_details[source_index-1] = 0
        list_Current[target_index-1] = int_marker
        list_details[target_index-1] = objToNum(obj_X)
        
        temp_coor = catch(source_index, target_index)
        temp_obj = numToObj(list_details[temp_coor-1])
        temp_obj.goto(init_X-BOARD_SIZE, init_Y-BOARD_SIZE-50)
        list_Current[temp_coor-1] = 0
        list_details[temp_coor-1] = 0
        
        #IF PROMOTION IS POSSIBLE:
        if target_index in [1, 2, 3, 4]:
            if int_marker == -1:
                if int_AIK == 0:
                    piece_BB_1.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_1.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -101
                    int_AIK = 1
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 1:
                    piece_BB_2.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_2.showturtle()
                    list_Current[target_index-1] = -2
                    list_details[target_index-1] = -102
                    int_AIK = 2
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 2:
                    piece_BB_3.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_3.showturtle()
                    list_Current[int_target-1] = -2
                    list_details[int_target-1] = -103
                    int_AIK = 3
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 3:
                    piece_BB_4.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_4.showturtle()
                    list_Current[int_target-1] = -2
                    list_details[int_target-1] = -104
                    int_AIK = 4
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 4:
                    piece_BB_5.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_5.showturtle()
                    list_Current[int_target-1] = -2
                    list_details[int_target-1] = -105
                    int_AIK = 5
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 5:
                    piece_BB_6.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_6.showturtle()
                    list_Current[int_target-1] = -2
                    list_details[int_target-1] = -106
                    int_AIK = 6
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 6:
                    piece_BB_7.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_7.showturtle()
                    list_Current[int_target-1] = -2
                    list_details[int_target-1] = -107
                    int_AIK = 7
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 7:
                    piece_BB_8.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_8.showturtle()
                    list_Current[int_target-1] = -2
                    list_details[int_target-1] = -108
                    int_AIK = 8
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 8:
                    piece_BB_9.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_9.showturtle()
                    list_Current[int_target-1] = -2
                    list_details[int_target-1] = -109
                    int_AIK = 9
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 9:
                    piece_BB_10.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_10.showturtle()
                    list_Current[int_target-1] = -2
                    list_details[int_target-1] = -110
                    int_AIK = 10
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 10:
                    piece_BB_11.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_11.showturtle()
                    list_Current[int_target-1] = -2
                    list_details[int_target-1] = -111
                    int_AIK = 11
                    #END THE TURN
                    list_AI_jumps = list()
                elif int_AIK == 11:
                    piece_BB_12.goto(target_X, target_Y)
                    obj_X.goto(init_X, init_Y)
                    obj_X.hideturtle()
                    piece_BB_12.showturtle()
                    list_Current[int_target-1] = -2
                    list_details[int_target-1] = -112
                    int_AIK = 12
                    #END THE TURN
                    list_AI_jumps = list()
        
        print_board()
        #IF A FURTHER MOVE IS POSSIBLE:
        #TURN OVER
        if len(list_AI_jumps) == 0:
            #int_Turn = int_Turn * (-1)
            list_AI_mand = list()
            switch_turn_to_Player()
        #else:
        #    list_AI_mand = list()
        #    list_AI_mand.append(target_index)
        #    AI_mand_move()
        else:
            state()
            mand_source = 0
            bool_mand = False
            for int_i in list_AI_jumps:
                if int_i[0] == target_index:
                    mand_source = int_i[0]
                    bool_mand = True
                    break
            if bool_mand:
                list_AI_mand = list()
                list_AI_mand.append(mand_source)
                AI_mand_move()
            else:
                list_AI_mand = list()
                switch_turn_to_Player()
    else:
        print("AI MANDATORY MOVE FAILURE!")
        
#HUMAN DECISION
def assignment(obj_X, source_index, target_index):
    global list_Current
    global list_details
    global int_PK
    global list_P_jumps
    global list_P_mand
    global int_Done
    
    #obj_X = numToObj(source_index)
    print("DEBUGGING_POINT: {0}, {1}".format(obj_X.xcor(), obj_X.ycor()))
    print("{0}: {1}".format(int_Victory, list_P_moves))
    target_X = 0
    target_Y = 0
    if len(list_P_jumps) != 0:
        if [source_index,target_index] in list_P_jumps:
            temp = numToCor(target_index)
            target_X = temp[0]
            target_Y = temp[1]
            obj_X.goto(target_X, target_Y)
            
            int_marker = 1
            if list_Current[source_index-1] == 2:
                int_marker = 2
            list_Current[source_index-1] = 0
            list_details[source_index-1] = 0
            list_Current[target_index-1] = int_marker
            list_details[target_index-1] = objToNum(obj_X)
            
            temp_coor = catch(source_index, target_index)
            temp_obj = numToObj(list_details[temp_coor-1])
            temp_obj.goto(init_X-BOARD_SIZE, init_Y-BOARD_SIZE)
            list_Current[temp_coor-1] = 0
            list_details[temp_coor-1] = 0
            
            #IF PROMOTION IS POSSIBLE:
            if target_index in [29, 30, 31, 32]:
                if int_marker == 1:
                    if int_PK == 0:
                        piece_AA_1.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_1.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 101
                        int_PK = int_PK + 1
                        #END THE TURN
                        list_P_jumps = list()
                    elif int_PK == 1:
                        piece_AA_2.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_2.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 102
                        int_PK = int_PK + 1
                        #END THE TURN
                        list_P_jumps = list()
                    elif int_PK == 2:
                        piece_AA_3.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_3.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 103
                        int_PK = int_PK + 1
                        #END THE TURN
                        list_P_jumps = list()
                    elif int_PK == 3:
                        piece_AA_4.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_4.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 104
                        int_PK = int_PK + 1
                        #END THE TURN
                        list_P_jumps = list()
                    elif int_PK == 4:
                        piece_AA_5.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_5.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 105
                        int_PK = int_PK + 1
                        #END THE TURN
                        list_P_jumps = list()
                    elif int_PK == 5:
                        piece_AA_6.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_6.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 106
                        int_PK = int_PK + 1
                        #END THE TURN
                        list_P_jumps = list()
                    elif int_PK == 6:
                        piece_AA_7.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_7.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 107
                        int_PK = int_PK + 1
                        #END THE TURN
                        list_P_jumps = list()
                    elif int_PK == 7:
                        piece_AA_8.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_8.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 108
                        int_PK = int_PK + 1
                        #END THE TURN
                        list_P_jumps = list()
                    elif int_PK == 8:
                        piece_AA_9.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_9.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 109
                        int_PK = int_PK + 1
                        #END THE TURN
                        list_P_jumps = list()
                    elif int_PK == 9:
                        piece_AA_10.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_10.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 110
                        int_PK = int_PK + 1
                        #END THE TURN
                        list_P_jumps = list()
                    elif int_PK == 10:
                        piece_AA_11.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_11.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 111
                        int_PK = int_PK + 1
                        #END THE TURN
                        list_P_jumps = list()
                    elif int_PK == 11:
                        piece_AA_12.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_12.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 112
                        int_PK = int_PK + 1
                        #END THE TURN
                        list_P_jumps = list()
            
            print_board()
            #IF A FURTHER MOVE IS POSSIBLE:
            #TURN OVER
            if len(list_P_jumps) == 0:
                #int_Turn = int_Turn * (-1)
                #print("Thinking...")
                #AI_move()
                int_Done = int_Done * (-1)
            else:
                state()
                print("test... T{0}".format(target_index))
                print("J{0}".format(list_P_jumps))
                mand_source = 0
                bool_mand = False
                for int_i in list_P_jumps:
                    print("i{0}: {1}".format(int_i, int_i[0]))
                    if int_i[0] == target_index:
                        mand_source = int_i[0]
                        bool_mand = True
                        print("found...")
                        break
                if bool_mand:
                    list_P_mand = list()
                    list_P_mand.append(obj_X)
                else:
                    int_Done = int_Done * (-1)
        else:
            print("MOVE FAILURE: {0} = {1}, {2}".format(list_Current[target_index-1], source_index, target_index))
            print("{0}: {1}".format(int_Turn, list_P_jumps))
            obj_X.goto(asking_cor[0], asking_cor[1])
    elif len(list_P_moves) != 0:
        if [source_index,target_index] in list_P_moves:
            temp = numToCor(target_index)
            target_X = temp[0]
            target_Y = temp[1]
            obj_X.goto(target_X, target_Y)
            
            int_marker = 1
            if list_Current[source_index-1] == 2:
                int_marker = 2
            list_Current[source_index-1] = 0
            list_details[source_index-1] = 0
            list_Current[target_index-1] = int_marker
            list_details[target_index-1] = objToNum(obj_X)
            
            #temp_coor = catch(source_index, target_index)
            #list_Current[temp_coor-1] = 0
            
            #IF PROMOTION IS POSSIBLE:
            if target_index in [29, 30, 31, 32]:
                if int_marker == 1:
                    if int_PK == 0:
                        piece_AA_1.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_1.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 101
                        int_PK = int_PK + 1
                    elif int_PK == 1:
                        piece_AA_2.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_2.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 102
                        int_PK = int_PK + 1
                    elif int_PK == 2:
                        piece_AA_3.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_3.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 103
                        int_PK = int_PK + 1
                    elif int_PK == 3:
                        piece_AA_4.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_4.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 104
                        int_PK = int_PK + 1
                    elif int_PK == 4:
                        piece_AA_5.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_5.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 105
                        int_PK = int_PK + 1
                    elif int_PK == 5:
                        piece_AA_6.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_6.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 106
                        int_PK = int_PK + 1
                    elif int_PK == 6:
                        piece_AA_7.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_7.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 107
                        int_PK = int_PK + 1
                    elif int_PK == 7:
                        piece_AA_8.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_8.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 108
                        int_PK = int_PK + 1
                    elif int_PK == 8:
                        piece_AA_9.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_9.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 109
                        int_PK = int_PK + 1
                    elif int_PK == 9:
                        piece_AA_10.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_10.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 110
                        int_PK = int_PK + 1
                    elif int_PK == 10:
                        piece_AA_11.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_11.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 111
                        int_PK = int_PK + 1
                    elif int_PK == 11:
                        piece_AA_12.goto(target_X, target_Y)
                        obj_X.goto(init_X, init_Y)
                        obj_X.hideturtle()
                        piece_AA_12.showturtle()
                        list_Current[target_index-1] = 2
                        list_details[target_index-1] = 112
                        int_PK = int_PK + 1
            
            print_board()
            #IF A FURTHER MOVE IS POSSIBLE:
            #TURN OVER
            #int_Turn = int_Turn * (-1)
            #print("Thinking...")
            #AI_move()
            int_Done = int_Done * (-1)
        else:
            print("MOVE FAILURE: {0} = {1}, {2}".format(list_Current[target_index-1], source_index, target_index))
            print("{0}: {1}".format(int_Turn, list_P_moves))
            obj_X.goto(asking_cor[0], asking_cor[1])
    else:    
        print("MOVE FAILURE: {0} = {1}, {2}".format(list_Current[target_index-1], source_index, target_index))
        print("{0}-{1}: {2}\n{3}".format(int_Turn, int_Victory, list_P_jumps, list_P_moves))
        obj_X.goto(asking_cor[0], asking_cor[1])

#SPECIAL MOVE FOR HUMAN TURN      
def mand_assig(obj_X, source_index, target_index):
    global list_Current
    global list_details
    global int_PK
    global list_P_jumps
    global list_P_mand
    global int_Done
    
    #obj_X = numToObj(source_index)
    print("mand_assig: {0}, {1}".format(obj_X.xcor(), obj_X.ycor()))
    print("V{0}: J{1}".format(int_Victory, list_P_jumps))
    target_X = 0
    target_Y = 0
    if obj_X in list_P_mand:
        if len(list_P_jumps) != 0:
            if [source_index,target_index] in list_P_jumps:
                temp = numToCor(target_index)
                target_X = temp[0]
                target_Y = temp[1]
                obj_X.goto(target_X, target_Y)
                
                int_marker = 1
                if list_Current[source_index-1] == 2:
                    int_marker = 2
                list_Current[source_index-1] = 0
                list_details[source_index-1] = 0
                list_Current[target_index-1] = int_marker
                list_details[target_index-1] = objToNum(obj_X)
                
                temp_coor = catch(source_index, target_index)
                temp_obj = numToObj(list_details[temp_coor-1])
                temp_obj.goto(init_X-BOARD_SIZE, init_Y-BOARD_SIZE)
                list_Current[temp_coor-1] = 0
                list_details[temp_coor-1] = 0
                
                #IF PROMOTION IS POSSIBLE:
                if target_index in [29, 30, 31, 32]:
                    if int_marker == 1:
                        if int_PK == 0:
                            piece_AA_1.goto(target_X, target_Y)
                            obj_X.goto(init_X, init_Y)
                            obj_X.hideturtle()
                            piece_AA_1.showturtle()
                            list_Current[target_index-1] = 2
                            list_details[target_index-1] = 101
                            int_PK = int_PK + 1
                            #END THE TURN
                            list_P_jumps = list()
                        elif int_PK == 1:
                            piece_AA_2.goto(target_X, target_Y)
                            obj_X.goto(init_X, init_Y)
                            obj_X.hideturtle()
                            piece_AA_2.showturtle()
                            list_Current[target_index-1] = 2
                            list_details[target_index-1] = 102
                            int_PK = int_PK + 1
                            #END THE TURN
                            list_P_jumps = list()
                        elif int_PK == 2:
                            piece_AA_3.goto(target_X, target_Y)
                            obj_X.goto(init_X, init_Y)
                            obj_X.hideturtle()
                            piece_AA_3.showturtle()
                            list_Current[target_index-1] = 2
                            list_details[target_index-1] = 103
                            int_PK = int_PK + 1
                            #END THE TURN
                            list_P_jumps = list()
                        elif int_PK == 3:
                            piece_AA_4.goto(target_X, target_Y)
                            obj_X.goto(init_X, init_Y)
                            obj_X.hideturtle()
                            piece_AA_4.showturtle()
                            list_Current[target_index-1] = 2
                            list_details[target_index-1] = 104
                            int_PK = int_PK + 1
                            #END THE TURN
                            list_P_jumps = list()
                        elif int_PK == 4:
                            piece_AA_5.goto(target_X, target_Y)
                            obj_X.goto(init_X, init_Y)
                            obj_X.hideturtle()
                            piece_AA_5.showturtle()
                            list_Current[target_index-1] = 2
                            list_details[target_index-1] = 105
                            int_PK = int_PK + 1
                            #END THE TURN
                            list_P_jumps = list()
                        elif int_PK == 5:
                            piece_AA_6.goto(target_X, target_Y)
                            obj_X.goto(init_X, init_Y)
                            obj_X.hideturtle()
                            piece_AA_6.showturtle()
                            list_Current[target_index-1] = 2
                            list_details[target_index-1] = 106
                            int_PK = int_PK + 1
                            #END THE TURN
                            list_P_jumps = list()
                        elif int_PK == 6:
                            piece_AA_7.goto(target_X, target_Y)
                            obj_X.goto(init_X, init_Y)
                            obj_X.hideturtle()
                            piece_AA_7.showturtle()
                            list_Current[target_index-1] = 2
                            list_details[target_index-1] = 107
                            int_PK = int_PK + 1
                            #END THE TURN
                            list_P_jumps = list()
                        elif int_PK == 7:
                            piece_AA_8.goto(target_X, target_Y)
                            obj_X.goto(init_X, init_Y)
                            obj_X.hideturtle()
                            piece_AA_8.showturtle()
                            list_Current[target_index-1] = 2
                            list_details[target_index-1] = 108
                            int_PK = int_PK + 1
                            #END THE TURN
                            list_P_jumps = list()
                        elif int_PK == 8:
                            piece_AA_9.goto(target_X, target_Y)
                            obj_X.goto(init_X, init_Y)
                            obj_X.hideturtle()
                            piece_AA_9.showturtle()
                            list_Current[target_index-1] = 2
                            list_details[target_index-1] = 109
                            int_PK = int_PK + 1
                            #END THE TURN
                            list_P_jumps = list()
                        elif int_PK == 9:
                            piece_AA_10.goto(target_X, target_Y)
                            obj_X.goto(init_X, init_Y)
                            obj_X.hideturtle()
                            piece_AA_10.showturtle()
                            list_Current[target_index-1] = 2
                            list_details[target_index-1] = 110
                            int_PK = int_PK + 1
                            #END THE TURN
                            list_P_jumps = list()
                        elif int_PK == 10:
                            piece_AA_11.goto(target_X, target_Y)
                            obj_X.goto(init_X, init_Y)
                            obj_X.hideturtle()
                            piece_AA_11.showturtle()
                            list_Current[target_index-1] = 2
                            list_details[target_index-1] = 111
                            int_PK = int_PK + 1
                            #END THE TURN
                            list_P_jumps = list()
                        elif int_PK == 11:
                            piece_AA_12.goto(target_X, target_Y)
                            obj_X.goto(init_X, init_Y)
                            obj_X.hideturtle()
                            piece_AA_12.showturtle()
                            list_Current[target_index-1] = 2
                            list_details[target_index-1] = 112
                            int_PK = int_PK + 1
                            #END THE TURN
                            list_P_jumps = list()
                
                print_board()
                #IF A FURTHER MOVE IS POSSIBLE:
                #TURN OVER
                if len(list_P_jumps) == 0:
                    #int_Turn = int_Turn * (-1)
                    #print("Thinking...")
                    #AI_move()
                    list_P_mand = list()
                    int_Done = int_Done * (-1)
                else:
                    state()
                    mand_source = 0
                    bool_mand = False
                    for int_i in list_P_jumps:
                        if int_i[0] == target_index:
                            mand_source = int_i[0]
                            bool_mand = True
                            break
                    if bool_mand:
                        list_P_mand = list()
                        list_P_mand.append(obj_X)
                    else:
                        list_P_mand = list()
                        int_Done = int_Done * (-1)
            else:
                print("mand_assig: C{0} = S{1}, T{2}".format(list_Current[target_index-1], source_index, target_index))
                print("T{0}: J{1}".format(int_Turn, list_P_jumps))
                obj_X.goto(asking_cor[0], asking_cor[1])
        else:
            print("mand_assig: C{0} = S{1}, T{2}".format(list_Current[target_index-1], source_index, target_index))
            print("T{0}: J{1}".format(int_Turn, list_P_jumps))
            obj_X.goto(asking_cor[0], asking_cor[1])
    else:    
        print("mand_assig: C{0} = S{1}, T{2}".format(list_Current[target_index-1], source_index, target_index))
        print("T{0}-V{1}: J{2}\nM{3}".format(int_Turn, int_Victory, list_P_jumps, list_P_moves))
        obj_X.goto(asking_cor[0], asking_cor[1])

#LOCK LOCOMOTION
def unlock(obj_token):
    bool_lock = False
    if int_Turn == 1:
        if int_Done == -1:
            if len(list_P_mand) != 0:
                if obj_token is list_P_mand[0]:
                    bool_lock = True
                    return bool_lock
                else:
                    bool_lock = False
                    return bool_lock
            else:
                bool_lock = True
                return bool_lock
        else:
            bool_lock = False
            return bool_lock
    else:
        bool_lock = False
        return bool_lock
        
#MOVEMENT PROPERTIES
def m_A1_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_A_1):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_A_1.xcor(), piece_A_1.ycor()]
        asking_token = recording_position(piece_A_1.xcor(), piece_A_1.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_A_1.ondrag(m_A1_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_A_1)))
def m_A1_move(cor_X, cor_Y):
    if unlock(piece_A_1):
        piece_A_1.ondrag(None)
        piece_A_1.setheading(piece_A_1.towards(cor_X, cor_Y))
        piece_A_1.goto(cor_X, cor_Y)
        piece_A_1.ondrag(m_A1_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_A_1)))
def m_A1_assign(cor_X, cor_Y):
    if unlock(piece_A_1):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()    
        if len(list_P_mand) != 0:
            if piece_A_1 is list_P_mand[0]:
                mand_assig(piece_A_1, asking_token, debug_record)
        else:
            assignment(piece_A_1, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_A_1.onrelease(m_A1_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_A_1)))

def m_A2_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_A_2):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_A_2.xcor(), piece_A_2.ycor()]
        asking_token = recording_position(piece_A_2.xcor(), piece_A_2.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_A_2.ondrag(m_A2_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_A_2)))
def m_A2_move(cor_X, cor_Y):
    if unlock(piece_A_2):
        piece_A_2.ondrag(None)
        piece_A_2.setheading(piece_A_2.towards(cor_X, cor_Y))
        piece_A_2.goto(cor_X, cor_Y)
        piece_A_2.ondrag(m_A2_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_A_2)))
def m_A2_assign(cor_X, cor_Y):
    if unlock(piece_A_2):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()
        if len(list_P_mand) != 0:
            if piece_A_2 is list_P_mand[0]:
                mand_assig(piece_A_2, asking_token, debug_record)
        else:
            assignment(piece_A_2, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_A_2.onrelease(m_A2_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_A_2)))
    
def m_A3_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_A_3):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_A_3.xcor(), piece_A_3.ycor()]
        asking_token = recording_position(piece_A_3.xcor(), piece_A_3.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_A_3.ondrag(m_A3_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_A_3)))
def m_A3_move(cor_X, cor_Y):
    if unlock(piece_A_3):
        piece_A_3.ondrag(None)
        piece_A_3.setheading(piece_A_3.towards(cor_X, cor_Y))
        piece_A_3.goto(cor_X, cor_Y)
        piece_A_3.ondrag(m_A3_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_A_3)))
def m_A3_assign(cor_X, cor_Y):
    if unlock(piece_A_3):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()
        if len(list_P_mand) != 0:
            if piece_A_3 is list_P_mand[0]:
                mand_assig(piece_A_3, asking_token, debug_record)
        else:
            assignment(piece_A_3, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_A_3.onrelease(m_A3_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_A_3)))
    
def m_A4_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_A_4):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_A_4.xcor(), piece_A_4.ycor()]
        asking_token = recording_position(piece_A_4.xcor(), piece_A_4.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_A_4.ondrag(m_A4_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_A_4)))
def m_A4_move(cor_X, cor_Y):
    if unlock(piece_A_4):
        piece_A_4.ondrag(None)
        piece_A_4.setheading(piece_A_4.towards(cor_X, cor_Y))
        piece_A_4.goto(cor_X, cor_Y)
        piece_A_4.ondrag(m_A4_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_A_4)))
def m_A4_assign(cor_X, cor_Y):
    if unlock(piece_A_4):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()
        if len(list_P_mand) != 0:
            if piece_A_4 is list_P_mand[0]:
                mand_assig(piece_A_4, asking_token, debug_record)
        else:
            assignment(piece_A_4, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_A_4.onrelease(m_A4_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_A_4)))
    
def m_A5_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_A_5):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_A_5.xcor(), piece_A_5.ycor()]
        asking_token = recording_position(piece_A_5.xcor(), piece_A_5.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_A_5.ondrag(m_A5_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_A_5)))
def m_A5_move(cor_X, cor_Y):
    if unlock(piece_A_5):
        piece_A_5.ondrag(None)
        piece_A_5.setheading(piece_A_5.towards(cor_X, cor_Y))
        piece_A_5.goto(cor_X, cor_Y)
        piece_A_5.ondrag(m_A5_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_A_5)))
def m_A5_assign(cor_X, cor_Y):
    if unlock(piece_A_5):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()
        if len(list_P_mand) != 0:
            if piece_A_5 is list_P_mand[0]:
                mand_assig(piece_A_5, asking_token, debug_record)
        else:
            assignment(piece_A_5, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_A_5.onrelease(m_A5_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_A_5)))
        
def m_A6_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_A_6):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_A_6.xcor(), piece_A_6.ycor()]
        asking_token = recording_position(piece_A_6.xcor(), piece_A_6.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_A_6.ondrag(m_A6_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_A_6)))
def m_A6_move(cor_X, cor_Y):
    if unlock(piece_A_6):
        piece_A_6.ondrag(None)
        piece_A_6.setheading(piece_A_6.towards(cor_X, cor_Y))
        piece_A_6.goto(cor_X, cor_Y)
        piece_A_6.ondrag(m_A6_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_A_6)))
def m_A6_assign(cor_X, cor_Y):
    if unlock(piece_A_6):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()
        if len(list_P_mand) != 0:
            if piece_A_6 is list_P_mand[0]:
                mand_assig(piece_A_6, asking_token, debug_record)
        else:
            assignment(piece_A_6, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_A_6.onrelease(m_A6_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_A_6)))
    
def m_A7_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_A_7):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_A_7.xcor(), piece_A_7.ycor()]
        asking_token = recording_position(piece_A_7.xcor(), piece_A_7.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_A_7.ondrag(m_A7_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_A_7)))
def m_A7_move(cor_X, cor_Y):
    if unlock(piece_A_7):
        piece_A_7.ondrag(None)
        piece_A_7.setheading(piece_A_7.towards(cor_X, cor_Y))
        piece_A_7.goto(cor_X, cor_Y)
        piece_A_7.ondrag(m_A7_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_A_7)))
def m_A7_assign(cor_X, cor_Y):
    if unlock(piece_A_7):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()
        if len(list_P_mand) != 0:
            if piece_A_7 is list_P_mand[0]:
                mand_assig(piece_A_7, asking_token, debug_record)
        else:
            assignment(piece_A_7, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_A_7.onrelease(m_A7_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_A_7)))

def m_A8_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_A_8):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_A_8.xcor(), piece_A_8.ycor()]
        asking_token = recording_position(piece_A_8.xcor(), piece_A_8.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_A_8.ondrag(m_A8_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_A_8)))
def m_A8_move(cor_X, cor_Y):
    if unlock(piece_A_8):
        piece_A_8.ondrag(None)
        piece_A_8.setheading(piece_A_8.towards(cor_X, cor_Y))
        piece_A_8.goto(cor_X, cor_Y)
        piece_A_8.ondrag(m_A8_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_A_8)))
def m_A8_assign(cor_X, cor_Y):
    if unlock(piece_A_8):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()
        if len(list_P_mand) != 0:
            if piece_A_8 is list_P_mand[0]:
                mand_assig(piece_A_8, asking_token, debug_record)
        else:
            assignment(piece_A_8, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_A_8.onrelease(m_A8_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_A_8)))

def m_A9_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_A_9):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_A_9.xcor(), piece_A_9.ycor()]
        asking_token = recording_position(piece_A_9.xcor(), piece_A_9.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_A_9.ondrag(m_A9_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_A_9)))
def m_A9_move(cor_X, cor_Y):
    if unlock(piece_A_9):
        piece_A_9.ondrag(None)
        piece_A_9.setheading(piece_A_9.towards(cor_X, cor_Y))
        piece_A_9.goto(cor_X, cor_Y)
        piece_A_9.ondrag(m_A9_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_A_9)))
def m_A9_assign(cor_X, cor_Y):
    if unlock(piece_A_9):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()
        if len(list_P_mand) != 0:
            if piece_A_9 is list_P_mand[0]:
                mand_assig(piece_A_9, asking_token, debug_record)
        else:
            assignment(piece_A_9, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_A_9.onrelease(m_A9_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_A_9)))

def m_A10_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_A_10):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_A_10.xcor(), piece_A_10.ycor()]
        asking_token = recording_position(piece_A_10.xcor(), piece_A_10.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_A_10.ondrag(m_A10_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_A_10)))
def m_A10_move(cor_X, cor_Y):
    if unlock(piece_A_10):
        piece_A_10.ondrag(None)
        piece_A_10.setheading(piece_A_10.towards(cor_X, cor_Y))
        piece_A_10.goto(cor_X, cor_Y)
        piece_A_10.ondrag(m_A10_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_A_10)))
def m_A10_assign(cor_X, cor_Y):
    if unlock(piece_A_10):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()
        if len(list_P_mand) != 0:
            if piece_A_10 is list_P_mand[0]:
                mand_assig(piece_A_10, asking_token, debug_record)
        else:
            assignment(piece_A_10, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_A_10.onrelease(m_A10_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_A_10)))
    
def m_A11_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_A_11):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_A_11.xcor(), piece_A_11.ycor()]
        asking_token = recording_position(piece_A_11.xcor(), piece_A_11.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_A_11.ondrag(m_A11_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_A_11)))
def m_A11_move(cor_X, cor_Y):
    if unlock(piece_A_11):
        piece_A_11.ondrag(None)
        piece_A_11.setheading(piece_A_11.towards(cor_X, cor_Y))
        piece_A_11.goto(cor_X, cor_Y)
        piece_A_11.ondrag(m_A11_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_A_11)))
def m_A11_assign(cor_X, cor_Y):
    if unlock(piece_A_11):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()
        if len(list_P_mand) != 0:
            if piece_A_11 is list_P_mand[0]:
                mand_assig(piece_A_11, asking_token, debug_record)
        else:
            assignment(piece_A_11, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_A_11.onrelease(m_A11_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_A_11)))
    
def m_A12_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_A_12):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_A_12.xcor(), piece_A_12.ycor()]
        asking_token = recording_position(piece_A_12.xcor(), piece_A_12.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_A_12.ondrag(m_A12_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_A_12)))
def m_A12_move(cor_X, cor_Y):
    if unlock(piece_A_12):
        piece_A_12.ondrag(None)
        piece_A_12.setheading(piece_A_12.towards(cor_X, cor_Y))
        piece_A_12.goto(cor_X, cor_Y)
        piece_A_12.ondrag(m_A12_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_A_12)))
def m_A12_assign(cor_X, cor_Y):
    if unlock(piece_A_12):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()
        if len(list_P_mand) != 0:
            if piece_A_12 is list_P_mand[0]:
                mand_assig(piece_A_12, asking_token, debug_record)
        else:
            assignment(piece_A_12, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()    
        piece_A_12.onrelease(m_A12_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_A_12)))

def m_AA1_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_AA_1):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_AA_1.xcor(), piece_AA_1.ycor()]
        asking_token = recording_position(piece_AA_1.xcor(), piece_AA_1.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_AA_1.ondrag(m_AA1_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_AA_1)))
def m_AA1_move(cor_X, cor_Y):
    if unlock(piece_AA_1):
        piece_AA_1.ondrag(None)
        piece_AA_1.setheading(piece_AA_1.towards(cor_X, cor_Y))
        piece_AA_1.goto(cor_X, cor_Y)
        piece_AA_1.ondrag(m_AA1_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_AA_1)))
def m_AA1_assign(cor_X, cor_Y):
    if unlock(piece_AA_1):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()    
        if len(list_P_mand) != 0:
            if piece_AA_1 is list_P_mand[0]:
                mand_assig(piece_AA_1, asking_token, debug_record)
        else:
            assignment(piece_AA_1, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_AA_1.onrelease(m_AA1_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_AA_1)))
        
def m_AA2_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_AA_2):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_AA_2.xcor(), piece_AA_2.ycor()]
        asking_token = recording_position(piece_AA_2.xcor(), piece_AA_2.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_AA_2.ondrag(m_AA2_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_AA_2)))
def m_AA2_move(cor_X, cor_Y):
    if unlock(piece_AA_2):
        piece_AA_2.ondrag(None)
        piece_AA_2.setheading(piece_AA_2.towards(cor_X, cor_Y))
        piece_AA_2.goto(cor_X, cor_Y)
        piece_AA_2.ondrag(m_AA2_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_AA_2)))
def m_AA2_assign(cor_X, cor_Y):
    if unlock(piece_AA_2):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()    
        if len(list_P_mand) != 0:
            if piece_AA_2 is list_P_mand[0]:
                mand_assig(piece_AA_2, asking_token, debug_record)
        else:
            assignment(piece_AA_2, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_AA_2.onrelease(m_AA2_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_AA_2)))

def m_AA3_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_AA_3):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_AA_3.xcor(), piece_AA_3.ycor()]
        asking_token = recording_position(piece_AA_3.xcor(), piece_AA_3.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_AA_3.ondrag(m_AA3_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_AA_3)))
def m_AA3_move(cor_X, cor_Y):
    if unlock(piece_AA_3):
        piece_AA_3.ondrag(None)
        piece_AA_3.setheading(piece_AA_3.towards(cor_X, cor_Y))
        piece_AA_3.goto(cor_X, cor_Y)
        piece_AA_3.ondrag(m_AA3_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_AA_3)))
def m_AA3_assign(cor_X, cor_Y):
    if unlock(piece_AA_3):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()    
        if len(list_P_mand) != 0:
            if piece_AA_3 is list_P_mand[0]:
                mand_assig(piece_AA_3, asking_token, debug_record)
        else:
            assignment(piece_AA_3, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_AA_3.onrelease(m_AA3_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_AA_3)))

def m_AA4_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_AA_4):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_AA_4.xcor(), piece_AA_4.ycor()]
        asking_token = recording_position(piece_AA_4.xcor(), piece_AA_4.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_AA_4.ondrag(m_AA4_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_AA_4)))
def m_AA4_move(cor_X, cor_Y):
    if unlock(piece_AA_4):
        piece_AA_4.ondrag(None)
        piece_AA_4.setheading(piece_AA_4.towards(cor_X, cor_Y))
        piece_AA_4.goto(cor_X, cor_Y)
        piece_AA_4.ondrag(m_AA4_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_AA_4)))
def m_AA4_assign(cor_X, cor_Y):
    if unlock(piece_AA_4):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()    
        if len(list_P_mand) != 0:
            if piece_AA_4 is list_P_mand[0]:
                mand_assig(piece_AA_4, asking_token, debug_record)
        else:
            assignment(piece_AA_4, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_AA_4.onrelease(m_AA4_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_AA_4)))

def m_AA5_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_AA_5):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_AA_5.xcor(), piece_AA_5.ycor()]
        asking_token = recording_position(piece_AA_5.xcor(), piece_AA_5.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_AA_5.ondrag(m_AA5_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_AA_5)))
def m_AA5_move(cor_X, cor_Y):
    if unlock(piece_AA_5):
        piece_AA_5.ondrag(None)
        piece_AA_5.setheading(piece_AA_5.towards(cor_X, cor_Y))
        piece_AA_5.goto(cor_X, cor_Y)
        piece_AA_5.ondrag(m_AA5_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_AA_5)))
def m_AA5_assign(cor_X, cor_Y):
    if unlock(piece_AA_5):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()    
        if len(list_P_mand) != 0:
            if piece_AA_5 is list_P_mand[0]:
                mand_assig(piece_AA_5, asking_token, debug_record)
        else:
            assignment(piece_AA_5, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_AA_5.onrelease(m_AA5_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_AA_5)))
        
def m_AA6_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_AA_6):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_AA_6.xcor(), piece_AA_6.ycor()]
        asking_token = recording_position(piece_AA_6.xcor(), piece_AA_6.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_AA_6.ondrag(m_AA6_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_AA_6)))
def m_AA6_move(cor_X, cor_Y):
    if unlock(piece_AA_6):
        piece_AA_6.ondrag(None)
        piece_AA_6.setheading(piece_AA_6.towards(cor_X, cor_Y))
        piece_AA_6.goto(cor_X, cor_Y)
        piece_AA_6.ondrag(m_AA6_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_AA_6)))
def m_AA6_assign(cor_X, cor_Y):
    if unlock(piece_AA_6):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()    
        if len(list_P_mand) != 0:
            if piece_AA_6 is list_P_mand[0]:
                mand_assig(piece_AA_6, asking_token, debug_record)
        else:
            assignment(piece_AA_6, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_AA_6.onrelease(m_AA6_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_AA_6)))

def m_AA7_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_AA_7):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_AA_7.xcor(), piece_AA_7.ycor()]
        asking_token = recording_position(piece_AA_7.xcor(), piece_AA_7.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_AA_7.ondrag(m_AA7_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_AA_7)))
def m_AA7_move(cor_X, cor_Y):
    if unlock(piece_AA_7):
        piece_AA_7.ondrag(None)
        piece_AA_7.setheading(piece_AA_7.towards(cor_X, cor_Y))
        piece_AA_7.goto(cor_X, cor_Y)
        piece_AA_7.ondrag(m_AA7_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_AA_7)))
def m_AA7_assign(cor_X, cor_Y):
    if unlock(piece_AA_7):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()    
        if len(list_P_mand) != 0:
            if piece_AA_7 is list_P_mand[0]:
                mand_assig(piece_AA_7, asking_token, debug_record)
        else:
            assignment(piece_AA_7, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_AA_7.onrelease(m_AA7_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_AA_7)))

def m_AA8_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_AA_8):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_AA_8.xcor(), piece_AA_8.ycor()]
        asking_token = recording_position(piece_AA_8.xcor(), piece_AA_8.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_AA_8.ondrag(m_AA8_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_AA_8)))
def m_AA8_move(cor_X, cor_Y):
    if unlock(piece_AA_8):
        piece_AA_8.ondrag(None)
        piece_AA_8.setheading(piece_AA_8.towards(cor_X, cor_Y))
        piece_AA_8.goto(cor_X, cor_Y)
        piece_AA_8.ondrag(m_AA8_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_AA_8)))
def m_AA8_assign(cor_X, cor_Y):
    if unlock(piece_AA_8):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()    
        if len(list_P_mand) != 0:
            if piece_AA_8 is list_P_mand[0]:
                mand_assig(piece_AA_8, asking_token, debug_record)
        else:
            assignment(piece_AA_8, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_AA_8.onrelease(m_AA8_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_AA_8)))

def m_AA9_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_AA_9):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_AA_9.xcor(), piece_AA_9.ycor()]
        asking_token = recording_position(piece_AA_9.xcor(), piece_AA_9.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_AA_9.ondrag(m_AA9_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_AA_9)))
def m_AA9_move(cor_X, cor_Y):
    if unlock(piece_AA_9):
        piece_AA_9.ondrag(None)
        piece_AA_9.setheading(piece_AA_9.towards(cor_X, cor_Y))
        piece_AA_9.goto(cor_X, cor_Y)
        piece_AA_9.ondrag(m_AA9_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_AA_9)))
def m_AA9_assign(cor_X, cor_Y):
    if unlock(piece_AA_9):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()    
        if len(list_P_mand) != 0:
            if piece_AA_9 is list_P_mand[0]:
                mand_assig(piece_AA_9, asking_token, debug_record)
        else:
            assignment(piece_AA_9, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_AA_9.onrelease(m_AA9_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_AA_9)))

def m_AA10_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_AA_10):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_AA_10.xcor(), piece_AA_10.ycor()]
        asking_token = recording_position(piece_AA_10.xcor(), piece_AA_10.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_AA_10.ondrag(m_AA10_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_AA_10)))
def m_AA10_move(cor_X, cor_Y):
    if unlock(piece_AA_10):
        piece_AA_10.ondrag(None)
        piece_AA_10.setheading(piece_AA_10.towards(cor_X, cor_Y))
        piece_AA_10.goto(cor_X, cor_Y)
        piece_AA_10.ondrag(m_AA10_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_AA_10)))
def m_AA10_assign(cor_X, cor_Y):
    if unlock(piece_AA_10):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()    
        if len(list_P_mand) != 0:
            if piece_AA_10 is list_P_mand[0]:
                mand_assig(piece_AA_10, asking_token, debug_record)
        else:
            assignment(piece_AA_10, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_AA_10.onrelease(m_AA10_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_AA_10)))

def m_AA11_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_AA_11):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_AA_11.xcor(), piece_AA_11.ycor()]
        asking_token = recording_position(piece_AA_11.xcor(), piece_AA_11.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_AA_11.ondrag(m_AA11_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_AA_11)))
def m_AA11_move(cor_X, cor_Y):
    if unlock(piece_AA_11):
        piece_AA_11.ondrag(None)
        piece_AA_11.setheading(piece_AA_11.towards(cor_X, cor_Y))
        piece_AA_11.goto(cor_X, cor_Y)
        piece_AA_11.ondrag(m_AA11_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_AA_11)))
def m_AA11_assign(cor_X, cor_Y):
    if unlock(piece_AA_11):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()    
        if len(list_P_mand) != 0:
            if piece_AA_11 is list_P_mand[0]:
                mand_assig(piece_AA_11, asking_token, debug_record)
        else:
            assignment(piece_AA_11, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_AA_11.onrelease(m_AA11_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_AA_11)))

def m_AA12_init(cor_X, cor_Y):
    global asking_cor
    global asking_token
    global int_Victory
    if unlock(piece_AA_12):
        state()
        if (len(list_P_moves) == 0) and (len(list_P_jumps) == 0):
            int_Victory = -1
            print("Nought Move; Defeat!")
        asking_cor = [piece_AA_12.xcor(), piece_AA_12.ycor()]
        asking_token = recording_position(piece_AA_12.xcor(), piece_AA_12.ycor())
        piece_C_0.showturtle()
        piece_C_0.goto(asking_cor[0], asking_cor[1])
        piece_AA_12.ondrag(m_AA12_move)
    else:
        print("init_{0}: Movement Locked!".format(objToNum(piece_AA_12)))
def m_AA12_move(cor_X, cor_Y):
    if unlock(piece_AA_12):
        piece_AA_12.ondrag(None)
        piece_AA_12.setheading(piece_AA_12.towards(cor_X, cor_Y))
        piece_AA_12.goto(cor_X, cor_Y)
        piece_AA_12.ondrag(m_AA12_move)
    else:
        print("move_{0}: Movement Locked!".format(objToNum(piece_AA_12)))
def m_AA12_assign(cor_X, cor_Y):
    if unlock(piece_AA_12):
        piece_C_0.goto((-1)*(BOARD_SIZE*SIZE_MULTIPLIER)/2 + BOARD_SIZE, (BOARD_SIZE*SIZE_MULTIPLIER)/2 - BOARD_SIZE)
        piece_C_0.hideturtle()    
        if len(list_P_mand) != 0:
            if piece_AA_12 is list_P_mand[0]:
                mand_assig(piece_AA_12, asking_token, debug_record)
        else:
            assignment(piece_AA_12, asking_token, debug_record)
        if int_Done > 0:
            switch_turn_to_AI()
        piece_AA_12.onrelease(m_AA12_assign)
    else:
        print("assig_{0}: Movement Locked!".format(objToNum(piece_AA_12)))

#ALIGNMENT
piece_A_1.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + LENGTH_UNIT*10 + BOARD_SIZE)
piece_A_2.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*5 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + LENGTH_UNIT*10 + BOARD_SIZE)    
piece_A_3.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*9 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + LENGTH_UNIT*10 + BOARD_SIZE)
piece_A_4.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*13 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + LENGTH_UNIT*10 + BOARD_SIZE)
piece_A_5.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*3 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + LENGTH_UNIT*10*3 + BOARD_SIZE)
piece_A_6.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*7 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + LENGTH_UNIT*10*3 + BOARD_SIZE)
piece_A_7.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*11 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + LENGTH_UNIT*10*3 + BOARD_SIZE)
piece_A_8.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*15 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + LENGTH_UNIT*10*3 + BOARD_SIZE)
piece_A_9.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + LENGTH_UNIT*10*5 + BOARD_SIZE)
piece_A_10.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*5 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + LENGTH_UNIT*10*5 + BOARD_SIZE)    
piece_A_11.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*9 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + LENGTH_UNIT*10*5 + BOARD_SIZE)
piece_A_12.goto((-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + (LENGTH_UNIT*10*13 + 30), (-1)*BOARD_SIZE*SIZE_MULTIPLIER/2 + LENGTH_UNIT*10*5 + BOARD_SIZE)

piece_B_1.goto(numToCor(21)[0], numToCor(21)[1])
piece_B_2.goto(numToCor(22)[0], numToCor(22)[1])
piece_B_3.goto(numToCor(23)[0], numToCor(23)[1])
piece_B_4.goto(numToCor(24)[0], numToCor(24)[1])
piece_B_5.goto(numToCor(25)[0], numToCor(25)[1])
piece_B_6.goto(numToCor(26)[0], numToCor(26)[1])
piece_B_7.goto(numToCor(27)[0], numToCor(27)[1])
piece_B_8.goto(numToCor(28)[0], numToCor(28)[1])
piece_B_9.goto(numToCor(29)[0], numToCor(29)[1])
piece_B_10.goto(numToCor(30)[0], numToCor(30)[1])
piece_B_11.goto(numToCor(31)[0], numToCor(31)[1])
piece_B_12.goto(numToCor(32)[0], numToCor(32)[1])

#OFFERING ABILITIES
piece_A_1.onclick(m_A1_init)
piece_A_1.onrelease(m_A1_assign)
piece_A_2.onclick(m_A2_init)
piece_A_2.onrelease(m_A2_assign)
piece_A_3.onclick(m_A3_init)
piece_A_3.onrelease(m_A3_assign)
piece_A_4.onclick(m_A4_init)
piece_A_4.onrelease(m_A4_assign)
piece_A_5.onclick(m_A5_init)
piece_A_5.onrelease(m_A5_assign)
piece_A_6.onclick(m_A6_init)
piece_A_6.onrelease(m_A6_assign)
piece_A_7.onclick(m_A7_init)
piece_A_7.onrelease(m_A7_assign)
piece_A_8.onclick(m_A8_init)
piece_A_8.onrelease(m_A8_assign)
piece_A_9.onclick(m_A9_init)
piece_A_9.onrelease(m_A9_assign)
piece_A_10.onclick(m_A10_init)
piece_A_10.onrelease(m_A10_assign)
piece_A_11.onclick(m_A11_init)
piece_A_11.onrelease(m_A11_assign)
piece_A_12.onclick(m_A12_init)
piece_A_12.onrelease(m_A12_assign)

piece_C_0.onclick(dummy_func_A)
piece_C_0.onrelease(dummy_func_B)
button_A_0.onrelease(click_box)

piece_AA_1.onclick(m_AA1_init)
piece_AA_1.onrelease(m_AA1_assign)
piece_AA_2.onclick(m_AA2_init)
piece_AA_2.onrelease(m_AA2_assign)
piece_AA_3.onclick(m_AA3_init)
piece_AA_3.onrelease(m_AA3_assign)
piece_AA_4.onclick(m_AA4_init)
piece_AA_4.onrelease(m_AA4_assign)
piece_AA_5.onclick(m_AA5_init)
piece_AA_5.onrelease(m_AA5_assign)
piece_AA_6.onclick(m_AA6_init)
piece_AA_6.onrelease(m_AA6_assign)
piece_AA_7.onclick(m_AA7_init)
piece_AA_7.onrelease(m_AA7_assign)
piece_AA_8.onclick(m_AA8_init)
piece_AA_8.onrelease(m_AA8_assign)
piece_AA_9.onclick(m_AA9_init)
piece_AA_9.onrelease(m_AA9_assign)
piece_AA_10.onclick(m_AA10_init)
piece_AA_10.onrelease(m_AA10_assign)
piece_AA_11.onclick(m_AA11_init)
piece_AA_11.onrelease(m_AA11_assign)
piece_AA_12.onclick(m_AA12_init)
piece_AA_12.onrelease(m_AA12_assign)

#############
# MAIN GAME #
#############
while True:
    checkers_app.update()

    debug_canvas.bind('<Motion>', debug_monitor)

    #!!!In write(), there is a crucial glitch which causes stack overflow when it comes to fast move.!!!
    debug_pen_A.clear()
    debug_pen_A.write("( {0} , {1} )".format(debug_Xcor, debug_Ycor), align="center", font=(TYPEFACE, FONT_SIZE, "normal"))
    debug_pen_B.clear()
    debug_pen_B.write("?> {0}".format(debug_record), align="center", font=(TYPEFACE, FONT_SIZE, "normal"))
    debug_pen_C.clear()
    debug_pen_C.write("( {0} <? )".format(asking_token), align="center", font=(TYPEFACE, FONT_SIZE, "normal"))
    
    debug_pen_D.clear()
    str_difficulty = ""
    if int_Difficulties == 0:
        str_difficulty = "UNSTABLE (RANDOM)"
    elif int_Difficulties == 1:
        str_difficulty = "EASY (DEPTH LIMIT 1)"
    elif int_Difficulties == 2:
        str_difficulty = "MEDIUM (DEPTH LIMIT 4)"

    debug_pen_D.write("AI STRENGTH: \n{0}={1}".format(int_Difficulties, str_difficulty), align="center", font=(TYPEFACE, FONT_SIZE, "normal"))
    
    debug_pen_E.clear()
    if int_Victory == -1:
        debug_pen_E.write("GAME END ({0}): AI WON!".format(int_Victory), align="center", font=(TYPEFACE, FONT_SIZE, "normal"))
        time.sleep(3)
        break
    elif int_Victory == 1:
        debug_pen_E.write("GAME END ({0}): PLAYER WON!".format(int_Victory), align="center", font=(TYPEFACE, FONT_SIZE, "normal"))
        time.sleep(3)
        break
  