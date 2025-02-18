import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_KlingerVolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und KlingerVolumeOscillator
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'KlingerVolumeOscillator': {
                'class': KlingerVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KlingerVolumeOscillator'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'KlingerVolumeOscillator': 1.0
        })
    )
