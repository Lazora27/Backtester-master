import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'VolumeOscillator': 1.0
        })
    )
