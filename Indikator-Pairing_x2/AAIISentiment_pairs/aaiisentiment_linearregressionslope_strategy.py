import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
