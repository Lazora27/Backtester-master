import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
