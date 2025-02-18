import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und GannAngles
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'GannAngles': 1.0
        })
    )
