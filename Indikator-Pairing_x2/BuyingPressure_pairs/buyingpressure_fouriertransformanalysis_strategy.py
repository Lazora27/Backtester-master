import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
