import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und MovingAverage
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'MovingAverage': 1.0
        })
    )
