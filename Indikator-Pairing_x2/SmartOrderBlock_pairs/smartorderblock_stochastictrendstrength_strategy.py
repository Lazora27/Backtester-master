import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
