import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
