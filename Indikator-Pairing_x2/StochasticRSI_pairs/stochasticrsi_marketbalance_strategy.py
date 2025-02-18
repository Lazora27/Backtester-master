import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und MarketBalance
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'MarketBalance': 1.0
        })
    )
