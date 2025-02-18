import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'FearGreedIndex': 1.0
        })
    )
