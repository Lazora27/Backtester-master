import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
