import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'ConnorsRSI': 1.0
        })
    )
