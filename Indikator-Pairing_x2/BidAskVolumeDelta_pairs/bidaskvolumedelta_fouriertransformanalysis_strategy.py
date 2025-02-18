import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
