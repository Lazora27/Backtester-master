import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
