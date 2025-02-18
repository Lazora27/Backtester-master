import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
