import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
