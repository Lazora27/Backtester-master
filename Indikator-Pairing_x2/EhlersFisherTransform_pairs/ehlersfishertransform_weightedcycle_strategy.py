import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'WeightedCycle': 1.0
        })
    )
