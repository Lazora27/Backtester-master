import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und MarketBalance
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'MarketBalance': 1.0
        })
    )
