import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
