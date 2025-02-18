import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und VWAPBands
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'VWAPBands': 1.0
        })
    )
