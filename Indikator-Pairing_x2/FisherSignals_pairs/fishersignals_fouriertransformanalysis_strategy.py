import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
