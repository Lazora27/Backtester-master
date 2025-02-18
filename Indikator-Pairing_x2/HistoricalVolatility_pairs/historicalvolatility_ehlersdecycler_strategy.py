import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'EhlersDecycler': 1.0
        })
    )
