import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'AverageTrueRange': 1.0
        })
    )
