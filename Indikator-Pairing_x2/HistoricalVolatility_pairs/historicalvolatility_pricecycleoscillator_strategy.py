import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
