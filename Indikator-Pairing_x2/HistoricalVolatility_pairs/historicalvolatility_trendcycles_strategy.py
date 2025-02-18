import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und TrendCycles
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'TrendCycles': 1.0
        })
    )
