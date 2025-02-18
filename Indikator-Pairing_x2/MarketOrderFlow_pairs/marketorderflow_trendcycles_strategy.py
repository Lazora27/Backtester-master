import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und TrendCycles
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'TrendCycles': 1.0
        })
    )
