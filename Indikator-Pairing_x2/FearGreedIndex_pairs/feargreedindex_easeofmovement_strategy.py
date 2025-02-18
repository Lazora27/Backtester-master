import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
