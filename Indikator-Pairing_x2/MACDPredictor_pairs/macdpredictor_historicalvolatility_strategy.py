import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
