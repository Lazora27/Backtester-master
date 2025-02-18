import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
