import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
