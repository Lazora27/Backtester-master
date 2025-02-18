import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
