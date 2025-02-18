import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
