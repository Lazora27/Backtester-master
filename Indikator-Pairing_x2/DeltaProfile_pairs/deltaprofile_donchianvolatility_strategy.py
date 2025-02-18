import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'DonchianVolatility': 1.0
        })
    )
