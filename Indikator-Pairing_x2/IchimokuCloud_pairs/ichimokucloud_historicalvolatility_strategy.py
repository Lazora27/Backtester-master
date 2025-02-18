import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
