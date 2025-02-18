import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
