import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
