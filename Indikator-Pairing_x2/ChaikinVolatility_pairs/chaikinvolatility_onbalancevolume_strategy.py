import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
