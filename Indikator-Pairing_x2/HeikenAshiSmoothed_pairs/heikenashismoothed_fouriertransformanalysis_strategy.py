import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiSmoothed_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiSmoothed und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'HeikenAshiSmoothed': {
                'class': HeikenAshiSmoothed,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiSmoothed'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'HeikenAshiSmoothed': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
