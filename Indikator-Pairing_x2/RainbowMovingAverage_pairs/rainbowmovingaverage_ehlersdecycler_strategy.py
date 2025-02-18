import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'EhlersDecycler': 1.0
        })
    )
