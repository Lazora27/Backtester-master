import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'SeasonalStrength': 1.0
        })
    )
