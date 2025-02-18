import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
