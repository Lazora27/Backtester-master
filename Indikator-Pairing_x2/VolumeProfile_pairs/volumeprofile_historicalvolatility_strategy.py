import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
