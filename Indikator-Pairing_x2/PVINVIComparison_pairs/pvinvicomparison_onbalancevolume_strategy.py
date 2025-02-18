import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
