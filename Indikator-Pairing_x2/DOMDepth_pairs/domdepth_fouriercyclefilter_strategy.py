import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
