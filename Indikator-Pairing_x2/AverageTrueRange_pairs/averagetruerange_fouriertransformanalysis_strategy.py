import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
