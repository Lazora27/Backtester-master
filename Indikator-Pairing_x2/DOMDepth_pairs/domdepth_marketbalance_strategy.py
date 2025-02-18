import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und MarketBalance
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'MarketBalance': 1.0
        })
    )
