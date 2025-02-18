import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'VortexIndicator': 1.0
        })
    )
