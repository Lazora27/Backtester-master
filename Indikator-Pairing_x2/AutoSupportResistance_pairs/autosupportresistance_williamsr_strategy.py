import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und WilliamsR
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'WilliamsR': 1.0
        })
    )
