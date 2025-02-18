import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
