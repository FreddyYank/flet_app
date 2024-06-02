
import time
import flet as ft

import asyncio
async def main(page: ft.Page) -> None:
    page.title = 'StarBit'
    page.favicon = 'https://cdn.discordapp.com/attachments/1155259038557290567/1246189185694568519/1675337648_gas-kvas-com-p-art-ri.png?ex=665b7b9e&is=665a2a1e&hm=9e42695b3f2ca97261779704f11dbffb815aa0c7493e177de915c7203ecf95c9&'
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = '#141221'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {"SourceCode":'https://github.com/adobe-fonts/source-code-pro/blob/release/TTF/SourceCodePro-Black.ttf'}
    page.theme = ft.Theme(font_family='SourceCode')



    async def score_up(event: ft.ContainerTapEvent) -> None:
        score.data += 1
        score.value = str(score.data)

        image.scale = 0.95

        score_counter.opacity = 50
        score_counter.value = "+1"
        score_counter.right = 0
        score_counter.left = 11
        score_counter.top = 10
        score_counter.bottom = 0

        await page.update_async()

        await asyncio.sleep(0.1)
        image.scale = 1
        score_counter.opacity = 0

        await page.update_async()




    score = ft.Text(value='0', size=65, data=0)
    score_counter = ft.Text(size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN))

    image = ft.Image(
        src='assets/imag.png',
        fit=ft.ImageFit.CONTAIN,

        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)
    )

    await page.add_async(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            margin=ft.Margin(0, 0, 0, 30),
            on_click=score_up

        )
    )

if __name__ == '__main__':
    ft.app(target=main, port=8000,view=ft.WEB_BROWSER)
