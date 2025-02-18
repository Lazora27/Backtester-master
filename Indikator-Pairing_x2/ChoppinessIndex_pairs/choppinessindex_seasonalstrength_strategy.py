import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
