import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
