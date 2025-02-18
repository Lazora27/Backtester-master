import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'AccelerationBands': 1.0
        })
    )
