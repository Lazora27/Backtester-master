import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
