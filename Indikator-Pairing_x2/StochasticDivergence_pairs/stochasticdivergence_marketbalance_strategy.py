import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und MarketBalance
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'MarketBalance': 1.0
        })
    )
