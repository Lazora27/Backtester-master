import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und TrendCycles
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'TrendCycles': 1.0
        })
    )
