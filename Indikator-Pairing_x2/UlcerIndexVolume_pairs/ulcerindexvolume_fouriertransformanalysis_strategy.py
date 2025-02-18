import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
