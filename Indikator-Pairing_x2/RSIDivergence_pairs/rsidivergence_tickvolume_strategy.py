import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und TickVolume
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'TickVolume': 1.0
        })
    )
