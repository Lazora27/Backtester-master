import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'VolumeOscillator': 1.0
        })
    )
