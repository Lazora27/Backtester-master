import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_VolumeProfileValueAreas_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und VolumeProfileValueAreas
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'VolumeProfileValueAreas': {
                'class': VolumeProfileValueAreas,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfileValueAreas'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'VolumeProfileValueAreas': 1.0
        })
    )
