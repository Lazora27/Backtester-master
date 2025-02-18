import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
