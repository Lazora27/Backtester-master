import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
