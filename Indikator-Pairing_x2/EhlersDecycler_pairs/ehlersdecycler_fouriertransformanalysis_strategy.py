import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
