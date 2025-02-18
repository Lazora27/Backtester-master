import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
