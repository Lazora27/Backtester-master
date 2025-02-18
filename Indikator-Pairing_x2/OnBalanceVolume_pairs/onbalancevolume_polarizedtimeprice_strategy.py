import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
