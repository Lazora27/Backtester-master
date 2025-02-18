import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
