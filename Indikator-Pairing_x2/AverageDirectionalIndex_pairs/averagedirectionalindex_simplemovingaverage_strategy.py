import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
