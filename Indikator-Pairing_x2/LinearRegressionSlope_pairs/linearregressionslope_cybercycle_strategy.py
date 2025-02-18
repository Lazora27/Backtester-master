import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und CyberCycle
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'CyberCycle': 1.0
        })
    )
