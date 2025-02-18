import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
