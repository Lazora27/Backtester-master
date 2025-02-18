import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und TimeCycle
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'TimeCycle': 1.0
        })
    )
