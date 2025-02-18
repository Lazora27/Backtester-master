import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
