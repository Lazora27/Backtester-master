import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
