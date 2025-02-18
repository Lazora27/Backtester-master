import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
