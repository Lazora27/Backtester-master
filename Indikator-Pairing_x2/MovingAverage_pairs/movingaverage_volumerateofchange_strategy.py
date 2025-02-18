import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
