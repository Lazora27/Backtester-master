import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
