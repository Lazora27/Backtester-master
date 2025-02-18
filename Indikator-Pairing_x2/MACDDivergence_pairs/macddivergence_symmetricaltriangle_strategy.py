import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
