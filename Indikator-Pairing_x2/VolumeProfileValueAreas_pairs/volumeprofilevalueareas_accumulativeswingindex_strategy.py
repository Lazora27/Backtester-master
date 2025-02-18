import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfileValueAreas_AccumulativeSwingIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfileValueAreas und AccumulativeSwingIndex
    """
    
    params = (
        ('indicators', {
            'VolumeProfileValueAreas': {
                'class': VolumeProfileValueAreas,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfileValueAreas'>
            },
            'AccumulativeSwingIndex': {
                'class': AccumulativeSwingIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulativeSwingIndex'>
            }
        }),
        ('weights', {
            'VolumeProfileValueAreas': 1.0,
            'AccumulativeSwingIndex': 1.0
        })
    )
