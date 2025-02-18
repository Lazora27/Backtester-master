import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'SeasonalStrength': 1.0
        })
    )
