import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
