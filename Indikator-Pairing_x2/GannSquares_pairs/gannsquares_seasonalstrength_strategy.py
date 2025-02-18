import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'SeasonalStrength': 1.0
        })
    )
