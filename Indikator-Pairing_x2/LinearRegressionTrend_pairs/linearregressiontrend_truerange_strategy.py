import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und TrueRange
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'TrueRange': 1.0
        })
    )
