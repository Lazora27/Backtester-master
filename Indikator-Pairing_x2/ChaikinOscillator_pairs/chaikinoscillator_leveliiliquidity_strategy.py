import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
