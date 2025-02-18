import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
