import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und GannFans
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'GannFans': 1.0
        })
    )
