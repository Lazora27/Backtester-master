import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
