import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
