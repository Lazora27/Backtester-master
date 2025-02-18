import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
