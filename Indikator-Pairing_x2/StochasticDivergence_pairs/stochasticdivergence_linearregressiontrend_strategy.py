import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
