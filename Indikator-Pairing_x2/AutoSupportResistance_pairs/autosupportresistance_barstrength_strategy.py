import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und BarStrength
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'BarStrength': 1.0
        })
    )
