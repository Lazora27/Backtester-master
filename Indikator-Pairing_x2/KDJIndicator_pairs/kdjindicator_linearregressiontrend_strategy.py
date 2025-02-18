import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
