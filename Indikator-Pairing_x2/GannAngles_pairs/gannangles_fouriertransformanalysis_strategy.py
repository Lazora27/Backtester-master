import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
