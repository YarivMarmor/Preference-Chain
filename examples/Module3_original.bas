Attribute VB_Name = "Module3"

Sub Macro2()
Attribute Macro2.VB_ProcData.VB_Invoke_Func = "M\n14"
'
' Macro2 Macro
'
' Keyboard Shortcut: Ctrl+Shift+M
'

Dim L1, L2 As Integer
Dim P1, P2 As Range
Dim Nom1, Nom2, Dom As Integer
Dim Matrix1, Matrix2 As Variant
Dim myValue As Variant

    Nom1 = 0: Nom2 = 0: Dom = 0
    Range("a2").Select
    Range(Selection, Selection.End(xlDown)).ClearContents
    
       
    
    Range("B2").Select
    Set P1 = Range(Selection, Selection.End(xlDown))
    L1 = P1.Rows.Count
    Range("C2").Select
    Set P2 = Range(Selection, Selection.End(xlDown))
    L2 = P2.Rows.Count
    Range("C14").Select
    
    ReDim Matrix1(1 To L1, 1 To L1)
    ReDim Matrix2(1 To L2, 1 To L2)
    
    If L1 <> L2 Then MsgBox "not same length"
    For i = 1 To L1
        If P1(i).Value <= 0 Or P1(i).Value > L1 Then
            'MsgBox "Category 1 at row " & i & " is not valid number"
            myValue = InputBox("Preference 1 at row " & i & " is not valid number. Please provide better one.")
            P1(i).Value = myValue
        End If
        If P2(i).Value <= 0 Or P2(i).Value > L1 Then
            'MsgBox "Category 2 at row " & i & " is not valid number"
            myValue = InputBox("Preference 2 at row " & i & " is not valid number. Please provide better one.")
            P2(i).Value = myValue
        End If
    Next i
    
    
    For i = 1 To L1
        
        Range("A2").Offset(i - 1, 0).Value = i
        For j = 1 To L1
            
            If P1(i).Value < P1(j) Then Matrix1(i, j) = 1
            If P1(i).Value > P1(j) Then Matrix1(i, j) = -1
            If P1(i).Value = P1(j) Then Matrix1(i, j) = 0
            If P2(i).Value < P2(j) Then Matrix2(i, j) = 1
            If P2(i).Value > P2(j) Then Matrix2(i, j) = -1
            If P2(i).Value = P2(j) Then Matrix2(i, j) = 0
            
            Nom1 = Nom1 + Matrix1(i, j) * Matrix1(i, j)
            Nom2 = Nom2 + Matrix2(i, j) * Matrix2(i, j)
            Dom = Dom + Matrix1(i, j) * Matrix2(i, j)
            
            
        Next j
    Next i
    
    If Nom1 = 0 Then MsgBox "Preference 1 is not correct, please modify"
    If Nom2 = 0 Then MsgBox "Preference 2 is not correct, please modify"
    If Nom1 * Nom2 > 0 Then
        Range("Cosin").Value = Dom / Sqr(Nom1 * Nom2)
        Range("Distance").Value = Application.Acos(Dom / Sqr(Nom1 * Nom2)) / WorksheetFunction.Pi
    End If
End Sub
