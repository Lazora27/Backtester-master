import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
