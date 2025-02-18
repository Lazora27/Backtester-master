import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
