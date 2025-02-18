import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
