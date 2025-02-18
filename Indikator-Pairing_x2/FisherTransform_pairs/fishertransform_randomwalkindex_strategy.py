import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
