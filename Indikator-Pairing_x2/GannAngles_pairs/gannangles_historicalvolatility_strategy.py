import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
