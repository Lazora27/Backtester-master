import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und TimeCycle
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'TimeCycle': 1.0
        })
    )
