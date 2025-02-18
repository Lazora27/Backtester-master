import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
