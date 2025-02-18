import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'SmoothedCycle': 1.0
        })
    )
