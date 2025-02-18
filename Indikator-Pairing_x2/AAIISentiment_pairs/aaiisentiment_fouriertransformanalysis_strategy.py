import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
