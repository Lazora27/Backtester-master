import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
