import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
