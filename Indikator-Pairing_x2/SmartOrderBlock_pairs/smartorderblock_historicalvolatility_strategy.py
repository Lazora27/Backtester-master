import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
