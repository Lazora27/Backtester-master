import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
