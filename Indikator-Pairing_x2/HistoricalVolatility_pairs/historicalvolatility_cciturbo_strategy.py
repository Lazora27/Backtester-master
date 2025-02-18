import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und CCITurbo
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'CCITurbo': 1.0
        })
    )
