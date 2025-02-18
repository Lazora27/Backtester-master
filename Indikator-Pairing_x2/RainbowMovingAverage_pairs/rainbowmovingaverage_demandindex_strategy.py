import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und DemandIndex
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'DemandIndex': 1.0
        })
    )
