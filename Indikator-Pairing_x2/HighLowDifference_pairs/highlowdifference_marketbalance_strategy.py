import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und MarketBalance
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'MarketBalance': 1.0
        })
    )
