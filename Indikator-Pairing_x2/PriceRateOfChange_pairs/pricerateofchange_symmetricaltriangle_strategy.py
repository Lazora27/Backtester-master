import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
