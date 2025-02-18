import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
