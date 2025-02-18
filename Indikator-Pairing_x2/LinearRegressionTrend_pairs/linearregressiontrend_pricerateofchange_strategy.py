import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
