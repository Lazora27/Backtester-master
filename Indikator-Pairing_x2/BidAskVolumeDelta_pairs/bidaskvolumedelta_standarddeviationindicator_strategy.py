import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
