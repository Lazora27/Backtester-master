import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
