import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'FearGreedIndex': 1.0
        })
    )
