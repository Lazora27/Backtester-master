import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und VWAPBands
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'VWAPBands': 1.0
        })
    )
