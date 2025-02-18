import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
