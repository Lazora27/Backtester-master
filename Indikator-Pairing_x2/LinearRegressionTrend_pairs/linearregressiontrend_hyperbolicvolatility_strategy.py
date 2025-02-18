import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
