import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
