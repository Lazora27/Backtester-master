import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
