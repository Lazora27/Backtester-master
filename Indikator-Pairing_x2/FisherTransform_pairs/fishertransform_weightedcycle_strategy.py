import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'WeightedCycle': 1.0
        })
    )
