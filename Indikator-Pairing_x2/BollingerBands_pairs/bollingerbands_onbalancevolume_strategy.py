import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
