import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'IchimokuCloud': 1.0
        })
    )
