import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
