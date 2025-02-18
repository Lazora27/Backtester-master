import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
