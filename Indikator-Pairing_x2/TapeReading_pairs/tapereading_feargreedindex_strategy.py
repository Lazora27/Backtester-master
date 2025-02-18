import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'FearGreedIndex': 1.0
        })
    )
