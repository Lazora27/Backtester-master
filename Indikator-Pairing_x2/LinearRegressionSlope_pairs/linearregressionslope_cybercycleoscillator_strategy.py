import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
