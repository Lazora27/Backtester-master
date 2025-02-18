import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
