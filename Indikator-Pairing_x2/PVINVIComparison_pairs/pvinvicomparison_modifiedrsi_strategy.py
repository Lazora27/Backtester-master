import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'ModifiedRSI': 1.0
        })
    )
