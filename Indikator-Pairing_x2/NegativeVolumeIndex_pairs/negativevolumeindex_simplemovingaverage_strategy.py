import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
