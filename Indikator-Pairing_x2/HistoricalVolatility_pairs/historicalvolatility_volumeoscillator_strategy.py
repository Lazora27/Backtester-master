import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'VolumeOscillator': 1.0
        })
    )
