import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
