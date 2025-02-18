import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
