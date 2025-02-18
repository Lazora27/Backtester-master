import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'AccelerationBands': 1.0
        })
    )
