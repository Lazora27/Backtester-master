import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
