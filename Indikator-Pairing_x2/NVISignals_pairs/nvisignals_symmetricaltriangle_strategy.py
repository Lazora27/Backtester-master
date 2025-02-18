import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
