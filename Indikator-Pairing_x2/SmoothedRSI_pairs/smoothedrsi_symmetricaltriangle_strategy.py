import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
