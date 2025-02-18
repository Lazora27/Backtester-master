import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'SmoothedRSI': 1.0
        })
    )
