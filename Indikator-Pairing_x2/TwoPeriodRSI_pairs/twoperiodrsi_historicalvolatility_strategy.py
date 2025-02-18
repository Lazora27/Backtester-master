import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
