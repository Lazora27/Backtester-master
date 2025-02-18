import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
