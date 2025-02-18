import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
