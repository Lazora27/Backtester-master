import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'SeasonalStrength': 1.0
        })
    )
