import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
