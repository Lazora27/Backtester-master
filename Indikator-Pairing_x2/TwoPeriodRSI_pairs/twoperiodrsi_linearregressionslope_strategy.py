import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
