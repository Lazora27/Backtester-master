import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und MovingAverage
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'MovingAverage': 1.0
        })
    )
