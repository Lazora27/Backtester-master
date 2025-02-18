import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und SuperMACD
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'SuperMACD': 1.0
        })
    )
