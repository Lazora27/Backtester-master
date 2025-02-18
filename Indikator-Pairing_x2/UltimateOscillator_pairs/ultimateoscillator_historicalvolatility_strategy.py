import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
