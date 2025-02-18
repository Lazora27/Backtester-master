import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
