import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'VolumeOscillator': 1.0
        })
    )
