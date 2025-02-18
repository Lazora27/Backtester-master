import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'FearGreedIndex': 1.0
        })
    )
