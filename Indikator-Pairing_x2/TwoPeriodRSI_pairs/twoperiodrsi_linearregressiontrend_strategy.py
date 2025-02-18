import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
