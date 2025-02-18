import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
