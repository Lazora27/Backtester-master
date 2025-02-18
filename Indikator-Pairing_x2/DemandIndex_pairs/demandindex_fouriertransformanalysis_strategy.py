import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
