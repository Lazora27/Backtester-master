import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und TrendCycles
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'TrendCycles': 1.0
        })
    )
