import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'StochasticRSI': 1.0
        })
    )
