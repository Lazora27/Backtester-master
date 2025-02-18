import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
