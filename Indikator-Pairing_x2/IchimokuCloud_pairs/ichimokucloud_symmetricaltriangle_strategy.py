import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
