import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'SeasonalStrength': 1.0
        })
    )
