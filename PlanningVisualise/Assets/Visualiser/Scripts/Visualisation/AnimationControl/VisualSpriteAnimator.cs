using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using Visualiser;
using UnityEngine.SceneManagement;

namespace VisualSpriteAnimation {

	public class VisualSpriteAnimator : MonoBehaviour
	{
		public bool Forming { get; set; }
		public bool Dying { get; set; }
		public bool Animating { get; set; }
		bool highlighting;
		public const float subgoal_brightness = (float)0.5;

		public bool Highlighting 
		{   get 
			{
				return highlighting;
			}
			set
			{
				highlighting = value;
				if (!highlighting)
				{
					if (canvasGroup != null)
						canvasGroup.alpha = 1;
				}
			}
		}

		protected bool fadeingOut = true;

		protected VisualSpriteObject visualSprite;

		protected Slider aniSpeedSlider;

		protected CanvasGroup canvasGroup;

		public event EventHandler OnDied;

		// Use this for initialization
		void Start()
		{
			visualSprite = GetComponent<SpriteController>().GetVisualSprite();
			canvasGroup = GetComponent<CanvasGroup>();
			aniSpeedSlider = GameObject.Find("AniSpeedSlider").GetComponent<Slider>();

			Setup();
		}

		protected virtual void Setup()
		{

		}

		// Update is called once per frame
		void Update()
		{
			try {
			if (Forming)
			{
				if (canvasGroup.alpha < 1)
				{
					canvasGroup.alpha += Time.deltaTime;
				}
				else
				{
					Forming = false;
				}
			}

			if (Dying)
			{
				if (canvasGroup.alpha > 0)
				{
					// canvasGroup.alpha -= Time.deltaTime;
				}
				else
				{
					Dying = false;
					OnDied?.Invoke(this, null);
				}
			}

			if (Animating)
			{
				switch(visualSprite.transferType)
				{
				default:
					Animate();
					break;
				}
			}

			// Get the original object colour
			var image = gameObject.GetComponent<Image>();
			var originalColor = visualSprite.color;
			float red = originalColor.r;
			float green = originalColor.g;
			float blue= originalColor.b;

			// Darkening of objects when subgoal is complete
			if (!Animating && Highlighting)

			{

				// Get new, adjusted color
				red *= subgoal_brightness;
				green *= subgoal_brightness;
				blue *= subgoal_brightness;

				if (canvasGroup.alpha <= 0.3)
				{
					fadeingOut = false;
				}
				else if (canvasGroup.alpha >= 1)
				{
					fadeingOut = true;
				}
			}

			// Set image colour
			image.color = new Color(red, green, blue, 1);
			}catch (Exception e){
				SceneManager.LoadScene("NetworkError");
			}
		}

		protected virtual void Animate()
		{
		}

		public void UpdateVisualSprite(VisualSpriteObject vso)
		{
			visualSprite = vso;
		}
	}
}