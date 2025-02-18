import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und MarketBalance
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'MarketBalance': 1.0
        })
    )
