import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DetrendedPriceIndicator_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DetrendedPriceIndicator und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'DetrendedPriceIndicator': {
                'class': DetrendedPriceIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceIndicator'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'DetrendedPriceIndicator': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
