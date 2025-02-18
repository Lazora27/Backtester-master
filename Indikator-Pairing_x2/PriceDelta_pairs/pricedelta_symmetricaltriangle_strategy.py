import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
