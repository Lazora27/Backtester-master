import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'SeasonalStrength': 1.0
        })
    )
