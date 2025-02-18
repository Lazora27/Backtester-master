import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'AroonIndicator': 1.0
        })
    )
