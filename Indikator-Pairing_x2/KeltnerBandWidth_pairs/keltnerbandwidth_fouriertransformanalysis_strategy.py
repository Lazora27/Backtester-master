import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
