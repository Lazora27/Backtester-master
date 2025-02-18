import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
