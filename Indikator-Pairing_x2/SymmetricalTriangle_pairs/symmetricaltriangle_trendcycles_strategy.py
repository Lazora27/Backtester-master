import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SymmetricalTriangle_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SymmetricalTriangle und TrendCycles
    """
    
    params = (
        ('indicators', {
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'SymmetricalTriangle': 1.0,
            'TrendCycles': 1.0
        })
    )
