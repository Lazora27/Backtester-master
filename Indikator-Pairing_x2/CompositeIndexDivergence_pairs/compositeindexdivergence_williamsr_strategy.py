import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und WilliamsR
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'WilliamsR': 1.0
        })
    )
