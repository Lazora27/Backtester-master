import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
