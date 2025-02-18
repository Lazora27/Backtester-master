import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
