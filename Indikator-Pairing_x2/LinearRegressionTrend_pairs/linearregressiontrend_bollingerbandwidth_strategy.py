import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
