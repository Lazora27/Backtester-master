import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
