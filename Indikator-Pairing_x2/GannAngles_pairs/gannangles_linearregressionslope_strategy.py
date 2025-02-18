import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
