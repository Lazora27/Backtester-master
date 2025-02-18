import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
