import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'FearGreedIndex': 1.0
        })
    )
