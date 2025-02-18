import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
