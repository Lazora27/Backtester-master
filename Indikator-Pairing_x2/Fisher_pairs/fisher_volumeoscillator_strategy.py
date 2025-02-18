import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'VolumeOscillator': 1.0
        })
    )
