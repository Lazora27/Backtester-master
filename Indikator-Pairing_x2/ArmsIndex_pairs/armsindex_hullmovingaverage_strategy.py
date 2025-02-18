import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'HullMovingAverage': 1.0
        })
    )
