import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'PriceSquawk': 1.0
        })
    )
