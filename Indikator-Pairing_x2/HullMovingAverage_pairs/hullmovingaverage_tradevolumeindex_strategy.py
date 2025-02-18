import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
