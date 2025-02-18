import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
