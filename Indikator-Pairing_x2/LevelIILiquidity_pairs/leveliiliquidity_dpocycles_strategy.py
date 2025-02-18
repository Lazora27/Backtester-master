import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und DPOCycles
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'DPOCycles': 1.0
        })
    )
