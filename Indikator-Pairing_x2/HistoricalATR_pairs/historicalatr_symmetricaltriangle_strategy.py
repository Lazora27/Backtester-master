import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
