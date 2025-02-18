import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
