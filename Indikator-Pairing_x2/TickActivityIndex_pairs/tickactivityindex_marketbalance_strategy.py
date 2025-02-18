import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und MarketBalance
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'MarketBalance': 1.0
        })
    )
