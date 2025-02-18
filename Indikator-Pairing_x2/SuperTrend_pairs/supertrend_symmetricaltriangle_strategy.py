import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
