import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
