import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PolarizedTimePrice_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PolarizedTimePrice und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'PolarizedTimePrice': 1.0,
            'SeasonalStrength': 1.0
        })
    )
