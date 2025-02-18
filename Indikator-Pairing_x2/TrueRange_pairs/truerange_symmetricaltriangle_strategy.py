import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
