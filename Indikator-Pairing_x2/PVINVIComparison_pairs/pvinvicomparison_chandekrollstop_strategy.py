import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
