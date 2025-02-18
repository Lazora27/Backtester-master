import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
