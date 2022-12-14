# Generated from Python.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete listener for a parse tree produced by PythonParser.
class PythonListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParser#prog.
    def enterProg(self, ctx:PythonParser.ProgContext):
        pass

    # Exit a parse tree produced by PythonParser#prog.
    def exitProg(self, ctx:PythonParser.ProgContext):
        pass


    # Enter a parse tree produced by PythonParser#Function_A.
    def enterFunction_A(self, ctx:PythonParser.Function_AContext):
        pass

    # Exit a parse tree produced by PythonParser#Function_A.
    def exitFunction_A(self, ctx:PythonParser.Function_AContext):
        pass


    # Enter a parse tree produced by PythonParser#Function_B.
    def enterFunction_B(self, ctx:PythonParser.Function_BContext):
        pass

    # Exit a parse tree produced by PythonParser#Function_B.
    def exitFunction_B(self, ctx:PythonParser.Function_BContext):
        pass


    # Enter a parse tree produced by PythonParser#Function_C.
    def enterFunction_C(self, ctx:PythonParser.Function_CContext):
        pass

    # Exit a parse tree produced by PythonParser#Function_C.
    def exitFunction_C(self, ctx:PythonParser.Function_CContext):
        pass


    # Enter a parse tree produced by PythonParser#Variable.
    def enterVariable(self, ctx:PythonParser.VariableContext):
        pass

    # Exit a parse tree produced by PythonParser#Variable.
    def exitVariable(self, ctx:PythonParser.VariableContext):
        pass


    # Enter a parse tree produced by PythonParser#Number.
    def enterNumber(self, ctx:PythonParser.NumberContext):
        pass

    # Exit a parse tree produced by PythonParser#Number.
    def exitNumber(self, ctx:PythonParser.NumberContext):
        pass


    # Enter a parse tree produced by PythonParser#Str.
    def enterStr(self, ctx:PythonParser.StrContext):
        pass

    # Exit a parse tree produced by PythonParser#Str.
    def exitStr(self, ctx:PythonParser.StrContext):
        pass


    # Enter a parse tree produced by PythonParser#string.
    def enterString(self, ctx:PythonParser.StringContext):
        pass

    # Exit a parse tree produced by PythonParser#string.
    def exitString(self, ctx:PythonParser.StringContext):
        pass


    # Enter a parse tree produced by PythonParser#main_function.
    def enterMain_function(self, ctx:PythonParser.Main_functionContext):
        pass

    # Exit a parse tree produced by PythonParser#main_function.
    def exitMain_function(self, ctx:PythonParser.Main_functionContext):
        pass


    # Enter a parse tree produced by PythonParser#custom_function.
    def enterCustom_function(self, ctx:PythonParser.Custom_functionContext):
        pass

    # Exit a parse tree produced by PythonParser#custom_function.
    def exitCustom_function(self, ctx:PythonParser.Custom_functionContext):
        pass


    # Enter a parse tree produced by PythonParser#Built_print.
    def enterBuilt_print(self, ctx:PythonParser.Built_printContext):
        pass

    # Exit a parse tree produced by PythonParser#Built_print.
    def exitBuilt_print(self, ctx:PythonParser.Built_printContext):
        pass


    # Enter a parse tree produced by PythonParser#Built_scan.
    def enterBuilt_scan(self, ctx:PythonParser.Built_scanContext):
        pass

    # Exit a parse tree produced by PythonParser#Built_scan.
    def exitBuilt_scan(self, ctx:PythonParser.Built_scanContext):
        pass


    # Enter a parse tree produced by PythonParser#Var_A.
    def enterVar_A(self, ctx:PythonParser.Var_AContext):
        pass

    # Exit a parse tree produced by PythonParser#Var_A.
    def exitVar_A(self, ctx:PythonParser.Var_AContext):
        pass


    # Enter a parse tree produced by PythonParser#Var_B.
    def enterVar_B(self, ctx:PythonParser.Var_BContext):
        pass

    # Exit a parse tree produced by PythonParser#Var_B.
    def exitVar_B(self, ctx:PythonParser.Var_BContext):
        pass


    # Enter a parse tree produced by PythonParser#var_decl.
    def enterVar_decl(self, ctx:PythonParser.Var_declContext):
        pass

    # Exit a parse tree produced by PythonParser#var_decl.
    def exitVar_decl(self, ctx:PythonParser.Var_declContext):
        pass


    # Enter a parse tree produced by PythonParser#var_assign.
    def enterVar_assign(self, ctx:PythonParser.Var_assignContext):
        pass

    # Exit a parse tree produced by PythonParser#var_assign.
    def exitVar_assign(self, ctx:PythonParser.Var_assignContext):
        pass


    # Enter a parse tree produced by PythonParser#Math_Operation.
    def enterMath_Operation(self, ctx:PythonParser.Math_OperationContext):
        pass

    # Exit a parse tree produced by PythonParser#Math_Operation.
    def exitMath_Operation(self, ctx:PythonParser.Math_OperationContext):
        pass


    # Enter a parse tree produced by PythonParser#Math_Operation_Simplified.
    def enterMath_Operation_Simplified(self, ctx:PythonParser.Math_Operation_SimplifiedContext):
        pass

    # Exit a parse tree produced by PythonParser#Math_Operation_Simplified.
    def exitMath_Operation_Simplified(self, ctx:PythonParser.Math_Operation_SimplifiedContext):
        pass


    # Enter a parse tree produced by PythonParser#conditional.
    def enterConditional(self, ctx:PythonParser.ConditionalContext):
        pass

    # Exit a parse tree produced by PythonParser#conditional.
    def exitConditional(self, ctx:PythonParser.ConditionalContext):
        pass


    # Enter a parse tree produced by PythonParser#conditional_branches.
    def enterConditional_branches(self, ctx:PythonParser.Conditional_branchesContext):
        pass

    # Exit a parse tree produced by PythonParser#conditional_branches.
    def exitConditional_branches(self, ctx:PythonParser.Conditional_branchesContext):
        pass


    # Enter a parse tree produced by PythonParser#Switch_Case.
    def enterSwitch_Case(self, ctx:PythonParser.Switch_CaseContext):
        pass

    # Exit a parse tree produced by PythonParser#Switch_Case.
    def exitSwitch_Case(self, ctx:PythonParser.Switch_CaseContext):
        pass


    # Enter a parse tree produced by PythonParser#If.
    def enterIf(self, ctx:PythonParser.IfContext):
        pass

    # Exit a parse tree produced by PythonParser#If.
    def exitIf(self, ctx:PythonParser.IfContext):
        pass


    # Enter a parse tree produced by PythonParser#conditional_branch.
    def enterConditional_branch(self, ctx:PythonParser.Conditional_branchContext):
        pass

    # Exit a parse tree produced by PythonParser#conditional_branch.
    def exitConditional_branch(self, ctx:PythonParser.Conditional_branchContext):
        pass


    # Enter a parse tree produced by PythonParser#conditional_lines.
    def enterConditional_lines(self, ctx:PythonParser.Conditional_linesContext):
        pass

    # Exit a parse tree produced by PythonParser#conditional_lines.
    def exitConditional_lines(self, ctx:PythonParser.Conditional_linesContext):
        pass


    # Enter a parse tree produced by PythonParser#print.
    def enterPrint(self, ctx:PythonParser.PrintContext):
        pass

    # Exit a parse tree produced by PythonParser#print.
    def exitPrint(self, ctx:PythonParser.PrintContext):
        pass


    # Enter a parse tree produced by PythonParser#scan.
    def enterScan(self, ctx:PythonParser.ScanContext):
        pass

    # Exit a parse tree produced by PythonParser#scan.
    def exitScan(self, ctx:PythonParser.ScanContext):
        pass



del PythonParser