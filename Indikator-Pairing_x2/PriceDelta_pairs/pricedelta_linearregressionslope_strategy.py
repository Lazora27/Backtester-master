import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
