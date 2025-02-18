import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
