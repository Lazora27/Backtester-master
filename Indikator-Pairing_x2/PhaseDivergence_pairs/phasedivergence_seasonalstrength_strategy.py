import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PhaseDivergence_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PhaseDivergence und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'PhaseDivergence': 1.0,
            'SeasonalStrength': 1.0
        })
    )
