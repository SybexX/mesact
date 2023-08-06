import os

from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

def aboutDialog(parent):
	dialogBox = QDialog()
	dialogBox.setMinimumSize(300, 300)
	dialogBox.setWindowTitle('About')

	layout = QVBoxLayout(dialogBox)


	titleLabel =  QLabel()
	titleLabel.setText('Mesa Configuration Tool')
	titleLabel.setAlignment(Qt.AlignCenter)
	layout.addWidget(titleLabel)

	imageLabel = QLabel()
	imageLabel.setAlignment(Qt.AlignCenter)

	image_path = os.path.join(parent.lib_path, 'mesact.jpg')
	pixmap = QPixmap(image_path)
	pixmap = pixmap.scaled(256, 256, Qt.KeepAspectRatio)
	imageLabel.setPixmap(pixmap)
	layout.addWidget(imageLabel)

	authorLabel =  QLabel()
	authorLabel.setText('Author: John Thornton')
	authorLabel.setAlignment(Qt.AlignCenter)
	layout.addWidget(authorLabel)

	versionLabel =  QLabel()
	versionLabel.setText(f'Version: {parent.version}')
	versionLabel.setAlignment(Qt.AlignCenter)
	layout.addWidget(versionLabel)

	aboutLabel =  QLabel()
	aboutLabel.setText('Mesa CT Creates LinuxCNC\nconfigurations for Mesa Boards')
	aboutLabel.setAlignment(Qt.AlignCenter)
	layout.addWidget(aboutLabel)


	websiteLabel =  QLabel()
	websiteLabel.setText("<a href='https://gnipsel.com/'>Authors Website</a>")
	websiteLabel.setAlignment(Qt.AlignCenter)
	websiteLabel.setOpenExternalLinks(True)
	layout.addWidget(websiteLabel)

	repoLabel =  QLabel()
	repoLabel.setText("<a href='https://github.com/jethornton/mesact'>Code Website</a>")
	repoLabel.setAlignment(Qt.AlignCenter)
	repoLabel.setOpenExternalLinks(True)
	layout.addWidget(repoLabel)


	copyrightLabel =  QLabel()
	copyrightLabel.setText('Copyright © 1953-2023 John Thornton')
	copyrightLabel.setAlignment(Qt.AlignCenter)
	layout.addWidget(copyrightLabel)


	layout.addStretch()

	buttonBox = QDialogButtonBox()
	buttonBox.setStandardButtons(QDialogButtonBox.Ok)
	buttonBox.setCenterButtons(True)
	#buttonBox.addButton("Credits", QDialogButtonBox.ActionRole)
	buttonBox.accepted.connect(dialogBox.close)
	layout.addWidget(buttonBox)

	dialogBox.exec()

