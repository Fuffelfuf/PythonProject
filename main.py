from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QUrl, QTime
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from mus_player import Ui_musPlayer
import pickle

class MusicListManager:
    def __init__(self):
        self.music_list = []
        self.current_song_index = 0
        self.load_music_list()

    def add_music(self, file_path):
        if file_path and file_path not in self.music_list:
            self.music_list.append(file_path)
            self.save_music_list()

    def remove_music(self, index):
        if index < len(self.music_list):
            self.music_list.pop(index)
            self.save_music_list()

    def next_song(self, media_controller):
            media_controller.stop_music()
            if media_controller.repeat_current_song:
                media_controller.set_media(self.get_current_song())
                media_controller.play()
            elif self.current_song_index < len(self.music_list) - 1:
                self.current_song_index += 1
                media_controller.set_media(self.get_current_song())
                media_controller.play()
            elif media_controller.repeat_all:
                self.current_song_index = 0
                media_controller.set_media(self.get_current_song())
                media_controller.play()

    def prev_song(self):
        if self.music_list:
            self.current_song_index = (self.current_song_index - 1) % len(self.music_list)
            return self.get_current_song()

    def get_current_song(self):
        if self.current_song_index < len(self.music_list):
            return self.music_list[self.current_song_index]
        return None

    def load_music_list(self):
        try:
            with open('music_list.pkl', 'rb') as file:
                self.music_list = pickle.load(file)
        except FileNotFoundError:
            self.music_list = []

    def save_music_list(self):
        with open('music_list.pkl', 'wb') as file:
            pickle.dump(self.music_list, file)

class MediaPlayerController:
    def __init__(self):
        self.media_player = QMediaPlayer()
        self.playing = False
        self.repeat_current_song = False
        self.repeat_all = False

    def set_media(self, song_path):
        if song_path:
            media_content = QMediaContent(QUrl.fromLocalFile(song_path))
            self.media_player.setMedia(media_content)

    def toggle_play_pause(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def stop_music(self):
        self.media_player.stop()

    def change_volume(self, value):
        self.media_player.setVolume(value)

    def set_position(self, position):
        self.media_player.setPosition(position)

    def play(self):
        self.media_player.play()

    def pause(self):
        self.media_player.pause()

    def is_playing(self):
        return self.media_player.state() == QMediaPlayer.PlayingState

    def toggle_repeat(self):
        self.repeat_current_song = not self.repeat_current_song

    def toggle_repeat_all(self):
        self.repeat_all = not self.repeat_all

class PlayerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_musPlayer()
        self.ui.setupUi(self)

        self.music_manager = MusicListManager()
        self.media_controller = MediaPlayerController()

        self.media_controller.media_player.stateChanged.connect(self.media_state_changed)
        self.media_controller.media_player.positionChanged.connect(self.position_changed)
        self.media_controller.media_player.durationChanged.connect(self.duration_changed)

        self.setup_ui_connections()

        self.update_music_list_widget()

        self.base_volume=10
        self.ui.volumeSlider.setValue(self.base_volume)
    def setup_ui_connections(self):
        self.ui.playPauseButton.clicked.connect(self.toggle_play_pause)
        self.ui.stopButton.clicked.connect(self.stop_music)
        self.ui.volumeSlider.valueChanged.connect(self.change_volume)
        self.ui.addButton.clicked.connect(self.add_music)
        self.ui.removeButton.clicked.connect(self.remove_music)
        self.ui.nextButton.clicked.connect(self.next_song_button_clicked)
        self.ui.prevButton.clicked.connect(self.prev_song_button_clicked)
        self.ui.songSlider.sliderPressed.connect(self.slider_pressed)
        self.ui.songSlider.sliderReleased.connect(self.slider_released)
        self.ui.songSlider.sliderMoved.connect(self.slider_moved)

        self.ui.repeatBox.clicked.connect(self.media_controller.toggle_repeat)
        self.ui.repeatallBox.clicked.connect(self.media_controller.toggle_repeat_all)
        self.ui.musiclist.itemClicked.connect(self.item_clicked)

    def toggle_play_pause(self):
        self.media_controller.toggle_play_pause()

    def stop_music(self):
        self.media_controller.stop_music()

    def change_volume(self, value):
        self.media_controller.change_volume(value)

    def add_music(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Choose file", "", "Audio Files (*.mp3);;All Files (*)",
                                                   options=options)
        self.music_manager.add_music(file_path)
        self.update_music_list_widget()

    def remove_music(self):
        self.music_manager.remove_music(self.music_manager.current_song_index)
        self.update_music_list_widget()
        self.ui.musicname.clear()
        self.media_controller.stop_music()

    def update_music_list_widget(self):
        self.ui.musiclist.clear()
        for file_path in self.music_manager.music_list:
            self.ui.musiclist.addItem(QUrl.fromLocalFile(file_path).fileName())

    def item_clicked(self, item):
        self.music_manager.current_song_index = self.ui.musiclist.row(item)
        self.play_selected_song()

    def play_selected_song(self):
        song = self.music_manager.get_current_song()
        if song:
            self.media_controller.set_media(song)
            self.media_controller.play()
            self.update_musicname()

    def next_song_button_clicked(self):
        self.music_manager.next_song(self.media_controller)
        self.update_musicname()

    def prev_song_button_clicked(self):
        self.media_controller.stop_music()
        prev_song = self.music_manager.prev_song()
        if prev_song:
            self.play_selected_song()

    def media_state_changed(self, state):
        if state == QMediaPlayer.PlayingState:
            self.media_controller.playing = True
        else:
            self.media_controller.playing = False

    def position_changed(self, position):
        if not self.ui.songSlider.isSliderDown():
            self.ui.songSlider.setValue(position)
        current_time = QTime(0, position // 60000, (position // 1000) % 60)
        self.ui.timerLabel.setText(current_time.toString("mm:ss"))
        if position >= self.media_controller.media_player.duration() - 1000 and position != 0:
            self.music_manager.next_song(self.media_controller)
            self.update_musicname()

    def duration_changed(self, duration):
        self.ui.songSlider.setMaximum(duration)

    def slider_pressed(self):
        self.media_controller.playing_before_slider_move = self.media_controller.is_playing()
        self.media_controller.pause()

    def slider_moved(self):
        if self.media_controller.playing_before_slider_move:
            new_position = self.ui.songSlider.value()
            self.media_controller.set_position(new_position)

    def slider_released(self):
        if self.media_controller.playing_before_slider_move:
            self.media_controller.play()

    def update_musicname(self):
        song = self.music_manager.get_current_song()
        if song:
            current_song_name = QUrl.fromLocalFile(song).fileName()
            self.ui.musicname.setText(current_song_name)

if __name__ == "__main__":
    app = QApplication([])
    window = PlayerWindow()
    window.show()
    app.exec_()
