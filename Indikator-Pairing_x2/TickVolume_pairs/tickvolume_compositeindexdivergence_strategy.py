import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
