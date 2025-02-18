import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
