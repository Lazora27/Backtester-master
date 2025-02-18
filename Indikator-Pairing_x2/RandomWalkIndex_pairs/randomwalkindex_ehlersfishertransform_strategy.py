import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
