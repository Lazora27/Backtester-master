import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
