import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
