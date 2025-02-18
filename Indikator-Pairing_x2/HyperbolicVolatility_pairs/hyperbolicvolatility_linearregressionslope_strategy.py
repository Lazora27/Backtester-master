import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
