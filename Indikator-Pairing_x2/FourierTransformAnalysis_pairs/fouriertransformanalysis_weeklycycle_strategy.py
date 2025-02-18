import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'WeeklyCycle': 1.0
        })
    )
