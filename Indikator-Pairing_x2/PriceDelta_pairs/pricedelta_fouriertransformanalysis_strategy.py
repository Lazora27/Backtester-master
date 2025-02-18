import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
