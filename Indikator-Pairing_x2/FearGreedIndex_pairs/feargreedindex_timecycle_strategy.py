import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
