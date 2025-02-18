import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'SeasonalStrength': 1.0
        })
    )
