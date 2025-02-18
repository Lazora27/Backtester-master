import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und MarketBalance
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'MarketBalance': 1.0
        })
    )
