import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
