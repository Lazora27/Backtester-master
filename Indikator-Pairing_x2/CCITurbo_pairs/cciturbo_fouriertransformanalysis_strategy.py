import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
