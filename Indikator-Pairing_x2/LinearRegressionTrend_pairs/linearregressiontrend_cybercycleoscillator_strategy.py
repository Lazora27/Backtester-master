import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
