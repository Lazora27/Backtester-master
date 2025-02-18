import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'SeasonalStrength': 1.0
        })
    )
