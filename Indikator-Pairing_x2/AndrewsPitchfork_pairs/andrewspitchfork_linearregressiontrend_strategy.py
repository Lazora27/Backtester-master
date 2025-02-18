import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
