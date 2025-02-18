import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und MarketBalance
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'MarketBalance': 1.0
        })
    )
