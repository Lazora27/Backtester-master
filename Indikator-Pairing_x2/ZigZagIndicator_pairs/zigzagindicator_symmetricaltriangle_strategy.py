import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
