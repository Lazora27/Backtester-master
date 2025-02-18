import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
