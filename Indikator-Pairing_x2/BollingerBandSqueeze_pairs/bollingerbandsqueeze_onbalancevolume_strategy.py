import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
