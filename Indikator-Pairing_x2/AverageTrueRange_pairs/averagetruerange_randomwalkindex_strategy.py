import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
