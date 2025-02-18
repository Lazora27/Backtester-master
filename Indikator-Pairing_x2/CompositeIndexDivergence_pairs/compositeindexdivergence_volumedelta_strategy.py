import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'VolumeDelta': 1.0
        })
    )
