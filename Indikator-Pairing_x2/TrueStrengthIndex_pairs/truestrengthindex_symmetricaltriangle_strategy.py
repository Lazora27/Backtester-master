import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
