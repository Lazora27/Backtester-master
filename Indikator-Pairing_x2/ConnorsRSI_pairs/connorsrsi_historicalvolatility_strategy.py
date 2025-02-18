import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
