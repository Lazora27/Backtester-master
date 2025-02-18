import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
