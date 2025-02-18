import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
