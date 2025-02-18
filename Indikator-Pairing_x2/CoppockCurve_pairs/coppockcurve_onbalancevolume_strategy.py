import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
