import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und TrendCycles
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'TrendCycles': 1.0
        })
    )
