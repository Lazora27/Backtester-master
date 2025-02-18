import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
