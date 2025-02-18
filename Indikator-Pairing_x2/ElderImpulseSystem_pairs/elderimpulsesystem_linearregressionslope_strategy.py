import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
