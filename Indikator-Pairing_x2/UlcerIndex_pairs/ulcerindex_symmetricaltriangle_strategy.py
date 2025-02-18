import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
