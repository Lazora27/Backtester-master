import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
