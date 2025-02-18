import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
