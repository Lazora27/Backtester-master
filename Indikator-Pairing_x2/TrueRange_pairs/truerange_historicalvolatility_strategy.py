import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
