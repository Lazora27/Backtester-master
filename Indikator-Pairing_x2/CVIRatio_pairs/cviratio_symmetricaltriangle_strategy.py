import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
