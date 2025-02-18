import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
