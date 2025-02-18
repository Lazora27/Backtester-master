import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
