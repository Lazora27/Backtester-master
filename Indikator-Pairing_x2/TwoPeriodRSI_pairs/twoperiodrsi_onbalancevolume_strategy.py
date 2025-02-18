import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
