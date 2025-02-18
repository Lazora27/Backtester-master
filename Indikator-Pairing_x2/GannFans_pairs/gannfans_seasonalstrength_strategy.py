import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'SeasonalStrength': 1.0
        })
    )
