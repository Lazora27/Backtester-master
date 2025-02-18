import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
