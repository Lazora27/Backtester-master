import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
