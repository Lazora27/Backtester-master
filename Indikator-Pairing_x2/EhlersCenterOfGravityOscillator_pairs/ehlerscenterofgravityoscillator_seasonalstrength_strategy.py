import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersCenterOfGravityOscillator_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersCenterOfGravityOscillator und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'EhlersCenterOfGravityOscillator': {
                'class': EhlersCenterOfGravityOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersCenterOfGravityOscillator'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'EhlersCenterOfGravityOscillator': 1.0,
            'SeasonalStrength': 1.0
        })
    )
