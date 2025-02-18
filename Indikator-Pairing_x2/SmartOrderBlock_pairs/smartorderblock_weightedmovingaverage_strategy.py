import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
