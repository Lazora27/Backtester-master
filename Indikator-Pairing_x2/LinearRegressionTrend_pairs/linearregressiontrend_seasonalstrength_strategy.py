import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'SeasonalStrength': 1.0
        })
    )
