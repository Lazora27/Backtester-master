import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TRIXIndicator_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TRIXIndicator und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'TRIXIndicator': 1.0,
            'SeasonalStrength': 1.0
        })
    )
