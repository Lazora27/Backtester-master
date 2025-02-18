import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
