import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
