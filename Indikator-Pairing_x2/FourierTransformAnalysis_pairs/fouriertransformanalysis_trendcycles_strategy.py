import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und TrendCycles
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'TrendCycles': 1.0
        })
    )
