import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
