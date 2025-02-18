import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'AccelerationBands': 1.0
        })
    )
