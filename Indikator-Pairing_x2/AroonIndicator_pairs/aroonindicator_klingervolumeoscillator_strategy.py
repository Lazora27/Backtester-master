import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_KlingerVolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und KlingerVolumeOscillator
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'KlingerVolumeOscillator': {
                'class': KlingerVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KlingerVolumeOscillator'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'KlingerVolumeOscillator': 1.0
        })
    )
