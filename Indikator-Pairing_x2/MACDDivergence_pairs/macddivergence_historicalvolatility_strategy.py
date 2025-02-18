import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
