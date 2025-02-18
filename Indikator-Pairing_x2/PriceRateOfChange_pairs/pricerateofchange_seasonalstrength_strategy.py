import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'SeasonalStrength': 1.0
        })
    )
