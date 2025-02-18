import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
