import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
