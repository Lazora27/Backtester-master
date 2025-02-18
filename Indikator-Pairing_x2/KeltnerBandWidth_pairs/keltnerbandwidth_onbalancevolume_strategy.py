import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
