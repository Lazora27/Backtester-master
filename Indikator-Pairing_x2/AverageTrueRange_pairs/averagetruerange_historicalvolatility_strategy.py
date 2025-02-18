import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
