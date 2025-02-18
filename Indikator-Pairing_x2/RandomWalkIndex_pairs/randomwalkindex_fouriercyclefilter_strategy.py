import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
