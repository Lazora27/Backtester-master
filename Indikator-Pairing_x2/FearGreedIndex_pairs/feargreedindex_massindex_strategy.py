import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und MassIndex
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'MassIndex': 1.0
        })
    )
