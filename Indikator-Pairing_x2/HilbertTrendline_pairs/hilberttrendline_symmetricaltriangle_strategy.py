import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendline_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendline und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'HilbertTrendline': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
