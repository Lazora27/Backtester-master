import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und MarketBalance
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'MarketBalance': 1.0
        })
    )
