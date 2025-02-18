import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und VWAPBands
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'VWAPBands': 1.0
        })
    )
