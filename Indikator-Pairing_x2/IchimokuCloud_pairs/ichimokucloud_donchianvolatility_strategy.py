import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'DonchianVolatility': 1.0
        })
    )
