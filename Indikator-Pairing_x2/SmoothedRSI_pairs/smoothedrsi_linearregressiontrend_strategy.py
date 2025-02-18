import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
