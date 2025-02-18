import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
