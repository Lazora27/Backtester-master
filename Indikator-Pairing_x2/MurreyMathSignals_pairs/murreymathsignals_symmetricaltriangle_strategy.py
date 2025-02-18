import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
