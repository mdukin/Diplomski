using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class TicTacManager : MonoBehaviour
{
    public TextMeshProUGUI uiText;
    public int interval = 1;
    Boolean isTic = true;
    void Start()
    {
        uiText = GetComponent<TextMeshProUGUI>();
        InvokeRepeating(nameof(tictac), interval, interval);
    }

    void tictac()
    {
        if (isTic)
            uiText.text = "TAC";
        else
            uiText.text = "TIC";
        isTic = !isTic;
    }
}
