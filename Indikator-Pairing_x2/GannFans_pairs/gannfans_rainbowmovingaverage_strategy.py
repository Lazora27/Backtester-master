import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
