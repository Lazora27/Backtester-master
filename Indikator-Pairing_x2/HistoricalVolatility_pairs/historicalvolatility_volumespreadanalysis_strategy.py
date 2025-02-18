import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_VolumeSpreadAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und VolumeSpreadAnalysis
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'VolumeSpreadAnalysis': {
                'class': VolumeSpreadAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeSpreadAnalysis'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'VolumeSpreadAnalysis': 1.0
        })
    )
