import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und CycleFinder
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'CycleFinder': 1.0
        })
    )
