import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und TimeCycle
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'TimeCycle': 1.0
        })
    )
