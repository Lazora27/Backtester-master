import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
