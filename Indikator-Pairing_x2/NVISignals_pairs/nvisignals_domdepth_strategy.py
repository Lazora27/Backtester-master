import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und DOMDepth
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'DOMDepth': 1.0
        })
    )
