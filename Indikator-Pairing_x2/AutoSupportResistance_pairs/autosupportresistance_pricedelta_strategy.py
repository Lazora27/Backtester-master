import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und PriceDelta
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'PriceDelta': 1.0
        })
    )
