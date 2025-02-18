import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'HistoricalATR': 1.0
        })
    )
