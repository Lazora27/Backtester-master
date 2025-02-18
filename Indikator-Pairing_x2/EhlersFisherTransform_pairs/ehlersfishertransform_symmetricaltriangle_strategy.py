import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
