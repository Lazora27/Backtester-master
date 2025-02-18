import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_ZeroLagStochasticIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und ZeroLagStochasticIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'ZeroLagStochasticIndicator': {
                'class': ZeroLagStochasticIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagStochasticIndicator'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'ZeroLagStochasticIndicator': 1.0
        })
    )
