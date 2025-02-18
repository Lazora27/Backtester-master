import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'BradleySiderograph': 1.0
        })
    )
