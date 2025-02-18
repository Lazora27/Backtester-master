import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
