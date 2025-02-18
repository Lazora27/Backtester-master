import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
