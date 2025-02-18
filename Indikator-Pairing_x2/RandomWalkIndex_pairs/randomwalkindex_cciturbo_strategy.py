import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
