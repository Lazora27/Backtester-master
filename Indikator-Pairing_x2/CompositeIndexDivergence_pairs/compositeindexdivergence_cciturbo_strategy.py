import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und CCITurbo
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'CCITurbo': 1.0
        })
    )
