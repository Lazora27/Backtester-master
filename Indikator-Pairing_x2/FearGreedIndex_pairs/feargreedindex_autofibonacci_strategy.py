import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'AutoFibonacci': 1.0
        })
    )
