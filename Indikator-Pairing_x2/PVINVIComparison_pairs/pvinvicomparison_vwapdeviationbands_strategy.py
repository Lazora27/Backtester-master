import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
