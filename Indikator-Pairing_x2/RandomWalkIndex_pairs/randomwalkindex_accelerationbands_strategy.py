import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'AccelerationBands': 1.0
        })
    )
