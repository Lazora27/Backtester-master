import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
