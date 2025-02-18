import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_VolumeSpreadAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und VolumeSpreadAnalysis
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'VolumeSpreadAnalysis': {
                'class': VolumeSpreadAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeSpreadAnalysis'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'VolumeSpreadAnalysis': 1.0
        })
    )
