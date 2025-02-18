import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
