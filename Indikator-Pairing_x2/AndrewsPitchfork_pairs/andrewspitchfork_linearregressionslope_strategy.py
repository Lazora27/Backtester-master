import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
