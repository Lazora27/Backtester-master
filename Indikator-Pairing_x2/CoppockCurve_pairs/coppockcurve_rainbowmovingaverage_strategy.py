import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
