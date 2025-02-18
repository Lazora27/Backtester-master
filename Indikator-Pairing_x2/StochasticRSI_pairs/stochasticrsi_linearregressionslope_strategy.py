import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
