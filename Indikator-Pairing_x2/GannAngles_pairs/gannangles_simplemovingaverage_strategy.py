import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
