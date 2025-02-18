import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'DonchianVolatility': 1.0
        })
    )
