import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'VolumeOscillator': 1.0
        })
    )
