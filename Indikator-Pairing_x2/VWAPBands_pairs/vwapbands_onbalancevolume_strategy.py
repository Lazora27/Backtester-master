import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
