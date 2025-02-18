import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
