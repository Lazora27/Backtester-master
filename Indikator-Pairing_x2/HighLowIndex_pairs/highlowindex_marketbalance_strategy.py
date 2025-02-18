import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und MarketBalance
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'MarketBalance': 1.0
        })
    )
