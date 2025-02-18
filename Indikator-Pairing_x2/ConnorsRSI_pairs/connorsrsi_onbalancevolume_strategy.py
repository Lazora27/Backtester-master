import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
