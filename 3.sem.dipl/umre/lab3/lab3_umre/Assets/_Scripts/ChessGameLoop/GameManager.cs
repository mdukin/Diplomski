﻿using Newtonsoft.Json.Linq;
using UnityEngine;
using UnityEngine.UI;
namespace ChessMainLoop
{
    public delegate void PieceMoved();

    public class GameManager : Singleton<GameManager>
    {
        [SerializeField] private CameraControl _camera;
        [SerializeField] private AudioSource _checkSound;
        private int _turnCount = 0;
        private SideColor _turnPlayer;
        private SideColor _checkedSide;
        private Pawn _passantable = null;
        private bool _isPieceMoving = false;
        private Pawn _promotingPawn = null;

        public int TurnCount { get => _turnCount; }
        public SideColor TurnPlayer { get => _turnPlayer; set => _turnPlayer = value; }
        public SideColor CheckedSide { get => _checkedSide; set => _checkedSide = Check(value); }
        public Pawn Passantable { get => _passantable; set => _passantable = value; }
        public bool IsPieceMoving { get => _isPieceMoving; set => _isPieceMoving = value; }

        private void Start()
        {
            _turnPlayer = SideColor.White;
            _checkedSide = SideColor.None;

        }

        /// <summary>
        /// Returns color of checked player and if there is a check plays check sound.
        /// </summary>
        /// <param name="checkSide"></param>
        /// <returns>Color of player that is checked</returns>
        private SideColor Check(SideColor checkSide)
        {
            if (_checkedSide == SideColor.None && checkSide != SideColor.None)
            {
                _checkSound.Play();
            }
            return checkSide == SideColor.Both ? _turnPlayer == SideColor.White ? SideColor.Black : SideColor.White : checkSide;
        }

        public void ChangeTurn()
        {

            ////
            
            int value = BoardState.Instance.getBoardValue();

            Debug.Log(value);

            if (Mathf.Abs(value) >= 1000) 
                GameEnd(_turnPlayer);

            ////
            _turnPlayer = _turnPlayer == SideColor.White ? SideColor.Black : SideColor.White;
            _turnCount++;

            SideColor sideColor = BoardState.Instance.CheckIfGameOver();
            if (sideColor != SideColor.None)
            {
                GameEnd(sideColor);
            }


        }

        public void GameEnd(SideColor winner)
        {
            Debug.Log("winner");
            UIManager.Instance.GameOver(winner);

            _camera.enabled = false;


        }

        /// <summary>
        /// Resets state variables and starts a new round.
        /// </summary>
        public void Restart()
        {
            ObjectPool.Instance.ResetPieces();
            BoardState.Instance.ResetPieces();
            _camera.enabled = true;
            MoveTracker.Instance.ResetMoves();
            _turnCount = 0;
            _turnPlayer = SideColor.White;
            _checkedSide = SideColor.None;
            _passantable = null;
        }

        public void PawnPromoting(Pawn _pawn)
        {
            _promotingPawn = _pawn;
            UIManager.Instance.PawnPromotionMenu(_pawn.PieceColor);
            _camera.enabled = false;
        }

        /// <summary>
        /// Replaces pawn that is getting promoted with selected piece, then checks for checkmate.
        /// </summary>
        public void SelectedPromotion(Piece piece, ChessPieceType pieceIndex)
        {
            _camera.enabled = true;
            piece.transform.parent = _promotingPawn.transform.parent;
            piece.transform.localScale = _promotingPawn.transform.localScale;
            BoardState.Instance.PromotePawn(_promotingPawn, piece, pieceIndex);

            SideColor _winner = BoardState.Instance.CheckIfGameOver();
            if (_winner != SideColor.None)
            {
                if (_turnPlayer == SideColor.White)
                {
                    _winner = SideColor.Black;
                }
                else if (_turnPlayer == SideColor.Black)
                {
                    _winner = SideColor.White;
                }

                GameEnd(_winner);
            }

            _promotingPawn = null;
        }
    }
}
