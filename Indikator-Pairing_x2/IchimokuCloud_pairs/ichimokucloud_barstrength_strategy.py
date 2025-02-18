import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und BarStrength
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'BarStrength': 1.0
        })
    )
