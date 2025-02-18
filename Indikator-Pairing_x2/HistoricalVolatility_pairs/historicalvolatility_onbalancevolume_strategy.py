import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
