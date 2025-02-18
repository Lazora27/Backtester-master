import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
