import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
