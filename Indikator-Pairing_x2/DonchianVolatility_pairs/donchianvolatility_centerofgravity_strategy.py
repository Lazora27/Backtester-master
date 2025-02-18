import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'CenterOfGravity': 1.0
        })
    )
