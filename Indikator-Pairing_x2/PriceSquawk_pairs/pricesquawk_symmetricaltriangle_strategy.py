import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
