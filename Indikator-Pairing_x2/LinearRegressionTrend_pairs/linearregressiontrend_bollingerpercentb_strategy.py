import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'BollingerPercentB': 1.0
        })
    )
