import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und TrueRange
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'TrueRange': 1.0
        })
    )
