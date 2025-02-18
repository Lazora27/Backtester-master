import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
