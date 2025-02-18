import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
