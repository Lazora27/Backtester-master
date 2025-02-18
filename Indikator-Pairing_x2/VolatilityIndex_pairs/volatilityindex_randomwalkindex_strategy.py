import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
