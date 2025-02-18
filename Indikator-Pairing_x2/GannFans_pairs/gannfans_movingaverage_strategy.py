import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und MovingAverage
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'MovingAverage': 1.0
        })
    )
