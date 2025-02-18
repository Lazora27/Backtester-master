import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
