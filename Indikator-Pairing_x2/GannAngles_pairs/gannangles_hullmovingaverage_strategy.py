import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'HullMovingAverage': 1.0
        })
    )
