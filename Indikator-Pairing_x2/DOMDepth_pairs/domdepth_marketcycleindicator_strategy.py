import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
