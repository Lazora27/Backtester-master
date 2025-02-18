import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'StochasticOscillator': 1.0
        })
    )
