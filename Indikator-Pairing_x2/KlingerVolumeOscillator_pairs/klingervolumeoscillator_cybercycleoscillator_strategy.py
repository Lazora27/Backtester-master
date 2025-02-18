import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KlingerVolumeOscillator_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KlingerVolumeOscillator und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'KlingerVolumeOscillator': {
                'class': KlingerVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KlingerVolumeOscillator'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'KlingerVolumeOscillator': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
