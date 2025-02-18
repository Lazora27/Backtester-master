import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'LiquidityIndex': 1.0
        })
    )
