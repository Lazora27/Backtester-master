import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
