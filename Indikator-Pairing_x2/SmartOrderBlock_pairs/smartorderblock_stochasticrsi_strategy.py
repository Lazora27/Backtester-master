import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'StochasticRSI': 1.0
        })
    )
