import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
