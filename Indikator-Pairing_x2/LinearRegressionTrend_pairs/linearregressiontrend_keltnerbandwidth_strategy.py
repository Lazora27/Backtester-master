import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
