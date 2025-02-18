import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
