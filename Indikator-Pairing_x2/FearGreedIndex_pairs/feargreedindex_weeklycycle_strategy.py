import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
