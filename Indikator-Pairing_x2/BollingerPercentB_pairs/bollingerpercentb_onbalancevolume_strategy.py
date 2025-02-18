import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
