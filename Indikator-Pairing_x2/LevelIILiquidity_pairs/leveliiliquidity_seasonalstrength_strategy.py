import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'SeasonalStrength': 1.0
        })
    )
