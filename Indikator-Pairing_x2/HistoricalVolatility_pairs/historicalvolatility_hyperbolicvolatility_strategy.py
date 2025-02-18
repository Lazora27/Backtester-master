import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
