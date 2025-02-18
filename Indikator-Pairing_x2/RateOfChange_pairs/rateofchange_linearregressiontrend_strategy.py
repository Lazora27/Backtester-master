import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
