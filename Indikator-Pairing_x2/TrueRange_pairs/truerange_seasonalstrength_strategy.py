import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'SeasonalStrength': 1.0
        })
    )
