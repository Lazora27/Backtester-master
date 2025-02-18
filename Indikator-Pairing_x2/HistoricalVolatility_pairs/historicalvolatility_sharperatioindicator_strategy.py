import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
