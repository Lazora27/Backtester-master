import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
