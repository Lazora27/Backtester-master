import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'IchimokuCloud': 1.0
        })
    )
