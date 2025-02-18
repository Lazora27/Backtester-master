import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
