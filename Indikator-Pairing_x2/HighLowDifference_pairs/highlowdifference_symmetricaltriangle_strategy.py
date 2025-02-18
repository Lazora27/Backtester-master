import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
