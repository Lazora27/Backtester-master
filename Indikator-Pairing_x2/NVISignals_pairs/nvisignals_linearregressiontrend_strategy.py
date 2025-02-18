import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
