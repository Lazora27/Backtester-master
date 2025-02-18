import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
