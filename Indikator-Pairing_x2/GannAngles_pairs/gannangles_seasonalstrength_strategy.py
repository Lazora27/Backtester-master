import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'SeasonalStrength': 1.0
        })
    )
