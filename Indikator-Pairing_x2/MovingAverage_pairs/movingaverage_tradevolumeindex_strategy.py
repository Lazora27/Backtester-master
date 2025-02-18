import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
