import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
