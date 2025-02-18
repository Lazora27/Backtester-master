import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und MarketBalance
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'MarketBalance': 1.0
        })
    )
