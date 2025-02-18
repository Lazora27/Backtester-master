import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und MarketBalance
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'MarketBalance': 1.0
        })
    )
