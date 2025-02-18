import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
