import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
