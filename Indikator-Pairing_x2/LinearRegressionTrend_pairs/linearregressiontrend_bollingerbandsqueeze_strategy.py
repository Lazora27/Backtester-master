import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
