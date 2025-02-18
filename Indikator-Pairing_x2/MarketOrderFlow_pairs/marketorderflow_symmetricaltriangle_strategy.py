import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
