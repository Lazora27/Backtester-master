import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'SeasonalStrength': 1.0
        })
    )
