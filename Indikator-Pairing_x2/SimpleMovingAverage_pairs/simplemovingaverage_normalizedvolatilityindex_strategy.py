import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_NormalizedVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und NormalizedVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'NormalizedVolatilityIndex': {
                'class': NormalizedVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedVolatilityIndex'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'NormalizedVolatilityIndex': 1.0
        })
    )
